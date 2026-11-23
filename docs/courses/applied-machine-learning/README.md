---
title: "Applied Machine Learning (AML)"
icon: material/slot-machine
url_img: "assets/images/ods_stickers.jpg"
color: "#eca62f"
---

{% include 'includes/banner.html' %}

## I. Course Introduction

**Description.** This course provides a comprehensive overview of Machine Learning (ML), bridging foundational theory and practical implementation. The curriculum focuses on core techniques and algorithms, enabling learners to master data exploration, preprocessing, and systematic model development. Alongside theoretical foundations, the course offers step-by-step guidance on training, tuning, and evaluating end-to-end ML models through hands-on exercises.

**Target Audience.** Designed for beginners entering the fields of Artificial Intelligence and Machine Learning. Learners with existing foundational knowledge can also use this material as a structured, practical reference.

**Structure.** Designed, synthesized, and organized into 5 core modules, progressing from theoretical foundations to real-world model deployment. Detailed lesson contents are outlined in the [[syllabus](#aml-syllabus)]:

- **Module 01. Overview & Environment** (ML fundamentals and development environment setup).
- **Module 02. EDA & Preprocessing** (exploratory data analysis and preprocessing techniques).
- **Module 03. Supervised Learning** (supervised learning algorithms).
- **Module 04. Unsupervised Learning** (unsupervised learning algorithms).
- **Module 05. Pipelines & Deployment** (workflow automation and model deployment).

## II. What will you learn?

Upon completing this course, you will be able to:

- Master the mathematical principles and mechanics of core ML algorithms, including Linear Regression, Support Vector Machines, Decision Trees, and K-Means Clustering.
- Apply exploratory data analysis (EDA), data cleaning, class imbalance handling, and feature engineering techniques.
- Execute end-to-end workflows for model building, cross-validation, and hyperparameter tuning from raw data to evaluation.
- Implement models proficiently in Python using standard scientific libraries: Scikit-learn, NumPy, Pandas, and Matplotlib.

## III. Requirements

To get the most out of this course, learners should have the following foundational background:

- **Basic Python Programming:** Familiarity with core data structures, loops, functions, and basic object-oriented programming (prior exposure to NumPy and Pandas is a plus).
- **Foundational Mathematics:** Working knowledge of linear algebra (matrices, vectors), calculus (derivatives, gradients), and probability & statistics.
- **Experimental Mindset:** Willingness to read technical documentation, execute code, and analyze experimental results on real-world datasets.

## IV. Syllabus { #aml-syllabus }

| Lecture | Status | Resources |
| :------ | :----: | :-------: |
| ^^**Module 01. Overview & Environment**^^ | | |
| **Lecture 01. Introduction to ML**<ul markdown="1"><li>ML taxonomy: Supervised, Unsupervised, and Reinforcement Learning</li><li>Problem formulation & real-world challenges</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 02. ML Development Roadmap**<ul markdown="1"><li>End-to-end ML lifecycle</li><li>Core pillars: Data, Model, Compute</li><li>MLOps fundamentals</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 03. Python for Data Science**<ul markdown="1"><li>Environment setup: Anaconda, Jupyter, Google Colab</li><li>Core ecosystem: NumPy (linear algebra), Pandas (data manipulation), Matplotlib (visualization)</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 02. EDA & Preprocessing**^^ | | |
| **Lecture 04. Exploratory Data Analysis (EDA)**<ul markdown="1"><li>Univariate & multivariate analysis</li><li>Distribution visualization & correlation matrix</li><li>Data splitting & leakage: Train/Validation/Test strategies and preventing data leakage</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 05. Data Cleaning & Preprocessing**<ul markdown="1"><li>Outlier detection & handling</li><li>Imputation & deduplication</li><li>Handling imbalanced data on the training set</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 06. Feature Engineering**<ul markdown="1"><li>Feature selection: RFE, Feature Importance</li><li>Feature transformation: scaling, encoding</li><li>Feature creation & extraction</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 03. Supervised Learning**^^ | | |
| **Lecture 07. Linear Models**<ul markdown="1"><li>Linear & Logistic Regression</li><li>Optimization methods: Gradient Descent, Normal Equation</li><li>Regularization: Ridge (L2), Lasso (L1), Elastic Net</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 08. Support Vector Machines**<ul markdown="1"><li>Hard Margin & Soft Margin principles</li><li>Kernel Trick & non-linear classification</li></ul> | :material-check-circle-outline: Ready | [[notes]({{ config.site_url }}{{ links.aml.les08 }})] [[code]({{ config.site_url }}{{ links.aml.les08 }}#implementation)] |
| **Lecture 09. Tree-based Models**<ul markdown="1"><li>Decision Tree architectures: CART, ID3</li><li>Ensemble learning: Random Forest, Gradient Boosting</li><li>Overfitting & pruning strategies</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 10. Instance-based & Probabilistic Models**<ul markdown="1"><li>k-Nearest Neighbors (k-NN) & distance metrics</li><li>Probabilistic classification with Naive Bayes (Gaussian, Multinomial)</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 04. Unsupervised Learning**^^ | | |
| **Lecture 11. Clustering Algorithms**<ul markdown="1"><li>Centroid-based clustering: K-Means, K-Medoids</li><li>Density-based clustering: DBSCAN</li><li>Clustering evaluation: Silhouette Score</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 12. Dimensionality Reduction**<ul markdown="1"><li>Principal Component Analysis (PCA)</li><li>t-SNE & manifold learning</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 05. Pipelines & Deployment**^^ | | |
| **Lecture 13. Model Evaluation & Tuning**<ul markdown="1"><li>Cross-validation: K-Fold, Stratified K-Fold</li><li>Hyperparameter tuning: GridSearch, RandomSearch</li><li>Evaluation metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 14. ML Pipelines & Deployment**<ul markdown="1"><li>Scikit-learn pipelines (bundling preprocessing & training workflows)</li><li>Model serialization: Pickle, Joblib</li><li>API serving & basic deployment strategies</li></ul> | :material-clock-outline: Coming soon | — |

## V. References

The course content is referenced, synthesized, and systematized from classic textbooks and reputable academic resources in Machine Learning, covering statistical foundations and algorithmic intuition [@james2021introduction], advanced probabilistic theory [@bishop2006pattern], Stanford's optimization lecture series [@ng2000cs229], and practical engineering patterns for deploying ML pipelines [@geron2022hands].

\bibliography