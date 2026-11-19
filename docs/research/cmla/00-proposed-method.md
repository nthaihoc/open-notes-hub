---
Title: CMLA - Cascaded Masked Loss Architecture for Cervical Cancer Cytology Diagnosis on Heterogeneous Datasets
Tag: 
  - deep leanring
  - classification
  - cervical cancer cytology
---

# </center>CMLA - Cascaded Masked Loss Architecture for Cervical Cancer Cytology Diagnosis</center>
---

## Motivation
---

- **Bối cảnh:** Ung thư cổ tử cung là căn bệnh nguy hiểm, có tỷ lệ gây tử vong cao ở phụ nữ. Nhưng hoàn toàn có thể phòng/chữa nếu phát hiện sớm. Vì vậy việc tầm soát căn bệnh này là chìa khoá để đảm bảo sức khoẻ an toàn.
- **Nút thắt lâm sàng:** Tầm soát truyền thống chủ yếu dựa vào (Pap/LBC) đòi hỏi sự tập trung cao độ, áp lực thời gian và khối lượng công việc dẫn đến sự mệt mỏi về thị giác dẫn đến những quyết định chẩn đoán sai lầm.
- **Khoảng trống nghiên cứu:** Kỳ vọng rằng sẽ giải quyết được các nút thắt trên bằng cách sử dụng các phương pháp AI, nhưng khi triển khai trong thực tế thì vấp phải 3 rào cản chí mạng:
	- Gộp chung không gian học (Flat classifiers): AI bị bắt học từ cái dễ đến cái cực khó trong cùng một bước, dẫn đến việc lẫn lộn không gian feature (đặc trưng).
	- Sự mơ hồ hình thái (Morphological ambiguity): Các tế bào chuyển hoá liên tục, ranh giới quá mờ nhạt khiến AI khó học và trở nên bối rối trước những dự đoán.
	- Lãng phí dữ liệu (Label Heterogeneity): Mỗi một bộ dữ liệu đều được gán nhãn theo một chuẩn riêng. Việc cố gắng ép toàn bộ các bộ dataset này về cùng một chuẩn để đồng nhất trong quá trình huấn luyện sẽ vô tình làm vứt bỏ các thông tin quý giá.
* **Giải pháp**: Cố gắng bắt chước cách tư duy của một bác sĩ thật (từ nhìn lướt đến soi kỹ) bằng kiến trúc C-MLA:
	* Hierarchical Cascade: Chia để trị. Sàng lọc nhị phân --> Đánh giá mức độ --> Phân loại chi tiết. Chống nhiễu loạn đặc trưng.
	* Sample-level Masked Loss: Một hàm mất mát thông minh. Dữ liệu có nhãn đến đâu, tính gradient và học đến đó. Không ép chuẩn, không vứt bỏ bất kỳ dữ liệu của bộ dataset nào.
  
## Related Work
---

- Các phương pháp phẳng đang ép một hệ thống sinh học phân cấp phức tạp vào một không gian phẳng, gây ra nhiễu đặc trưng.
- Để giải quyết, sử dụng mạng Cascaded/Hierarchical. Tuy nhiên, các mạng này (dù là 2 hay 3 stage) hiện tại thường bị cô lập về mặt tối ưu hoá **isolated optimization** hoặc bị **Error propagation** do thiếu cơ chế huấn luyện end-to-end hiệu quả.
- Khi mở rộng ra dữ liệu dạng đa trung tâm, gặp phải bài toán heterogeneous taxonomy. Các phương pháp masked loss truyền thống từ mảng segmentation/multi-label sẽ thất bại do chúng hoạt động trên các nhãn độc lập. Ví dụ: Chúng bỏ qua tính phụ thuộc có điều kiện của các nhãn y khoa.
- Để khắc phục khoảng trống này, C-MLA đưa ra một cơ chế **masked loss** nhận thức phân cấp, cho phép mô hình điều hướng gradient tự động theo độ sâu của nhãn khả dụng, vừa giải quyết được nhiễu đặc trưng vừa vắt kiệt giá trị của dữ liệu đa trung tâm mà không cần ép chuẩn.

## Proposed Model
---

**Preliminaries.** Gọi hàm dự đoán nhãn $y$ của mô hình cho dữ liệu $x$ với tham số $\theta$ là $\mathbf{f}[x, \theta]$.
 
**Defined Problem.** Không giống như các mô hình phân loại phẳng (flat classification) ép buộc các mạng nơ-ron phải ánh xạ trực tiếp từ ảnh thô sang các nhãn bệnh lý phức tạp (chuẩn Bethesda). Phương pháp đề xuất dược thiết kế để xác suất mô hình hoá chẩn đoán tế bào học thành một không gian xác suất tuần tự và có điều kiện (cascaded). Đối với mỗi ảnh đầu vào $x$, sử dụng một backbone chung để trích xuất đặc trưng $\phi[x]$ nén thông tin thành một vector đặc trưng duy nhất.

$$z = \phi[x] \in \mathbb{R}^d$$

Điểm cốt lõi chính của phương pháp chính là việc tiền xử lý dữ liệu đa trung tâm. Mỗi ảnh $x$ sẽ được gán một vector nhãn gốc $y = \left[y^{(1)}, y^{(2)}, y^{(3)}\right]$. Để duy trì được sự đồng nhất của đồ thị tính toán trong quá trình training, mọi nhãn bị khuyết sẽ được gán bằng giá trị bằng âm một.

**Backpropagation and Cascaded Architecture.** Các vector đặc trưng $\mathbf{z}$ đểu trải qua tuần tự 3 tầng phân loại (tương ứng với 3 nhiệm vụ khác nhau) có mức độ chi tiết tăng dần. 

- **Stage 01. Binary Screening.** Tầng này cố gắng thiết lập một không gian phân rã nhằm cô lập tế bào bình thường (normal) ra khỏi các tế bào bệnh lý (abnormal).

$$
\hat{y}^{(1)} = \mathbf{f_1}[z, \theta_1]
$$

