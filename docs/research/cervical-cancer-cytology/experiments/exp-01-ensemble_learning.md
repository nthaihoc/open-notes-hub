---
title: Notes on Data Aggregation, Training, and Evaluation Strategies
---

# Notes on Data Aggregation, Training, and Evaluation Strategies
---
!!! warning ""
    Trong nghiên cứu này, tập trung vào các mô hình đơn lẻ (single models). Mục tiêu là phân tích cách gộp dữ liệu từ nhiều nguồn, triển khai huấn luyện và đánh giá để đảm bảo tính tổng quát hóa và khả năng so sánh giữa các bộ dữ liệu khác nhau.

## Experiments setup

Áp dụng 3 chiến lược huấn luyện và đánh giá bao gồm:

- **Chiến lược 1.** Gộp dữ liệu thống nhất (Unified Training). Tất cả các bộ dữ liệu được tiền xử lý theo cùng một chuẩn, gộp thành một tập duy nhất. Dữ liệu được chia theo tỷ lệ cố định (train/dev/test 70/15/15) để huấn luyện và đánh giá.

- **Chiến lược 2.** Đánh giá chéo theo bộ dữ liệu (Cross-Dataset Evaluation). Mô hình được huấn luyện trên một bộ dữ liệu cụ thể và đánh giá trên các bộ dữ liệu khác. Quy trình này giúp phân tích khả năng khái quát hóa và độ ổn định của mô hình.

- **Chiến lược 3.** Huấn luyện đa nguồn với đánh giá chéo (Multi-Source Training). Tất cả các bộ dữ liệu được gộp lại trong quá trình huấn luyện. Tuy nhiên, đánh giá được tiến hành riêng biệt trên tập test của từng bộ dữ liệu, cho phép quan sát hiệu suất trên từng phân phối khác nhau.

## Data Aggregation

Dựa vào thông tin thống kê, đặc điểm của các bộ dữ liệu [[datasets-overview](exp-02-self_supervised_learning.md)], thực hiện mapping về dữ liệu dạng 2 nhãn. 

| Datasets | Label                  | Class     |
| :------  | :------------------------|-----------|
| Herlev | superficiel            | Normal    |
|| intermediate           | Normal    |
|| columnar               | Normal    |
|| light dysplastic       | Abnormal  |
|| moderate_dysplastic    | Abnormal  |
|| severe dysplastic      | Abnormal  |
|| carcinoma in situ      | Abnormal  |
||||
| LBC | NILM  | Normal    |
|| LSIL  | Abnormal  |
|| HSIL  | Abnormal  |
|| SCC   | Abnormal  |
||||
| Hicervix | ASC_H   | Abnormal  |
|| ASC_US  | Abnormal  |
|| HSIL    | Abnormal  |
|| LSIL    | Abnormal  |
|| SCC     | Abnormal  |
||||
|SipakMed | Dyskeratotic (DYSK)         | Abnormal  |
|| Koilocytotic (KOIL)         | Abnormal  |
|| Metaplastic (META)          | Normal    |
|| Parabasal (PARA)            | Normal    |
|| Superficial-Moderate (SM)   | Normal    |
||||
|BVA| ASC_H   | Abnormal  |
|| ASC_US  | Abnormal  |
|| HSIL    | Abnormal  |
|| LSIL    | Abnormal  |
|| SCC     | Abnormal  |

/// caption
**Bảng 1.** Bảng quy đổi nhãn tương ứng trên từng bộ dữ liệu dựa trên quy ước phân loại trong tế bào học tử cung. 
///

Sau khi mapping tiến hành gộp dữ liệu và thu được bộ dữ liệu lớn được thống kê mô tả như sau:

| Dataset    | Normal | Abnormal | Total  |
|------------|--------|----------|--------|
| Herlev     | 242    | 675      | 917    |
| LBC        | 0      | 963      | 963    |
| HiCervix   | 0      | 8,840    | 8,840  |
| SIPaKMed   | 1,618  | 2,472    | 4,090  |
| Hospital A | 0      | 22,434   | 22,434 |
| **Total**  | **1,860** | **35,384** | **37,244** |

/// caption
**Bảng 2.** Bảng dữ liệu thống kê sau khi tiến hành gộp dữ liệu từ 5 bộ riêng biệt, với hai nhãn bình thường + bất thường.
///

## Cross-Dataset Evaluation

- __Ý tưởng.__ Trong chiến lược này, các mô hình được huấn luyện trên bộ dữ liệu Bệnh viện A và sau đó đánh giá khả năng khái quát hóa (generalization) trên nhiều bộ dữ liệu công khai khác nhau. Toàn bộ dữ liệu được quy đổi về cùng một nhiệm vụ phân loại nhị phân (normal vs. abnormal).

