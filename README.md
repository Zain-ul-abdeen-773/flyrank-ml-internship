# FlyRank ML Internship — Zain ul Abdeen

Applied Search Intelligence · Google Search Ranking & Discoverability
---
A compact, runnable internship workspace demonstrating end-to-end data → model → evaluation for search page refresh prioritization. This repository contains executed notebooks, a small anonymized sample dataset, a reproducible pipeline, and an experimental research helper (research_scout.py).

Quick links
- Notebooks: notebooks/01_first_look_and_discovery.ipynb, notebooks/02_your_first_readable_model.ipynb
- Pipeline: scripts/run_all.py (01_prepare_features → 05_build_pdf_report)
- Outputs: outputs/ (example model_report.md, refresh_queue_sample.csv, charts/)
- Data: data/raw/content_refresh_anonymized.csv (anonymized sample)
- New helper: research_scout.py — small scripted agent for quick paper + repo scouting

Highlights — what I ran & found
- Pipeline executed end-to-end on the included sample (30k rows).
- Best model (random forest) achieved a strong lift over the handwritten baseline:
  ```
  Hand-written rule   Precision@50: 0.240   (~12 of the top 50 right)
  Random forest       Precision@50: 0.740   (~37 of the top 50 right)
  → ~3.1x lift · split: client_holdout · best model: random_forest
  ```
- Notebooks executed top-to-bottom; the “Your turn” cells include concrete discoveries and experiments (see Notebook 01 & Notebook 02).

Why this repo exists
- Teaching point: the model is the capstone — the real lesson is the reproducible workflow:
  problem framing → data cleaning → baseline → explainable first model → evaluation → production-style ranked export.
- Safe, anonymized starter data: learn the full flow without exposing client data.

Quickstart — first win (2 minutes)
- Google Colab (one-click): open either notebook and "Save a copy in GitHub" to your own public fork, then run top-to-bottom.
- Local:
  ```bash
  git clone https://github.com/Zain-ul-abdeen-773/flyrank-ml-internship.git
  cd flyrank-ml-internship
  python -m pip install -r requirements.txt
  python scripts/run_all.py
  ```
  That runs the pipeline on the bundled sample and writes results to outputs/.

What's new in this fork (tailored to this submission)
- Executed notebooks are included, with documented discoveries and experiments.
- research_scout.py: a small scripted agent that fetches arXiv abstracts and searches GitHub for related repos — useful for lightweight research scouting (see `python research_scout.py`).
- Clean, public repo ready for assignment submission and portfolio review.

Files & structure (important paths)
- notebooks/ — interactive analysis / reporting (Colab-ready)
- scripts/
  - 01_prepare_features.py — clean + build feature vector
  - 02_baseline_score.py — transparent hand-rule baseline
  - 03_train_model.py — train (logistic, tree, random forest) with client-holdout split
  - 04_evaluate_and_export.py — ranked queue, charts, markdown report
  - 05_build_pdf_report.py — produce PDF summary
  - run_all.py — runs the pipeline end-to-end
- data/raw/content_refresh_anonymized.csv — anonymized starter dataset (~30k rows)
- outputs/ — example outputs to show target artifact shapes
- work/ — your experimentation space (use this for your assignment)
- docs/ — design notes, data dictionary, and guides (SETUP.md, GUIDE.md, DATA_USE.md)
- research_scout.py — research helper that queries arXiv and GitHub for topical repos

Safety & data use
- Only an anonymized sample CSV is included. NEVER commit private client data to this repo or your fork.
- See DATA_USE.md for the full policy and handling rules.
- The repository's .gitignore prevents committing large/secret files; grading checks validate this.

Running research_scout.py (short)
- Purpose: small utility to fetch recent arXiv hits and quickly locate related GitHub repos.
- Run:
  ```bash
  python research_scout.py
  ```
- Note: it uses unauthenticated HTTP requests (arXiv + GitHub), so rate limits may apply. For heavy usage, add proper API auth.

Recommended next steps for your repo
1. Fork this repo into your GitHub account and keep it public (this is how the internship submission is collected).
2. In Colab: File → Save a copy in GitHub → choose your fork and branch main (Colab handles the auth).
3. Run notebooks and iterate in work/ — keep experiments, notebooks, and final write-ups under work/.
4. When ready, share your fork URL as your Assignment 1 submission.

Contributing & contact
- This repository is your personal submission; if others contribute, keep a clean commit history and document experiments in work/.
- License: MIT (see LICENSE)
- Questions: open an Issue in your fork or contact the track leads named in GUIDE.md.

Acknowledgements
- Starter curriculum & pipeline adapted from FlyRank internship materials.
- Track leads: Mirza Ašćerić (ML) · Hole (Data Engineering).

Changelog (this README)
- Rewritten to be concise, modern, and actionable; added explicit quickstart, file map, and notes about the included research_scout.py utility.
