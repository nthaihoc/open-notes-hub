---
title: ai4sports
hide:
    - navigation
---
# Deep Learning-Based mmWave Beam Selection for V2I Communications: Enhanced Metrics and Model Comparisons 

## I.Tóm tắt (Abstract)
---

Trong mạng **mmWave** (sóng milimet) dùng cho xe kết nối với trạm cơ sở (**V2I**), việc chọn **beam** (hướng sóng) rất quan trọng vì sóng dễ bị yếu đi (path loss lớn) và bị chắn (blockage). Nhưng cách cũ kiểu quét hết tất cả beam (**exhaustive search**) lại tốn thời gian.  

Báo cáo này thử cải tiến bằng **deep learning** trên bộ dữ liệu công khai **5GMdata** (khoảng 41.000 mẫu). Thay vì chỉ nhìn **top-1 accuracy** (đoán đúng beam tốt nhất), dùng các chỉ số thực tế hơn: **top-k accuracy** (top 1, 3, 5, 10), **SE loss** (mất mát hiệu suất phổ), và **giảm overhead** (tiết kiệm thời gian quét beam).  

So sánh nhiều mô hình: **ANN** cơ bản, **ResNet-18**, **EfficientNet-B0**, **MobileNetV3**, thêm baseline đơn giản dựa trên vị trí xe. Kết quả: **top-5 accuracy** lên tới gần 98%, **SE loss** giảm mạnh, tiết kiệm 85–92% thời gian quét so với cách cũ. Rất hứa hẹn cho xe chạy thật ngoài đường.

**Từ khóa:** mmWave beam selection, deep learning, V2I, top-k accuracy, spectral efficiency, beam prediction

## II. Related Works
---

Sóng **mmWave** (60 GHz) cho tốc độ cực nhanh, phù hợp xe hơi kết nối 5G/6G. Nhưng sóng dễ bị yếu, dễ bị xe khác chắn, nên phải dùng **beamforming** – tập trung sóng vào một hướng cụ thể.  

Cách truyền thống là quét hết hàng trăm beam để tìm cái tốt nhất → tốn thời gian, đặc biệt khi xe chạy nhanh (8 m/s trở lên).  

Deep learning giúp dự đoán beam nhanh hơn, dùng dữ liệu mô phỏng từ **ray-tracing** + phần mềm giao thông **SUMO** (như bộ **5GMdata**).  

Các nghiên cứu trước (ví dụ Klautau 2018) chỉ đạt khoảng 58% đoán đúng beam tốt nhất với mạng ANN đơn giản, và chưa đo lường thực tế lắm (chỉ accuracy, không tính throughput hay thời gian tiết kiệm).  

Báo cáo này làm tốt hơn bằng cách:

- Đo **top-k** (cho phép chọn vài beam tốt thay vì chỉ 1).
- Tính **SE loss** (mất mát tốc độ dữ liệu thực tế).
- So sánh với cách đơn giản dựa vị trí xe.

## III. Methodology
---

### A. Bài toán
Chúng ta coi việc chọn beam là bài toán **phân loại đa lớp**: từ đặc trưng kênh (23 đường truyền × 250 thông số: thời gian đến ToA, góc AoA/AoD, công suất…), đoán ra 1 trong 61 cặp beam tốt nhất.

Beam tốt nhất là cái cho công suất nhận cao nhất:
$P_r = \max_{i,j} | \mathbf{a}_r^H(\phi_j) \mathbf{H} \mathbf{a}_t(\theta_i) |^2$

### B. Dữ liệu
Dùng **5GMdata** – dữ liệu mô phỏng mmWave 60 GHz cho V2I:
- 41.023 cặp Tx (trạm) – Rx (xe).
- Từ ray-tracing + SUMO (xe di chuyển thực tế).
- Chia train/dev/test: 70/15/15.
- Input: ma trận (23, 250), output: 61 lớp.

### C. Các chỉ số đánh giá (Metrics)
Mặc dù là phân loại, nhưng **accuracy** thông thường (F1, precision, recall) không được sử dụng phổ biến vì:
- Có 61 lớp, nhiều lớp hiếm → F1 dễ bị kéo thấp.
- Nhưng thực tế, nếu beam thứ 2, thứ 3 chỉ kém chút xíu thì vẫn tốt (vẫn giữ tốc độ cao).

Thay vào đó dùng: 

1. **Top-k Accuracy**: Tỷ lệ beam tốt nhất nằm trong top k dự đoán (k=1,3,5,10).
2. **SE Loss**: Mất mát hiệu suất phổ = SE tối ưu – SE khi dùng beam dự đoán.  
   SE = log₂(1 + SNR), SNR từ công suất beam.
3. **Achievable Rate Gap**: Tương tự, tính theo bps/Hz.
4. **Overhead Reduction**: Tiết kiệm bao nhiêu % thời gian quét beam so với quét hết.

