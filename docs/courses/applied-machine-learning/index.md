---
title: "Applied Machine Learning (AML)"
icon: material/brain
url_img: "assets/images/ods_stickers.jpg"
color: "#eca62f"
---

{% include 'includes/banner.html' %}

<div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 6px; line-height: 0; width: 100%; margin: 12px 0;">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://numpy.org"><img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white" alt="NumPy"></a>
  <a href="https://pandas.pydata.org"><img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas"></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" alt="scikit-learn"></a>
  <a href="https://matplotlib.org"><img src="https://img.shields.io/badge/Matplotlib-11557c?style=flat&logo=python&logoColor=white" alt="Matplotlib"></a>
  <a href="https://seaborn.pydata.org"><img src="https://img.shields.io/badge/Seaborn-4c72b0?style=flat&logo=python&logoColor=white" alt="Seaborn"></a>
  <a href="https://colab.research.google.com"><img src="https://img.shields.io/badge/Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white" alt="Colab"></a>
  <a href="https://www.kaggle.com"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=flat&logo=kaggle&logoColor=white" alt="Kaggle"></a>
</div>

## Course Introduction

**Description.** This course provides a comprehensive overview of Machine Learning (ML), bridging foundational theory and practical implementation. The curriculum focuses on core techniques and algorithms, enabling learners to master exploratory data analysis, data preprocessing, and systematic model development. Alongside theoretical foundations, it offers step-by-step guidance on training, tuning, and evaluating end-to-end ML models through hands-on practice.

**Target Audience.** Designed for beginners entering the fields of Artificial Intelligence (AI) and Machine Learning. Learners with existing foundational knowledge can also use this material as a structured, practical reference.

