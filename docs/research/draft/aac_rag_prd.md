---
title: Product Requirements Document - Hệ thống AaC-RAG Engine
---

# Product Requirements Document - Hệ thống AaC-RAG Engine

## I. Overview
---

**Product vision.** Xây dựng một hệ thống "Architecture-as-Code" tối giản nơi kỹ sư chỉ cần định nghĩa kiến trúc RAG một lần bằng ngôn ngữ khai báo (YAML) Hệ thống sẽ đóng vai trò là single source of truth (bộ tiêu chuẩn) để vừa tự động vẽ sơ đồ kiến trúc chuẩn mực, vừa trực tiếp điều phối và chạy luồng dữ liệu RAG trong thực tế.

**Core objective.**

- Tái sử dụng và chuẩn hoá: Chuẩn hoá các thành phần của hệ thống RAG thành thư viện chung.

- Bản vẽ kiến trúc và hệ thống thực tế luôn đồng nhất với nhau.

**Scope (6 weeeks).**

- Hỗ trợ luồng RAG cơ bản: Document Loader, Text Splitter, Embedding, VectorDB và LLM Generator.

- Hỗ trợ xuất sơ đò C4 (L1, L2) dưỡi dạng mã mermaid.js.

- Chạy được pipeline RAG hoàn chỉnh từ ingestion $\rightarrow$ retrieval $\rightarrow$ generator trực tiếp từ file YAML.

## II. Plan
---

| Sprint | Objective | Task | 
| :----: | :-------: | :--- |
| **01** | <li>Định nghĩa các chuẩn component library</li> <li>Xây dựng parser module</li> | <li>Thiết kế các schema YAML chuẩn bao gồm đầy đủ các thành phần cơ bản của hệ thống RAG.</li> <li>Xây dựng cơ chế đọc YAML file, validate cấu trúc và chuyển đổi thàh cấu trúc đồ thị (DAG) trên bộ nhớ memory.</li> |
| **02** | <li>Phát triển diagram render.</li> <li>Phát triển RAG runner (Ingestion)</li> | <li>Đọc DAG, tự động sinh ra mã code để hiển thị sơ đồ cho từng level (L1/L2)</li> <li> Ánh xạ DAG với các thư viện AI, xây dựng luồng thực thi: Đọc file -> cắt text -> nhúng -> lưu vector DB </li> |
| **03** | <li>Phát triển RAG runner (Retrieval + LLM generator).</li> <li>Hoàn thiện, đóng gói và báo cáo.</li> | <li> Xây dựng luồng thực thi: nhận query -> tìm kiếm vector DB -> đưa context vào LLM -> trả kết quả.</li> <li>Tối ưu hoá, refactor code, viết docs, demo.</li> |

## III. User stories (trọng tâm)
---

| # | User | Story |
| :--: | :---: | :--- |
| **US1** | **Kỹ sư AI** | Là một kỹ sư AI, tôi muốn khai báo cấu hình RAG (chọn mô hình LLM, kích thước chunk size) bằng file YAML, dể tôi có thể dễ dàng thay đổi chiến lược mà không cần sửa code logic |
| **US2** | **Kiến trúc sư hệ thống** | Là một kiến trúc sư hệ thống, tôi muốn hệ thống tự động sinh ra sơ đồ kiến trúc từ file YAML, để tài liệu dự án luôn được cập nhật chính xác theo thực tế cấu hình. |
| **US3** | **Developer** | Là một dev tôi muốn có thể định nghĩa sự phụ thuộc giữa các component bằng DAG. (Ví dụ muốn chạy được retrieval thì phải phụ thuộc vào vector DB) để hệ thống hoạt động tuần tự một cách chinh xác. |

## IV. Use cases (trọng tâm)
---

| # | Input | Pipeline | Output |
| :--- | :--- | :---- | :----- |
| **UC1. Biên dịch và vẽ kiến trúc** | Một file yaml cấu hình kiến trúc RAG | Hệ thống parser file, kiểm tra tính hợp lệ của các node, edge sau đó sinh ra biểu đồ | Các biểu đồ trực quan minh hoạ luồng đi của dữ liệu từ user -> llm -> vectorDB |
| **UC2. Thực thi Ingestion Pipeline** | File cấu hình kiến trúc RAG + tài liệu PDF | Chế độ runner được kích họat, tự động gọi các hàm khởi tạo tương ứng với cấu hình | Dữ liệu được cắt, nhúng và lưu thành công vào VectorDB cục bộ |
| **UC3. Thực thi Retrieval Pipeline.** | File cấu hình kiến trúc rag và câu hỏi của người dùng | Runner đọc DAG để biết cần lấy dữ liệu từ vectorDB nào, sử dụng prompt template nào, gọi LLM nào để sinh câu trả lời. | Câu trả lời chính xác dựa trên ngữ cảnh context đã nạp |

## V. Tech Stack
---

```yaml 
- Frontend: Streamlit/Gratio

- Diagram: Thư viện streamlit-mermaid-interactive

- Parser & Graph logic: Thư viện PyYAML, NetworkX

- RAG Engine: LangChain, Qdrant, Gemini. 
```