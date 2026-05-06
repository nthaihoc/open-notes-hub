---
icon: 
title: Guidelines
---

# :simple-readthedocs: Guidelines

## :material-gavel: Workflows
---

Hằng tuần, các thành viên chủ động đăng ký chủ đề (thuộc 02 tracks chính) hoặc thực hiện theo phân công của Team Lead, tham chiếu tại [Operational Framework](tracks.md). 

**Triết lý "No Slides:"** Áp dụng triết lý "Narrative over Bullet points". Việc viết ra một văn bản hoàn chỉnh (Memo) đòi hỏi tư duy mạch lạc và sâu sắc hơn so với việc gạch đầu dòng trên Slides.

**Mục tiêu:** Thay vì chuẩn bị Slides trình chiếu, Speaker phải tổng hợp, phân tích và viết lại toàn bộ nội dung nghiên cứu thành dạng Memo (4-6 trang). Tài liệu này phải đảm bảo tính đầy đủ, logic chặt chẽ và có dẫn chứng số liệu cụ thể.

**Cấu trúc cuộc họp:** Quy trình diễn ra theo cơ chế 03 giai đoạn: Preparation $\to$ Silent Reading $\to$ Deep Dive Discussion.

- **Preparation (Chuẩn bị - trước buổi họp):** Đây là giai đoạn Writing, speaker có trách nhiệm nghiên cứu sâu, tổng hợp và cô đọng kiến thức thành tài liệu Memo (Docs/Markdown/PDF/LaTex).

- **Silent Reading (Đọc sâu):** Đầy là giai đoạn Reading, khi phiên họp bắt đầu, toàn bộ Lab sẽ đọc tài liệu Memo.

    - Các thành viên đọc sâu, suy ngẫm và comment trực tiếp các câu hỏi, phản biện hoặc highlight những điểm chưa rõ ngay trên file tài liệu.

    - Đảm bảo mọi người có cùng một mức độ hiểu biết nền tảng trước khi thảo luận. 

- **Deep Dive Discussion (Thảo luận sâu):** Đây là giai đoạn tranh luận, sau khi thời gian đọc kết thúc, speaker sẽ không thuyết trình lại từ đầu mà đi thẳng vào giải quyết vấn đề:

    - Phản hồi các comments, câu hỏi được note trong file.

    - Thảo luận mở rộng về tính khả thi, các lỗ hổng và hướng phát triển tiếp theo.

    - Chốt lại các actionable insights cho tuần tiếp theo.

## Memo Specification
---

### :material-format-list-checks: Format

- **Tiêu đề:** Đặt tiêu đề file theo cấu trúc sau [Tên] - [Track] - [Topic]. Ví dụ: *NguyenThaiHoc-02-Speech2Phoneme.*

