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

## Giới thiệu khóa học

**Mô tả.** Khóa học cung cấp cái nhìn tổng quan và toàn diện về lĩnh vực Machine Learning (học máy - ML) từ lý thuyết nền tảng đến thực hành triển khai. Nội dung tập trung vào các kỹ thuật và thuật toán cốt lõi, giúp người học nắm vững quy trình khám phá, tiền xử lý dữ liệu và xây dựng mô hình một cách bài bản, có hệ thống. Bên cạnh lý thuyết, tài liệu hướng dẫn từng bước cách huấn luyện, tinh chỉnh và đánh giá mô hình ML hoàn chỉnh thông qua các ví dụ thực hành.

**Đối tượng.** Phù hợp với người mới bắt đầu làm quen với Trí tuệ nhân tạo (AI) và Học máy (ML). Ngoài ra, những người đã có kiến thức nền tảng có thể sử dụng tài liệu này như một nguồn tham khảo hệ thống và thực tiễn.

**Cấu trúc.** Khóa học được thiết kế thành 5 module chính, đi từ nền tảng lý thuyết đến triển khai thực tế chi tiết trong [[syllabus](#aml-syllabus)]:

- **Module 01. Tổng quan & Môi trường phát triển (Overview & Environment):** Nền tảng Machine Learning và thiết lập không gian làm việc.
- **Module 02. Khám phá & Tiền xử lý dữ liệu (EDA & Preprocessing):** Phân tích khám phá dữ liệu, làm sạch và kỹ nghệ đặc trưng.
- **Module 03. Học có giám sát (Supervised Learning):** Đánh giá & kiểm thử chéo, các họ thuật toán hồi quy - phân loại, và tinh chỉnh siêu tham số.
- **Module 04. Học không giám sát (Unsupervised Learning):** Phân cụm dữ liệu và các kỹ thuật giảm chiều.
- **Module 05. Đóng gói quy trình & Triển khai (Pipelines & Deployment):** Đóng gói quy trình tiền xử lý - huấn luyện với Pipelines và triển khai mô hình qua API.

## Bạn sẽ học được gì?

Sau khi hoàn thành khóa học này, bạn có thể:

- Nắm vững nguyên lý toán học và cơ chế hoạt động của các thuật toán cốt lõi: Linear Regression, Support Vector Machines (SVM), Decision Trees, k-Means Clustering.
- Thành thạo kỹ thuật phân tích khám phá dữ liệu (EDA - Exploratory Data Analysis), làm sạch dữ liệu, xử lý mất cân bằng (imbalanced data) và kỹ thuật trích xuất đặc trưng (feature engineering).
- Làm chủ quy trình xây dựng mô hình, kiểm thử chéo (cross-validation) và tinh chỉnh siêu tham số (hyperparameter tuning) từ dữ liệu thô đến đánh giá kết quả.
- Triển khai thành thạo mô hình bằng Python cùng hệ sinh thái thư viện chuẩn: Scikit-learn, NumPy, Pandas, Matplotlib.

## Yêu cầu tiên quyết

Để tiếp cận nội dung thuận lợi, người học cần chuẩn bị:

- **Lập trình Python:** Nắm vững cấu trúc dữ liệu, vòng lặp, hàm và lập trình hướng đối tượng (OOP - Object-Oriented Programming) cơ bản; quen thuộc với NumPy và Pandas là một lợi thế.
- **Toán học nền tảng:** Kiến thức cơ sở về đại số tuyến tính (ma trận, vector), giải tích (đạo hàm, gradient) và xác suất thống kê.
- **Tư duy thực nghiệm:** Sẵn sàng đọc tài liệu kỹ thuật, tự chạy mã nguồn và phân tích kết quả thực nghiệm trên các bộ dữ liệu thực tế.

## Khung chương trình { #aml-syllabus }

| Bài học | Trạng thái | Tài nguyên |
| :------ | :--------: | :--------: |
| ^^**Module 01. Tổng quan & Môi trường phát triển (Overview & Environment)**^^ | | |
| **Bài 01. Nhập môn Machine Learning**<ul markdown="1"><li>Phân loại Machine Learning: Học có giám sát (Supervised), Không giám sát (Unsupervised) và Học tăng cường (Reinforcement Learning)</li><li>Định hình bài toán thực tế & các thách thức kỹ thuật cốt lõi (Problem formulation)</li></ul> | :material-clock-outline: | — |
| **Bài 02. Lộ trình phát triển hệ thống ML**<ul markdown="1"><li>Vòng đời phát triển mô hình toàn diện (End-to-end ML lifecycle)</li><li>Ba trụ cột cốt lõi: Dữ liệu (Data), Mô hình (Model) và Hạ tầng tính toán (Compute)</li><li>Nhập môn vận hành học máy (MLOps - Machine Learning Operations)</li></ul> | :material-clock-outline: | — |
| **Bài 03. Python cho Khoa học dữ liệu**<ul markdown="1"><li>Thiết lập môi trường làm việc: Anaconda, Jupyter, Google Colab và Kaggle</li><li>Hệ sinh thái thư viện cốt lõi: NumPy (đại số tuyến tính), Pandas (thao tác dữ liệu), Matplotlib & Seaborn (trực quan hóa)</li></ul> | :material-clock-outline: | — |
| ^^**Module 02. Khám phá & Tiền xử lý dữ liệu (EDA & Preprocessing)**^^ | | |
| **Bài 04. Phân tích khám phá dữ liệu (EDA - Exploratory Data Analysis)**<ul markdown="1"><li>Phân tích đơn biến & đa biến (Univariate & multivariate analysis)</li><li>Trực quan hóa phân phối dữ liệu & ma trận tương quan (Correlation matrix)</li><li>Chiến lược phân chia tập dữ liệu (Train/Val/Test) & kỹ thuật chống rò rỉ dữ liệu (Data Leakage)</li></ul> | :material-clock-outline: | — |
| **Bài 05. Làm sạch & Tiền xử lý dữ liệu**<ul markdown="1"><li>Phát hiện & xử lý ngoại lai (Outlier handling)</li><li>Điền dữ liệu khuyết thiếu (Imputation) & khử trùng lặp dữ liệu (Deduplication)</li><li>Kỹ thuật xử lý mất cân bằng dữ liệu (Handling imbalanced data)</li></ul> | :material-clock-outline: | — |
| **Bài 06. Kỹ nghệ đặc trưng (Feature Engineering)**<ul markdown="1"><li>Lựa chọn đặc trưng (Feature Selection): RFE (Recursive Feature Elimination), Độ quan trọng đặc trưng (Feature Importance)</li><li>Biến đổi & chuẩn hóa đặc trưng: Scaling (chuẩn hóa tỷ lệ), Encoding (mã hóa dữ liệu)</li><li>Tạo mới & trích xuất đặc trưng (Feature creation & extraction)</li></ul> | :material-clock-outline: | — |
| ^^**Module 03. Học có giám sát (Supervised Learning)**^^ | | |
| **Bài 07. Đánh giá mô hình & Kiểm thử chéo**<ul markdown="1"><li>Đánh đổi Độ chệch - Phương sai (Bias-Variance Tradeoff) & Đường cong học tập (Learning Curves)</li><li>Chiến lược kiểm thử chéo (Cross-validation): K-Fold, Stratified K-Fold</li><li>Hệ thống độ đo Hồi quy (MAE, MSE, RMSE, $R^2$) & Phân loại (Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC, PR-AUC)</li></ul> | :material-clock-outline: | — |
| **Bài 08. Các mô hình tuyến tính (Linear Models)**<ul markdown="1"><li>Hồi quy tuyến tính (Linear Regression) & Hồi quy Logistic</li><li>Phương pháp tối ưu hóa: Gradient Descent, Phương trình chuẩn (Normal Equation)</li><li>Kiểm soát chính quy hóa (Regularization): Ridge (L2), Lasso (L1), Elastic Net</li></ul> | :material-clock-outline: | — |
| **Bài 09. Máy vector hỗ trợ (Support Vector Machines - SVM)**<ul markdown="1"><li>Nguyên lý tối ưu lề phân lớp: Biên cứng (Hard Margin) & Biên mềm (Soft Margin)</li><li>Thủ thuật hạt nhân (Kernel Trick) & giải quyết bài toán phi tuyến (Non-linear classification)</li></ul> | :material-check-circle: | [[notes]({{ config.site_url }}{{ links.aml.les09 }})] [[code]({{ config.site_url }}{{ links.aml.les09 }}#implementation)] |
| **Bài 10. Các mô hình dạng cây (Tree-based Models)**<ul markdown="1"><li>Cấu trúc & thuật toán cây quyết định (Decision Tree): CART, ID3</li><li>Học kết hợp (Ensemble Learning): Random Forest, Gradient Boosting</li><li>Kiểm soát hiện tượng quá khớp (Overfitting) & chiến lược cắt tỉa cây (Pruning)</li></ul> | :material-check-circle: | [[notes]({{ config.site_url }}{{ links.aml.les10 }})] |
| **Bài 11. Mô hình dựa trên mẫu & Mô hình xác suất**<ul markdown="1"><li>Thuật toán láng giềng gần nhất (k-NN - k-Nearest Neighbors) & các độ đo khoảng cách (Distance metrics)</li><li>Phân loại xác suất với Naive Bayes (Gaussian, Multinomial)</li></ul> | :material-clock-outline: | — |
| **Bài 12. Tinh chỉnh siêu tham số & Lựa chọn mô hình**<ul markdown="1"><li>Phân biệt Tham số mô hình (Parameters) & Siêu tham số (Hyperparameters)</li><li>Chiến lược tìm kiếm siêu tham số: Grid Search, Random Search</li><li>Quy trình so sánh và lựa chọn mô hình tối ưu (Model Selection)</li></ul> | :material-clock-outline: | — |
| ^^**Module 04. Học không giám sát (Unsupervised Learning)**^^ | | |
| **Bài 13. Các thuật toán phân cụm (Clustering Algorithms)**<ul markdown="1"><li>Phân cụm dựa trên trọng tâm (Centroid-based): k-Means, k-Medoids</li><li>Phân cụm dựa trên mật độ (Density-based): DBSCAN</li><li>Đánh giá chất lượng phân cụm với hệ số Silhouette (Silhouette Score)</li></ul> | :material-clock-outline: | — |
| **Bài 14. Giảm chiều dữ liệu (Dimensionality Reduction)**<ul markdown="1"><li>Phân tích thành phần chính (PCA - Principal Component Analysis)</li><li>Giảm chiều phi tuyến & học đa tạp với t-SNE (t-Distributed Stochastic Neighbor Embedding)</li></ul> | :material-clock-outline: | — |
| ^^**Module 05. Đóng gói quy trình & Triển khai (Pipelines & Deployment)**^^ | | |
| **Bài 15. Đóng gói quy trình & Triển khai mô hình**<ul markdown="1"><li>Tự động hóa luồng tiền xử lý & huấn luyện với Scikit-learn Pipelines</li><li>Tuần tự hóa và lưu trữ mô hình (Model serialization): Pickle, Joblib</li><li>Cơ bản về phục vụ mô hình qua API (API Serving) & triển khai hệ thống</li></ul> | :material-clock-outline: | — |

## Tài liệu tham khảo

Nội dung khóa học được tham khảo, tổng hợp và hệ thống hóa từ các giáo trình kinh điển cùng nguồn tài liệu học thuật uy tín trong lĩnh vực học máy, bao gồm nền tảng thống kê và trực giác thuật toán [@james2021introduction], lý thuyết xác suất chuyên sâu [@bishop2006pattern], hệ thống bài giảng tối ưu hóa của Stanford [@ng2000cs229], cũng như tư duy kỹ thuật triển khai ML Pipelines trong thực tế [@geron2022hands].

\bibliography