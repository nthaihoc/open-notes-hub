---
title: Ensemble Learning for Cervical Cancer Classification
icon: material/numeric-2-circle
---

# 🐛 Ensemble Learning for Cervical Cancer Classification
---
!!! warning ""
    Nghiên cứu các kỹ thuật, phương pháp học tập kết hợp (ensemble learning) và lên các phương án thực nghiệm cho bộ dữ liệu Ung thư cổ tử cung. Đánh giá kết quả, nhận xét về hiệu suất của các phương pháp học tập kết hợp và so sánh với các mô hình đơn lẻ. Bên cạnh đó, triển khai inference trên các bộ dữ liệu công khai khác, nhắm phân tích sự tương thích, hỗ trợ và sự khác biệt giữa các bộ dữ liệu. 

## Performance Evaluation of Models
Phần này tập trung đánh giá hiệu suất của các mô hình học sâu và các phương pháp kết hợp được huấn luyện trên bộ dữ liệu gốc từ Bệnh viện A. Sau đó, các mô hình được kiểm tra khả năng tổng quát hóa (generalization) trên nhiều bộ dữ liệu công khai, vốn đã được mô tả chi tiết tại đây [[datasets](../cervical-cancer-cytology/note-01-ssl-for-cervical-cancer.md)]. 

Để đảm bảo tính nhất quán trong so sánh, toàn bộ các bộ dữ liệu đều được quy đổi về cùng một bài toán phân loại nhị phân (normal so với abnormal).

### Hospital A

<!-- **Bảng 1** là các chỉ số đánh giá hiệu suất mô hình đơn lẻ trên bộ dữ liệu Bệnh viện A. Nhìn chung:

- InceptionResNetV2 đạt kết quả tốt nhất với Accuracy 71.62% và F1-Score ~78%.
- InceptionV3 đứng thứ hai Acc ~70% và F1 ~76.6%.
- MobileNetV2 và Xception có hiệu suất tương đương Acc ~65–66% và F1 ~71–72%.
- VGG16 cho kết quả thấp hơn rõ rệt Acc ~62% và F1 ~69%, ResNet101 kém nhất Acc ~59% và F1 ~64%
- Nhóm Inception (V3 và ResNetV2) vượt trội hơn so với VGG16 và ResNet101 khoảng 10–15% điểm F1-score. -->

| Model              | Accuracy | Precision | Recall | F1-Score |
|---------------------|:--------:|:---------:|:------:|:--------:|
| MobileNetV2         | 65.51    | 72.84     | 73.05  | 72.41    |
| InceptionV3         | 69.93    | 77.24     | 76.25  | 76.57    |
| InceptionResNetV2   | 71.62    | 78.36     | 78.12  | 78.04    |
| VGG16               | 61.94    | 69.22     | 69.15  | 68.65    |
| ResNet101           | 58.83    | 65.08     | 65.91  | 64.41    |
| Xception            | 65.58    | 71.74     | 72.75  | 71.18    |

/// caption
**Bảng 1.** Hiệu suất của các mô hình đơn lẻ trên bộ dữ liệu Bệnh viện A, Thái Nguyên.
///

| Model                  | Accuracy | Precision | Recall | F1-Score |
|-------------------------|:--------:|:---------:|:------:|:--------:|
| Voting                 | 73.83    | 80.01     | 80.44  | 80.17    |
| K-Nearest Neighbor     | 73.05    | 79.32     | 79.43  | 79.36    |
| Naive Bayes            | 73.44    | 78.19     | 80.29  | 79.01    |
| Decision Tree          | 72.72    | 78.91     | 79.25  | 79.05    |
| Support Vector Machine | 74.22    | 80.48     | 80.69  | 80.57    |
| Logistic Regression    | 73.76    | 80.05     | 80.23  | 80.14    |

/// caption
**Bảng 2.** Kết quả đánh giá mô hình kết hợp trên bộ dữ liệu Bệnh viện A, Thái Nguyên.
///

<!-- Kết quả trình bày trong **Bảng 2** cho thấy các mô hình kết hợp nhìn chung đạt hiệu suất phân loại khá cao trên bộ dữ liệu ung thư cổ tử cung.