- **Stage 02. Lession Grading.** Tại tầng này, các thông tin trong tầng một được tiếp nhận và kế thùa thông qua việc áp dụng cơ chế **FILM** (Feature-wise Linear Modulation).

    - Tích hợp một mạng MLP đơn giản gồm 2 lớp. Mạng này không nhận vector đặc trưng $z$ thô, mà chỉ nhận và mô phỏng xác suất đầu ra $\hat{y}^{(1)}$ ở tầng một thành hai vector có cùng kích thước với dim_model (ví dụ 256) ký hiệu là $\gamma$ và $\beta$.
    - Sau đó, mới đem vector đặc trưng thô $z$ kết hợp với hai vector vừa được tạo ra theo phương trình (1). Sau đó lớp phân loại ở giai đoạn ở tầng này nhận trực tiếp không gian tinh chỉnh $z[\cdot]$ để đưa ra dự đoán cấp độ (công thức 2).

$$
\begin{equation}
z_1 = \gamma_1 \odot z + \beta_1
\end{equation}
$$

$$
\begin{equation}
\hat{y}^{(2)} = \mathbf{f}_2 [z_1, \theta_2]
\end{equation}
$$

- **Stage 03. Fine-grained Subtyping.** Tầng cuối cùng sử dụng hai nhánh chuyên gia độc lập để xử lý song song, nhăm phân ly các tổn thương vi mô có ranh mới mờ nhạt và dễ nhầm lẫn mà không làm phân tán toàn bộ kiến thức của mô hình. Giống như tầng hai, tại đây cũng sử dụng cơ chế FILM để mô phỏng xác suất đầu ra của tầng hai.

$$
\begin{equation}
z_2 = \gamma_2 \odot z_1 + \beta_2
\end{equation}
$$

$$
\begin{equation}
\hat{y}_{\operatorname{low}}^{(3)} = \mathbf{f}_{3L}[z_2, \theta_3]; \qquad
\hat{y}_{\operatorname{high}}^{(3)} = \mathbf{f}_{3H}[z_2, \theta_3];
\end{equation}
$$

**Loss Function & Optimization.** Do mô hình được thiết kế để training trên nhiều dữ liệu bất đồng bộ. Nhằm ngăn chặn cac dự đoán dư thừa gây nhiễu cho quá trình cập nhất và tối ưu tham số. Hàm loss được thiết kế cơ chế mặt nạ (masked) với mục tiêu là khoá chặt các luồng gradient tại các vị trí nhãn khuyết đảm bảo mô hình chỉ học trên các dữ liệu không bị khuyết nhãn $y$.

## Processing and Split Data Strategies

**Datasets.** Toàn bộ quá trình thực nghiệm được tiến hành trên 5 bộ dữ liệu tế bào học đa trung tâm: **HiCervix**, **Herlev**, **Mendeley LBC**, **BVA (Hospital A)** và **SipakMed**.

**Data Preprocessing and Splitting.** Mỗi bộ dữ liệu ban đầu được phân tách độc lập thành ba tập: Huấn luyện (Train), Phát triển (Dev) và Kiểm thử (Test) theo tỷ lệ **70/15/15 (%)**. Chiến lược lấy mẫu phân tầng (**stratified sampling**) được áp dụng để đảm bảo sự cân bằng về tỷ lệ các lớp bệnh lý trong từng tập, đặc biệt quan trọng đối với các bộ dữ liệu có quy mô nhỏ. Sau đó, các tập dữ liệu tương ứng từ 5 trung tâm được gộp lại thành một tập Train, Dev và Test duy nhất nhằm phục vụ quá trình huấn luyện và đánh giá mô hình đa miền.

