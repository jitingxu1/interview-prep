# Looking at Data: Build Your Own Viewer

Why manually reading data matters so much for LLM work, why Hamel Husain recommends building your own annotation and curation tools instead of buying one, and the stack he uses (Shiny for Python + Quarto). Part of the [evaluation section](./README.md). This is the tooling behind Phase 7 ("read traces") of the [eval-driven development workflow](../../blog/eval/eval_driven_development.md).

**Sources**
- Hamel Husain — [*Curating LLM data*](https://hamel.dev/notes/llm/finetuning/data_cleaning.html) (notes on data annotation and curation tools, including the [general-purpose frameworks](https://hamel.dev/notes/llm/finetuning/data_cleaning.html#general-purpose-frameworks) section)
- Jason Wei — [tweet on manually inspecting data](https://x.com/_jasonwei/status/1708921475829481683) (X blocked fetching it; the wording below is as Hamel quotes it)
- [Quarto](https://quarto.org/) — open-source publishing system for technical work
- Related: Greg Brockman on manual inspection, via [Simon Willison](https://simonwillison.net/2025/Jan/16/greg-brockman/)

---

## TL;DR

1. **The best AI researchers read lots of data, and they build tools so they can read it fast.** That's the whole argument.
2. **Build your own viewer.** Hamel's verdict after trying vendors: "many people should build their own data annotation/curation tools for LLMs. The benefits far outweigh costs in many situations."
3. **Use a general-purpose Python UI framework.** Hamel recommends **Shiny for Python** over Gradio, Panel and Streamlit.
4. **Quarto** turns notebooks and markdown into reports and sites, and it integrates natively with Shiny — so eval reports and interactive viewers live in one stack.

---

## 1. Why reading data matters

> "Great AI researchers are willing to manually inspect lots of data … they build infrastructure that allows them to manually inspect data quickly."
> — Jason Wei (OpenAI at the time), as quoted by Hamel Husain

> "Manual inspection of data has probably the highest value-to-prestige ratio of any activity in machine learning."
> — Greg Brockman (OpenAI), via Simon Willison

Two points in those quotes:
- **Reading data is unglamorous and high-value.** It's where you find failure modes nobody predicted, like the support bot computing lateness from the first ETA instead of the latest.
- **Speed is the bottleneck.** If reading one trace takes a minute of clicking through logs, nobody reads a hundred. The tool decides how much data people actually look at.

This is the same message as Hamel's *Your AI Product Needs Evals*: "You must remove all friction from the process of looking at data" ([notes](./hamel_your_ai_product_needs_evals.md)).

**Where it shows up in the workflow:**

| Activity | What you're reading |
| --- | --- |
| Error analysis (Phase 7) | Failing traces, plus a sample of passing ones |
| Judge calibration | Conversations to label pass/fail with a critique |
| Scenario design (Phase 1) | Real transcripts, to find cases the policy is silent on |
| Fine-tuning data | Candidate examples to keep, fix or drop |
| Production monitoring | Traces flagged by a dipping pass rate |

---

## 2. Buy or build? Hamel's review

From [*Curating LLM data*](https://hamel.dev/notes/llm/finetuning/data_cleaning.html):

| Tool | Hamel's take |
| --- | --- |
| **spaCy Prodigy** | His favorite pre-packaged tool, "the cleanest UI," but hard to customize for his needs |
| **Argilla** | LLM features were inadequate; couldn't do basic sorting and filtering; "LLM vs non-LLM functionality has very different APIs" |
| **Lilac** | Mostly a dataset viewer, not a labeling and curation tool; limited UI extensibility |

**His conclusion:** hackability and integration with your existing stack matter most. Vendor tools are built for generic labeling; LLM curation needs domain-specific views (the whole trace, tool calls, links to your systems), and you'll want to change them often. Building also avoids vendor lock-in.

**When building makes sense:** you look at data every week, your traces have domain structure (tools, policies, order data), and you want labels to flow straight into evals and fine-tuning. That describes almost any team shipping an LLM product.

---

## 3. Which framework

From the [general-purpose frameworks](https://hamel.dev/notes/llm/finetuning/data_cleaning.html#general-purpose-frameworks) section:

| Framework | Notes |
| --- | --- |
| [Gradio](https://www.gradio.app/) | Popular for ML demos |
| [Panel](https://panel.holoviz.org/) | HoloViz ecosystem |
| [Streamlit](https://streamlit.io/) | Hamel explicitly advises against it |
| **[Shiny for Python](https://shiny.posit.co/py/)** | **Hamel's pick** |

**Why Shiny, in Hamel's words and points:**
1. **Native integration with Quarto.**
2. **A powerful, responsive reactive model:** only the parts that depend on a changed input re-run.
3. **A minimalist API** that's easy to keep in your head.
4. **Excellent WASM support,** so apps can run in the browser and be embedded in web pages.

> "Shiny apps always required much less code and were easier to understand than the other frameworks."

---

## 4. Quarto

**Tagline:** "Analyze. Share. Reproduce. You have a story to tell with data — tell it with Quarto."

An open-source publishing system for technical work, often described as the successor to R Markdown:
- **Runs code** in Python, R, Julia and Observable JS, from Jupyter notebooks or plain markdown (`.qmd`).
- **Publishes** HTML, PDF, Word, ePub, and whole **websites and books**.
- **Interactive content** through Jupyter widgets, Observable JS and **Shiny**.
- **Reproducible:** re-render the document when the data changes, and every table and chart updates.

Hamel's own site, hamel.dev, is a good example of the style: notes and blog posts written as executable documents.

**How it fits eval work:**

| Use | How |
| --- | --- |
| **Eval report per run** | A `.qmd` that reads `runs/*.json` and renders pass-rate tables and charts; re-render after every run |
| **PR evidence** | Render the report to HTML and link it from the PR (the v1 → v4 table, the taxonomy) |
| **Team notes** | Error-analysis write-ups that include live code, not screenshots |
| **Embedded viewer** | A Shiny app inside the report, so readers can click from a failing number to the traces behind it |

---

## 5. What a good trace viewer needs

For the support bot, a viewer worth building in a day:

| Feature | Why |
| --- | --- |
| **The whole trace on one screen:** customer turns, bot turns, every tool call with inputs and outputs | Most bugs live in the tool calls, not the reply text |
| **Context next to it:** scenario, expected behavior, the policy rule, mock order data | So you can judge correctness without opening other systems |
| **Filters:** scenario, test, pass/fail, version, date | Jump straight to "failing `no_amount_before_preview` in v3" |
| **Random sample of passing traces** | Catches false passes from weak assertions |
| **One-click pass/fail + a critique box** | Labels and critiques feed judge calibration (Hamel's Critique Shadowing) |
| **Failure-category tags** | Builds the taxonomy while you read |
| **Keyboard shortcuts, next/previous** | Reading 100 traces should take an hour, not a day |
| **Version diff** | The same case in v2 vs. v3, side by side |
| **Save to files in the repo** (`labels.jsonl`, `taxonomy.md`) | Labels flow straight into evals, judges and fine-tuning data |
| **Links out:** trace ID to the tracing system, order ID to internal tools | One click to the full context |

Rechat's viewer for Lucy, described in Hamel's evals post, had the same idea: labels by feature and scenario, synthetic vs. real filters, links to the CRM and the trace, and editable outputs that became curated data.

### A minimal Shiny for Python sketch

Illustrative; adapt to your trace format.

```python
# viewer.py — run with: shiny run viewer.py
import json
from shiny import App, reactive, render, ui

TRACES = [json.loads(l) for l in open("traces/failing_v3.jsonl")]
CATEGORIES = ["wrong lateness math", "amount before preview", "mixed issue", "tone", "other"]

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("test", "Test", ["all"] + sorted({t["test"] for t in TRACES})),
        ui.input_radio_buttons("label", "Label", ["pass", "fail"], inline=True),
        ui.input_select("category", "Failure category", CATEGORIES),
        ui.input_text_area("critique", "Critique", rows=4),
        ui.input_action_button("save", "Save + next", class_="btn-primary"),
    ),
    ui.output_ui("trace"),
    title="Support bot trace viewer",
)

def server(input, output, session):
    idx = reactive.value(0)

    @reactive.calc
    def filtered():
        return [t for t in TRACES if input.test() in ("all", t["test"])]

    @render.ui
    def trace():
        rows = filtered()
        if not rows:
            return ui.p("No traces.")
        t = rows[idx() % len(rows)]
        turns = [ui.tags.pre(f'{s["role"]}: {s["content"]}') for s in t["steps"]]
        return ui.div(
            ui.h4(f'{t["scenario"]} · {t["test"]} · {t["version"]}'),
            ui.p(f'Expected: {t["expected"]}'),
            *turns,
        )

    @reactive.effect
    @reactive.event(input.save)
    def _():
        t = filtered()[idx() % len(filtered())]
        with open("labels.jsonl", "a") as f:
            f.write(json.dumps({"trace_id": t["id"], "label": input.label(),
                                "category": input.category(),
                                "critique": input.critique()}) + "\n")
        idx.set(idx() + 1)

app = App(app_ui, server)
```

About 50 lines gets you filtering, the full trace with context, pass/fail plus critique, a category tag, and labels saved to a file the rest of the workflow reads.

---

## 6. How this connects to the rest of the section

- **[Eval-driven development](../../blog/eval/eval_driven_development.md), Phase 7:** the viewer is how "read failing traces and a sample of passing traces" stays cheap enough to do every round.
- **Judge calibration** ([evals and observability](./evals_and_observability.md)): the critique box produces the expert labels and few-shot critiques a judge is aligned against.
- **[Level 1 unit tests](./level1_unit_tests.md):** each failure category tagged in the viewer becomes a candidate assertion.
- **DoorDash:** the simulator platform persists results for SQL queries and dashboards; the Ask DoorDash team uses background agents to cluster failures into reports. Both reduce the cost of looking — the same goal as a custom viewer.

---

## How to say it (about 30 seconds)

> "The highest-leverage habit in LLM work is reading data — Jason Wei's point is that great researchers read a lot of it and build tools to read it fast. So I'd build a small custom trace viewer rather than buy one: Hamel Husain tried Prodigy, Argilla and Lilac and found none flexible enough for LLM traces. A Shiny for Python app in a day shows the whole trace with tool calls next to the expected behavior, filters by test and version, samples passing traces too, and saves pass/fail labels with critiques straight into the files our evals and judges use. Quarto renders the eval report for each run, with the viewer embedded."
