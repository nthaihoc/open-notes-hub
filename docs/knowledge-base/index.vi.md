---
title: "Knowledge Base"
url_img: "assets/images/ods_stickers.jpg"
quote:
  - "Live as if you were to die tomorrow. Learn as if you were to live forever"
  - "Dreams don't work unless you do"
---

{% include 'includes/banner.html' %}

<div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 6px; line-height: 0; width: 100%; margin: 12px 0;">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://jupyter.org"><img src="https://img.shields.io/badge/Jupyter_Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook"></a>
  <a href="https://colab.google.com"><img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Google Colab"></a>
  <a href="https://git-scm.com/"><img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"></a>
  <a href="https://www.geeksforgeeks.org/"><img src="https://img.shields.io/badge/GeeksforGeeks-298D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks"></a>
  <a href="https://www.notion.com/templates"><img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white" alt="Notion"></a>
  <a href="https://ubuntu.com/download"><img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu"></a>
  <a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions"></a>
</div>

## Giới thiệu

**Mô tả.** Knowledge Base là kho lưu trữ ghi chú kỹ thuật, hướng dẫn thực hành (tutorials) và tổng hợp kiến trúc hệ thống phục vụ quá trình phát triển phần mềm và kỹ thuật AI. Nội dung tập trung vào các công cụ lập trình, quy trình triển khai backend, hệ thống truy xuất kết hợp sinh (RAG) và các thực hành chuẩn trong kỹ nghệ phần mềm.

**Mục tiêu.** Hệ thống hóa kiến thức thực chiến thành các tài liệu ngắn gọn, dễ tra cứu và có thể tái sử dụng trực tiếp trong các dự án thực tế.

## Danh mục chủ đề { #kb-topics }

| Chuyên đề | Nội dung trọng tâm | Trạng thái | Tài nguyên |
| :-------- | :----------------- | :--------: | :--------: |
| **FastAPI Tutorials** | Xây dựng RESTful API hiệu năng cao, xác thực dữ liệu với Pydantic, lập trình bất đồng bộ (Async) và đóng gói dịch vụ AI | :material-check-circle: | [[notes]({{ config.site_url }}{{ links.fastapi.les01 }})] |
| **RAG Framework** | Kiến trúc Retrieval-Augmented Generation, phân mảnh văn bản (Chunking), Vector Database và đánh giá chất lượng truy xuất | :material-check-circle: | [[notes]({{ config.site_url }}{{ links.rag.les01 }})] |