- **Mẫu báo cáo:** Có thể sử dụng docs, pdf, latex, markdown, notion..., tuy nhiên khuyến khích sử dụng mẫu latex của các hội nghị hàng đầu [CVPR paper format](https://www.overleaf.com/latex/templates/cvpr-2022-author-kit/qbmjsdxryffn).


### :material-text-box-search: Novel Problem Solving

**1. Abstract**

- Một câu tóm tắt cực ngắn nội dung chính.

- 2-3 câu về động lực và các ý tưởng chủ đạo của phương pháp cơ sở - baseline (cần thêm trích dẫn)

- Vài câu tóm tắt về định nghĩa bài toán và các đóng góp chính.

- 1-2 câu tóm tắt về kết quả thực nghiệm.

- Có thể, thêm dòng: "Code is available at ...".

**2. Introduction**

- **Động lực:** Động lực nghiên cứu bài toán này là gì? Tại sao việc giải quyết bài tóan này lại quan trọng? Những tác động tiềm năng của công trình này trong lĩnh vực nghiên cứu là gì, hoặc các ứng dụng có thể có là gì?

- **Thách thức:** Những khó khăn trong bài toán này là gì? Các công trình trước đây (bao gồm cả phương pháp baseline) đã tiếp cận vấn đề này như thế nào, và hạn chế của chúng là gì (trích dẫn)? Tại sao vấn đề này quan trọng mà vẫn chưa được giải quyết?

- **Định nghĩa bài toán:** Bài toán là gì? Đầu vào và đẩu ra mong muốn là gì? Những thông tin nào được cho trước trong quá trình huấn luyện và các giả định được đặt ra?

- **Ý tưởng chính:** Các ý tưởng chủ đạo của bạn để giải quyết các thách thức trên là gì?

- **Thiết lập thực nghiệm:** Mô tả ngắn gọn về thiết lập thí nghiệm. Sử dụng bô dữ liệu/benchmark nào? Đánh giá kết quả như thế nào? Kết luận là gì?

- **Đóng góp:** Một bản tóm tắt các đóng góp ở cuối phần này cũng được khuyến nghị dưới dạng danh sách gạch đầu dòng.

**3. Related Works**

- Cân nhắc chia các bài báo liên quan thành 2 hoặc 3 nhóm và viết một đoạn văn ngắn cho mỗi nhóm, kèm theo tiêu đề cho đọan đó. Một câu mở đầu giới thiệu ngắn gọn về các nhóm (nên viết).

- Tóm tắt mỗi công trình trong 1-2 câu, tập trung mô tả vào khía cạnh mà bài làm của bạn khác biệt hoặc cách bạn khắc phục các hạn chế của họ.

**4. Method**

- Mô tả lại thiết lập bài toán, nhưng chi tiết hơn và theo cách trang trọng (formal) hơn. Giới thiệu các ký hiệu toán học cần thiết cho các công thức sau đó. Khuyến nghị nên có một hình ảnh mô tả phương pháp tổng thể.

- Báo cáo cần phải mang tính tự thân (self-contained); người đọc phải hiểu được ý tưởng mà không cần đọc các bài báo khác. Nếu cần, hãy cung cấp kiến thức nền tảng (kiến thức tối thiểu để hiểu công trình của bạn).

- Hãy suy nghĩ về cách hiệu quả nhất để giải thích các ý tưởng chính. Một lựa chọn là ưu tiên trình bày các thành phần trong phương pháp của bạn không phải theo thứ tự xuất hiện, mà theo mức độ quan trọng. Các chi tiết ít quan trọng hơn có thể để ở cuối hoặc đưa vào phần phụ lục.

- Sử dụng các hỗ trợ trực quan (hình ảnh, biểu đồ) trong phần trình bày. Càng nhiều càng tốt.

- Trình bày càng rõ ràng và cụ thể càng tốt. Các công thức toán học có thể làm cho phần giải thích rõ ràng và súc tích hơn.

**5. Experimental Results**

- Mô tả rõ ràng thiết lập thí nghiệm, bao gồm các benchmarks/datasets, các chỉ số đánh giá (metrics), và các phương pháp baseline.

- Cung cấp cả kết quả định lượng (bảng biểu) và kết quả định tính (hình ảnh).

- So sánh với các phương pháp baseline. Giải thích rõ phương pháp của bạn tốt hơn ở khía cạnh nào. Hãy nghĩ về cách tốt nhất để chứng minh ưu thế của phương pháp bạn so với baseline.

- Thực hiện nghiên cứu cắt giảm (ablation study) và hiển thị kết quả. Nếu bạn có nhiều đóng góp kỹ thuật, hãy chứng minh từng thành phần ảnh hưởng đến kết quả như thế nào.

- Không được bỏ sót bất kỳ benchmark/dataset nổi tiếng, chỉ số đánh giá chuẩn, hoặc phương pháp trước đây nào.

- Thực hiện các so sánh công bằng và hợp lý (so sánh "táo với táo"). Hoặc, nếu phương pháp baseline có lợi thế nào đó (như được giám sát mạnh hơn), hãy mô tả rõ ràng.

- Tại đây hoặc trong phần kết luận, cân nhắc việc hiển thị một số trường hợp thất bại (failure cases) đáng chú ý để giải thích hạn chế của phương pháp đề xuất hoặc làm động lực cho các nghiên cứu tương lai.

**6. Conclusion**

- Tóm tắt ngắn gọn dự án, đặc biệt là các ý tưởng chính và kết quả thực nghiệm.

- Mô tả hạn chế của công trình đề xuất và các hướng nghiên cứu tiềm năng trong tương lai.

---