- Support Vector Machine (SVM) đạt hiệu suất cao nhất Accuracy 74.22% và F1-Score 80.57%. 
- Voting và Logistic Regression có kết quả cạnh tranh F1-Score ~80.1%. 
- Naive Bayes, Decision Tree và K-Nearest Neighbor cho hiệu suất thấp hơn đôi chút F1-Score xấp xỉ 79%. -->

### Herlev

| Model              | Accuracy | Precision | Recall | F1-Score |
|---------------------|:--------:|:---------:|:------:|:--------:|
| MobileNetV2         | 57.13    | 64.27     | 64.62  | 63.58    |
| InceptionV3         | 61.12    | 68.34     | 67.41  | 67.05    |
| InceptionResNetV2   | 63.48    | 70.21     | 69.67  | 69.14    |
| VGG16               | 53.26    | 60.38     | 60.71  | 59.63    |
| ResNet101           | 50.47    | 57.16     | 57.42  | 56.54    |
| Xception            | 57.39    | 64.11     | 65.08  | 63.62    |

/// caption
**Bảng 3.** Hiệu suất ước lượng của các mô hình học sâu trên bộ dữ liệu Herlev
///

| Model                  | Accuracy | Precision | Recall | F1-Score |
|------------------------|:--------:|:---------:|:------:|:--------:|
| Support Vector Machine | 60.38    | 66.27     | 67.14  | 66.42    |
| Voting                 | 59.21    | 65.18     | 65.46  | 65.12    |
| Logistic Regression    | 59.07    | 65.09     | 65.12  | 64.76    |
| K-Nearest Neighbor     | 58.43    | 64.31     | 63.68  | 63.74    |
| Naive Bayes            | 57.36    | 62.47     | 62.64  | 62.29    |
| Decision Tree          | 56.18    | 61.39     | 61.23  | 61.14    |

/// caption
**Bảng 4.** Hiệu suất ước lượng của các mô hình kết hợp trên bộ dữ liệu Herlev
///

### LBC Pap Smear

| Model              | Accuracy | Precision | Recall | F1-Score |
|---------------------|:--------:|:---------:|:------:|:--------:|
| MobileNetV2         | 54.72    | 61.14     | 61.85  | 61.02    |
| InceptionV3         | 58.43    | 65.12     | 65.07  | 64.78    |
| InceptionResNetV2   | 60.07    | 66.83     | 66.14  | 66.02    |
| VGG16               | 51.29    | 57.41     | 57.82  | 57.09    |
| ResNet101           | 48.75    | 54.62     | 55.18  | 54.71    |
| Xception            | 54.06    | 60.72     | 61.41  | 60.38    |

/// caption
**Bảng 5.** Hiệu suất của các mô hình học sâu trên bộ dữ liệu LBC Pap Smear
///

| Model                  | Accuracy | Precision | Recall | F1-Score |
|------------------------|:--------:|:---------:|:------:|:--------:|
| Support Vector Machine | 57.12    | 62.14     | 62.83  | 62.25    |
| Voting                 | 56.18    | 60.93     | 61.02  | 60.74    |
| Logistic Regression    | 55.72    | 60.48     | 60.72  | 60.15    |
| K-Nearest Neighbor     | 55.08    | 59.93     | 60.02  | 59.71    |
| Naive Bayes            | 54.32    | 58.72     | 58.94  | 58.53    |
| Decision Tree          | 53.64    | 58.11     | 58.25  | 57.93    |

/// caption
**Bảng 6.** Hiệu suất của các mô hình ensemble trên bộ dữ liệu LBC Pap Smear
///

### HiCervix

| Model              | Accuracy | Precision | Recall | F1-Score |
|---------------------|:--------:|:---------:|:------:|:--------:|
| MobileNetV2         | 52.63    | 59.82     | 60.44  | 59.67    |
| InceptionV3         | 56.38    | 62.94     | 63.05  | 62.58    |
| InceptionResNetV2   | 58.07    | 65.11     | 64.82  | 64.55    |
| VGG16               | 49.41    | 55.48     | 56.02  | 55.17    |
| ResNet101           | 47.22    | 53.27     | 53.68  | 53.01    |
| Xception            | 52.05    | 58.74     | 59.16  | 58.42    |

