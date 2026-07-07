# FlyRank ML Internship — Zain ul Abdeen

**Applied Search Intelligence: Google Search Ranking & Discoverability**

---

## Assignment 1 — Submission Context

> **Intern:** Zain ul Abdeen · **Repo:** [`Zain-ul-abdeen-773/flyrank-ml-internship`](https://github.com/Zain-ul-abdeen-773/flyrank-ml-internship)

### ✅ What was completed

| Requirement | Status | Details |
|---|---|---|
| Pipeline ran end-to-end | ✅ | `python scripts/run_all.py` — 30,000 rows, 5 steps, all passing |
| Notebook 01 executed top to bottom | ✅ | [`notebooks/01_first_look_and_discovery.ipynb`](notebooks/01_first_look_and_discovery.ipynb) |
| Notebook 02 executed top to bottom | ✅ | [`notebooks/02_your_first_readable_model.ipynb`](notebooks/02_your_first_readable_model.ipynb) |
| "Your turn" cell attempted (NB01) | ✅ | Discovery D — see below |
| "Your turn" cell attempted (NB02) | ✅ | Depth & feature experiments — see below |
| Public repo | ✅ | Visible at the link above |
| No private data committed | ✅ | `scripts/` untouched, CI leak-guard intact |

### Key pipeline result

```
Hand-written rule   Precision@50: 0.240   (~12 of the top 50 right)
Random forest       Precision@50: 0.740   (~37 of the top 50 right)
→ ~3.1x lift · split: client_holdout · best model: random_forest
```

### Notebook 01 — "Your turn" discovery (cell 8)

**Discovery D: Does `content_age_days` relate to `trend_direction`?**

- Declining pages have a **lower** median content age (216 days) than stable (300) or up (291.5) pages — younger content declines more, contradicting the "old content decays" intuition.
- `avg_position` vs `ctr` correlation: **−0.073** — directionally negative but weak; position alone doesn't explain CTR variation.
- Declining rate by age tier: 31–90 days (0.669) → 365+ days (0.426) — newer-to-mid content shows the highest decline rates in this dataset.

### Notebook 02 — "Your turn" experiment (cell 7)

**Experiment 1: Effect of `max_depth` on Precision@50 (in-sample)**

| max_depth | Precision@50 |
|---|---|
| 2 | 0.720 |
| 3 | 0.680 |
| 4 | 0.660 |

Deeper ≠ better in-sample here — the depth-2 tree already captures the main signal, and extra splits overfit to noise. The depth-3 tree is still readable (first split: `impressions_90d ≤ 5.50`, then `content_age_days`).

**Experiment 2: Alternative feature set** (dropped `impressions_90d` and `word_count`, added `engagement_rate` and `scroll_rate`)

- Precision@50 dropped to **0.560** — `impressions_90d` was carrying important signal.
- First split changed to `avg_position ≤ 0.55` → feature choice fundamentally reshapes the model.
- All results are in-sample; the real evaluation uses client-holdout (`scripts/03_train_model.py`).

---

This is the starting point for the FlyRank ML Internship. You **clone it**, build your work in
**your own public repo**, and share that repo URL with Assignment 1 — it's your workspace, your
submission, and your portfolio all at once. Everything you build stays there; we review it all
in one pass at the end of the track.

Everything here runs on a small **anonymized** slice of real FlyRank search data. No credentials,
no private client data, no setup headaches.

> **New here?** Two reads: **[SETUP.md](SETUP.md)** (GitHub, Colab, and data access — ten
> minutes, with every silent pitfall flagged), then **[GUIDE.md](GUIDE.md)** (every file
> explained, what to edit vs. leave alone, and where your own work goes — five minutes).

---

## Quickstart — first win in 2 minutes

The fastest path is Google Colab (one click, zero install). Open Notebook 1 and run all cells:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/flyrank-bih/flyrank-ml-internship-starter/blob/main/notebooks/01_first_look_and_discovery.ipynb)
 **Week 1 — Run it, then discover a real truth yourself**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/flyrank-bih/flyrank-ml-internship-starter/blob/main/notebooks/02_your_first_readable_model.ipynb)
 **Week 2 — The model is just a rule you can read**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/flyrank-bih/flyrank-ml-internship-starter/blob/main/notebooks/03_working_with_the_full_release.ipynb)
 **Weeks 3+ — The full release (~79M rows) via DuckDB, no download needed** — hosted at
 [`FlyRank/internship-warehouse`](https://huggingface.co/datasets/FlyRank/internship-warehouse) (gated: request access + accept the data-use terms, approval is instant)

### Prefer local?

```bash
git clone <this-repo-url>
cd flyrank-ml-internship-starter
pip install -r requirements.txt          # or: uv pip install -r requirements.txt
python scripts/run_all.py
```

That runs the whole pipeline on the bundled sample and writes results to `outputs/`.

---

## What you get

| Path | What it is |
|---|---|
| `notebooks/` | Week 1–2 **first-win notebooks** (Colab-ready). Start here. |
| `scripts/01–05` + `run_all.py` | The runnable reference pipeline: prepare → baseline → train → evaluate → PDF. |
| `data/raw/content_refresh_anonymized.csv` | The anonymized starter dataset (~30k pages). |
| `outputs/` | Example outputs so you can see the **target shape** (`model_report.md`, `refresh_queue_sample.csv`, `charts/`). |
| `work/` | **Your space.** Lane experiments and your capstone live here — see `work/README.md`. |
| `docs/` | The core docs + the data dictionary (see below). |

### Read these (in `docs/`)

1. **`ml-core-foundation-framework.md`** — the first-principles map of ML as a whole system. The backbone of the live sessions.
2. **`ml-intern-dataset-and-lane-guide.md`** — how to use the data safely, the capstone workflow, and the analysis "lanes" you can pick from.
3. **`intern-free-tooling-guide.md`** — the zero-budget tool stack (Python, Colab, free AI assistants). You never need to pay for anything.
4. **`data-dictionary.md`** — all 44 columns: meaning, scale, and gotchas. Keep it open while you work.

---

## The pipeline (what `run_all.py` does)

```text
01_prepare_features.py   clean + build the feature vector, define the label
02_baseline_score.py     a transparent hand-rule "fix this first" score
03_train_model.py        logistic regression, decision tree, random forest (client-holdout split)
04_evaluate_and_export.py  ranked queue + charts + Markdown report
05_build_pdf_report.py   a shareable PDF summary
```

On the bundled sample, the learned model clearly beats the hand-written rule at picking the right
pages to review first (**Precision@50 ≈ 0.24 → 0.74**; the model number can land 0.68–0.74
depending on library versions — the ~3x lift is the point). The notebooks compute these numbers
live, so they always reflect the current data and environment.

**Teaching point:** the model is the capstone, but the *workflow* is the lesson —
`problem framing → data cleaning → baseline → first model → evaluation → explainable recommendation`.

---

## Data safety (read `DATA_USE.md`)

- Only the small **anonymized** CSV ships here — no client names, domains, URLs, titles, or keywords.
- **Never** add raw private client data to this repo or your fork. Need more data? Request an approved
  release from your mentor — never export it yourself.
- Don't paste client data into third-party AI tools.
- Frame every result as **observed / measured / directional / decision-support** — never
  "I predicted Google's algorithm."

The `.gitignore` blocks datasets by default, and grading checks that no dataset was committed.

---

## Assignments & schedule

Weekly assignments, live events, and the capstone rubric live on the **InternHQ board** at
`internhq.flyrank.ai` (your enrollment email has your access). This repo is the shared technical
foundation they all build on.

**First time with GitHub?** You need exactly four things (full walkthrough: [SETUP.md](SETUP.md)):
1. A free account at github.com.
2. Your own copy of this repo: **Use this template → Create a new repository** → public.
   (One click — brings the notebooks, `work/`, and the CI leak-guard with it.)
3. In Colab: *File → Save a copy in GitHub* → pick your copy, branch `main` (Colab handles auth).
4. That's your submission repo — share its **github.com/you/your-repo** URL with Assignment 1
   (never a colab.research.google.com or drive.google.com link).

---

*Track leads: Mirza Ašćerić (ML) · Hole (data engineering). Code under MIT (see `LICENSE`); data under `DATA_USE.md`.*
