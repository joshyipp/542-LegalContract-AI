# 542-LegalContract-AI


## 📓 Notebooks Overview

This repository supports the DL4DS Legal Contract Dataset project, which aims to segment, classify, and summarize clauses in legal contracts. The following Jupyter notebooks contain the core experimentation and implementation logic for clause-level NLP.

---

### `clause_condenser.ipynb`

A notebook focused on **clause summarization and condensation**. It includes:

- Experiments with sentence embedding models to identify the most semantically meaningful parts of a clause.
- Techniques for reducing verbose legal text while preserving critical meaning.
- A foundation for developing tools to support legal professionals in reviewing and simplifying contracts.

---

### `segmentation_fixed.ipynb`

A notebook implementing a **hybrid clause segmentation pipeline**. It includes:

- Rule-based boundary detection using legal-specific regex patterns (e.g., numbered headers, all-caps titles).
- Semantic boundary detection using `SentenceTransformer` embeddings to find natural shifts in meaning.
- A merged strategy for splitting full-text contracts into discrete clause units, ready for classification.
- Output examples and evaluation techniques to ensure segmentation quality.

---

These notebooks are central to building a high-quality, labeled clause dataset and support future tasks such as clause classification, polarity detection, and summarization.