**Structure.** Designed into 5 core modules, progressing from theoretical foundations to real-world deployment, detailed in [[syllabus](#aml-syllabus)]:

- **Module 01. Overview & Environment:** ML fundamentals and workspace environment setup.
- **Module 02. EDA & Preprocessing:** Data exploration, cleaning, and feature engineering.
- **Module 03. Supervised Learning:** Model evaluation & cross-validation, regression/classification algorithms, and hyperparameter tuning.
- **Module 04. Unsupervised Learning:** Clustering algorithms and dimensionality reduction techniques.
- **Module 05. Pipelines & Deployment:** End-to-end workflow automation with Pipelines and API-based model deployment.

## What will you learn?

Upon completing this course, you will be able to:

- Master the mathematical principles and mechanics of core ML algorithms: Linear Regression, Support Vector Machines (SVM), Decision Trees, and k-Means Clustering.
- Proficiently apply exploratory data analysis (EDA), data cleaning, class imbalance handling, and feature engineering techniques.
- Master the end-to-end workflow for model building, cross-validation, and hyperparameter tuning from raw data to final evaluation.
- Proficiently implement models in Python using standard scientific libraries: Scikit-learn, NumPy, Pandas, and Matplotlib.

## Prerequisites

To get the most out of this course, learners should prepare the following foundational background:

- **Python Programming:** Familiarity with core data structures, loops, functions, and basic object-oriented programming (OOP); prior exposure to NumPy and Pandas is a plus.
- **Foundational Mathematics:** Basic working knowledge of linear algebra (matrices, vectors), calculus (derivatives, gradients), and probability & statistics.
- **Experimental Mindset:** Willingness to read technical documentation, execute code, and analyze experimental results on real-world datasets.

## Syllabus { #aml-syllabus }

| Lecture | Status | Resources |
| :------ | :--------: | :--------: |
| ^^**Module 01. Overview & Environment**^^ | | |
| **Lecture 01. Introduction to ML**<ul markdown="1"><li>ML taxonomy: Supervised, Unsupervised, and Reinforcement Learning</li><li>Problem formulation & core engineering challenges</li></ul> | :material-clock-outline: | — |
| **Lecture 02. ML Development Roadmap**<ul markdown="1"><li>End-to-end ML lifecycle</li><li>Core pillars: Data, Model, and Compute</li><li>MLOps fundamentals (Machine Learning Operations)</li></ul> | :material-clock-outline: | — |
| **Lecture 03. Python for Data Science**<ul markdown="1"><li>Environment setup: Anaconda, Jupyter, Google Colab, and Kaggle</li><li>Core ecosystem: NumPy (linear algebra), Pandas (data manipulation), Matplotlib & Seaborn (visualization)</li></ul> | :material-clock-outline: | — |
| ^^**Module 02. EDA & Preprocessing**^^ | | |
| **Lecture 04. Exploratory Data Analysis (EDA)**<ul markdown="1"><li>Univariate & multivariate analysis</li><li>Distribution visualization & correlation matrix</li><li>Data splitting strategies (Train/Val/Test) & data leakage prevention</li></ul> | :material-clock-outline: | — |
| **Lecture 05. Data Cleaning & Preprocessing**<ul markdown="1"><li>Outlier detection & handling</li><li>Missing data imputation & deduplication</li><li>Class imbalance handling techniques</li></ul> | :material-clock-outline: | — |
| **Lecture 06. Feature Engineering**<ul markdown="1"><li>Feature selection: RFE (Recursive Feature Elimination), Feature Importance</li><li>Feature transformation: Scaling, Encoding</li><li>Feature creation & extraction</li></ul> | :material-clock-outline: | — |
| ^^**Module 03. Supervised Learning**^^ | | |
| **Lecture 07. Model Evaluation & Cross-Validation**<ul markdown="1"><li>Bias-Variance Tradeoff & Learning Curves</li><li>Cross-validation strategies: K-Fold, Stratified K-Fold</li><li>Evaluation metrics: Regression (MAE, MSE, RMSE, $R^2$) & Classification (Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC, PR-AUC)</li></ul> | :material-clock-outline: | — |
| **Lecture 08. Linear Models**<ul markdown="1"><li>Linear & Logistic Regression</li><li>Optimization methods: Gradient Descent, Normal Equation</li><li>Regularization: Ridge (L2), Lasso (L1), Elastic Net</li></ul> | :material-clock-outline: | — |
| **Lecture 09. Support Vector Machines (SVM)**<ul markdown="1"><li>Hard Margin & Soft Margin principles</li><li>Kernel Trick & non-linear classification</li></ul> | :material-check-circle: | [[notes]({{ config.site_url }}{{ links.aml.les09 }})] [[code]({{ config.site_url }}{{ links.aml.les09 }}#implementation)] |
| **Lecture 10. Tree-based Models**<ul markdown="1"><li>Decision Tree architectures: CART, ID3</li><li>Ensemble learning: Random Forest, Gradient Boosting</li><li>Overfitting control & pruning strategies</li></ul> | :material-check-circle: | [[notes]({{ config.site_url }}{{ links.aml.les10 }})] |
| **Lecture 11. Instance-based & Probabilistic Models**<ul markdown="1"><li>k-Nearest Neighbors (k-NN) & distance metrics</li><li>Probabilistic classification with Naive Bayes (Gaussian, Multinomial)</li></ul> | :material-clock-outline: | — |
| **Lecture 12. Hyperparameter Tuning & Model Selection**<ul markdown="1"><li>Model Parameters vs. Hyperparameters</li><li>Hyperparameter search strategies: Grid Search, Random Search</li><li>Model comparison and selection workflows</li></ul> | :material-clock-outline: | — |
| ^^**Module 04. Unsupervised Learning**^^ | | |
| **Lecture 13. Clustering Algorithms**<ul markdown="1"><li>Centroid-based clustering: k-Means, k-Medoids</li><li>Density-based clustering: DBSCAN</li><li>Clustering evaluation with Silhouette Score</li></ul> | :material-clock-outline: | — |
| **Lecture 14. Dimensionality Reduction**<ul markdown="1"><li>Principal Component Analysis (PCA)</li><li>Non-linear dimensionality reduction & manifold learning with t-SNE</li></ul> | :material-clock-outline: | — |
| ^^**Module 05. Pipelines & Deployment**^^ | | |
| **Lecture 15. ML Pipelines & Deployment**<ul markdown="1"><li>Automating preprocessing & training with Scikit-learn Pipelines</li><li>Model serialization: Pickle, Joblib</li><li>API serving fundamentals & model deployment</li></ul> | :material-clock-outline: | — |

## References

The course content is referenced, synthesized, and systematized from classic textbooks and reputable academic resources in Machine Learning, covering statistical foundations and algorithmic intuition [@james2021introduction], advanced probabilistic theory [@bishop2006pattern], Stanford's optimization lecture series [@ng2000cs229], and practical engineering patterns for deploying ML pipelines [@geron2022hands].

\bibliography