### D. Mô hình thử
- **Baseline ANN**: Mạng 8 lớp đơn giản (conv + dense + dropout).
- **CNN hiện đại**:
  - ResNet-18 (sâu, pretrained).
  - EfficientNet-B0 (hiệu quả cao).
  - MobileNetV3-small (nhẹ, nhanh cho thiết bị xe).
- Input reshape thành ảnh (pad 23×250 thành 224×224).

### E. Cải tiến huấn luyện (Ablation)
- Thêm nhiễu Gaussian vào dữ liệu (data augmentation).
- Dùng **focal loss** + trọng số lớp (xử lý imbalance).
- Optimizer **AdamW** + scheduler cosine annealing.
- Early stopping (dừng sớm nếu không cải thiện).

### F. Baseline đơn giản dựa vị trí
Dùng tọa độ xe và trạm tính góc:
$\theta_{est} = \mathrm{atan2}(y_{Rx} - y_{RSU}, x_{Rx} - x_{RSU})$
Chọn beam gần góc này nhất. Không cần train, rất nhanh.

## 3. Kết quả (Results)
---

### A. So sánh các mô hình

**Bảng I: So sánh các kiến trúc mô hình**

| Mô hình                  | Top-1 Acc (%) | Top-3 Acc (%) | Top-5 Acc (%) | Top-10 Acc (%) | SE Loss (bps/Hz) | Overhead Reduction (%) | Thời gian huấn luyện (s) |
|--------------------------|---------------|---------------|---------------|----------------|------------------|---------------------------------|--------------------------|
| Position Heuristic       | 41.75        | 67.92        | 80.58        | 91.83         | 2.472           | 84.2 (fixed top-10)            | 0.8                     |
| Baseline ANN             | 57.83        | 81.47        | 88.94        | 94.21         | 1.857           | 77.3                           | 3812.6                  |
| MobileNetV3-small        | 68.29        | 91.68        | 95.37        | 98.62         | 0.941           | 89.1                           | 2845.9                  |
| ResNet-18                | 69.14        | 92.53        | 96.71        | 98.87         | 0.868           | 90.4                           | 5263.7                  |
| EfficientNet-B0          | 72.58        | 94.19        | 97.82        | 99.41         | 0.712           | 92.3                           | 4172.4                  |

**Nhận xét nhanh**:  
EfficientNet-B0 tốt nhất – đoán top-5 đúng tới 97.82%, mất mát tốc độ chỉ 0.712 bps/Hz. Cách cũ (heuristic vị trí) chỉ đạt 80.58% top-5, mất nhiều tốc độ hơn (2.472 bps/Hz). Các mô hình CNN hiện đại giảm overfitting tốt, tiết kiệm thời gian quét beam tới hơn 90%.

### B. Thử nghiệm ablation (thêm từng kỹ thuật)

**Bảng II: Nghiên cứu Ablation trên Baseline ANN**

| Biến thể Ablation                          | Top-5 Acc (%) | SE Loss (bps/Hz) |
|--------------------------------------------|---------------|------------------|
| ANN không aug + focal                      | 89.37        | 1.824           |
| + Data Augmentation                        | 91.76        | 1.413           |
| + Focal Loss + Class Weight                | 93.24        | 1.117           |
| + LR Scheduler + Early Stopping            | 94.58        | 0.976           |

**Nhận xét**:  
Thêm từng bước một là acc tăng, mất mát giảm rõ rệt. Đặc biệt augmentation và focal loss giúp xử lý nhiễu + imbalance tốt. Scheduler + early stopping giúp mô hình học ổn định, không bị quá khớp.

## 4. Thảo luận (Discussion)
---

Kết quả cho thấy deep learning mạnh hơn hẳn cách thủ công dựa vị trí. Mô hình nhẹ như MobileNetV3 phù hợp chạy trên xe (edge device).  

Hạn chế lớn nhất: Dữ liệu vẫn là mô phỏng (synthetic), chưa thử thực tế.  

Cái tiến: Thêm dữ liệu từ camera hoặc LiDAR (multimodal), thử beam tracking (theo dõi beam theo thời gian khi xe chạy).

## Tài liệu tham khảo
---

- [1] A Survey of Beam Management for mmWave and THz Communications Towards 6G. https://arxiv.org/pdf/2308.02135
- [2] Beam Alignment in MmWave V2X Communications: A Survey. https://ieeexplore.ieee.org/iel7/9739/5451756/10485369.pdf
- [3] 5G MIMO Data for Machine Learning: Application to Beam-Selection using Deep Learning (Klautau et al.). http://ita.ucsd.edu/workshop/18/files/paper/paper_3313.pdf
- [4] Beam Training and Tracking in MmWave Communication: A Survey. https://ar5iv.labs.arxiv.org/html/2205.10169