- __Ưu điểm.__ Đánh giá được khả năng khái quát hóa của mô hình sang nguồn dữ liệu khác và cho phép so sánh mức độ phụ thuộc phân phối dữ liệu giữa các kiến trúc.

- __Nhược điểm.__ Không tận dụng được toàn bộ dữ liệu có sẵn, việc dẫn đến sự khái quát hóa kém hoàn toàn có thể xảy ra.

__Đánh giá.__

- Mô hình huấn luyện trên dữ liệu Bệnh viện A đạt hiệu suất cao. 

- Khi đánh giá trên các bộ dữ liệu công khai, F1-score giảm cho thấy sự phụ thuộc vào phân phối dữ liệu gốc.

- Nhóm InceptionV3 / InceptionResNetV2 vượt trội hơn VGG16 và ResNet101 khoảng hơn 10% điểm F1-score.

- MobileNetV2 và Xception đạt kết quả trung bình nhưng ổn định, cân bằng giữa độ chính xác và chi phí tính toán.

Đánh giá chéo cho thấy mô hình duy trì hiệu suất trên trung bình với dữ liệu mới, nhưng vẫn còn khoảng cách lớn so với tập gốc.

| Dataset | Model              | Accuracy | Precision | Recall | F1-Score |
| :------ |---------------------|:--------:|:---------:|:------:|:--------:|
| *Hospital A* | MobileNetV2         | 65.51    | 72.84     | 73.05  | 72.41    |
|| InceptionV3         | 69.93    | 77.24     | 76.25  | **76.57**    |
|| InceptionResNetV2   | 71.62    | 78.36     | 78.12  | **78.04**    |
|| VGG16               | 61.94    | 69.22     | 69.15  | 68.65    |
|| ResNet101           | 58.83    | 65.08     | 65.91  | 64.41    |
|| Xception            | 65.58    | 71.74     | 72.75  | 71.18    |
||                     |          |           |        |          |
|*Herlev*| MobileNetV2         | 57.13    | 64.27     | 64.62  | 63.58    |
|| InceptionV3         | 61.12    | 68.34     | 67.41  | **67.05**    |
|| InceptionResNetV2   | 63.48    | 70.21     | 69.67  | **69.14**    |
|| VGG16               | 53.26    | 60.38     | 60.71  | 59.63    |
|| ResNet101           | 50.47    | 57.16     | 57.42  | 56.54    |
|| Xception            | 57.39    | 64.11     | 65.08  | 63.62    |
||                     |          |           |        |          |
|*LBC Pap Smear* | MobileNetV2         | 54.72    | 61.14     | 61.85  | 61.02    |
|| InceptionV3         | 58.43    | 65.12     | 65.07  | **64.78**    |
|| InceptionResNetV2   | 60.07    | 66.83     | 66.14  | **66.02**    |
|| VGG16               | 51.29    | 57.41     | 57.82  | 57.09    |
|| ResNet101           | 48.75    | 54.62     | 55.18  | 54.71    |
|| Xception            | 54.06    | 60.72     | 61.41  | 60.38    |
||                     |          |           |        |          |
|*HiCervix*| MobileNetV2         | 52.63    | 59.82     | 60.44  | 59.67    |
|| InceptionV3         | 56.38    | 62.94     | 63.05  | **62.58**    |
|| InceptionResNetV2   | 58.07    | 65.11     | 64.82  | **64.55**    |
|| VGG16               | 49.41    | 55.48     | 56.02  | 55.17    |
|| ResNet101           | 47.22    | 53.27     | 53.68  | 53.01    |
|| Xception            | 52.05    | 58.74     | 59.16  | 58.42    |
||                     |          |           |        |          |
|*SIPakMed*| MobileNetV2         | 54.82    | 61.37     | 61.92  | 61.14    |
|| InceptionV3         | 58.63    | 64.95     | 65.21  | **64.58**    |
|| InceptionResNetV2   | 60.42    | 67.24     | 67.01  | **66.73**    |
|| VGG16               | 51.73    | 57.68     | 58.12  | 57.42    |
|| ResNet101           | 49.28    | 55.02     | 55.41  | 54.86    |
|| Xception            | 54.15    | 60.34     | 60.82  | 60.02    |

/// caption
**Bảng 3.** Đánh giá hiệu suất của các mô hình được huấn luyện trên BVA trên các bộ dữ liệu công khai khác.
///

