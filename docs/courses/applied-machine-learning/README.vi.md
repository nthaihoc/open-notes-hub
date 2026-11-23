---
title: "Applied Machine Learning (AML)"
icon: material/slot-machine
url_img: "assets/images/ods_stickers.jpg"
color: "#eca62f"
---

{% include 'includes/banner.html' %}

## I. Course Introduction

**Mô tả.** Khóa học này cung cấp cho người học cái nhìn tổng quan và toàn diện về lĩnh vực Machine Learning (học máy - ML) từ lý thuyết nền tảng đến thực hành triển khai. Nội dung tập trung vào các kỹ thuật và thuật toán cốt lõi, giúp người học nắm vững quy trình khám phá, tiền xử lý dữ liệu và xây dựng mô hình một cách bài bản, có hệ thống. Bên cạnh lý thuyết, khóa học hướng dẫn từng bước cách huấn luyện, tinh chỉnh và đánh giá mô hình ML hoàn chỉnh thông qua các ví dụ thực hành.

**Đối tượng.** Phù hợp với người mới bắt đầu làm quen với Trí tuệ nhân tạo và Học máy. Ngoài ra, những người đã có kiến thức nền tảng có thể sử dụng tài liệu này như một nguồn tham khảo hệ thống và thực tiễn.

**Cấu trúc.** Khóa học được thiết kế, tổng hợp và chia thành 5 Module chính, đi từ nền tảng lý thuyết đến thực hành triển khai mô hình trong thực tế. Nội dung chi tiết từng bài học được trình bày tại [[syllabus](#aml-syllabus)]:

- **Module 01. Overview & Environment** (tổng quan về học máy và môi trường phát triển).
- **Module 02. EDA & Preprocessing** (khám phá và tiền xử lý dữ liệu).
- **Module 03. Supervised Learning** (các thuật toán học có giám sát).
- **Module 04. Unsupervised Learning** (các thuật toán học không giám sát).
- **Module 05. Pipelines & Deployment** (đóng gói quy trình và triển khai mô hình).

## II. What will you learn?

Sau khi hoàn thành khóa học này, bạn có thể đạt được các mục tiêu sau:

- Nắm vững nguyên lý toán học và cơ chế hoạt động của các thuật toán ML cốt lõi như Linear Regression, Support Vector Machines, Decision Trees, K-Means Clustering.
- Thành thạo kỹ thuật phân tích khám phá (EDA), làm sạch, xử lý mất cân bằng và trích xuất đặc trưng dữ liệu.
- Làm chủ quy trình xây dựng, kiểm thử chéo và tối ưu hóa siêu tham số mô hình từ dữ liệu thô đến đánh giá kết quả.
- Triển khai thành thạo mô hình bằng Python cùng hệ sinh thái thư viện chuẩn: Scikit-learn, NumPy, Pandas, Matplotlib.

## III. Requirements

Để tiếp cận nội dung khóa học một cách thuận lợi, người học cần chuẩn bị sẵn một số nền tảng cơ bản:

- **Lập trình Python cơ bản:** Nắm được cấu trúc dữ liệu, vòng lặp, hàm và lập trình hướng đối tượng cơ bản (đã từng làm quen với NumPy và Pandas là một lợi thế).
- **Toán học nền tảng:** Có kiến thức cơ sở về đại số tuyến tính (ma trận, vector), giải tích (đạo hàm, gradient) và xác suất thống kê.
- **Tư duy thực nghiệm:** Sẵn sàng đọc tài liệu kỹ thuật, tự chạy mã nguồn và phân tích kết quả thực nghiệm trên tập dữ liệu thực tế.

## IV. Syllabus { #aml-syllabus }

| Lecture | Status | Resources |
| :------ | :----: | :-------: |
| ^^**Module 01. Overview & Environment**^^ | | |
| **Lecture 01. Introduction to ML**<ul markdown="1"><li>ML taxonomy: Supervised, Unsupervised, Reinforcement Learning (phân loại học máy)</li><li>Problem formulation & real-world challenges (định hình bài toán & thách thức thực tế)</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 02. ML Development Roadmap**<ul markdown="1"><li>End-to-end ML lifecycle (vòng đời phát triển mô hình)</li><li>Core pillars: Data, Model, Compute (ba trụ cột cốt lõi)</li><li>MLOps fundamentals (nhập môn vận hành học máy)</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 03. Python for Data Science**<ul markdown="1"><li>Environment setup: Anaconda, Jupyter, Google Colab</li><li>Core ecosystem: NumPy (đại số), Pandas (xử lý dữ liệu), Matplotlib (trực quan hóa)</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 02. EDA & Preprocessing**^^ | | |
| **Lecture 04. Exploratory Data Analysis (EDA)**<ul markdown="1"><li>Univariate & multivariate analysis (phân tích đơn biến & đa biến)</li><li>Distribution visualization & correlation matrix (trực quan hóa phân phối & ma trận tương quan)</li><li>Data splitting & leakage: chiến lược chia tập Train/Validation/Test và chống rò rỉ dữ liệu</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 05. Data Cleaning & Preprocessing**<ul markdown="1"><li>Outlier handling (phát hiện & xử lý dữ liệu ngoại lai)</li><li>Imputation & deduplication (điền dữ liệu khuyết thiếu & khử trùng lặp)</li><li>Imbalanced data (xử lý mất cân bằng dữ liệu trên tập Train)</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 06. Feature Engineering**<ul markdown="1"><li>Feature selection: RFE, Feature Importance (chọn lọc đặc trưng)</li><li>Feature transformation: scaling, encoding (biến đổi & chuẩn hóa đặc trưng)</li><li>Feature creation & extraction (tạo mới & trích xuất đặc trưng)</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 03. Supervised Learning**^^ | | |
| **Lecture 07. Linear Models**<ul markdown="1"><li>Linear & Logistic Regression (hồi quy tuyến tính & hồi quy logistic)</li><li>Optimization methods: Gradient Descent, Normal Equation</li><li>Regularization: Ridge (L2), Lasso (L1), Elastic Net</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 08. Support Vector Machines**<ul markdown="1"><li>Hard Margin & Soft Margin (nguyên lý biên cứng & biên mềm)</li><li>Kernel Trick & non-linear classification (thủ thuật hạt nhân & bài toán phi tuyến)</li></ul> | :material-check-circle-outline: Ready | [[notes]({{ config.site_url }}{{ links.aml.les08 }})] [[code]({{ config.site_url }}{{ links.aml.les08 }}#implementation)] |
| **Lecture 09. Tree-based Models**<ul markdown="1"><li>Decision Tree architectures: CART, ID3 (cấu trúc cây quyết định)</li><li>Ensemble learning: Random Forest, Gradient Boosting</li><li>Overfitting & pruning (kiểm soát quá khớp & chiến lược cắt tỉa cây)</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 10. Instance-based & Probabilistic Models**<ul markdown="1"><li>k-Nearest Neighbors (k-NN) & distance metrics (thuật toán láng giềng gần nhất & độ đo khoảng cách)</li><li>Naive Bayes: phân lớp xác suất với Gaussian, Multinomial</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 04. Unsupervised Learning**^^ | | |
| **Lecture 11. Clustering Algorithms**<ul markdown="1"><li>Centroid-based clustering: K-Means, K-Medoids</li><li>Density-based clustering: DBSCAN (phân cụm theo mật độ)</li><li>Clustering evaluation: Silhouette Score (đánh giá hiệu quả phân cụm)</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 12. Dimensionality Reduction**<ul markdown="1"><li>Principal Component Analysis (PCA) (phân tích thành phần chính)</li><li>t-SNE & manifold learning (giảm chiều phi tuyến & học đa tạp)</li></ul> | :material-clock-outline: Coming soon | — |
| ^^**Module 05. Pipelines & Deployment**^^ | | |
| **Lecture 13. Model Evaluation & Tuning**<ul markdown="1"><li>Cross-validation: K-Fold, Stratified K-Fold (kiểm thử chéo)</li><li>Hyperparameter tuning: GridSearch, RandomSearch (tinh chỉnh siêu tham số)</li><li>Evaluation metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC</li></ul> | :material-clock-outline: Coming soon | — |
| **Lecture 14. ML Pipelines & Deployment**<ul markdown="1"><li>Scikit-learn pipelines (đóng gói quy trình tiền xử lý & huấn luyện)</li><li>Model serialization: Pickle, Joblib (lưu trữ & xuất mô hình)</li><li>API serving (chiến lược triển khai mô hình cơ bản)</li></ul> | :material-clock-outline: Coming soon | — |

## V. References

Nội dung khóa học được tham khảo, tổng hợp và hệ thống hóa từ các giáo trình kinh điển cùng nguồn tài liệu học thuật uy tín trong lĩnh vực học máy, bao gồm nền tảng thống kê và trực giác thuật toán [@james2021introduction], lý thuyết xác suất chuyên sâu [@bishop2006pattern], hệ thống bài giảng tối ưu hóa của Stanford [@ng2000cs229], cũng như tư duy kỹ thuật triển khai ML Pipelines trong thực tế [@geron2022hands].

\bibliography