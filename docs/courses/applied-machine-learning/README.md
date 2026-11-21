---
title: "Applied Machine Learning (AML)"
icon: material/slot-machine
url_img: "assets/images/ods_stickers.jpg"
color: "#05E1FA"   
---

{% include 'includes/banner.html' %}

## I. Course Introduction

**Mô tả.** Applied Machine Learning (AML) cung cấp cho người học cái nhìn tổng quan và toàn diện về lĩnh vực Machine Learning (ML) từ lý thuyết cốt lõi đến thực hành triển khai. Toàn bộ nội dung tập trung vào các kỹ thuật và thuật toán nền tảng, giúp người học nắm vững cách thức thu thập, tiền xử lý dữ liệu và xây dựng các mô hình Học máy một cách bài bản, có hệ thống. Khóa học không chỉ chú trọng vào kiến thức lý thuyết mà còn hướng dẫn người học từng bước triển khai, huấn luyện và đánh giá mô hình ML từ đầu đến cuối thông qua các bài tập thực hành.

**Đối tượng.** Khóa học phù hợp với người mới bắt đầu làm quen với Trí tuệ Nhân tạo và Học máy. Ngoài ra, những người đã có kiến thức nền tảng cũng có thể sử dụng tài liệu này như một nguồn tham khảo hệ thống và thực tiễn.

