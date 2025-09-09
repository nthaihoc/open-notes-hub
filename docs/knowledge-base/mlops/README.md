---
title: MLOps Tutorials
hide:
    - navigation
---

# 🫒 MLOps Tutorials: Fundamentals & Practices
---

## I. Nguyên lý nền tảng của một quy trình MLOps
### 1. Sự phát triển của hạ tầng và phát triển phầm mềm
Sự ra đời của kỷ nguyên internet hiện đại (khoảng năm 1995), đã chứng kiến sự gia tăng của các ứng dụng phần mềm, từ các hệ điều hành như Windows 95, Linux cho đến các website như Google và Amazon, đây là những nền tảng trực tuyến đã phục vụ toàn cầu trong hơn hai thập kỷ. Điều này đã vô tình tạo ra một văn hóa cải tiến dịch vụ liên tục bằng cách thu thập, lưu trữ và xử lý lượng dữ khổng lồ từ tương tác của người dùng chung. Những sự phát triển này đã định hình sự tiến hóa của hạ tầng CNTT và phát triển phần mềm.

Các doanh nghiệp ngày càng áp dụng điện toán đám mây (cloud computing), vì chúng mở ra khả năng thuê ngoài việc bảo trì hạ tầng CNTT, đồng thời cung cấp các tài nguyên cần thiết như lưu trữ và tính tóan để vận hành và mở rộng hoạt động. Điện toán đám mây mang lại khả năng cung cấp theo nhu cầu và sẵn sàng các tài nguyên CNTT mà không cần người dùng trực tiếp quản lý. Ví dụ: các công ty có thể thuê năng lực tính toán và lưu trữ mà không phải chịu trách nhiệm duy trì - việc này được giao cho nhà cung cấp dịch vụ. Nhờ đó, doanh nghiệp đã tiết kiệm được chi phí, giảm nhu cầu đội ngũ kỹ thuật IT và có thể tối ưu hóa nguồn lực. Điện toán đám mây cũng cho phép mở rộng và thanh toán dựa trên mức sử dụng thực tế khi cần.

Trong thập kỷ qua, nhiều công ty lớn như Google, IBM, Microsoft đã đầu tư mạnh vào nghiên cứu và phát triển dịch vụ đám mây. Điều này đã dẫn đến sự chuyển dịch từ máy chủ cục bộ (localized computing) sang điện toán theo nhu cầu (on-demand computing).

### 2. Sự phát triển của Machine Learning và Deep Learning
Trong suốt thập kỷ qua, chúng ta đã chứng kiến các ứng dụng Machine Leanring (ML) đã len lỏi vào nhiều lĩnh vực trong đời sống hàng ngày. Từ dịch máy (machine translation), xử lý hình ảnh (image processing) cho đến nhận dạng giọng nói (voice recognition). Những ứng dụng này được thúc đẩy bởi sự phát triển của hạ tầng tính toán, đặc biệt là khai thác sức mạnh xử lý (computation power), mở ra tiềm năng to lớn cho Deep Learning (DL) và ML.

Những bước đột phá trong DL có mối tương quan chặt chẽ với sự gia tăng của năng lực tính toán. Những đột phá này được hỗ trợ bởi sự tăng trưởng theo câp số nhân của sức mạnh tính toán, với mức tăng khoảng 35 lân mỗi 18 tháng. Tuy nhiên, trong tương lại, với nhu cầu ngày càng lớn, việc gặp phải giới hạn khi mở rộng khả năng tính toán trung tâm dựa trên CPU, GPU hoặc TPU là điều không thể tránh khỏi. Điều này đã buộc phải xem xét các giải pháp thay thế, chẳng hạn như:

- Distributed learning (học phân tán): xử lý dữ liệu được phân bổ trên nhiều nút tính toán.
- Federated learning (học liên kết): học liên kết, dữ liệu vẫn ở thiết bị người dùng, chỉ mô hình được huấn luyện chung.
- Edge computing: xử lý dữ liệu ngay tại thiết bị biên (smartphone, IoT) thay vì gửi toán bộ lên trung tâm dữ liệu.

Toàn bộ các phương pháp học phân tán đã cho thấy được tiềm năng và mang lại nhiều sự hứa hẹn để đáp ứng nhu cầu ngày càng tăng của DL.

