---
title: Cervical Cancer Cytology
icon: material/hospital-box
hide:
    - toc
---

<div class="hero-banner" style="background-image: url('../../assets/images/cervical_cancer.jpg')"></div>

<div align="left">
    <h1 style="margin-bottom: 10px; font-size: 2.5em;">🏥 Cervical Cancer Cytology</h1>
</div>

!!! info "Tổng quan dự án"
    **Cervical Cancer Cytology** là dự án hợp tác R&D giữa [Viện Khoa học & Công nghệ Ứng dụng (IAST)](https://iast.ictu.edu.vn) và **Bệnh viện A Thái Nguyên**. 
    
    Dự án tập trung xây dựng hệ thống **Computer-Aided Diagnosis (CAD)**, sử dụng các kiến trúc Deep Learning tiên tiến để hỗ trợ bác sĩ sàng lọc, khoanh vùng và phân loại tổn thương trên hình ảnh tế bào học cổ tử cung, nhằm rút ngắn thời gian chẩn đoán và giảm thiểu sai sót.

## I. Các hướng nghiên cứu chính
---

| Topic | Status | Key Contributions |
| :---- | :----: | :---------------- |
| **Ensemble Learning Strategy** <br> [[Notes](https://)] [[Code](https://)] | :material-check-all: | <li> Phát triển chiến lược **Học tập tổ hợp (Ensemble Learning)** nhằm tổng hợp sức mạnh của nhiều kiến trúc CNNs. <li> Nghiên cứu tập trung vào việc giảm thiểu phương sai (variance) và nâng cao độ tin cậy của mô hình trên dữ liệu lâm sàng thực tế. |
| **Self-Supervised Learning (SSL)** <br> [[Notes](../cervical-cancer-cytology/notes/ssl_for_cervical_cancer.md)] [[Code](https://)] | :material-close: | <li> Giải quyết bài toán thiếu hụt dữ liệu gán nhãn thông qua các kỹ thuật **Học tự giám sát**. <li> Tối ưu hóa các tác vụ tiền huấn luyện (Pre-text tasks) để trích xuất đặc trưng hiệu quả từ ảnh tế bào học không nhãn. |

## II. Tài liệu tham khảo
---

Danh sách các công trình nghiên cứu nền tảng (SOTA) được sử dụng để tham chiếu và phát triển phương pháp:

**Topic 01. Ensemble Learning Approaches**

* [Analysis of Cytology Pap Smear Images Based on Ensemble Deep Learning Approach](https://www.mdpi.com/2075-4418/12/11/2756). 

* [A Deep Learning Ensemble Method to Assist Cytopathologists in Pap Test Image Classification](https://www.mdpi.com/2313-433X/7/7/111). 

* [A fuzzy rank-based ensemble of CNN models for classification of cervical cytology](https://www.nature.com/articles/s41598-021-93783-8). 

**Topic 02. Self-Supervised Learning Foundations**

* [A Simple Framework for Contrastive Learning of Visual Representations (SimCLR)](https://arxiv.org/pdf/2002.05709). 

* [Emerging Properties in Self-Supervised Vision Transformers (DINO)](https://arxiv.org/pdf/2104.14294). 

* [Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning (BYOL)](https://arxiv.org/pdf/2006.07733). 

## III. Tài nguyên dự án
---

Truy cập mã nguồn, ghi chú kỹ thuật và dữ liệu thực nghiệm:

| Resource | Access Link | Note |
| :--- | :--- | :--- |
| **Project Notes** | [:material-notebook: View Notes](https://) | Nhật ký thực nghiệm và phân tích kỹ thuật. |
| **Source Code** | [:material-github: View Repository](https://) | Mã nguồn triển khai mô hình. |
| **Atlat Dataset** | [:material-database: Access Portal](https://label.ai4med.vn/auth/login) | **Account:** `{++BOCSDL@ai4med.com++}` <br> **Password:** `{++BenhvienAThaiNguyen++}` |


<div class="footer-garden">
    <span>🌾</span><span>🌿</span><span>🌻</span><span>🌿</span><span>🌾</span>
</div>
---