---
title: Cascaded Acoustic-Phonetic Representation Transfer for Multi-Aspect Pronunciation Assessment
---

# Cascaded Acoustic-Phonetic Representation Transfer for Multi-Aspect Pronunciation Assessment

## I. Motivation
---
Đánh giá phát âm tự động (CAPT) đa khía cạnh đòi hỏi hệ thống không chỉ nắm bắt được đặc tính vật lý nguyên bản của âm thanh (để chấm độ trôi chảy, ngữ điệu) mà còn phải hiểu sâu sắc về ngữ nghĩa và âm vị học (để chấm độ chính xác). Các hệ thống End-to-End hiện tại gặp nhiều khó khăn khi cố gắng dự đoán trực tiếp điểm số từ đặc trưng âm thanh gốc do thiếu hụt dữ liệu gán nhãn lớn và hiện tượng nhiễu chéo đặc trưng.

Nghiên cứu này đề xuất khung học chuyển giao tuần tự hai luồng (Cascaded Dual-Stream Framework). Cụ thể, mô hình khai thác tri thức lỗi âm vị từ tập dữ liệu chuyên biệt (L2-Arctic), sau đó đóng băng tri thức này và dung hợp song song với đặc trưng âm thanh gốc để dự đoán điểm số trên tập SpeechOcean762. Cách tiếp cận này giúp cô lập luồng thông tin, giảm thiểu nhiễu và tăng độ chính xác của toàn hệ thống.