### 3. Ứng dụng lấy AI làm trung tâm
Các ứng dụng ngày càng trở nên AI-centric, điều này diễn ra ở nhiều nghành công nghiệp. Hầu như mọi ứng dụng hiện nay đều tích hợp AI, và chúng thường chạy tách biệt trên các tải công việc phân tán (distributed workloads) như HPC (High-Performance Computing), Microservices và Big Data. Bằng cách kết hợp HPC và AI, ta có được khả năng tính toán mạnh mẽ cần thiết để huấn luyện các mô hình DL và ML. Vơi sự giao thoa của Big Data và AI, ta có thể khai thác dữ liệu ở quy mô lớn để huấn luyện mô hình AI. Với sự giao thoa của Microservices và AI, ta có thể triển khai mô hình AI phục vụ suy luận (inference) tăng cường hoạt động kinh doanh và tạo ra các tác động thực tiễn. Chính vì vậy, các ứng dụng phân tán đã trở thành một chuẩn mực mới (new norm).

Để phát triển ứng dụng AI-centric ở quy mô lớn, cần có sự cộng hưởng của các ứng dụng phân tán. Và để đạt được điêu này, cần một cách phát triển phần mềm mới.

### 4. Sự tiến hóa trong phát triển phầm mềm
Phát triển phầm mềm đã tiến hóa song hành với sự phát triển của hạ tầng CNTT nhằm hỗ trợ việc phát triển ứng dụng một cách hiệu quả. Mô hình thác nước (Waterfall method) là một phương pháp truyền thống, trong đó quá trình phát triển diễn ra theo tuyến tính: thu thập yêu cầu, thiết kế và phát triển. Tuy nhiên, phương pháp này có nhiều hạn chế, dẫn đến sự xuất hiện của các phương pháp mới như Agile và DevOps.

Mô hình Waterfall được sử dụng rộng rãi từ khi bắt đầu kỷ nguyên internet. Đây là một cach phát triển không lặp lại (non-iterative), thực hiện theo chiêu đơn hướng (unidirectional). Mỗi giai đoạn được xác định sẵn và thực hiện tuần tự. Mô hình này thích hợp khi yêu cẩu được xác định rõ ràng, cụ thể và không thay đổi theo thời gian. Ngược lại, không phù hợp với các dự dán động - nơi yêu cầu thường xuyên thay đổi theo nhu câu người dùng.

Nhìn chung, mô hình Waterfall tồn tại những nhược điểm chính như:

- Toàn bộ yêu cầu phải được xác định ngay từ đầu, không thể thay đổi trong quá trình hoặc sau khi phát triển.
- Khó tạo ra hoặc tái sử dụng các thành phần phần mềm.
- Kiểm thử chỉ diễn ra sau khi phát triển xong, không thể lặp lại, và không dễ sửa lỗi khi đã hoàn tất.
- Việc kiểm thử chấp nhận của khách hàng thường dấn đến thay đổi, gây chậm trễ và chi phí cao.
- Hệ thống thường được xây dựng theo cách hiểu của lập trình viên, không phải là từ góc nhìn người dùng, dẫn đến sản phẩm không đáp ứng nhu cầu thực tế.

Phương pháp Agile khắc phục những hạn chế của Waterfall với ưu thế tạo điều kiện cho một cách tiếp cận lặp lại (iterative) và tiến bộ trong phát triển phần mèm. khác với Waterfall, Agile lấy người dùng làm trung tâm. Phương pháp này mang tính hai chiều (bidirectional) và thường có sự tham gia trực tiếp của người dùng hoặc khách hàng trong quá trình phát triển và kiểm thử. Nhờ đó, có cơ hội để kiểm tra, phản hồi, và đề xuất cải tiến xuyên suốt các giai đoạn của dự án.

Một số ưu điểm của Agile:

- Yêu cầu được xác định trước khi bắt đầu phát triển ứng dụng, nhưng có thể được thay đổi bất cứ lức nào.
- Có thể tạo hoặc triển khai các thành phần tái sử dụng.
- Giải pháp có thể được chia thành nhiều module nhỏ, được xử lý và bàn giao định kỳ.
- Người dùng hoặc khách hàng có thể đồng sáng tạo bằng cách kiểm thử và đánh giá các module đã phát triển theo từng giai đoạn, đảm bảo rằng nhu cầu thực tế được đáp ứng.

