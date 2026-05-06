---
icon: 
title: Operational Framework
---

# :material-domain: Operational Framework

## :material-layers-triple: Weekly Seminar Tracks
---

Để đảm bảo mỗi buổi Weekly Seminar đều mang lại giá trị thực tiễn (Actionable Insights) và tránh tình trạng thảo luận lý thuyết xa rời thực tế, IAI Lab quy hoạch nội dung sinh hoạt vào **02 luồng chủ đề cốt lõi**. Cấu trúc này được thiết kế để duy trì trạng thái cân bằng động cho Lab. **Track 01** giúp chúng ta không bị lạc hậu về công nghệ (Input), trong khi **Track 02** đảm bảo chất lượng và tiến độ của dự án nội bộ (Output).

!!! tip ""

    <div class="grid cards" markdown>

    -   :telescope: ^^Track 01: Research & Engineering Frontier^^

        ---

        - **Mục tiêu:** Là quá trình **Nạp kiến thức (Input)**. Chúng ta tìm kiếm "vũ khí" mới từ bên ngoài để giải quyết các nút thắt của dự án.

        - **Phạm vi (Scope):**
            1.  **Research:** Các bài báo SOTA (CVPR, NeurIPS, ICASSP...) liên quan trực tiếp đến bài toán đang giải quyết.
            2.  **Engineering:** Các công cụ, kỹ thuật tối ưu mới (MLOps, Docker, PyTorch optimizations...).

        - **Yêu cầu chuẩn bị (Memo/Tutorial):**

            - *Problem Statement: Chúng ta đang gặp khó khăn gì? (Model độ chính xác thấp hay Code chạy quá chậm?)*

            - *The Solution: Bài báo/Công cụ này giải quyết vấn đề đó như thế nào? (Cơ chế hoạt động).*

            - *Actionable Plan: Kế hoạch tích hợp giải pháp này vào codebase của Lab ngay trong tuần tới.*

    -   :chart_with_upwards_trend: ^^Track 02: Impact & Retrospective^^

        ---

        - **Mục tiêu:** Là quá trình **Đánh giá hiệu quả (Output)**. Chúng ta nhìn thẳng vào số liệu nội bộ để tìm nguyên nhân thất bại và hướng cải thiện.

        - **Phạm vi (Scope):** Kết quả thực nghiệm (Experiments Logs), Biểu đồ huấn luyện (WandB), và các trường hợp dự đoán sai (Failure Cases).

        - **Yêu cầu chuẩn bị (Deep-dive Report):**

            - *Metric Board: Bảng so sánh chỉ số (F1, Precision, WER, Accuracy, Latency...) giữa các phiên bản model.*

            - *Error Analysis: "Mổ xẻ" 10-20 mẫu dữ liệu thất bại. Tại sao sai? Do dữ liệu nhiễu hay do model chưa đủ tốt?*

            - *Hypothesis & Next Steps: Đặt giả thuyết kỹ thuật (Hypothesis) và lên kế hoạch cải tiến cho phiên bản tiếp theo.*

    </div>

## :material-file-document-edit: Research Proposal
---

Trong quá trình thảo luận và tương tác giữa hai luồng sinh hoạt chính (Track 01 & 02), các thành viên được khuyến khích phát triển các ý tưởng tiềm năng thành một đề cương nghiên cứu hoàn chỉnh. Các đề xuất này sẽ được phân loại và định nghĩa theo 02 định hướng (tracks) cụ thể dưới đây. Thành viên cần xác định rõ hướng đi của mình để chuẩn bị nội dung phù hợp

### :material-lightbulb-on: Novel Problem Solving

Dành cho các đề xuất tập trung vào việc định nghĩa lại hoặc mở rộng phạm vi của một bài toán chưa được giải quyết triệt để.

- <u>**Định nghĩa bài toán (Problem Definition):**</u>

    - Đầu vào: Lọai dữ liệu, định dạng, cách biểu diễn dữ liệu...

    - Đẩu ra: Loại dữ liệu đầu ra, định dạng kết quả...

    - Dữ liệu train/dev/test: Loại và cách biểu diễn của dữ liệu dùng để huấn luyện.

    - Các giả định, diều kiện: Các điều kiện tiên quyết để bài toán có thể thực hiện (cấu hình phần cứng, điều kiện ánh sáng...).
    
- <u>**So sánh với Baseline:**</u>

    - Phân tích và so sánh sự khác nhau giữa định nghĩa bài toán của phương pháp baseline và định nghĩa bài toán mới của bạn.

    - Để chọn một phương pháp cơ sở cần đáp ứng các tiêu chí sau:
        
        - Phải là phương pháp hiện đại nhất (State-of-the-Art), mang lại hiệu quả tốt nhất tại thời điểm đề xuất.

        - Bài báo liên quan đến phương pháp này đã được đăng và trình bày tại hội nghị.

        - Code và dữ liệu có thể đều phải được công khai.

- <u>**Động lực và Giải pháp:**</u>

    - Động lực (motivation): Tại sao cần phải giải quyết bài toán mới này? Tại sao các phương pháp cũ chưa giải quyết được?

    - Ý tưởng chính (main idea): Phương pháp tiếp cận, kiến trúc mô hình hoặc thuật toán cốt lõi để giải quyết vấn đề nêu trên.

- <u>**Thiết lập thực nghiệm:**</u>

    - Tập dữ liệu:

        - Mô tả các tập dữ liệu dùng cho huấn luyện và kiểm thử.

        - Cung cấp chi tiết về: biểu diễn dữ liệu, quy mô tập dữ liệu, độ đa dạng và cách chia tập dữ liệu.

    - Chỉ số đánh giá:

        - Xác định các chỉ số định lượng.

        - Đảm bảo kết hợp các chỉ số đánh giá tiêu chuẩn phù hợp với bài toán cụ thể.

- <u>**Tiêu chí khác:**</u>

    - Định tính: Hình dung các kết quả đầu ra, phương pháp mới chúng sẽ khắc phục được lỗi cụ thể nào về mặt thị giác mà các phương pháp baseline gặp phải?

    - Định lượng: Thiết lập mục tiêu cụ thể dựa trên các chỉ số đánh giá.

### :material-rocket-launch: Performance Improvement

Dành cho các đề xuất tập trung vào việc tối ưu hoá một giải pháp đã có.

- <u>**Mục tiêu cải thiện:**</u> Xác định chính xác khía cạnh **hiệu suất** cần nâng cao:

    - Độ chính xác (Accuray/Precision/Recall).

    - Tốc độ thực thi (Inference time/Latency).

    - Tối ưu tài nguyên (Memory Usage/Model Size)

- <u>**Ý tưởng chính:**</u> Mô tả kỹ thuật hoặc phương pháp cụ thể sẽ áp dụng để đạt được sự cải thiện.

- <u>**Thiết lập thực nghiệm:**</u> Yêu cầu tương tự như Novel Problem Solving track, nhưng cần nhấn mạnh vào sự thay đổi của các chỉ số.

---