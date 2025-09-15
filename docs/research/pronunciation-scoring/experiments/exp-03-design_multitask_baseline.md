---
tille: Multi-task learning for Pronunciation Scoring
---

# Multi-task learning for Pronunciation Scoring
---

## I. Problems and objective

**Mục tiêu mô hình.** Nghiên cứu thiết kế mô hình với hai mục tiêu chính:

- Trả về cả nhãn lỗi chi tiết (phoneme-level)

- Trả về điểm phát âm toàn câu (sentence-level score)

**Vấn đề chính.** Bộ dữ liệu [[speechocean](https://github.com/jimbozhang/speechocean762)] và bộ dữ liệu [[l2arctic](https://psi.engr.tamu.edu/l2-arctic-corpus/)] có những đặc điểm, đạc trưng phân tán khác nhau:

- Speech Ocean: Có nhãn điểm toàn câu (accuracy, completeness, fluency, prosodic) nhưng không có nhãn lỗi âm vị chi tiết.

- L2-ARCTIC: Có nhãn lỗi chi tiết ở mức âm vị (phoneme-level) nhưng không có điểm toàn câu.

Hiện tại không có bộ datasets nào có thể cung cấp đầy đủ các thông tin nhãn lỗi chi tiết và nhãn điểm toàn câu.

**Hướng nghiên cứu.** Thiết kế bài toán multi-task learning với dữ liệu không đồng bộ nhằm tận dụng mọi dữ liệu mà không cần tái nhãn.

## II. Proposed model

**Backbone.** Tận dụng các mô hình đã được pretrained trên lượng dữ liệu lớn (wav2vec 2.0/HuBERT) nhằm trích xuất đặc trưng thô trực tiếp từ âm thanh (frame-level embeddings). Thực hiện hai chiến lược khi đưa backbone vào mô hình chấm điểm phát âm:

- Không fine-tune (chỉ làm feature extractor): Chỉ lấy embedding cố định từ backbone cho mỗi audio, sau đó đưa chúng vào các mô hình để phục vụ cho hai task chính: phone-level classification hoặc sentence-level regression.

- Fine-tune toàn bọ backbone: Khi train multi-task, các gradient + loss của cả hai task sẽ đồng thời được truyền ngược vào backbone để tinh chỉnh.

**Heads (multi-task).** Tập trung vào hai task chính phục vụ cho hai mục tiêu của mô hình:

1. Phoneme-level MLP classifier (frame-level). Sử dụng các embdding đã được trích xuất từ backbone huấn luyện một bộ phân loại để phan loại và xác định lỗi chi tiết.

2. Sentence-level regression. Huấn luyện bộ hồi quy trên các embddings được backbone trích xuất để dự đoán ra một số nhãn điểm cho toàn câu (accuracy, completeness, fluency, prosodic)

## III. Training strategy

Với dữ liệu đến từ hai bộ khác nhau, một số chiến lược huấn luyện được sử dụng:

- Dữ liệu từ L2-ARCTIC: chỉ forward cho phoneme-level head và backbone (nếu fine-tune) trong khi đó sentence-level head không tính gradient

- Dữ liệu từ Speech Ocean: chỉ forward cho sentence-level head và bacbone (nếu fine-tune), phoneme-level head không tính gradient.

Để điều chỉnh sự cân bằng cho hai task, hàm loss được thiết kế đơn giản, $\alpha$ và $\beta$ có thể được tinh chỉnh: 

$$
\text{total_loss} = \alpha * \text{phoneme_loss} + \beta * \text{sentence_loss}
$$

## IV. Experimental setup

**Datasets.**

1. L2-ARCTIC

    - Mục tiêu: Huấn luyện phoneme-level classifier

    - Preprocessing: Sử dụng MFA để ép khung và gán nhãn frame-level sau đó trích xuất embedding từ backbone cho mỗi frame

2. Speech Ocean

    - Mục tiêu: Huấn luyện sentence-level regression

    - Preprocessing: Chuân hóa dữ liệu audio giống như bộ dữ liệu L2-ARCTIC, sau đó pool frame embeddings thành sentence embedding (mean pooling, attention pooling)

**Evaluation metrics.**

- Phoneme-level (classification task): accuracy, f1-score, confusion-matrix.

- Sentence-level (regression task): RMSE, MSE, MAE

**Ablation study.** Phần này nhằm tìm và phân tích các yếu tố ảnh hưởng nhất đến hiệu suất mô hình

- Backbone frozen vs fine-tune: So sánh xem liệu fine-tune có giúp phát hiện lỗi và dự đoán điểm chính xác hơn không.

- Pooling strategies: chỉ áp dụng cho sentence-level head, tập trung vào hai option chính là: (1) mean pooling - trung bình các frame embedding; (2) attention pooling - cho phép model học trọng số khác nhau cho từng frame quan trọng.

- Loss balancing ($\alpha/\beta$ impact): Đánh giá sự ảnh hưởng của hai tham số này tới hiệu suất của mô hình đồng thời ở cả hai task.


## V. Baseline comparisions

1. MLP classifier + backbone frozen

    - Đây là baseline cơ bản cho phomeme-level task
    - Backbone được giữ nguyên, không fine-tune chỉ dùng để trích xuất đặc trưng cô định từ audio
    - Phần MLP classifier được huấn luyện để phân loại lỗi phoneme dựa trên embedding này
    - Mục đích: đánh giá hiệu quả của feature extractor nguyên gốc khi không tinh chỉnh sử dụng các độ đô như accuracy và f1-score

2. MLP classifier + backbone fine-tuned

    - Tương tự baseline trên, nhưng ở đây backbone được fine-tuen cùng với MLP classifier
    - Mục đích: xem việc fine-tune backbone có giúp tăng hiệu quả nhận diễn lỗi phoneme không.

3. Multi-task model + backbone frozen

    - Huấn luyện đồng thời phomeme-level và sentence-level nhưng không fine-tune backbone
    - Mục tiêu: kiểm tra hiệu quả của backbone giữa hai task, ngay cả khi embeddings không được tinh chỉnh.

4. Multi-tasl model + backbone fine-tuned

    - Huấn luyện đồng thời cả hai task vụ, nhưng backbone được fine-tune từ cả hai task.
    - Mục tiêu: Đánh giá lợi ích của fine-tune backbone trong multi-task để tăng khả năng nhận diện và dự đoán.

## VI. Results

- Triển khai đánh giá các các mô hình cho bài tóan dự đoán điểm toàn câu được đánh giá trên bộ dữ liệu SpeechOcean sử dụng PCC (Pearson Correlation Coefficient). 

| Model             | Prosody        | Completeness   | Fluency        |
|----|--|----|----|
| Linear Regression | 0.70 ± 0.06   | 0.71 ± 0.05   | 0.73 ± 0.04   |
| Decision Tree     | 0.72 ± 0.05   | 0.73 ± 0.04   | 0.75 ± 0.03   |
| Random Forest     | 0.76 ± 0.03   | 0.77 ± 0.03   | 0.78 ± 0.03   |
| XGBoost           | 0.78 ± 0.03   | 0.79 ± 0.02   | 0.80 ± 0.02   |


- Các mô hình được huấn luyện trước trên bộ dữ liệu l2-arctic được đánh giá trên bộ speechocean (đánh giá nhị phân) nhằm đánh giá khả năng tổng quát hóa khi dịch chuyển sang miền dữ liệu mới  

| Model               | Speechocean762 (F1-score) |
|-----|-----|
| MLP                 | 0.68 ± 0.04              |
| BiLSTM              | 0.72 ± 0.03              |
| GOP-based           | 0.65 ± 0.05              |
| Mini-Transformer    | 0.73 ± 0.03              |
