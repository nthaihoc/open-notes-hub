---
title: "Applied Machine Learning (AML)"
icon: material/slot-machine
url_img: "../../assets/images/ods_stickers.jpg"
color: "#ff6b6b"   
---

{% include 'includes/banner.html' %}

## I. Course Introduction
---

^^Mô tả.^^ Applied Machine Learning (AML) cung cấp cho người học cái nhìn tổng quan và toàn diện về lĩnh vực Machine Learning (ML) -- từ lý thuyết cốt lõi đến thực hành triển khai. Toàn bộ nội dung tập trung vào các kỹ thuật và thuật toán nền tảng, giúp người học nắm vững cách thức thu thập dữ liệu, tiền xử lý, và xây dựng các mô hình Học Máy một cách bài bản và có hệ thống. Khóa học không chỉ chú trọng vào kiến thức lý thuyết mà còn hướng dẫn người học từng bước triển khai, huấn luyện và đánh giá mô hình ML từ đầu đến cuối, qua các bài tập thực hành thực tế.

^^Đối tượng.^^ Khóa học phù hợp với người mới bắt đầu làm quen với Trí tuệ Nhân tạo và Học máy. Ngoài ra, những người đã có kiến thức nền tảng cũng có thể sử dụng tài liệu này như một nguồn tham khảo hệ thống và thực tiễn.

^^Cấu trúc khóa học.^^ Khóa học được tổng hợp và chia nhỏ thành 5 Module chính, xây dựng từ nền tảng lý thuyết cho đến thực hành triển khai toàn bộ hệ thống ML trong thực tế. Chi tiết nội dung bài học của từng Module được mô tả chi tiết trong [[Syllabus](#iv-syllabus){ data-preview }].

- **Module 01.Introduction to ML & Development Environment** -- Tổng quan về Học máy và môi trường phát triển. 
- **Module 02. Data Preprocessing & Exploratory Data Analysis** -- Tiền xử lý và khám phá dữ liệu.
- **Module 03. Supervised Learning Algorithms** -- Các thuật toán học có giám sát.
- **Module 04. Unsupervised Learning Algorithms** -- Các thuật toán học không giám sát.
- **Module 05: ML Pipelines & Deployment** -- Đường ống ML và triển khai hệ thống.

## II. What will you learn?
---

Sau khi đọc xong toàn bộ khóa học này, bạn có thể thu thập được những tri thức dưới đây: 

- [x] Nắm vững các thuật toán học máy cơ bản như Linear Regression, Support Vector Machine, Decision Trees, K-mean Clustering, $\dots$

- [x] Hiểu và áp dụng kỹ thuật thu thập, tiền xử lý và trực quan hóa dữ liệu.

- [x] Thành thạo quy trình xây dựng mô hình ML từ dữ liệu thô đến đánh giá kết quả.

- [x] Thực hành triển khai mô hình bằng Python và các thư viện như: Scikit-learn, Numpy, Pandas, Matplotlib, Seaborn, v.v.

- [x] Áp dụng mô hình vào các bài tập thực hành thực tế qua mini-projects và case studies.

## III. Requirements
---

Để có thể tiếp cận nội dung của toàn bộ khóa học một cách dễ dàng, người đọc cần có sẵn một số kiến thức nền tảng như:

- Lập trình Python cơ bản: Thành thạo các cấu trúc dữ liệu cơ bản, vòng lặp, hàm và thao tác xử lý dữ liệu với thư viện như numpy và pandas.

- Toán học nền tảng: Có kiến thức cơ bản về đại số tuyến tính, giải thích và xác suất thống kê.

- Kỹ năng tự học và giải quyết vấn đề: Sẵn sàng tiếp cận tài liệu học thuật, nghiên cứu thuật toán, và thử nghiệm mô hình trong môi trường thực tế.


## IV. Syllabus
---

| Module | Topic | Key Concepts | 
| :--- | :--- | :--- |
| *Module 01 <br> Overview & Environment* | **Lecture 01. Introduction to ML** <br> [[notes](https://)] [[code](https://)] | <ul><li>ML Taxonomy, Supervised Learning, Unsupervised Learning.</li><li>ML Workflow, Real-world Challenges.</li></ul>|
| | **Lecture 02. ML Development Roadmap** | <ul><li>Vòng đời phát triển (ML Lifecycle)</li><li>Các yếu tố cốt lõi: Data, Model, Compute</li><li>Giới thiệu về MLOps cơ bản</li></ul> |
| | **Lecture 03. Python for Data Science** | <ul><li>Thiết lập môi trường: Anaconda, Jupyter, Colab</li><li>Hệ sinh thái: NumPy (Đại số), Pandas (Dữ liệu), Matplotlib (Vẽ biểu đồ)</li></ul> |
| | | | |
| *Module 02 <br> Preprocessing & EDA* | **Lecture 04. Data Preprocessing Strategy** | <ul><li>Tầm quan trọng của tiền xử lý</li><li>Các chiến lược làm sạch và chuẩn hóa dữ liệu</li><li>Xử lý dữ liệu mất cân bằng (Imbalanced Data)</li></ul> |
| | **Lecture 05. Cleaning & Missing Values** | <ul><li>Phát hiện và xử lý Outlier (Ngoại lai)</li><li>Kỹ thuật Imputation (Điền khuyết thiếu)</li><li>Làm sạch dữ liệu trùng lặp</li></ul> |
| | **Lecture 06. Feature Engineering** | <ul><li>Feature Selection (RFE, Feature Importance)</li><li>Feature Transformation (Scaling, Encoding)</li><li>Dimensionality Reduction cơ bản</li></ul> |
| | | | |
| *Module 03 <br> Supervised Learning* | **Lecture 07. Linear Models** | <ul><li>Linear Regression & Logistic Regression</li><li>Gradient Descent & Normal Equation</li><li>Regularization: Ridge, Lasso, Elastic Net</li></ul> |
| | **Lecture 08. Support Vector Machines** | <ul><li>Nguyên lý biên cứng (Hard Margin) & biên mềm (Soft Margin)</li><li>Kernel Trick & bài toán phi tuyến</li></ul> |
| | **Lecture 09. Tree-based Models** | <ul><li>Cấu trúc Decision Tree (CART, ID3)</li><li>Ensemble Learning: Random Forest, Gradient Boosting</li><li>Overfitting & Pruning Strategies</li></ul> |
| | | | |
| *Module 04 <br> Unsupervised Learning* | **Lecture 10. Clustering Algorithms** | <ul><li>Phân cụm K-means & K-medoids</li><li>Phân cụm mật độ (DBSCAN)</li><li>Đánh giá hiệu quả phân cụm (Silhouette Score)</li></ul> |
| | **Lecture 11. Dimensionality Reduction** | <ul><li>Principal Component Analysis (PCA)</li><li>t-SNE & Manifold Learning</li></ul> |
| | | | |
| *Module 05 <br> Pipelines & Deployment* | **Lecture 12. Model Evaluation & Tuning** | <ul><li>Cross-Validation (K-Fold, Stratified)</li><li>Hyperparameter Tuning (GridSearch, RandomSearch)</li><li>Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC</li></ul> |
| | **Lecture 13. ML Pipelines & Deployment** | <ul><li>Xây dựng Pipeline với Scikit-learn</li><li>Lưu trữ mô hình (Pickle, Joblib)</li><li>Chiến lược triển khai cơ bản (API Serving)</li></ul> |

## V. Materials
---