**Cấu trúc.** Khóa học được tổng hợp và chia nhỏ thành 5 Module chính, xây dựng từ nền tảng lý thuyết cho đến thực hành triển khai toàn bộ hệ thống ML trong thực tế. Nội dung bài học của từng Module được mô tả chi tiết trong [Syllabus](#iv-syllabus){ data-preview }.

- **Module 01 - Introduction to ML & Development Environment:** Tổng quan về Học máy và môi trường phát triển. 
  
- **Module 02 - EDA & Data Preprocessing:** Khám phá và tiền xử lý dữ liệu.

- **Module 03 - Supervised Learning Algorithms:** Các thuật toán học có giám sát.

- **Module 04 - Unsupervised Learning Algorithms:** Các thuật toán học không giám sát.
  
- **Module 05 - ML Pipelines & Deployment:** ML Pipelines và triển khai hệ thống.

## II. What will you learn?

Sau khi học xong toàn bộ khóa học này, bạn có thể nắm vững những kiến thức dưới đây: 

- Nắm vững các thuật toán học máy cơ bản như Linear Regression, Support Vector Machines, Decision Trees, K-Means Clustering, v.v.

- Hiểu và áp dụng kỹ thuật thu thập, tiền xử lý và trực quan hóa dữ liệu.

- Thành thạo quy trình xây dựng mô hình ML từ dữ liệu thô đến đánh giá kết quả.

- Thực hành triển khai mô hình bằng Python và các thư viện như: Scikit-learn, NumPy, Pandas, Matplotlib, Seaborn, v.v.

- Áp dụng mô hình vào các bài tập thực tế qua mini-projects và case studies.

## III. Requirements

Để có thể tiếp cận nội dung của toàn bộ khóa học một cách dễ dàng, người đọc cần có sẵn một số kiến thức nền tảng như:

- Lập trình Python cơ bản: Thành thạo các cấu trúc dữ liệu cơ bản, vòng lặp, hàm và thao tác xử lý dữ liệu với thư viện như NumPy và Pandas.

- Toán học nền tảng: Có kiến thức cơ bản về đại số tuyến tính, giải tích và xác suất thống kê.

- Kỹ năng tự học và giải quyết vấn đề: Sẵn sàng tiếp cận tài liệu học thuật, nghiên cứu thuật toán và thử nghiệm mô hình trong môi trường thực tế.

## IV. Syllabus

^^**Module 01: Overview & Environment**^^
{ style="text-align: center;" }

<div class="grid cards" markdown>

-   **:material-book-open-variant: Lecture 01. Introduction to ML**

    ---

    ==**Key Concepts:**==

    -   ML Taxonomy: Supervised, Unsupervised, Reinforcement Learning (Phân loại ML).
    -   Problem Formulation & Real-world Challenges (Vấn đề và thách thức của ML).

    [[:material-notebook-outline: **notes**](https://)] &nbsp; [[:material-code-tags: **code**](https://)]

-   **:material-book-open-variant: Lecture 02. ML Development Roadmap**

    ---

    ==**Key Concepts:**==

    -   Vòng đời phát triển (End-to-End ML Lifecycle)
    -   Các yếu tố cốt lõi: Data, Model, Compute
    -   Giới thiệu về MLOps cơ bản

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 03. Python for Data Science**

    ---

    ==**Key Concepts:**==

    -   Thiết lập môi trường: Anaconda, Jupyter, Colab
    -   Hệ sinh thái: NumPy (Đại số), Pandas (Dữ liệu), Matplotlib (Vẽ biểu đồ)

    :material-clock-outline: *Coming soon*

</div>

^^**Module 02: EDA & Preprocessing**^^
{ style="text-align: center;" }

<div class="grid cards" markdown>

-   **:material-book-open-variant: Lecture 04. Exploratory Data Analysis (EDA)**

    ---

    ==**Key Concepts:**==

    -   Phân tích đơn biến & đa biến (Univariate & Multivariate Analysis)
    -   Trực quan hóa phân phối & Correlation Matrix
    -   Chiến lược chia tập Train/Validation/Test & chống Data Leakage

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 05. Data Cleaning & Preprocessing**

    ---

    ==**Key Concepts:**==

    -   Phát hiện và xử lý Outlier (Ngoại lai)
    -   Kỹ thuật Imputation (Điền dữ liệu khuyết thiếu) & làm sạch trùng lặp
    -   Xử lý dữ liệu mất cân bằng (Imbalanced Data) trên tập Train

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 06. Feature Engineering**

    ---

    ==**Key Concepts:**==

    -   Feature Selection (RFE, Feature Importance)
    -   Feature Transformation (Scaling, Encoding)
    -   Feature Creation & Extraction

    :material-clock-outline: *Coming soon*

</div>

^^**Module 03: Supervised Learning**^^
{ style="text-align: center;" }

<div class="grid cards" markdown>

-   **:material-book-open-variant: Lecture 07. Linear Models**

    ---

    ==**Key Concepts:**==

    -   Linear Regression & Logistic Regression
    -   Gradient Descent & Normal Equation
    -   Regularization: Ridge, Lasso, Elastic Net

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 08. Support Vector Machines**

    ---

    ==**Key Concepts:**==

    -   Nguyên lý biên cứng (Hard Margin) & biên mềm (Soft Margin)
    -   Kernel Trick & bài toán phi tuyến

    [[:material-notebook-outline: **notes**](08-support-vector-machines/)] &nbsp; [[:material-code-tags: **code**](08-support-vector-machines/#implementation)]

-   **:material-book-open-variant: Lecture 09. Tree-based Models**

    ---

    ==**Key Concepts:**==

    -   Cấu trúc Decision Tree (CART, ID3)
    -   Ensemble Learning: Random Forest, Gradient Boosting
    -   Overfitting & Pruning Strategies

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 10. Instance-based & Probabilistic Models**

    ---

    ==**Key Concepts:**==

    -   Thuật toán k-Nearest Neighbors (k-NN) & Distance Metrics
    -   Phân lớp xác suất với Naive Bayes (Gaussian, Multinomial)

    :material-clock-outline: *Coming soon*

</div>

^^**Module 04: Unsupervised Learning**^^
{ style="text-align: center;" }

<div class="grid cards" markdown>

-   **:material-book-open-variant: Lecture 11. Clustering Algorithms**

    ---

    ==**Key Concepts:**==

    -   Phân cụm K-Means & K-Medoids
    -   Phân cụm mật độ (DBSCAN)
    -   Đánh giá hiệu quả phân cụm (Silhouette Score)

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 12. Dimensionality Reduction**

    ---

    ==**Key Concepts:**==

    -   Principal Component Analysis (PCA)
    -   t-SNE & Manifold Learning

    :material-clock-outline: *Coming soon*

</div>

^^**Module 05: Pipelines & Deployment**^^
{ style="text-align: center;" }

<div class="grid cards" markdown>

-   **:material-book-open-variant: Lecture 13. Model Evaluation & Tuning**

    ---

    ==**Key Concepts:**==

    -   Cross-Validation (K-Fold, Stratified)
    -   Hyperparameter Tuning (GridSearch, RandomSearch)
    -   Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC

    :material-clock-outline: *Coming soon*

-   **:material-book-open-variant: Lecture 14. ML Pipelines & Deployment**

    ---

    ==**Key Concepts:**==

    -   Xây dựng Pipeline với Scikit-learn
    -   Lưu trữ mô hình (Pickle, Joblib)
    -   Chiến lược triển khai cơ bản (API Serving)

    :material-clock-outline: *Coming soon*

</div>

## VI. References

Nội dung khóa học được tham khảo, tổng hợp và hệ thống hóa từ các giáo trình kinh điển cùng nguồn tài liệu học thuật uy tín trong lĩnh vực Học máy, bao gồm nền tảng thống kê và trực giác thuật toán [@james2021introduction], lý thuyết xác suất chuyên sâu [@bishop2006pattern], hệ thống bài giảng tối ưu hóa của Stanford [@ng2000cs229], cũng như tư duy kỹ thuật triển khai ML Pipelines trong thực tế [@geron2022hands].

\bibliography

