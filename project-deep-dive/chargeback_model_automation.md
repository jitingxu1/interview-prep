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

We decided to build a comprehensive automation framework. The idea was: what if we could standardize the entire process, from feature generation to model training to productionization? We'd build an offline feature store and an orchestrated training pipeline.

**Key components:**

1. **Offline Feature Store**: Pre-computed, standardized features so engineers don't have to write data generation code for every model. Features are computed in batch, stored in a central location, and versioned.

2. **Orchestrated Training Pipeline**: Instead of individual notebooks, we built a pipeline that handles the entire flow: data sampling, feature retrieval, training, validation, score calibration, model promotion.

3. **Standardized Experimentation Framework**: New framework for running A/B tests and experiments, including threshold adjustment and score calibration steps.

## Technical Approach

**Model Development Velocity** was the first goal. We needed to reduce MLE dev time from 6-8 weeks down to something reasonable.

The old process: Each stage was manual.
- Model Development: 6-8 weeks (ad-hoc notebooks, feature exploration)
- Training Data Prep: 4-6 weeks (ad-hoc notebooks, manual sampling)
- Model Training: 2-3 weeks (ad-hoc notebooks, Fireworks cluster jobs)
- Model Productionization: 1-2 weeks (backend changes, integration, calibration)
- Experimentation: 2-3 months (waiting for data to mature, manual threshold adjustment)

Our solution: Standardize and automate every step.

We built an offline feature store that pre-computes features at different granularities. Instead of engineers writing their own feature generation code, they declare what features they need, and the feature store handles it. This alone cut the data prep stage by 50%.

For training, we created a configurable pipeline. You specify your model architecture, hyperparameters, evaluation criteria, and the pipeline handles feature retrieval, training, validation, and score calibration. It runs on a batch orchestration system (Fireworks cluster) so everything is parallel and scalable.

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
