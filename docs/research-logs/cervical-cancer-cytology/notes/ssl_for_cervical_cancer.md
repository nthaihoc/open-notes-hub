---
title: Self-Supervised Learning (SSL) for Cervical Cancer Classification
icon:
hide: navigation
---

# Topic 01. Self-Supervised Learning for Cervical Cancer Classification
---

## I. Experimental Setup
### 1. Datasets

**Herlev datasets.** Bộ dữ liệu tế bào học cổ tử cung được sử dụng rộng rãi trong nghiên cứu về nhận dạng và phân loại tế bào ung thư cổ tử cung từ ảnh hiển vi ([**Jan Jantzen et al., 2006**](https://www.researchgate.net/publication/282157686_The_Pap_Smear_Benchmark)), được thu thập tại Herlev University Hospital, Đan Mạch. Thống kê bộ dữ liệu được mô tả trong **Bảng 1**. Bộ dữ liệu gồm 917 ảnh với 7 loại nhãn khác nhau, trong đó có 3 nhãn là normal (bình thường) và 4 nhãn là bất thường (abnormal). 

| Label | Number for label | Types |
| :---- | :--------------: | :---: |
| superficiel | 74 | Normal | 
| intermediate | 70 | Normal |
| columnar | 98 | Normal |
| light dysplastic | 182 | Abnormal | 
| severe dysplastic | 197 | Abnormal |
| moderate_dysplastic | 146 | Abnormal | 
| carcinoma in situ | 150 | Abnormal |
| **Total** | **917** | |

/// caption
**Bảng 1.** Thống kê mô tả bộ dữ liệu Herlev Pap-smear.
///

**LBC Pap smear datasets.** LBC (Liquid-Based Cytology) là một trong các xét nghiệm sàng lọc ung thư cổ tử cung ([**Elima Husain et al., 2020**](https://pmc.ncbi.nlm.nih.gov/articles/PMC7186519/)). Bộ dữ liệu này bao gồm tổng cộng 963 ảnh LBC, được chia thành bốn nhóm tương ứng với bốn lớp tổn thương: NILM, LSIL, HSIL và SCC. Các lớp này đại diện cho các tổn thương tiền ung thư và ung thư cổ tử cung. Hình ảnh được thu thập từ 460 bệnh nhân, với nhiều vấn đề phụ khoa khác nhau. Mô tả thống kê của bộ dữ liệu được cung cấp trong **Bảng 2**.

| Label | Number for label | Types |
| :---- | :--------------: | :---: |
| LSIL  | 113 | Precancerous |
| NILM  | 613 | Precancerous |
| HSIL  | 163 | Precancerous |
| SCC   | 74  | Cancer       |
| **Total** | **963** |      |

/// caption
**Bảng 2.** Bộ dữ liệu LBC bao gồm bốn đại diện tổn thương: NILM, LSIL, HSIL và SCC.
///

**HiCerix datasets.** Bộ dữ liệu tế bào học cổ tử cung lớn nhất và đa trung tâm nhất được công bố công khai ([**De Cai et al., 2024**](https://ieeexplore.ieee.org/document/10571965)). HiCervix bao gồm 40.299 ảnh tế bào cổ tử cung được cắt từ 4.496 ảnh lát cắt toàn bộ (whole slide images), được phân loại thành 29 lớp và có chú thích. Các lớp này được tổ chức theo một cây phân cấp ba tằng nhằm nắm bắt thông tin chi tiết về các nhóm nhỏ (fine-grained subtypes).

























<!-- ## 1. Main contribution details
### __1.1 Tác động của các kỹ thuật augmentation__

**Ý tưởng.** Phân tích nhóm tác động và chức năng của các phương pháp augmentation.

- Hình học: crop, flip, rotation.
- Màu sắc: color jitter, histogram equalization.
- Biến dạng mềm: elastic deformation.
- Nhiễu ảnh: gaussian blur, speckle noise.
- Tăng độ phân giải ảnh: blur, sharpen.

**Phương pháp thực hiện.** Thiết lập một baseline ban đầu, bao gồm các kỹ thuật augmentation đơn giản, ít gây nhiễu sinh học, phù hợp với dữ liệu ảnh y tế và có khả năng giữ nguyên thông tin cấu trúc trong ảnh tế bào. 

| Config | Augment | Notes |
| :----: | :------ | :---: |
|  A | random crop, horizontal/vertical flip | baseline |
| B | baseline + group màu sắc | |
| C | baseline + group biến dạng mềm | |
| D | basline + group nhiễn ảnh | |
| E | basline + tăng độ phẩn giải anh | |

**Phương pháp đánh giá.** Sử dụng t-NSE với các thuật toán phân cụm (K-means hoặc DBSCAN) trên embedding sau khi quá trình huấn luyện không nhãn kết thúc, trực quan hóa kết quả đó trên nhiều cấu hình augmentation để so sánh. Có thể sử dụng thêm các độ đo để đánh giá biểu diễn linear protocol trên một ít tỷ lễ dữ liệu có nhãn. 

### __1.2 Xây dựng hàm mất mát phù hợp cho ảnh y tế__

**Motivation.** Barlow Twins Loss (BT Loss) được đề xuất bởi ([**Zbontar et al., 2021**](https://)), là một phương pháp học biểu diễn tự giám sát. Mục tiêu của phương pháp này là học các đặc trưng ổn định từ các ảnh đầu vào đã qua biến đổi bằng cách tối ưu hóa ma trận tương quan giữa hai tập embedding thu được từ hai phép biến đổi khác nhau của cùng một ảnh. Hàm mất mát BT được thiết kế với hai mục tiêu chính: (1) tăng cường tính tương quan trên đường chéo - đảm bảo các đặc trưng tương ứng giữa hai views giống nhau; (2) giảm nhiễu dữ thừa giữa các đặc trưng - khử tương quan giữa các đặc trưng khác nhau.

Cũng giống như các phương pháp học tự giám sát khác như SimCLR, MoCo, BYOL hay DINO, Barlow Twins dựa trên việc sinh ra hai biến thể của cùng một ảnh đầu vào thông qua pipeline biến đổi dữ liệu $\mathcal{T}$. Từ một batch ảnh ban đầu $\mathbf{X}$, hai batch ảnh augmented được tạo ra, ký hiệu là $H^A$ và $H^B$. Các batch này sau đó được đưa vào backbone CNN để trích xuất đặc trưng, tạo thành các batch embedding tương ứng $Z^A$ và $Z^B.$

Khác với các mô hình SSL khác, thay vì sử dụng L2 normalization, BT thực hiện chuẩn hóa embedding bằng cách trung bình hóa từng chiều đặc trưng theo batch, nhằm đảm bảo mỗi chiều có kỳ vọng bằng 0. Điêu này giúp tăng tính ổn định trong việc tính toán ma trận tương quan và giảm sự phụ thuộc nhất định vào chuẩn hóa L2.

Công thức BT cơ bản được định nghĩa như sau:

$$
\mathcal{L}_{BT} = 
\underbrace{\sum_i (1 - C_{ii})^2}_{\text{Invariance term}} 
+ 
\lambda 
\underbrace{\sum_i \sum_{j \neq i} C_{ij}^2}_{\text{Redundancy reduction term}} 
\tag{1}
$$


Trong đó $C$ được coi là cross correlation matrix giữa 2 view $Z^A$ và $Z^B$, và $C_{ij}$ được xác định bằng:

$$
C_{ij} = \frac{1}{N} \frac{\sum_b \mathcal{z}^A_{b, i} \mathcal{z}^B_{b, j}}{\sqrt{\sum (\mathcal{z}^A_{b, i})^2} \sqrt{\sum (\mathcal{z}^B_{b, j})^2}} \tag{2}
$$

$\sum (\mathcal{z}^A_{b, i})^2, \sum (\mathcal{z}^B_{b, j})^2$ lần lượt là độ lệch chuẩn theo batch của các đặc trưng trong 2 view $Z^A$ và $Z^B$, và $N$ là batch size. 

Việc tính toán hàm BT có thể được minh họa thông qua ví dụ sau. Giả sử một batch huấn luyện gồm $N=3$ ảnh đầu vào, ký hiệu $X = [x_a; x_b; x_c]$, mỗi ảnh trong batch sẽ tạo thành 2 phiên bản tăng cường khi đó $X = [x_{a1}; x_{a2}; x_{b1}; x_{b2}; x_{c1}; x_{c2 }]$. 

Toàn bộ ảnh sau đó được tổ chức thành 2 batch riêng biệt, tương ứng với hai view khác nhau của cùng một batch gốc: 

- Batch A: $Z_A = [x_{a1}; x_{b1}, x_{c1}]$.
- Batch B: $Z_B = [x_{a2}; x_{b2}, x_{c2}]$. 

Cả hai batch này được đưa qua một encoder chung thu được embedding, sau đó đưa qua một projection head với số chiêu là 3 thu được các tensor tương ứng như sau:

```python
torch.manual_seed(42)

z_a = torch.randn(3, 3)
z_b = torch.randn(3, 3)

print("z_a:\n", z_a)
print("z_b:\n", z_b)

# z_a:
#  tensor([[ 0.3367,  0.1288,  0.2345],
#         [ 0.2303, -1.1229, -0.1863],
#         [ 2.2082, -0.6380,  0.4617]])
# z_b:
#  tensor([[ 0.2674,  0.5349,  0.8094],
#         [ 1.1103, -1.6898, -0.9890],
#         [ 0.9580,  1.3221,  0.8172]])
```

Từ công thức (2), $C_{ij}$ có thể được viết như sau:

$$
C_{ij} = \frac{1}{N} \sum_{n=1}^N \frac{z^A_{b,i}}{\sigma(z^A_{b,i})} \frac{z^B_{b,j}}{\sigma(z^B_{b,j})} \tag{3}
$$

Công thức (3) này chính là tích vô hướng của $Z_A$ và $Z_B$ được chuẩn hóa (mean-centered và chia độ lệch chuẩn theo từng chiều). 

```python
mean_a = z_a.mean(dim=0)
std_a = z_a.std(dim=0, unbiased=False)
mean_b = z_b.mean(dim=0)
std_b = z_b.std(dim=0, unbiased=False)

z_a_norm = (z_a - mean_a) / std_a
z_b_norm = (z_b - mean_b) / std_b

print("z_a_norm:\n", z_a_norm)
print("z_b_norm:\n", z_b_norm)

# z_a_norm:
#  tensor([[-0.6478,  1.3057,  0.2404],
#         [-0.7648, -1.1233, -1.3271],
#         [ 1.4126, -0.1824,  1.0867]])
# z_b_norm:
#  tensor([[-1.3937,  0.3757,  0.7025],
#         [ 0.9045, -1.3686, -1.4142],
#         [ 0.4892,  0.9929,  0.7117]])

```

Sau khi chuẩn hóa lần lượt $Z_A$ và $Z_B$, $C_{ij}$ đơn giản chỉ là tích vô hướng giữa hai tensor này. Kết quả thu được ở bước này chính là ma trận tương quan chéo. 

```python
c_ij = (z_a_norm.T @ z_b_norm) / 3
c_ij

# tensor([[ 0.3007,  0.7353,  0.5440],
#         [-0.9750,  0.6156,  0.7920],
#         [-0.3346,  0.9952,  0.9397]])
```

Quay trở lại với mục tiêu chính của BT Loss, mục tiêu đầu tiên là tăng cường tính tương quan trên đường chéo - chính là việc đi tính Invariance Term (IT) trong công thức (1). Để tính được IT, chỉ cần lấy các giá trị trên đương chéo chính thực hiện tính toán. Trong ví dụ này có ba gía trị trên đương chéo là [0.3007; 0.6156; 0.9397].

$$\text{IT} = (1-0.3007)^2 + (1-0.6156)^2 + (1-0.9397)^2 = 2.0347$$

Mục tiêu thứ hai là giảm nhiễu dư thừa giữa các đặc trưng - chính là việc đi tính Redundancy Reduction Term (RRT) trong công thức (1). Nếu IT sử dụng các giá trị trên đường chéo thì RRT sẽ sử dụng các giá trị nằm ngoài đường chéo.

$$
\text{RRT} = (-0.9750)^2 + (-0.3346)^2 + 0.7353^2 + 0.9952^2 + 0.5440^2 + 0.7920^2 = 4.7803
$$

Khi đó BT loss của toàn bộ batch với $\lambda=0.005$ là:

$$
\mathcal{L}_{BT} = \text{IT} + 0.005 \cdot \text{RRT} = 2.0586
$$

**Hạn chế của BT Loss.** Mặc dù Barlow Twins là một phương pháp học biểu diễn tự giám sát mạnh mẽ, tuy nhiên vẫn có thể dễ dàng thấy một số hạn chế.

- Coi mức độ quan trọng giữa các vùng trong toàn bộ ảnh là như nhau: BT sử dụng toàn bộ embedding vector một cách đồng đều để tính tương qan giữa các view.

- Không có cơ chế tập trung: Thiếu cơ chế chú ý làm cho mô hình khó học được feature có tính phân biệt cao hoặc bỏ qua nhiễu. 

- Không khai thác tốt cấu trúc không gian: chủ yếu trên các vector embedding cuối cùng, bỏ qua thông tin không gian có giá trị từ feature map.

**Phương pháp đề xuất.** Cải tiến hàm mất mát Barlow Twins, nhằm thích ứng tốt hơn với đặc trưng của ảnh y tế. Phương pháp này tích hợp một cơ chế attention định hướng vào embedding (Attention Guided Barlow Twins Loss - AGBT), cho phép mô hình tập trung vào các vùng ảnh có khả năng mang thông tin chẩn đoán. Đặc biệt, khác với một số phương pháp như ([**Hagen el at., 2022**](https://arxiv.org/pdf/2205.15428)), ([**Guanghao Zhu el at., 2024**](https://arxiv.org/pdf/2205.15428)), ([**Chaitanya el at., 2021**](https://arxiv.org/pdf/2112.09645)), phương pháp này không cần thêm hàm mất mát phụ, giúp mô hình giữ được độ ổn định và đơn giản trong huấn luyện.

Với hai ảnh tăng cường $x_1, x_2$ được lấy từ cùng một ảnh gốc, mục tiêu là học được các biểu diễn $z_1, z_2$ nhằm nhấn mạnh các vùng quan trọng của ảnh. Để làm được điều này thì thêm vào một cơ chế attention trong không gian embedding, và kết hợp trực tiếp trước khi áp dụng vào Barlow Twins.

*Attention trong không gian embedding.* Gọi $f(\cdot)$ là encoder, $h(\cdot)$ là projection head và $k(.)$ là mạng con dùng để dự đoán attention. Với hai ảnh tăng cường $x_1, x_2$ có:

$$
z_1^{thô} = f(x_1); z_2^{thô} = f(x_2) \tag{4}
$$

$$
p_1 = h(z_1^{thô}); p_2 = h(z_2^{thô}) \tag{5}
$$

$$
a_1 = k(p_1); a_2 = k(p_2) \tag{6}
$$

Để tránh sự lệch pha giữa hai nhánh (view), tạo một attention dùng chung cho toàn bộ batch bằng cách tính trung bình giữa $a_1, a_2$:

$$
a_{shared} = \sqrt{a_1 \cdot a_2 + \epsilon} \tag{7}
$$

Sau đó, áp dụng attention lên từng embedding:

$$
z_1 = z_1^{thô} \cdot a_{shared}; z_2 = z_2^{thô} \cdot a_{shared} \tag{8}
$$

*Hàm mất mát Barlow Twins.* Vẫn sử dụng cơ chế như hàm BT Loss gốc nhằm tối đa hóa tính tương quan chéo giữa hai embedding, giảm thiểu tương quan giữa các chiều khác nhau. Đầu tiên, các vector được chuẩn hóa và tính tương tự như công thức (2). Hàm mất mát được giữ nguyên như (1), chỉ thay đầu vào là $z_1, z_2$ đã được attention-weighted. Tóm lại, loss cuối cùng cơ bản vẫn là một hàm Barlow Twins cổ điển, nhưng áp dụng trên embedding đã được điều chỉnh bởi attention:

### __1.3 Tác động của một số yếu tố đến hiệu suất mô hình__

**Tác động của pre-trained.** Đánh giá tác động của mô hình SSL khi khởi tạo huấn luyện từ đầu và khi sử dụng trọng số ImageNet, nhàm đánh giá sự tác động của miền dữ liệu tới hiệu suất của mô hình.

**Đánh giá sự cải thiện của hàm loss đề xuất.** Huấn luyện mô hình với một số hàm loss (NT-Xent, Barlow Twins, AGBT - hàm loss đề xuất) trong giai đoạn pretext_task, đánh giá hiệu suất mô hình khi sử dụng 3 hà loss này.

**Tác động của chiến lược fine-tune.** Triển khai hai kỹ thuật fine-tune chính: (1) Linear probing - đóng băng encoder và huấn luyện trên một lớp kết nối đầy đủ; (2) Full finetuning - huấn luyện toàn bộ mô hình trên cả encoder + classifier. 

**Ảnh hưởng của tỷ lệ dữ liệu có nhãn.** Sau khi quá trình pretext-task kết thúc, fine-tune mô hình với nhiều tỷ lệ dữ liệu có nhãn, nhàm đánh giá sự ảnh hưởng của dữ liệu có nhãn tới mô hình trong giai đoạn downstream task.

### __1.4 So sánh với các mô hình supervised baseline__

**Ý tưởng.** Đánh giá hiệu suất của mô hình SSL với các mô hình học có giám sát truyền thống trong trường hợp dữ liệu có nhãn khan hiếm.

**Phương pháp thực hiện.** Huấn luyện một số mô hình supervised learning trên cùng bộ dữ liệu (3-5 models), cùng tỷ lệ nhãn, cùng các tham số cấu hình (nhằm đảm bảo tính công bằng trong so sánh). 

### __1.5 Bộ dữ liệu__

**Ý tưởng.** Sử dụng bộ dữ liệu 22k ảnh kết hợp thêm với một số bộ dữ liệu công khai có nhãn tuông đương hoặc khác, nhằm tạo ra sự đa dạng và khác biệt giúp mô hình tổng quát hóa, biểu diễn tốt cho dữ liệu trong quá trình huấn luyện không nhãn.

**Phương pháp thực hiện.** Sử dụng bộ dữ liệu Herlev, SIPakMed, Mendeley và HiCervix.  -->