Danh sách các phương pháp, nghiên cứu liên quan: [[related work](https://docs.google.com/spreadsheets/d/16DlLrI1dq6fAb7VFoXNRrisnw9JxYDQN3AXDFnYEyYM/edit?usp=sharing)].

## II. Datasets
---

### 1. Thông tin chung
---
Nghiên cứu sử dụng hai bộ dataset về âm thanh là [[L2-Arctic](https://psi.engr.tamu.edu/l2-arctic-corpus/)] và [[SpeechOcean762](https://www.openslr.org/101/)]. Trong khuôn khổ kiến trúc Cascaded Dual-Stream đề xuất, tập L2-Arctic sẽ được sử dụng độc lập ở Giai đoạn 1 (Stage 1) để tinh chỉnh khả năng nhận thức âm vị học. Trong khi đó, tập SpeechOcean762 được sử dụng ở Giai đoạn 2 (Stage 2) để huấn luyện bộ kết hợp và dự đoán điểm số đa khía cạnh.

- **L2-Arctic:** Là bộ dữ liệu chỉ chứa nhãn lỗi âm vị (phoneme-level). Được thu thập từ 24 người nói (không phải tiếng mẹ đẻ) đến từ nhiều quốc gia như: Ấn Độ, Hàn Quốc, Tây Ban Nha, v.v. Bộ dữ liệu này cung cấp 4 nhãn âm vị chính là

    - `a (addition/insertion)`
    - `s (substitution)`, 
    - `d (deletion)`
    - còn lại là phát âm đúng.

!!! example "Định dạng mãu dữ liệu L2-Arctic"

    ```json
    xmin = 0 --> thời gian bắt đầu của audio
    xmax = 1.6214965986394558 --> thời gian kết thúc của audio
    tiers? <exists> 
    size = 3 
    item []: 
        item [1]:
            class = "IntervalTier" 
            name = "words" --> gán nhãn cấp độ từ
            xmin = 0 
            xmax = 1.6214965986394558 
            intervals: size = 7 
            intervals [1]:
                xmin = 0 
                xmax = 0.04 
                text = "" 
            intervals [2]:
                xmin = 0.04 --> thời gian bắt đầu của từ trong audio
                xmax = 0.28 --> thời gian kết thúc từ trong audio
                text = "there" --> từ xuất hiện trong khoảng thời gian này.
            intervals [3]:
                xmin = 0.28 
                xmax = 0.53 
                text = "was" 
            intervals [4]:
                xmin = 0.53 
                xmax = 0.64 
                text = "a" 
            intervals [5]:
                xmin = 0.64 
                xmax = 1.01 
                text = "change" 
            intervals [6]:
                xmin = 1.01 
                xmax = 1.44 
                text = "now" 
            intervals [7]:
                xmin = 1.44 
                xmax = 1.6214965986394558 
                text = "" 
        item [2]:
            class = "IntervalTier" 
            name = "phones" --> gán nhãn cấp độ âm vị
            xmin = 0 
            xmax = 1.6214965986394558 
            intervals: size = 16 
            intervals [1]:
                xmin = 0 
                xmax = 0.04 
                text = "sil" --> viết tắt của silence (khoảng lặng) không có tiếng nói
            intervals [2]:
                xmin = 0.04 
                xmax = 0.11 
                text = "DH" 
            intervals [3]:
                xmin = 0.11 
                xmax = 0.2 
                text = "EH1" 
            intervals [4]:
                xmin = 0.2 --> thời gian bắt đầu của âm vị
                xmax = 0.28 --> thời gian kết thúc của âm vị
                text = "R,AH0,s" --> R[âm vị đúng cần phát âm]; AH0(âm vị thực tế người dùng phát âm); s[lỗi substitution].
            intervals [5]:
                xmin = 0.28 
                xmax = 0.34 
                text = "W"
            intervals [6]:
                xmin = 0.34 
                xmax = 0.44 
                text = "AH1" 
            intervals [7]:
                xmin = 0.44 
                xmax = 0.53 
                text = "Z,S,s" 
            intervals [8]:
                xmin = 0.53 
                xmax = 0.64 
                text = "AH0" 
            intervals [9]:
                xmin = 0.64 
                xmax = 0.8 
                text = "CH" 
            intervals [10]:
                xmin = 0.8 
                xmax = 0.85 
                text = "EY1" 
            intervals [11]:
                xmin = 0.85 
                xmax = 0.94 
                text = "N" 
            intervals [12]:
                xmin = 0.94 
                xmax = 1.01 
                text = "JH,CH,s" 
            intervals [13]:
                xmin = 1.01 
                xmax = 1.16 
                text = "N" 
            intervals [14]:
                xmin = 1.16 
                xmax = 1.44 
                text = "AW1" 
            intervals [15]:
                xmin = 1.44 
                xmax = 1.6 
                text = "sp" 
            intervals [16]:
                xmin = 1.6 
                xmax = 1.6214965986394558 
                text = "" 
        item [3]:
            class = "IntervalTier" 
            name = "IPA" 
            xmin = 0 
            xmax = 1.6214965986394558 
            intervals: size = 7 
            intervals [1]:
                xmin = 0 
                xmax = 0.2 
                text = "" 
            intervals [2]:
                xmin = 0.2 
                xmax = 0.28 
                text = "É¹,É™,s" 
            ...
    ```

- **SpeechOcean762:** Bộ dữ liệu này cung cấp điểm số ở mức câu (sentence-level) với nhãn là 4 tiêu chí điểm: 

    - `accuracy (độ chính xác)`
    - `fluency (trôi chảy)`
    - `prosodic (ngữ điệu)`
    - `completeness (đầy đủ)`.

!!! warning "Một mẫu dữ liệu của SpeechOcean762"

    ```json
    {'accuracy': 9, --> điểm chính xác toàn câu
    'completeness': 10.0, --> điểm đầy đủ toàn câu (không phát âm thiếu âm vị/từ nào)
    'fluency': 9, --> điểm trôi chảy của toàn câu
    'prosodic': 9, --> điểm ngữ điệu toàn câu
    'text': 'MARK IS GOING TO SEE ELEPHANT', --> câu nói của người dùng phát âm
    'total': 9, --> điểm tổng cho toàn câu
    'words': [{'accuracy': 10,
    'phones': ['M', 'AA0', 'R', 'K'],
    'phones-accuracy': [2.0, 2.0, 1.8, 2.0],
    'stress': 10,
    'text': 'MARK',
    'total': 10,
    'mispronunciations': []},
    ...
    'speaker': '0003',
    'gender': 'm',
    'age': 6,
    'audio': {'path': '000030012.wav',
    'array': array([-0.00119019, -0.00500488, -0.00283813, ...,  0.00274658,
            0.        ,  0.00125122]),
    'sampling_rate': 16000}}
    ```

### 2. Setup bộ dữ liệu
---

Vì nghiên cứu này hướng tới hai nhiệm vụ chính là đánh giá hiệu suất phát hiện, chẩn đoán lỗi phát âm (Mispronunciation Detection Diagnosis - MDD) và chấm điểm phát âm toàn câu (Pronunciation Scoring), bộ dữ liệu cần được cài đặt và phân chia một cách phù hợp để đảm bảo tính công bằng và phản ánh đúng hiệu suất của mô hình.

1. **Phân chia dữ liệu L2-Arctic (Cho nhiệm vụ MDD - Stage 1)**. Cài đặt mặc định bám sát các nghiên cứu tiền nhiệm để đảm bảo tính công bằng khi so sánh:

    - **Test set:** Lựa chọn 6 người nói (NJS, TLV, TNI, TXHC, YKWK, ZHAA) để đánh giá.
    - **Training set:** Dữ liệu từ các người nói còn lại được gộp chung để tiến hành huấn luyện.
    - **Development (Valid) set:** Trích xuất một tập con nhỏ từ Training set để tinh chỉnh các siêu tham số (hyperparameters).

2. **Phân chia dữ liệu SpeechOcean762 (Cho nhiệm vụ Scoring - Stage 2)**

    - Sử dụng chuẩn phân chia gốc của bộ dữ liệu (2500 câu phát âm dành cho huấn luyện và 2500 câu dành cho kiểm thử).
    - Đảm bảo kiểm soát chặt chẽ để không có sự rò rỉ dữ liệu (data leakage) giữa tập train và test về mặt danh tính người nói.

### 3. Data Preprocessing Pipeline
---

Để tương thích với kiến trúc mạng đầu vào của phương pháp đề xuất, dữ liệu từ TextGrid và JSON được chuẩn hóa qua một pipeline đồng nhất:

- **Xử lý nhãn L2-Arctic:** Ánh xạ (mapping) chuỗi TextGrid thành các chuỗi nhãn 1D. Các nhãn lỗi (`a`, `s`, `d`) kết hợp với âm vị thực tế (ví dụ: `AH0`, `EH1`) được chuyển đổi thành một từ điển số nguyên (Integer Dictionary) phục vụ cho việc tối ưu hóa hàm mất mát CTC (Connectionist Temporal Classification).
- **Đồng bộ hóa khung thời gian (Time-alignment):** Do dữ liệu âm thanh là chuỗi liên tục nhưng nhãn lại có tính thời điểm (từ khoảng $t_{\text{start}}$ đến $t_{\text{end}}$), một cơ chế gióng hàng (alignment) được áp dụng để ép khớp các mốc thời gian `xmin`, `xmax` trong dữ liệu gốc với các khung hình (frames) đầu ra tương ứng của mô hình âm thanh học tự giám sát.

Bộ dữ liệu sau khi đã được tiền xử lý và làm sạch: [[L2arctic](https://drive.google.com/drive/u/0/folders/1MuBH31ibGJDRGcRYjwvOf8n4r_CNYhC3)] và [[SpeechOcean762](https://drive.google.com/drive/u/0/folders/1MuBH31ibGJDRGcRYjwvOf8n4r_CNYhC3)].

## III. Methodology
---

Kiến trúc đề xuất được chia làm hai giai đoạn độc lập:

^^Stage 01. Phonetic Representation Learning (Học biểu diễn âm vị)^^

- Sử dụng Wav2Vec2/HuBERT/Whisper fine-tune trên L2-Arctic với hàm mất mát CTC (Connectionist Temporal Classification).
- Mục tiêu tạo ra một chuyên gia phát hiện lỗi âm vị.

^^Stage 02. Stage 2: Dual-Stream Decoupled Extraction & Fusion^^

Giả sử tại một khung hình thời gian $T$, sau khi đi qua luồng trích xuất, ta thu được hai ma trận đặc trưng:

*   **Đặc trưng âm học (Acoustic):** $F_{A} \in \mathbb{R}^{T \times d_{a}}$ (với $d_{a}$ là số chiều của luồng SSL gốc).
*   **Đặc trưng âm vị (Phonetic):** $F_{P} \in \mathbb{R}^{T \times d_{p}}$ (với $d_{p}$ là số chiều xác suất hậu nghiệm từ luồng MDD).

Quá trình kết hợp và dự đoán điểm số diễn ra qua 4 bước tuần tự như sau:

- **Bước 1: Ghép nối và Đồng bộ không gian (Feature Concatenation & Projection)** Đầu tiên, hai ma trận được ghép nối dọc theo chiều đặc trưng. Vì số chiều ghép nối có thể rất lớn, sử dụng một lớp tuyến tính (Linear layer) để chiếu (project) chúng về cùng một không gian ẩn (hidden space) có kích thước $d_{model}$:

$$X = \text{Linear}(\text{Concat}(F_{A}, F_{P})) \in \mathbb{R}^{T \times d_{model}}$$

- **Bước 2: Học tương quan ngữ cảnh (Contextual Fusion với Transformer)** Chuỗi đặc trưng $X$ được cộng thêm Positional Encoding ($PE$) nhằm giữ thông tin về vị trí và thứ tự thời gian của các âm tiết, trước khi đưa vào mạng Transformer Encoder (gồm 2 layers, 4 attention heads). Cơ chế Self-Attention tại đây làm nhiệm vụ phân tích sự phụ thuộc chéo trong không gian thời gian. *Ví dụ: Mô hình sẽ học được cách chú ý xem một lỗi sai âm vị ở giây thứ 2 có làm đứt gãy âm thanh ở giây thứ 3 hay không.*

$$H = \text{TransformerEncoder}(X + PE) \in \mathbb{R}^{T \times d_{model}}$$

- **Bước 3: Trích xuất đặc trưng toàn câu (Temporal Pooling)** Để chuyển từ chuỗi đặc trưng cấp độ khung hình dọc theo trục $T$ sang một vector đại diện duy nhất cho toàn bộ câu nói (sentence-level representation), sử dụng phép toán Mean Pooling:

$$v = \frac{1}{T} \sum_{t=1}^{T} H_{t} \in \mathbb{R}^{d_{model}}$$

- **Bước 4: Mạng dự đoán đa nhánh (Multi-Branch Scoring Heads)** Đây là mạng đầu ra cuối cùng. Vector $v$ được truyền vào 4 nhánh mạng truyền thẳng độc lập (Multi-Layer Perceptrons - MLPs). Mỗi nhánh đại diện cho một bộ đánh giá chuyên biệt nhằm chấm điểm một tiêu chí cụ thể. Cấu trúc của mỗi nhánh MLP bao gồm: `Linear Layer` $\to$ `ReLU Activation` $\to$ `Dropout (0.1)` $\to$ `Linear Output Layer`.

$$\text{Score}_{Acc} = \text{MLP}_{Acc}(v)$$

$$\text{Score}_{Flu} = \text{MLP}_{Flu}(v)$$

$$\text{Score}_{Pros} = \text{MLP}_{Pros}(v)$$

$$\text{Score}_{Comp} = \text{MLP}_{Comp}(v)$$

Toàn bộ mạng ở Stage 2 này được tối ưu hóa thông qua hàm mất mát L2 (Mean Squared Error - MSE) tính trên tổng sai số của cả 4 tiêu chí dự đoán so với nhãn gốc (ground-truth scores).

## IV. Research Questions
---

1. **RQ1 (Nền tảng):** Mô hình học tự giám sát (SSL) khi được tinh chỉnh có khả năng phát hiện lỗi và chẩn đoán âm vị (MDD) tốt như thế nào trên tập dữ liệu L2-Arctic so với các phương pháp Baseline?

2. **RQ2 (Tác động chéo):** Việc bổ sung kiến thức âm vị học (được trích xuất từ mô hình đã giải quyết RQ1) có giúp cải thiện hiệu năng chấm điểm phát âm đa khía cạnh trên tập SpeechOcean762 không?

3. **RQ3 (Ablation Study):** Việc tách biệt hai luồng trích xuất (Dual-Stream) có thực sự ngăn chặn hiện tượng "Task-Specific Representation Shift" (nhiễu đặc trưng âm học) so với việc dùng chung một mô hình hay không?

4. **RQ4 (Độ nhạy của tiêu chí):** Tiêu chí chấm điểm nào (trong 4 tiêu chí) có sự tương quan mạnh mẽ nhất và được hưởng lợi nhiều nhất từ độ chính xác của bộ trích xuất âm vị học?


## V. Experimental Results
---

Nghiên cứu này sử dụng hai nhóm độ đo chính:

- MDD Task: PER (Phoneme Error Rate - càng thấp càng tốt) và F1-Score (càng cao càng tốt).
- Scoring Task: PCC (Pearson Correlation Coefficient - tương quan càng gần 1 càng tốt).

**RQ1. Đánh giá hiệu năng phát hiện lỗi âm vị (Stage 1 trên L2-Arctic).**

> Mục tiêu: Chứng minh mô hình Stage 1 là chuyên gia đủ tốt trong việc bắt lỗi âm vị trước khi đóng băng chúng để làm bộ trích xuất cho Stage 2.

| Model | PER (%) | F1-Score (%) |
| :---- | :---: | :---: |
| GOP | - | 42.42 |
| CTC-ATT | - | 56.02 |
| CNN-RNN-CTC | - | 56.08 |
| w2v2.0-XLSR | 16.20 | 60.44 |
| $MV_{multi} - MT_{seq}$ | **14.13** | 60.31 |
| xlsr-ctc | 15.47 | 59.10 |
| **Ours (Wav2Vec2-large-xlsr)** | 15.20 | **61.11** |

/// caption
**Bảng 1.** Đánh giá hiệu suất mô hình cho tác vụ MDD trên tập dữ liệu L2-Arctic.
///

Hiệu suất tổng thể được trình bày trong **Bảng 1**, phương pháp tinh chỉnh đề xuất (Ours: Wav2Vec2-large-xlsr) đạt mức F1-Score cao nhất là 61.11%, vượt qua hoàn toàn các phương pháp cơ sở như CNN-RNN-CTC (56.08%) hay các biến thể kiến trúc tinh vi hơn như $MV_{multi} - MT_{seq}$ (60.31%).

Mặc dù mô hình đạt mức PER (15.20%) cao hơn một chút so với $MV_{multi} - MT_{seq}$ (14.13%), nhưng độ đo F1-Score lại cho thấy sự vượt trội. Trong bài toán chẩn đoán lỗi phát âm (MDD) trên tập L2-Arctic, dữ liệu có sự mất cân bằng lớp nghiêm trọng (âm vị phát âm đúng chiếm đa số, lỗi phát âm chiếm thiểu số). F1-Score là một độ đo khắt khe và toàn diện hơn PER vì nó đánh giá sự cân bằng giữa Precision và Recall trên các lớp thiểu số. Việc đạt F1-Score kỷ lục chứng minh mô hình không bị thiên lệch (bias) vào lớp đa số, mà thực sự có khả năng bắt trúng các lỗi phát âm tinh vi.

Việc cải thiện F1-Score lên ngưỡng lớn hơn 61% đồng thời duy trì mức PER ổn định (~15%) từ một mô hình SSL gốc đảm bảo rằng trình huấn luyện đã hội tụ tốt. Các ma trận xác suất hậu nghiệm (posterior probabilities) sinh ra từ mô hình này hoàn toàn đủ độ tin cậy và sự phong phú về thông tin lỗi sai để đóng vai trò làm bộ trích xuất đặc trưng âm vị học (Phonetic feature extractor) cho mạng dự đoán điểm số ở Stage 2.


**RQ2 & RQ4: Đánh giá tổng thể hiệu năng chấm điểm trên SpeechOcean762**

> Mục tiêu: Chứng minh phương pháp đề xuất vượt qua các baseline và đánh giá sự ảnh hưởng của Stage 1 tới hiệu suất Scoring.

| Model | Acc (%) | Flu (%) | Pro (%) | Comp (%) | Total (%) | PCC (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| GOPT | 71.40 | 75.30 | 76.00 | 74.20 | 74.20 | 61.20 |
| Joint-CAPT | 71.90 | 77.50 | 77.30 | 74.30 | - | - |
| HCB | 77.20 | **79.10** | **83.60** | 82.60 | **79.60** | **80.04** |
| **Ours** | **78.85** | 74.50 | 77.80 | **84.33** | 79.10 | 79.66 |

/// caption
**Bảng 2.** Đánh giá hiệu suất mô hình cho tác vụ chấm điểm tổng thể toàn câu trên tập dữ liệu SpeechOcean762.
///

Như được thể hiện trong **Bảng 2**, mô hình đề xuất (Ours) đạt mức tương quan (PCC) cao nhất ở tiêu chí Accuracy (78.85%) và Completeness (84.33%), vượt qua hoàn toàn các baseline mạnh như GOPT và HCB. Điều này thiết lập một mối tương quan nhân quả trực tiếp với kết quả từ RQ1. Việc mô hình Giai đoạn 1 có khả năng nhận diện xuất sắc các lỗi phát âm với F1-Score 61.11% đã cung cấp một nguồn tri thức hậu nghiệm vô cùng phong phú. Nhờ luồng tri thức này, Giai đoạn 2 có cơ sở vững chắc để phát hiện chính xác các hiện tượng nuốt âm hoặc sai âm, từ đó dự đoán điểm số Accuracy và Completeness sát với đánh giá của chuyên gia con người nhất.

Mặc dù vượt trội ở nhóm điểm phát âm từ vựng, phương pháp đề xuất ghi nhận kết quả thấp hơn mô hình HCB ở tiêu chí Fluency (74.50% vs 79.10%) và Prosody (77.80% vs 83.60%). Về mặt ngôn ngữ học, độ trôi chảy và ngữ điệu phụ thuộc chủ yếu vào đặc tính vật lý nguyên bản của âm thanh chứ không bị ảnh hưởng quá nhiều bởi lỗi sai của một vài âm vị đơn lẻ. Việc sử dụng phép ghép nối trực tiếp (Concatenation) ở module Fusion có thể đã gây ra hiện tượng nhiễu thông tin cục bộ, khiến các đặc trưng lỗi âm vị làm mờ đi một phần thông tin vật lý, dẫn đến sự suy giảm nhẹ ở hai tiêu chí này.

Mức điểm tổng thể (Total PCC) đạt 79.66%, tiệm cận rất sát với mức cao nhất của mô hình HCB (80.04%) và bỏ xa các phương pháp khác, chứng minh tính khả thi, hiệu quả và sự cân bằng của khung học chuyển giao tuần tự (Cascaded Dual-Stream).


**RQ3: Ablation Study thiết kế luồng đặc trưng**

> Mục tiêu: Chứng minh sự cần thiết của cấu trúc Dual-Stream.

| Extraction Strategy | Acc (%) | Flu (%) | Pro (%) | Comp (%) | PCC (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Single-Shared | 73.90 | 71.50 | 71.20 | 73.50 | 72.52 |
| **Dual-Stream** | **78.85** | **74.50** | **77.80** | **84.33** | **79.66** |

/// caption
**Bảng 3.** So sánh hiệu suất giữa phương pháp dùng chung một mô hình và tách luồng.
///

Khi sử dụng duy nhất mô hình đã fine-tune MDD (Single-Shared) để trích xuất cả hai luồng đặc trưng, điểm Fluency và Prosody sụt giảm nghiêm trọng (ví dụ: Fluency giảm từ 74.50% xuống 71.50%). Điều này củng cố giả thuyết rằng việc tối ưu hóa PER ở Stage 1 đã làm biến dạng các đặc tính vật lý nguyên bản của âm thanh. Giải pháp Dual-Stream giải quyết hoàn toàn nút thắt này bằng cơ chế phân lập: sử dụng một mô hình SSL gốc (chưa fine-tune) chuyên biệt để giữ nguyên vẹn đặc trưng âm học đầu vào, kết hợp song song với mô hình MDD để trích xuất lỗi âm vị.

---

---