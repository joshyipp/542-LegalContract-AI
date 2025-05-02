# LLM-Assisted Legal Contract Classification with LegalBERT Fine-Tuning

This project builds a scalable and cost-effective system for classifying legal contracts into well-defined categories. It leverages the high accuracy of large language models (LLMs) like GPT-4 for labeling, and trains a smaller transformer-based model (LegalBERT) for efficient downstream classification.

## Workflow

1. **Define Contract Taxonomy**
   - A detailed taxonomy of 16 contract types is created, each with inclusion and exclusion rules.

2. **LLM-Assisted Labeling (`LLM_tagging.ipynb`)**
   - A subset of unlabeled contract texts is sampled.
   - GPT-4 is prompted to classify each document based on the taxonomy.
   - Labels, confidence scores, and rationales are extracted.
   - Labeled data is manually spot-checked for quality.

3. **Model Pretraining and Fine-Tuning (`Predictive_Model.ipynb`)**
   - LegalBERT is first adapted to the domain using masked language modeling (MLM) on contract texts.
   - It is then fine-tuned using the LLM-labeled dataset for supervised classification.
   - A custom `WeightedTrainer` is used to apply weighted categorical cross-entropy loss for class imbalance.

---

## 📂 Files

- `LLM_tagging.ipynb`: Uses chatGPT to assign labels to contract snippets according to a taxonomy.
- `Predictive_Model.ipynb`: Fine-tunes LegalBERT using the labeled data.
- `CUAD_sampler.py`: script for sampling contracts from the CUAD set
- `combined_labels.csv`: The 5,000 contracts labeled by chatGPT

---

## 📊 Evaluation

The fine-tuned model achieves:
- **Accuracy**: 81.3%
- **Macro F1-score**: 0.79
- **Weighted F1-score**: 0.81