Phương pháp DevOps mở rộng các thực tiễn của Agile bằng cách tinh gọn hơn nữa quá trình thay đổi phần mềm qua các giai đoạn: xây dựng (build), kiểm thử (test), triển khai (deploy) và bàn giao (delivery). DevOps trao quyền cho các nhóm đa chức năng quyền tự chủ trong việc thực thi ứng dụng phần mềm, dựa trên các cơ chế: CI (Continuous Integration - Tích hợp liên tục), CD (Continous Deployment - Triển khai liên tục) và CD (Continous Delivery - Bàn giao liên tục).

Phương pháp này khuyến khích sự hợp tác, tích hợp và tự động hóa giữa lập trình viên và nhân viện vận hành IT, năng cao hiệu quả, tốc độ và chât lượng trong việc cung cấp phầm mềm hướng tới người dùng. DevOps cung cấp một khung phát triển phầm mềm tinh gọn cho việc thiết kế, kiểm thử, triển khai và giám sát hệ thống trong môi trường production.

### 5. Thách thức của việc phát triển phầm mềm truyền thống 
Mặc dù DevOps đã giúp doanh nghiệp triển khai phần mềm một cách nhanh chóng và tin cậy, cho phép đưa phần mềm vào production chỉ trong vài phút và vẫn giũ cho hệ thống hoạt động oonrn định. Tuy nhiên, chúng không thể áp dụng y nguyên cho ứng dụng ML và DL. Nguyên nhân chính là ML development khác căn bản so với software development truyền thống. Phần mềm truyền thống chỉ gồm code, trong khi đó ML là code và data. Trong khi code được viết và kiểm soát cẩn thận trong môi trường phát triển, thì dữ liệu lại được thu thập từ nhiều nguồn khác nhau. Dữ liệu luôn luôn thay đổi theo khối lượng, tốc độ, độ tin cậy và đa dạng. Do đó, khi dữ liệu tiến hóa, code cũng cần phải thay đổi theo thời gian.

Có thể hình dung code và data tồn tại trên hai mặt phẳng khác nhau: cùng chia sẻ trục thời gian, nhưng độc lập ở các khía cạnh khác. Thách thức trong phát triển ML là xây cầu nối giữa code và data theo cách có kiểm soát. Nếu không quản lý tốt, triển khai sẽ chậm chạp, mong manh, rời rạc và không nhất quán, thiếu sự tái lập và truy xuất nguồn gốc. Để giải quyết các vấn đề trên, MLOPs đưa ra một cách tiếp cận có hệ thống:

- Kết nối code và data cùng tiến triển theo thời gian với một mục tiêu duy nhất, xây dựng và duy trì một hệ thống ML mạnh mẽ, có thể mở rộng.
- Hỗ trợ phát triển, triển khai, giám sát ML model một cách tinh gọn và hệ thống.
- Trao quyền hợp tác cho nhóm Data Science & IT, cùng xác thực, kiểm soát và quản trị hoạt động.
- Tất cả các hoạt động đều được ghi lại, kiểm toán có thể truy xuất và lặp lại.

### 6. Khái niệm và quy trình làm việc của MLOps

**Khái niệm.** MLOps là một phương pháp mới nổi nhằm kết hợp ML với phát triển phần mềm bằng cách tích hợp nhiều lĩnh vực khác nhau, vì MLOPs kết hợp ML, DevOps và kỹ thuật dữ liệu (Data Engineering) với mục tiêu xây dựng, triển khai và duy trì các hệ thống ML trong môi trường sản xuất. Do đó, MLOps có thể được giải thích như là một giao điểm của ba lĩnh vực này.

**Quy trình làm việc.** Nhìn chung, quy trình công việc của MLOps được chia thành hai mô-đun. 

- Pipeline MLOps (xây dựng, triển khai và giám sát) - lớp trên cùng. 
- Các ýếu tố điều khiển (drivers): dữ liệu, mã nguồn, artifacts, middleware và hạ tầng - lớp giữa và lớp dưới.

Lớp Pipeline MLOPs được vận hành nhờ các yếu tố điều khiển như dữ liệu, mã nguồn, artifacts, middleware và hạ tầng. Chúng được hỗ trợ bởi một tập hợp các dịch vụ, drivers, middleware và hạ tầng, từ dó tạo ra các giải pháp dựa trên ML.


