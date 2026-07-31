# Project Deep Dive: Chargeback Model Automation (DoorDash)

**Authors: Fengying Yang, Zhifeng Wang, Jiting Xu, Lear Wang**

---

## Problem Statement

When I started working on this, our chargeback model development process was a complete bottleneck. Here's what it looked like:

The process was highly manual and fragmented. We relied on ad-hoc Databricks notebooks to link different components together. You'd have one notebook for feature exploration, another for data sampling, another for training, another for validation. Everything was siloed, and there was no orchestration.

What that meant in practice: if an ML engineer wanted to retrain an existing model or onboard a new chargeback transaction-level model, they'd spend 6-8 weeks just going through the development cycle. And most of that time wasn't actually spent on ML work—it was spent on data engineering, feature generation, and manual coordination.

## The Scale & Impact

Chargebacks are critical to DoorDash. Every fraudulent transaction that gets through costs money directly. So we have multiple chargeback models running in production—different transaction types, different signals, different strategies. When a model needs to be retrained or when we want to try a new approach, it takes forever.

The operational overhead was massive. ML engineers spending weeks on non-ML work. Model release velocity was slow—experiments took 2-3 months to run because you had to wait for chargeback data to mature before you could evaluate.

## The Solution

Here's the key insight: **a model is a hypothesis; a trained model in production is a product.** The gap isn't mathematical—it's operational. That's what we realized.

We decided to build a comprehensive automation framework treating the entire process as a distributed systems problem with distinct, independently restartable stages. Instead of notebooks scattered everywhere, we built an orchestrated pipeline.

**The Five-Stage Pipeline:**

1. **Data Ingestion & Versioning**: Raw transaction data arrives from the data lake. Before anything trains, we fingerprint every dataset version using Delta Lake. This solves the "what data produced this model?" problem six months later.

2. **Preprocessing & Tokenization**: We clean and standardize the raw transaction features. This is CPU-bound work—tokenization, feature normalization, sampling—and it runs on separate CPU workers, not during training. Huge win: no more wasting GPU cycles on data prep.

3. **Training Job Orchestration**: The actual training job. We submit to a job scheduler (Fireworks cluster in our case) with explicit resource requests. Decisions here: batch size, number of training steps, gradient accumulation if needed. The key: make it reproducible and schedulable.

4. **Checkpoint Management**: Training jobs fail. We write checkpoints to durable storage at regular intervals. The pipeline automatically resumes from the latest valid checkpoint without human intervention. We validate checkpoints on write to catch corruption.

5. **Evaluation, Registry & Promotion**: After training, models run against a frozen eval harness—standardized tests that don't change between runs. Models that pass thresholds get registered in our model registry with full lineage: dataset version, hyperparameters, eval scores. Promotion to production requires explicit approval.

**Key Components:**

1. **Offline Feature Store**: Pre-computed, versioned features. Engineers declare what they need; the store handles retrieval. No more data generation code in notebooks.

2. **Orchestrated Training Pipeline**: Configurable, reproducible, observable. You specify your model, hyperparameters, eval criteria; the pipeline handles everything else.

3. **Model Registry with Lineage**: Every model tracks what data it trained on, what config, what hardware, what eval scores. You can always answer "why did we promote this checkpoint?"

## Technical Approach

**The Core Principle: Separation of Concerns**

The old process mixed everything together. One notebook did data prep, another did feature generation, another did training. This meant:
- If you changed data prep logic, you had to re-run everything
- Failures were non-deterministic and hard to debug
- You couldn't parallelize different stages
- Reproducibility was a nightmare

Our solution: Treat each stage as independently testable and restartable.

**Stage 1: Data Versioning & Immutability**

We stopped treating datasets as ephemeral. Every training dataset gets a fingerprint (hash of content + metadata). We use Delta Lake for immutable snapshots. Why? So six months later, you can answer "what data trained this model?" instantly. This matters for auditing, compliance, and debugging.

**Stage 2: Preprocessing Isolation**

Here's a subtle but critical win: we moved all CPU-bound work (data cleaning, tokenization, feature normalization) off the GPU training path. We have separate CPU workers that pre-compute all features and write them to sharded binary files. GPU training nodes just read pre-computed data.

Why does this matter? Your GPU is expensive. If you waste it on CPU work (parsing JSON, running min-hash deduplication, normalizing features), you're leaving money on the table. Plus, preprocessing becomes non-deterministic when it happens during training—different batch orders → different cache effects → non-reproducible results.

**Stage 3: Stateful Training with Checkpointing**