## Unified Training

- __Ý tưởng.__ Tất cả các bộ dữ liệu được tiền xử lý theo cùng một chuẩn (kích thước, số lớp normal vs. abnormal, v.v.). Sau đó được gộp lại thành một tập dữ liệu duy nhất để huấn luyện và đánh giá.

- __Ưu điểm.__ Dễ triển khai, tạo ra tập dữ liệu đủ lớn giúp mô hình học được nhiều đặc trưng hơn.

- __Nhược điểm.__ Đặc thù phân phối bộ dữ liệu có thể bị mất đi, dẫn đến kết quả đánh giá không phản ánh đầy đủ khả năng khái quát hóa cho mỗi nguồn dữ liệu riêng biệt.

__Kết quả đánh giá.__

- Nhìn chung hiệu suât tổng thể khá đồng đều, các mô hình InceptionResNetV2 và Xception cho kết quả cao nhất vượt trội so với các mô hình cổ điển VGG16.

- Sự khác biệt giữa các chỉ số, độ đô hiệu suất là không lớn, tuy nhiên không phản ánh hết được khả năng tương thích theo từng miền dữ liệu riêng lẻ.

| Model              | Accuracy | Precision | Recall | F1-Score |
|---------------------|:--------:|:---------:|:------:|:--------:|
| MobileNetV2         | 71.12    | 71.85     | 70.43  | 70.82    |
| InceptionV3         | 73.21    | 73.88     | 72.65  | 72.94    |
| InceptionResNetV2   | 74.95    | 75.41     | 73.88  | **74.11**    |
| VGG16               | 70.42    | 70.11     | 69.87  | 69.35    |
| ResNet101           | 71.76    | 71.94     | 70.68  | 71.28    |
| Xception            | 73.48    | 73.92     | 72.75  | **73.02**    |

/// caption
**Bảng 4.** So sánh hiệu suất của các mô hình đơn lẻ sau khi được huấn luyện và đánh giá trên bộ dữ liệu được gộp.
///

## Multi-Source Training

- **Ý tưởng.** Trong chiến lược này, nhiều bộ dữ liệu được gộp chung để huấn luyện, đảm bảo mô hình tiếp xúc với phân phối phong phú và đa dạng. Quá trình đánh giá sau đó được thực hiện riêng biệt trên từng bộ dữ liệu, cho phép phân tích hiệu suất trong từng ngữ cảnh cụ thể.

- **Ưu điểm.** Giúp mô hình tiếp xúc với phân phối dữ liệu đa dạng, tăng khả năng khái quát hóa, cho phép nhìn thấy được hiệu suất riêng biệt của từng nguồn dữ liệu.

- **Hạn chế.** Có thể bị bias nếu một bộ dữ liệu từ một nguồn vượt trội hơn (ví dụ bộ Hircervix và BVA).

**Đánh giá.** Toàn bộ dữ liệu train của 5 bộ dữ liệu được gộp lại để huấn luyện, quá trình dánh giá các mô hình sẽ sử dụng tập test của từng bộ dữ liệu gốc.

- Nhóm Inception (V3, ResNetV2) vẫn ổn định và vượt trội hơn. 

- MobileNetV2, Xception cho kết quả trung bình nhưng khá đồng đều trên các bộ dữ liệu.

- VGG16, ResNet101 consistently thấp hơn, đặc biệt trên HiCervix.

Kết quả phản ánh rằng huấn luyện đa nguồn giúp duy trì hiệu suất tương đối khá trên các tập test khác nhau, dù vẫn có chênh lệch theo từng phân phối dữ liệu.

| Model             | Hospital A | Herlev   | LBC     | HiCervix | SIPakMed |
|-------------------|------------|----------|---------|----------|----------|
| MobileNetV2       | 70.42      | 62.18    | 59.87   | 58.41    | 61.22    |
| InceptionV3       | **74.63**  | 66.32    | 63.95   | 61.72    | 65.48    |
| InceptionResNetV2 | 73.58      | **68.77**| **66.42**| 63.18    | 67.23    |
| VGG16             | 67.11      | 59.24    | 57.13   | 54.62    | 58.04    |
| ResNet101         | 64.88      | 57.86    | 55.42   | 53.01    | 56.27    |
| Xception          | 69.14      | 63.02    | 60.71   | **64.02**| **68.11**|


/// caption
**Bảng 5.** . Kết quả F1-Score (%) của các mô hình theo từng bộ dữ liệu (được đánh giá trên tập test).
///

## Leave-On-Dataset-out

## Domain Adaptation

## Multi-Task Learning

--- 