/// caption
**Bảng 7.** Hiệu suất của các mô hình học sâu trên bộ dữ liệu HiCervix
///

| Model                  | Accuracy | Precision | Recall | F1-Score |
|------------------------|:--------:|:---------:|:------:|:--------:|
| Support Vector Machine | 55.24    | 60.81     | 61.32  | 60.44    |
| Voting                 | 54.16    | 59.28     | 59.74  | 59.13    |
| Logistic Regression    | 53.87    | 58.94     | 59.02  | 58.67    |
| K-Nearest Neighbor     | 53.22    | 58.23     | 58.35  | 58.04    |
| Naive Bayes            | 52.41    | 57.18     | 57.34  | 57.01    |
| Decision Tree          | 51.68    | 56.39     | 56.52  | 56.21    |

/// caption
**Bảng 8.** Hiệu suất của các mô hình ensemble trên bộ dữ liệu HiCervix
///

### SIPakMed

| Model              | Accuracy | Precision | Recall | F1-Score |
|---------------------|:--------:|:---------:|:------:|:--------:|
| MobileNetV2         | 54.82    | 61.37     | 61.92  | 61.14    |
| InceptionV3         | 58.63    | 64.95     | 65.21  | 64.58    |
| InceptionResNetV2   | 60.42    | 67.24     | 67.01  | 66.73    |
| VGG16               | 51.73    | 57.68     | 58.12  | 57.42    |
| ResNet101           | 49.28    | 55.02     | 55.41  | 54.86    |
| Xception            | 54.15    | 60.34     | 60.82  | 60.02    |

/// caption
**Bảng 7.** Hiệu suất của các mô hình học sâu trên bộ dữ liệu SIPakMed
///


| Model                  | Accuracy | Precision | Recall | F1-Score |
|------------------------|:--------:|:---------:|:------:|:--------:|
| Support Vector Machine | 56.42    | 61.82     | 62.41  | 61.95    |
| Voting                 | 55.38    | 60.37     | 60.72  | 60.21    |
| Logistic Regression    | 55.06    | 60.14     | 60.23  | 59.84    |
| K-Nearest Neighbor     | 54.32    | 59.21     | 59.48  | 59.03    |
| Naive Bayes            | 53.67    | 58.41     | 58.62  | 58.25    |
| Decision Tree          | 52.91    | 57.64     | 57.83  | 57.42    |

/// caption
**Bảng 8.** Hiệu suất của các mô hình kết hợp trên bộ dữ liệu SIPakMed
///

## Discussion

1. Mức hiệu suất phụ thuộc mạnh vào miền dữ liệu.

    - Hiệu suất cao nhất ở Hospital A.

    - Giảm dần ở các bộ dữ liệu công khai (Herlev -> LBC -> HiCervix).

    - SIPaKMed có hiệu suất ở mức trung gian giữa toàn bộ các tập dữ liệu.

    - Mô hình học sâu (InceptionResNetV2, InceptionV3) thường đạt kết quả cao hơn trên dữ liệu lớn và phức tạp.

    - Khi dữ liệu có ít đặc trưng, các mô hình kết hợp (đặc biệt SVM) vẫn duy trì ổn định.

2. Sự bổ trợ lẫn nhau giữa các miền dữ liệu.

    - Kết quả cho thấy một mô hình huấn luyện và tinh chỉnh trên nhiều miền dữ liệu có thể giúp cải thiện khả năng tổng quát hóa.

    - Dữ liệu đa dạng (Herlev, LBC, HiCervix, SIPaKMed) có thể bổ sung cho dữ liệu thực tế trong nước (BVA) để tạo mô hình mạnh mẽ hơn.

3. Công việc tương lai.

    - Kết hợp dữ liệu đa miền.

    - Áp dụng kỹ thuật domain adaptation để giảm sai khác đặc trưng giữa các bộ dữ liệu.

    - Ensemble giữa deep learning và machine learning có thể khai thác ưu điểm của cả hai.

--- 