Training jobs are brittle. GPUs preempt, spot instances evict, network timeouts happen. We wrote the pipeline to checkpoint at fixed intervals (every N steps), write to durable storage, and resume from the latest valid checkpoint. We validate checkpoints on write—if the file is corrupted, we keep the previous one.

The pipeline is built on a job scheduler (Fireworks) with explicit resource requests and timeouts. The scheduler handles retry logic and failure notifications.

**Stage 4: Frozen Evaluation Harness**

Models without evaluation are just hypothesis. We built a frozen benchmark that doesn't change between runs: standard chargeback test sets, performance thresholds, regression tests for general fraud signals. After training completes, the model runs through this harness.

Only models that pass get registered in the model registry with full lineage: dataset version, hyperparameters, hardware specs, eval scores.

**Stage 5: Promotion Gates**

Production deployment isn't automatic. Models are registered, staged for A/B testing, then promoted with explicit approval. The registry tracks which version is live, which is staging, which are archived.

## Key Technical Decisions

**Decision 1: Offline Feature Store vs. Real-time Feature Serving**

We chose offline features because:
- Chargebacks are historical analysis. You're building models from past transaction data, not serving predictions in real-time.
- Offline let us batch-compute at scale without worrying about latency.
- We could version features easily and reproduce experiments.

Tradeoff: We couldn't use real-time features. But for chargeback models, that wasn't a constraint.

**Decision 2: Orchestrated Pipeline vs. Notebook-based Development**

We built a proper orchestrated pipeline instead of just "better notebooks" because:
- Notebooks are great for exploration, terrible for reproducibility and ops.
- A pipeline meant we could standardize the process, validate assumptions at each step, and make it idempotent.
- Non-ML engineers could operate the pipeline without understanding every detail.

Tradeoff: Less flexibility for highly custom models. But 80% of our chargeback work fits the standard pipeline.

**Decision 3: Batch Computation vs. Real-time Training**

We chose batch for model training because:
- Chargeback models retrain weekly or monthly, not in real-time.
- Batch let us use Fireworks cluster (cheaper, more powerful than real-time serving systems).
- We could afford to wait a few hours for training to complete.

## Impact & Results

**Model Development Velocity**: We reduced MLE dev time from 6-8 weeks to 2-3 weeks for a standard model. For engineers using the pipeline, it's closer to 1-2 weeks.

**Model Release Velocity**: This was the bigger win. We reduced experiment duration from 2-3 months to 4-6 weeks by automating threshold adjustment and score calibration. Instead of waiting for data to mature, the pipeline validates models as they train.

**Operational Overhead**: We eliminated the manual coordination overhead. Now it's: define your model in config, submit the job, monitor results. No more manual linking of notebooks.

**Team Impact**: Freed up 2-3 ML engineers to focus on actual modeling and feature engineering instead of data plumbing.

## Challenges & Learnings

**Challenge 1: Standardization vs. Flexibility**

Some edge cases didn't fit the standard pipeline. We had to balance between "make it work for everyone" and "keep it simple."

Solution: We built escape hatches—if you needed a custom step, you could plug in your own code. But 80% of work used the standard path.

Learning: Don't try to solve everything in v1. Make it work for the common case, and iterate.

**Challenge 2: Data Quality & Reproducibility**

With so much automation, if something broke, it was hard to debug. We had to invest heavily in:
- Data validation at each step
- Logging and monitoring
- Test data for CI/CD

Learning: Automation is only good if it's debuggable. Invest in observability early.

**Challenge 3: Adoption**

Engineers were skeptical at first. "Will this work for my specific use case?" "What if I need something custom?"

We solved it by:
- Having champions who were early adopters and success stories
- Documenting real examples
- Having dedicated support during the rollout

Learning: Building great tools is half the battle. Change management and support are the other half.

## What I'm Proud Of

This was one of those projects where the impact was both technical and organizational. We didn't just build a system—we fundamentally changed how a team works. Engineers who used to spend 6-8 weeks on plumbing could now focus on modeling. That's a 2-3x productivity improvement.

The project also brought together multiple teams: ML engineers, data engineers, platform engineers, product. Everyone had to align on what "standardized" meant. That cross-functional coordination is something I learned a lot from.

## Key Takeaway for Interviews

I think the big lesson here is: don't just optimize for technical sophistication. Optimize for removing friction from the path to impact. A simple system that everyone uses is better than a perfect system no one understands. That's why we focused on standardization and automation—it wasn't about building the coolest tech, it was about unblocking a team and accelerating model velocity.
