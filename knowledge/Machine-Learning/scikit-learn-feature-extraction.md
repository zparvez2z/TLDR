---
source_url: https://scikit-learn.org/stable/modules/feature_extraction.html
author: Unknown
date: 30-07-2026
---

# 8.2. Feature extraction — scikit-learn 1.9.0 documentation

This guide explains how scikit-learn’s feature_extraction module transforms raw data (text, images, dicts) into numerical features suitable for machine learning models. It distinguishes feature extraction from feature selection and details tools for categorical, hashed, and text features. Key components include DictVectorizer for one-hot encoding of mappings, FeatureHasher for fast, low-memory hashing, and standard text vectorization via Bag-of-Words and TF-IDF. The module emphasizes sparse representations for scalability and provides practical guidance on input formats, parameter choices, and trade-offs.
- Feature extraction converts arbitrary data (e.g., text, images, dicts) into numeric feature vectors; it is distinct from feature selection.
- DictVectorizer transforms lists of Python dicts into sparse matrices, performing one-hot encoding for categorical features and handling multi-valued features.
- Sparse output (scipy.sparse) is used by default to manage very wide, mostly zero matrices.
- FeatureHasher implements the hashing trick for high-speed, low-memory vectorization, sacrificing inspectability (no inverse_transform).
- Uses signed MurmurHash3 (32-bit) with alternate_sign=True by default to mitigate collision bias; can disable for estimators expecting non-negative inputs (e.g., MultinomialNB, chi2 selectors).
- Accepts mappings, (feature, value) pairs, or strings via input_type, and sums repeated feature values per sample; outputs CSR sparse matrices.
- Recommended to choose n_features as a power of two for even feature distribution; practical limit up to 2^31 - 1 features.
- Text feature extraction includes tokenization, counting (Bag-of-Words), and weighting via TF-IDF (e.g., CountVectorizer + TfidfTransformer).
- Generators can introduce lazy feature extraction for efficiency in NLP pipelines.
- Appropriate for large corpora and sequence labeling tasks (e.g., PoS-context windows) with memory-efficient representations.