Bảng 1 trình bày chi tiết sự phân bố số lượng mẫu của các tập dữ liệu sau khi phân chia. Ngoải ra thống kê chi tiết đặc điểm và sự phân bố nhãn của từng bộ dữ liệu được mô tả trong [Appendix B](#appendix-b-datasets-statistic).

**Table 1: Distribution of samples across Train, Dev, and Test sets.**

| Name | #Train | #Dev | #Test | Total |
| :-- | :--: | :---: | :---: | :---: |
| BVA | 15,703 | 3,365 | 3,366 | 22,434 |
| Herlev | 641 | 137 | 139 | 917 |
| HiCervix | 6,188 | 1,325 | 1,327 | 8,840 |
| MendeleyLBC | 673 | 144 | 145 | 962 |
| SipakMed | 2,834 | 607 | 608 | 4,049 |

**Label Mapping and Hierarchical Strategy.** Mục tiêu của bài toán là phân loại tế bào học dựa trên 5 nhãn tiêu chuẩn theo hệ thống Bethesda: ASC-H, ASC-US, HSIL, LSIL và SCC. Để tương thích với kiến trúc phân cấp của mô hình CMLA, dữ liệu nhãn được ánh xạ thành 3 tầng (stage) với cấu trúc như sau:

*   **Stage 1 (Binary Screening):** Phân loại Bình thường (0) và Bất thường (1).
*   **Stage 2 (Lesion Grading):** Phân loại tổn thương mức độ Thấp (Low - 0) và Cao (High - 1).
*   **Stage 3 (Fine-grained Subtyping):** Phân loại chi tiết các lớp bệnh lý.

Do sự khác biệt về hệ thống phân loại giữa các trung tâm, các bộ dữ liệu như Hospital A, HiCervix và Mendeley LBC có đầy đủ nhãn ở cả 3 tầng, do đó chúng tham gia vào quá trình huấn luyện và tính đạo hàm (backpropagation) ở tất cả các Stage. Ngược lại, các bộ dữ liệu bị khuyết nhãn chi tiết (Herlev, SipakMed) chỉ cung cấp tín hiệu giám sát cho Stage 1. Các nhãn không xác định được gán giá trị `-1` để bỏ qua trong hàm Loss. Chi tiết rule gán nhãn mô tả trong [Appendix A](#a2-label-mapping).

## Pseudocode for CMLA Loss

**Preliminaries.** Xét một batch dữ liệu đầu vào với nhãn tương ứng $\mathbf{y} = (y_{s1}, y_{s2}, y_{s3})$. Mô hình sinh ra các vector logits $\mathbf{z} = (z_{s1}, z_{s2}, z_{s3\_low}, z_{s3\_high})$ cho từng nhánh phân loại. 

**Compute Loss Step-by-Step.** Trước khi tính toán loss, cần tạo ra các mặt nạ (mask) để loại bỏ những mẫu không hợp lệ (chứa nhãn khuyết `-1`) tại từng tầng, đảm bảo tín hiệu giám sát được lan truyền chính xác.

- **Giả lập vòng lặp huấn luyện (Training Loop):**

```python
# Khởi tạo data_loader, model, criterion, optimizer...
device = "cuda" if torch.cuda.is_available() else "cpu"
model = MyModel().to(device)
criterion = CMLAFocalLoss().to(device)
optimizer = MyOptimizer(model.parameters())

for step, batch in enumerate(train_loader):
    optimizer.zero_grad()
    
    inputs = batch["image"].to(device)
    y_s1 = batch["y_s1"].to(device)
    y_s2 = batch["y_s2"].to(device)
    y_s3 = batch["y_s3"].to(device)

    targets = (y_s1, y_s2, y_s3)
    logits = model(inputs)
    
    total_loss, loss_dict = criterion(logits, targets)

    total_loss.backward()
    optimizer.step()
```

- **Stage 1 (Binary Screening):** Chỉ những mẫu có nhãn tầng 1 hợp lệ (khác `-1`) mới tham gia tính loss. Các mẫu này luôn có nhãn nhị phân là 0 hoặc 1.

```python
valid_s1 = (y_s1 != -1)
logits_s1_valid = logits_s1[valid_s1]
targets_s1_valid = y_s1[valid_s1]
```

- **Stage 2 (Lesion Grading):** Tầng 2 phân loại chi tiết hơn (Low/High), nên chỉ những mẫu được xác định là "Có bệnh" ở tầng 1 ($y_{s1} == 1$) và có nhãn tầng 2 hợp lệ mới được đưa vào tính toán.
  
```python
valid_s2 = (y_s1 == 1) & (y_s2 != -1)
logits_s2_valid = logits_s2[valid_s2]
targets_s2_valid = y_s2[valid_s2]
```

- **Stage 3 (Fine-grained Subtyping):** Tầng cuối tách thành 2 nhánh song song, yêu cầu hai mặt nạ riêng biệt. Nhánh `low` chỉ nhận các mẫu có nhãn tầng 2 bằng 0. Ngược lại, nhánh `high` nhận các mẫu có nhãn tầng 2 bằng 1. Cả hai đều yêu cầu nhãn tầng 3 phải hợp lệ (khác `-1`).

```python
valid_low = (y_s1 == 1) & (y_s2 == 0) & (y_s3 != -1)
valid_high = (y_s1 == 1) & (y_s2 == 1) & (y_s3 != -1)

logits_low_valid = logits_s3_low[valid_low]
targets_low_valid = y_s3[valid_low]

logits_high_valid = logits_s3_high[valid_high]
targets_high_valid = y_s3[valid_high]
```

- **Tính toán Loss:** Sau khi trích xuất các mẫu hợp lệ, đưa chúng qua các hàm loss tương ứng. Tầng 1 và tầng 2 sử dụng **BCE** (với Logits), trong khi tầng 3 sử dụng **CE** (Cross-Entropy). 

```python
import torch
import torch.nn as nn

# reduction='none' là bắt buộc để giữ nguyên loss của từng mẫu, phục vụ tính Focal Loss
loss_bce = nn.BCEWithLogitsLoss(reduction='none')
loss_ce = nn.CrossEntropyLoss(reduction='none')

lambda_1, lambda_2, lambda_3 = 1.0, 1.0, 1.0

# Tính loss từng nhánh (giả định đã qua xử lý Focal và lấy trung bình)
loss_s1 = loss_bce(logits_s1_valid, targets_s1_valid).mean()
loss_s2 = loss_bce(logits_s2_valid, targets_s2_valid).mean()

loss_low = loss_ce(logits_low_valid, targets_low_valid).mean()
loss_high = loss_ce(logits_high_valid, targets_high_valid).mean()

# Loss tầng 3 là trung bình có trọng số dựa trên số lượng mẫu của 2 nhánh
count_low = targets_low_valid.shape[0]
count_high = targets_high_valid.shape[0]
loss_s3 = (loss_low * count_low + loss_high * count_high) / (count_low + count_high + 1e-8)

# Tổng loss
total_loss = loss_s1 * lambda_1 + loss_s2 * lambda_2 + loss_s3 * lambda_3
```

Chi tiết mã nguồn của hàm Focal Loss được trình bày trong [Appendix A](#a1-focal-loss-with-pytorch).

**Notes for Implementation.**

1.  **Về tham số `reduction`:** Khi khởi tạo các hàm loss từ thư viện `torch`, tham số `reduction` bắt buộc phải được set là `'none'`. Nếu để mặc định (`'mean'`), PyTorch sẽ lấy trung bình loss của *toàn bộ* batch, điều này vô tình phá hỏng cơ chế mask và tính trung bình có trọng số của CMLA Loss.
2.  **Về cách tính trung bình:** Luôn tính trung bình loss của một batch dựa trên **tổng số mẫu hợp lệ thực tế** (ví dụ: `count_s1`, `count_s3_low`). Tuyệt đối không chia cho tổng số mẫu của batch (batch size). Do trong một batch có thể chứa các mẫu bị khuyết nhãn ở các tầng khác nhau, việc chia cho batch size sẽ làm sai lệch gradient lan truyền về.
 
## Experiments

**Baseline.** Lựa chọn họ mô hình **ResNet50** đại diện cho kiến trúc phân loại phẳng, tích hợp thêm các lớp classifier để phân loại chi tiết 6 lớp.

**Research Requets.** Xây dựng các câu hỏi nghiên cứu để xác định hướng thực nghiệm qua đó chứng minh và trả lời các câu hỏi.

- **RQ1.** Mô hình CMLA có cái thiện hay khắc phục được các nhược điểm và hạn chế của mô hình phân loại phẳng?

- **RQ2.** Việc tận dựng và xây dựng tập dữ liệu bất đồng bộ có thật sự giúp cho mô hình học tốt hơn và có khả năng khái quát hoá tốt hơn trên một nhiệm vụ cụ thể không?

- **RQ3.** Thực nghiệm cắt bỏ, thành phần nào có đóng góp or tác động trực tiếp đến hiệu suất đầu ra của mô hình?

- **RQ4.** Kiến trúc CMLA có hiệu quả đối với tất cả các backbone khác ngoài ResNet không?

- **RQ5.** Đánh giá hiệu suất chi tiết của mô hình CMLA và Baseline trên từng bộ dữ liệu tham gia huấn luyện. Làm rõ hiệu suất của mô hinh trên nhiều miền dữ liệu có miền đặc trưng khác biệt. Sau đó phân tích kỹ lưỡng cấc case tiêu biểu mà kiến trúc CMLA tỏ ra ổn định và vượt trội hơn so với Baseline.

Để trả lời và chứng minh các câu hỏi nghiên cứu, các bảng ma trận thực nghiệm được thiết kế chi tiết trong [Appendix C](#appendix-b-matrix-implementation) cho từng câu hỏi.

**Settings.** Để đảm bảo tính khách quan và độ tin cậy, mỗi phương pháp đề xuất được huấn luyện và đánh giá độc lập qua 5 lần (5 runs) trên cấu hình phần cứng gồm 2 GPU NVIDIA T4 (16GB) và 15GB RAM. Kết quả thực nghiệm được báo cáo dưới dạng trung bình và độ lệch chuẩn ($mean \pm std$), đi kèm với kiểm định thống kê để xác định mức ý nghĩa với ngưỡng $p \leq 0.05$. Quá trình huấn luyện sử dụng thuật toán tối ưu Adam, kết hợp bộ điều chỉnh tốc độ học tuyến tính (Linear Scheduler) và cơ chế dừng sớm (Early Stopping). Chi tiết toàn bộ các siêu tham số (hyperparameters) được cung cấp trong [Appendix A.](#appendix-a-implementation-details)

## Evaluation Protocol

**Metrics.** Để đánh giá hiệu suất cho mô hình nói chung và các nhiệm vụ nói riêng. Các thước đo được lựa chọn để đánh giá là **F1-Score**, **Precision**, **Recall** và **Accuracy**. Trong quá trình đánh gía, ngoại trừ Accuracy được tính toán bằng cơ chế `micro` thì tất cả đều được tính dựa trên `macro` để đảm hiệu suất của mô hình phản ánh đúng trên dữ liệu mất cân bằng.

**Pipeline.** Do mô hình được huấn luyện trên bộ dữ liệu đa trung tâm, vậy nên quá trình đánh giá cho từng nhiệm vụ cũng được xử lý theo một cách riêng biệt. Mục tiêu của bài toán là xoay quanh hai task chính: (1) binary classification cho việc nhận diện normal/abnormal (phân loại âm và dương tính) và low/high (cấp độ tổn thương); (2) Multi-label classification phân loại chi tiết các nhãn bệnh dựa theo chuẩn Bethesda.

- **Binary Classification:** Thực hiện đánh giá trên toàn bộ dữ liệu test đa trung tâm. Vì tất cả các dữ liệu này đều có thể tham gia vào tác vụ nhị phân.
- **Multi-label classification:** Đánh giá trên các tập dữ liệu có nhãn thuộc một trong 6 loại nhãn theo chuẩn Bethesda, những mẫu dữ liệu không có nhãn này sẽ bị loại bỏ.

## Results

**Bảng 1.** Kết qủa đánh giả trên toàn bộ dữ liệu (all) và hiệu suất trên từng bộ dữ liệu riêng lẻ của mô hình CMLA và mô hình baseline khi huấn luyện với hàm Cross-Entropy.

| Model    | Task   | Metrics   | ALL          | BVA           | HERLEV       | HICERVIX      | MENDELEY_LBC   | SIPAKMED      |
|:---------|:-------|:----------|:-------------|:--------------|:-------------|:--------------|:---------------|:--------------|
| baseline | binary | acc       | 93.92 ± 0.09 | 99.99 ± 0.01  | 28.86 ± 1.30 | 99.97 ± 0.07  | 100.00 ± 0.00  | 60.59 ± 0.47  |
| baseline | binary | f1        | 96.55 ± 0.05 | 100.00 ± 0.00 | 10.71 ± 3.21 | 99.98 ± 0.04  | 100.00 ± 0.00  | 5.05 ± 2.21   |
| baseline | binary | pre       | 99.97 ± 0.01 | 100.00 ± 0.00 | 78.33 ± 6.02 | 100.00 ± 0.00 | 100.00 ± 0.00  | 100.00 ± 0.00 |
| baseline | binary | rec       | 93.36 ± 0.09 | 99.99 ± 0.01  | 5.77 ± 1.80  | 99.97 ± 0.07  | 100.00 ± 0.00  | 2.60 ± 1.17   |
| cmla     | binary | acc       | 99.55 ± 0.07 | 100.00 ± 0.00 | 91.71 ± 1.30 | 100.00 ± 0.00 | 98.63 ± 0.97   | 98.06 ± 0.24  |
| cmla     | binary | f1        | 99.75 ± 0.04 | 100.00 ± 0.00 | 94.56 ± 0.89 | 100.00 ± 0.00 | 98.19 ± 1.25   | 97.61 ± 0.30  |
| cmla     | binary | pre       | 99.66 ± 0.03 | 100.00 ± 0.00 | 92.16 ± 0.71 | 100.00 ± 0.00 | 96.48 ± 2.40   | 97.18 ± 0.28  |
| cmla     | binary | rec       | 99.84 ± 0.05 | 100.00 ± 0.00 | 97.12 ± 1.80 | 100.00 ± 0.00 | 100.00 ± 0.00  | 98.05 ± 0.53  |
| baseline | multi  | acc       | 69.00 ± 0.23 | 62.66 ± 0.31  | 95.55 ± 1.52 | 72.94 ± 0.63  | 96.30 ± 1.25   | 100.00 ± 0.00 |
| baseline | multi  | f1        | 72.51 ± 0.27 | 61.80 ± 4.63  | 39.15 ± 9.27 | 70.48 ± 5.00  | 84.97 ± 11.58  | 100.00 ± 0.00 |
| baseline | multi  | pre       | 72.21 ± 0.37 | 61.33 ± 4.59  | 40.00 ± 9.13 | 70.62 ± 4.98  | 84.73 ± 10.98  | 100.00 ± 0.00 |
| baseline | multi  | rec       | 73.08 ± 0.34 | 62.72 ± 4.79  | 38.33 ± 9.38 | 70.53 ± 5.06  | 86.45 ± 11.54  | 100.00 ± 0.00 |
| cmla     | multi  | acc       | 68.52 ± 0.33 | 62.26 ± 0.36  | 76.11 ± 2.49 | 73.25 ± 0.86  | 95.07 ± 0.75   | 98.07 ± 0.19  |
| cmla     | multi  | f1        | 72.05 ± 0.28 | 63.74 ± 0.39  | 18.46 ± 3.26 | 73.38 ± 0.67  | 80.31 ± 9.82   | 29.71 ± 4.54  |
| cmla     | multi  | pre       | 72.11 ± 0.41 | 63.46 ± 0.59  | 21.33 ± 3.61 | 73.66 ± 0.77  | 79.55 ± 9.59   | 30.00 ± 4.56  |
| cmla     | multi  | rec       | 72.12 ± 0.17 | 64.23 ± 0.21  | 16.27 ± 2.96 | 73.26 ± 0.69  | 81.88 ± 10.76  | 29.43 ± 4.51  |

**Bảng 2.** Kết qủa đánh giả trên toàn bộ dữ liệu (all) và hiệu suất trên từng bộ dữ liệu riêng lẻ của mô hình CMLA và mô hình baseline khi huấn luyện với hàm Focal loss không sử dụng label smoothing.

| Model    | Task   | Metrics   | ALL          | BVA           | HERLEV       | HICERVIX      | MENDELEY_LBC   | SIPAKMED      |
|:---------|:-------|:----------|:-------------|:--------------|:-------------|:--------------|:---------------|:--------------|
| baseline | binary | acc       | 94.02 ± 0.08 | 100.00 ± 0.00 | 32.14 ± 1.60 | 99.98 ± 0.04  | 99.18 ± 0.89   | 60.89 ± 0.43  |
| baseline | binary | f1        | 96.61 ± 0.05 | 100.00 ± 0.00 | 17.60 ± 4.00 | 99.99 ± 0.02  | 98.91 ± 1.18   | 6.43 ± 1.98   |
| baseline | binary | pre       | 99.95 ± 0.02 | 100.00 ± 0.00 | 89.52 ± 1.93 | 100.00 ± 0.00 | 97.87 ± 2.29   | 100.00 ± 0.00 |
| baseline | binary | rec       | 93.49 ± 0.08 | 100.00 ± 0.00 | 9.81 ± 2.49  | 99.98 ± 0.04  | 100.00 ± 0.00  | 3.33 ± 1.05   |
| cmla     | binary | acc       | 99.52 ± 0.01 | 100.00 ± 0.00 | 91.86 ± 0.82 | 100.00 ± 0.00 | 99.04 ± 0.38   | 97.70 ± 0.31  |
| cmla     | binary | f1        | 99.74 ± 0.01 | 100.00 ± 0.00 | 94.69 ± 0.52 | 100.00 ± 0.00 | 98.72 ± 0.49   | 97.13 ± 0.40  |
| cmla     | binary | pre       | 99.69 ± 0.05 | 100.00 ± 0.00 | 91.88 ± 1.14 | 100.00 ± 0.00 | 97.48 ± 0.96   | 97.70 ± 0.44  |
| cmla     | binary | rec       | 99.79 ± 0.06 | 100.00 ± 0.00 | 97.69 ± 1.10 | 100.00 ± 0.00 | 100.00 ± 0.00  | 96.58 ± 1.10  |
| | | | | | | | | 
| baseline | multi  | acc       | 68.20 ± 0.50 | 61.92 ± 0.65  | 96.66 ± 1.24 | 71.79 ± 0.40  | 94.93 ± 1.42   | 100.00 ± 0.00 |
| baseline | multi  | f1        | 71.96 ± 0.44 | 63.46 ± 0.55  | 45.92 ± 7.57 | 69.77 ± 5.67  | 83.01 ± 10.17  | 100.00 ± 0.00 |
| baseline | multi  | pre       | 71.66 ± 0.40 | 62.92 ± 0.64  | 46.67 ± 7.46 | 69.95 ± 5.50  | 82.56 ± 9.81   | 100.00 ± 0.00 |
| baseline | multi  | rec       | 72.43 ± 0.44 | 64.33 ± 0.47  | 45.18 ± 7.66 | 69.75 ± 5.75  | 84.70 ± 11.34  | 100.00 ± 0.00 |
| cmla     | multi  | acc       | 68.22 ± 0.34 | 62.13 ± 0.39  | 75.00 ± 3.93 | 72.35 ± 0.66  | 94.80 ± 0.61   | 98.45 ± 0.32  |
| cmla     | multi  | f1        | 71.78 ± 0.29 | 63.46 ± 0.46  | 20.35 ± 5.53 | 72.47 ± 0.69  | 75.85 ± 8.11   | 32.09 ± 11.36 |
| cmla     | multi  | pre       | 71.92 ± 0.24 | 63.37 ± 0.28  | 23.67 ± 5.82 | 72.91 ± 0.45  | 75.28 ± 7.81   | 32.33 ± 11.40 |
| cmla     | multi  | rec       | 71.81 ± 0.45 | 63.89 ± 0.72  | 17.87 ± 5.23 | 72.34 ± 0.93  | 77.15 ± 8.57   | 31.85 ± 11.32 |

**Bảng 3.** Kết qủa đánh giả trên toàn bộ dữ liệu (all) và hiệu suất trên từng bộ dữ liệu riêng lẻ của mô hình CMLA và mô hình baseline khi huấn luyện với hàm Focal loss kết hợp label smoothing.

| Model    | Task   | Metrics   | ALL          | BVA           | HERLEV        | HICERVIX      | MENDELEY_LBC   | SIPAKMED      |
|:---------|:-------|:----------|:-------------|:--------------|:--------------|:--------------|:---------------|:--------------|
| baseline | binary | acc       | 93.92 $\pm$ 0.09 | 99.98 $\pm$ 0.02  | 29.28 $\pm$ 2.20  | 99.97 $\pm$ 0.04  | 99.73 $\pm$ 0.61   | 60.66 $\pm$ 0.59  |
| baseline | binary | f1        | 96.55 $\pm$ 0.05 | 99.99 $\pm$ 0.01  | 11.99 $\pm$ 4.65  | 99.98 $\pm$ 0.02  | 99.64 $\pm$ 0.81   | 5.35 $\pm$ 2.73   |
| baseline | binary | pre       | 99.96 $\pm$ 0.02 | 100.00 $\pm$ 0.00 | 77.61 $\pm$ 16.20 | 100.00 $\pm$ 0.00 | 99.29 $\pm$ 1.60   | 100.00 $\pm$ 0.00 |
| baseline | binary | rec       | 93.38 $\pm$ 0.09 | 99.98 $\pm$ 0.02  | 6.54 $\pm$ 2.67   | 99.97 $\pm$ 0.04  | 100.00 $\pm$ 0.00  | 2.77 $\pm$ 1.45   |
| cmla     | binary | acc       | 99.59 $\pm$ 0.05 | 100.00 $\pm$ 0.00 | 93.72 $\pm$ 0.93  | 100.00 $\pm$ 0.00 | 98.63 $\pm$ 0.48   | 98.00 $\pm$ 0.38  |
| cmla     | binary | f1        | 99.77 $\pm$ 0.02 | 100.00 $\pm$ 0.00 | 95.88 $\pm$ 0.64  | 100.00 $\pm$ 0.00 | 98.18 $\pm$ 0.63   | 97.52 $\pm$ 0.47  |
| cmla     | binary | pre       | 99.71 $\pm$ 0.04 | 100.00 $\pm$ 0.00 | 93.28 $\pm$ 0.42  | 100.00 $\pm$ 0.00 | 96.44 $\pm$ 1.22   | 97.64 $\pm$ 0.52  |
| cmla     | binary | rec       | 99.84 $\pm$ 0.07 | 100.00 $\pm$ 0.00 | 98.65 $\pm$ 1.46  | 100.00 $\pm$ 0.00 | 100.00 $\pm$ 0.00  | 97.40 $\pm$ 0.84  |
| | | | | | | | |
| baseline | multi  | acc       | 68.28 $\pm$ 1.38 | 62.03 $\pm$ 1.27  | 95.00 $\pm$ 3.04  | 71.72 $\pm$ 2.39  | 96.30 $\pm$ 1.58   | 100.00 $\pm$ 0.00 |
| baseline | multi  | f1        | 71.90 $\pm$ 1.13 | 57.01 $\pm$ 5.75  | 39.14 $\pm$ 13.91 | 67.14 $\pm$ 8.24  | 92.13 $\pm$ 2.72   | 100.00 $\pm$ 0.00 |
| baseline | multi  | pre       | 71.78 $\pm$ 0.89 | 56.76 $\pm$ 5.82  | 40.00 $\pm$ 13.69 | 67.65 $\pm$ 7.69  | 91.49 $\pm$ 3.03   | 100.00 $\pm$ 0.00 |
| baseline | multi  | rec       | 72.22 $\pm$ 1.32 | 57.56 $\pm$ 5.84  | 38.33 $\pm$ 14.07 | 66.99 $\pm$ 8.40  | 93.87 $\pm$ 1.87   | 100.00 $\pm$ 0.00 |
| cmla     | multi  | acc       | 68.60 $\pm$ 0.37 | 62.54 $\pm$ 0.38  | 79.45 $\pm$ 1.52  | 72.86 $\pm$ 0.95  | 93.29 $\pm$ 1.49   | 98.40 $\pm$ 0.36  |
| cmla     | multi  | f1        | 72.05 $\pm$ 0.42 | 63.90 $\pm$ 0.44  | 18.88 $\pm$ 3.15  | 72.91 $\pm$ 0.99  | 73.49 $\pm$ 6.02   | 29.76 $\pm$ 4.55  |
| cmla     | multi  | pre       | 71.85 $\pm$ 0.35 | 63.44 $\pm$ 0.36  | 21.33 $\pm$ 3.61  | 72.87 $\pm$ 0.93  | 73.37 $\pm$ 5.68   | 30.00 $\pm$ 4.56  |
| cmla     | multi  | rec       | 72.41 $\pm$ 0.56 | 64.63 $\pm$ 0.64  | 16.94 $\pm$ 2.80  | 73.12 $\pm$ 1.07  | 75.30 $\pm$ 5.76   | 29.53 $\pm$ 4.54  |


## Appendix A: Implementation Details
### A.1. Focal Loss with Pytorch

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CMLAFocalLoss(nn.Module):
    def __init__(
        self,
        device="cpu",
        class_weight_low=torch.tensor([1.0044, 0.9956], dtype=torch.float32),
        class_weight_high=torch.tensor([0.95, 0.85, 1.50], dtype=torch.float32),
        gamma=0.0,
        lamd_1=1.0,
        lamd_2=1.0,
        lamd_3=1.0,
        label_smoothing=0.0
    ):
        super().__init__()
        self.gamma = gamma
        self.lamd_1 = lamd_1
        self.lamd_2 = lamd_2
        self.lamd_3 = lamd_3

        cw_low = class_weight_low.to(device) if class_weight_low is not None else None
        cw_high = class_weight_high.to(device) if class_weight_high is not None else None

        self.bce = nn.BCEWithLogitsLoss(reduction='none')
        self.ce_low = nn.CrossEntropyLoss(
            weight=cw_low, reduction='none', ignore_index=-1,
            label_smoothing=label_smoothing
        )
        self.ce_high = nn.CrossEntropyLoss(
            weight=cw_high, reduction='none', ignore_index=-1,
            label_smoothing=label_smoothing
        )

    def _binary_focal(self, logits, targets):
        logits = logits.view(-1)
        targets = targets.view(-1)
        if logits.numel() == 0:
            return logits.sum() * 0.0, 0

        bce = self.bce(logits, targets)

        if self.gamma > 0:
            p = torch.sigmoid(logits)
            pt = torch.where(targets == 1, p, 1 - p)
            bce = (1 - pt) ** self.gamma * bce

        return bce.mean(), targets.shape[0]

    def _multi_focal(self, logits, targets, ce_fn):
        if logits.numel() == 0:
            return logits.sum() * 0.0, 0

        ce = ce_fn(logits, targets)

        if self.gamma > 0:
            probs = F.softmax(logits, dim=1)
            pt = probs.gather(1, targets.unsqueeze(1)).squeeze(1)
            ce = (1 - pt) ** self.gamma * ce

        return ce.mean(), targets.shape[0]

    def forward(self, logits, targets):
        logits_s1, logits_s2, logits_s3_low, logits_s3_high = logits
        y_s1, y_s2, y_s3 = targets

        # Tạo mặt nạ (mask) lọc mẫu hợp lệ
        v_s1 = (y_s1 != -1)
        v_s2 = (y_s1 == 1) & (y_s2 != -1)
        v_low = (y_s1 == 1) & (y_s2 == 0) & (y_s3 != -1)
        v_high = (y_s1 == 1) & (y_s2 == 1) & (y_s3 != -1)

        loss_s1, count_s1 = self._binary_focal(logits_s1[v_s1], y_s1[v_s1])
        loss_s2, count_s2 = self._binary_focal(logits_s2[v_s2], y_s2[v_s2])

        loss_s3_low, count_s3_low = self._multi_focal(
            logits_s3_low[v_low], y_s3[v_low], self.ce_low,
        )
        loss_s3_high, count_s3_high = self._multi_focal(
            logits_s3_high[v_high], y_s3[v_high], self.ce_high,
        )

        # Tính trung bình có trọng số cho Stage 3
        denom = float(count_s3_low + count_s3_high)
        numerator = loss_s3_low * count_s3_low + loss_s3_high * count_s3_high
        loss_s3 = numerator / (denom + 1e-8)

        # Tổng loss toàn cục
        total_loss = (
            self.lamd_1 * loss_s1
            + self.lamd_2 * loss_s2
            + self.lamd_3 * loss_s3
        )

        loss_dict = {
            "loss_s1": loss_s1.item(),
            "loss_s2": loss_s2.item(),
            "loss_s3": loss_s3.item(),
            "loss_s3_low": loss_s3_low.item(),
            "loss_s3_high": loss_s3_high.item(),
            "count_s1": count_s1,
            "count_s2": count_s2,
            "count_s3_low": count_s3_low,
            "count_s3_high": count_s3_high,
        }
        return total_loss, loss_dict
```

### A.2. Label Mapping

```python
LABEL_MAPPING = {
    # Mapping labels datasets using bethesda templates (ASCH, ASCUS, HSIL, LSIL, SCC)
    # Stage 01: Binary screening (normal vs abnormal) label in {0, 1}
    # Stage 02: Lesion Grading (low vs high) label in {0, 1}
    # Stage 03: Fine-grained Subtyping
    #       Stage 3.1: Low (ASCUS, LSIL) label in {0, 1}
    #       Stage 3.2: High {ASCH, HSIL, SCC} label in {0, 1, 2}
    # Value -1 indicates missing labels at specific stages.

    # Hospital A & HiCervix
    "asc_us": {"stage1": 1.0, "stage2": 0.0, "stage3": 0},
    "lsil":   {"stage1": 1.0, "stage2": 0.0, "stage3": 1},
    "asc_h":  {"stage1": 1.0, "stage2": 1.0, "stage3": 0},
    "hsil":   {"stage1": 1.0, "stage2": 1.0, "stage3": 1},
    "scc":    {"stage1": 1.0, "stage2": 1.0, "stage3": 2},

    # Mendeley LBC
    "negative_for_intraepithelial_malignancy": {"stage1": 0.0, "stage2": -1.0, "stage3": -1}, # NILM
    "low_squamous_intra_epithelial_lesion":    {"stage1": 1.0, "stage2": 0.0, "stage3": 1},  # LSIL
    "high_squamous_intra_epithelial_lesion":   {"stage1": 1.0, "stage2": 1.0, "stage3": 1},  # HSIL
    "squamous_cell_carcinoma":                 {"stage1": 1.0, "stage2": 1.0, "stage3": 2},  # SCC

    # Herlev
    "normal_superficiel":  {"stage1": 0.0, "stage2": -1.0, "stage3": -1},
    "normal_intermediate": {"stage1": 0.0, "stage2": -1.0, "stage3": -1},
    "normal_columnar":     {"stage1": 0.0, "stage2": -1.0, "stage3": -1},
    
    "light_dysplastic":    {"stage1": 1.0, "stage2": -1.0, "stage3": -1},
    "moderate_dysplastic": {"stage1": 1.0, "stage2": -1.0, "stage3": -1},
    "severe_dysplastic":   {"stage1": 1.0, "stage2": -1.0, "stage3": -1},
    "carcinoma_in_situ":   {"stage1": 1.0, "stage2": -1.0, "stage3": -1},

    # SipakMed
    "superficial_intermediate": {"stage1": 0.0, "stage2": -1.0, "stage3": -1},
    "parabasal":                {"stage1": 0.0, "stage2": -1.0, "stage3": -1},
    "metaplastic":              {"stage1": 0.0, "stage2": -1.0, "stage3": -1},
    
    "koilocytotic":             {"stage1": 1.0, "stage2": -1.0, "stage3": -1},
    "dyskeratotic":             {"stage1": 1.0, "stage2": -1.0, "stage3": -1}
}
```

### Training Parameters

```python
@dataclass
class TrainConfig:    
    freeze_feature_encoder: bool = False
    
    num_workers: int = 2
    batch_size: int = 256
    backbone_lr: float = 2e-5
    learning_rate: float = 1e-4
    weight_decay: float = 5e-4
    num_train_epochs: int = 50
    warmup_ratio: float = 0.05
    max_grad_norm: float = 0.5
    gamma: float = 2.0
    
    patience: int = 5
    delta: float = 0.001
    mode: str = "max"
    monitor: str = "val_f1"
```

## Appendix B: Datasets Statistic

- [Herlev.](https://github.com/openmedlab/Awesome-Medical-Dataset/blob/main/resources/Herlev.md) Dữ liệu chứa ảnh y tế bào được cắt thủ công để tách riêng từng tế bào. Gồm 3 lớp bất thường và 4 lớp bất thường.

| # | Label | Number | Categorical |
| :-: | :---- | :---: | :----: |
| 1 |   normal_columnar   |   98    | Normal |
| 2 | normal_intermediate |   70    | Normal | 
| 3 | normal_superficiel  |   74    | Normal | 
| 4 |  carcinoma_in_situ  |   150   | Abnormal | 
| 5 |  light_dysplastic   |   182   | Abnormal | 
| 6 | moderate_dysplastic |   146   | Abnormal | 
| 7 |  severe_dysplastic  |   197   | Abnormal | 
| **Total** | | **917** |

- [Mendeley LBC.](https://datamanagement.hms.harvard.edu/share-publish/data-repositories/mendeley-data) Cung cấp 4 nhãn chính trong đó duy nhất NILM là bình thường còn lại là bất thường. 

| # | Label | Number | Categorical |
| :--: | :--: | :----: | :----: |
| 1 | NILM | 612 | Normal |
| 2 | HSIL | 163 | Abnormal |
| 3 | LSIL | 113 | Abnormal |
| 4 | SCC | 74 | Abnormal |
| **Total** | | **962** |

- [Hospital A.](https://www.kaggle.com/datasets/nguyenthaihoc/datasets-iast) Bộ dữ liệu gồm 5 nhãn đều là tế bào bất thường.

| # | Label | Number | Categorical |
| :--: | :-- | :----: | :-----: |
| 1 | ASCH | 5669 | Abnormal |
| 2 | ASCUS | 3869 | Abnormal |
| 3 | HSIL | 6355 | Abnormal |
| 4 | LSIL | 4780 | Abnormal |
| 5 | SCC | 1761 | Abnormal |
| **Total** | | **22,434** |

- [SipakMed.](https://www.kaggle.com/datasets/prahladmehandiratta/cervical-cancer-largest-dataset-sipakmed) Bộ dữ liệu được phân loại thành 5 lớp trong đó có 3 lớp bình thường (parabasal, metaplastic, superficial) còn lại dyskeratotic và koilocytoci là bất thường.

| # | Label | Number | Categorical |
| :--: | :-- | :----: | :-----: |
| 1 | metaplastic | 793 | Normal |
| 2 | parabasal | 787 | Normal |
| 3 | superficial_intermediate | 831 | Normal |
| 4 | dyskeratotic | 813 | Abnormal |
| 5 | koilocytotic | 825 | Abnormal |
| **Total** | | **4.049** |

- [Hicervic.](https://github.com/Scu-sen/HiCervix) Tương tự như bộ dữ liệu BVA, toàn bộ các nhãn trong tập dữ liệu này đề là các nhãn bất thường.

| # | Label | Number | Categorical |
| :--: | :-- | :----: | :-----: |
| 1 | ASCH | 1437 | Abnormal |
| 2 | ASCUS | 2599 | Abnormal |
| 3 | HSIL | 1988 | Abnormal |
| 4 | LSIL | 1744 | Abnormal |
| 5 | SCC | 1072 | Abnormal |
| **Total** | | **8.840** |

## Appendix C: Matrix Implementation

- For research question 1 and 3.

| RQs | Model | Loss | Class_Weight |
| :-- | :---: | :---: | :----: |
| 1 & 3 | Baseline | CE | - |
| 1 & 3 | Baseline | CE | v |
| 1 & 3 | Baseline | FL | - |
| 1 & 3 | Baseline | FL | v |
| | | |
| 1 & 3 | CMLA | CE | - |
| 1 & 3 |CMLA | CE | v |
| 1 & 3 | CMLA | FL | - |
| 1 & 3 | CMLA | FL | v |

- For research question 2 and 5.
  
| RQs | Model | BVA | Herlev | SipakMed | MendeleyLBC | HiCervix |
| :--- | :---: | :-----: | :---: | :---: | :---: | :---: |
| 2 & 5 | Baseline | v | x | x | x | x |
| 2 & 5 |Baseline | v | v | v | x | x |
| 2 & 5 | Baseline | v | v | v | v | v |
| 2 & 5 | CMLA | v | x | x | x | x | x |
| 2 & 5 | CMLA |  v | v | v | x | x |
| 2 & 5 | CMLA | v | v | v | v | v |

- For research question 4.

| RQs | Backbone | Model | 
| :--- | :---: | :---: |
| 4 | Baseline | Resnet50 |
| 4 | Baseline | Resnet101 |
| 4 | Baseline | EfficientNet_B2 |
| 4 | Baseline | ViT |
| 4 | CMLA | Resnet50 |
| 4 | CMLA | Resnet101 |
| 4 | CMLA | EfficientNet_B2 |
| 4 | CMLA | ViT |