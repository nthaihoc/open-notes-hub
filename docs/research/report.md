# I. Tên đề tài: {Bài toán là gì?}\_{Em dùng phương pháp gì?}\_{Dữ liệu}

## 1. Motivation (Động lực nghiên cứu)

## 2. Related Work (Các nghiên cứu liên quan)

## 3. Method (Phương pháp đề xuất)

## 4. Datasets (Dữ liệu)

## 5. Evaluation Protocol (Đánh giá)

## 6. Reference (Tài liệu tham khảo)

# II. Nhật ký nghiên cứu.

## 1. Motivation (Động lực nghiên cứu)

## 2. Related Work (Các nghiên cứu liên quan)

## 3. Method (Phương pháp đề xuất)

## 4. Datasets (Dữ liệu)

- Quy trình xử lý dữ liệu: làm sạch và chuẩn hoá âm vị theo chuẩn IPA.
- Chia dữ liệu thành 3 tập train/dev/test
- Thống kê dữ liệu: (1) thống kê dữ liệu ban đầu (gốc), (2) thống kê dữ liệu sau khi chia xong của cả 3 tập train/dev/test.

**Notes.** 
- Làm sạch: xử lý âm thanh bị lỗi, không có nhãn v.v.
- Nếu em áp dụng thêm phương pháp tăng cường dữ liệu (augmentattion) $\rightarrow$ trình bày chi tiết là em sử dụng phương pháp gì để tăng cường $\rightarrow$ thống kê lại dữ liệu. 

## 5. Evaluation Protocol (Đánh giá)

- F1, Precision, Recall, Accuracy
- TA, FA, TA, FA $\rightarrow$ ý nghĩa của nó là gì? tại sao phải dùng nó
- PER, WER ...

**Notes.** Thêm một phần để ghi lại lịch sử tài nguyên trong quá trình huấn luyện. Ghi lại thông sô về CPU/RAM/GPU.

**Inference time.** Độ trễ phản hồi của mô hình khi triển khai mô hình. 30s/1000 request.

## 6. Implementation (Thực nghiệm)

Bàng 1: Thiết kế ma trận thực nghiệm cắt bỏ.

| model | datasets | loss | status |
| :---: | :------: | :--: | :----: |
| wav2vec2 | l2arctic v5 | ctc |
| wav2vec2 | l2arctic v5 (augment) | ctc |
| wav2vec2 | l2arctic v5 | focal_loss |
| .... | ... | ... |

## 7. Results (Kết quả)

Bàng 1: Kết quả ma trận thực nghiệm

| model | datasets | loss | status | f1 | per |
| :---: | :------: | :--: | :----: | :--: | :--: |
| wav2vec2 | l2arctic v5 | ctc | done | 60.60 | 12.12 |
| wav2vec2 | l2arctic v5 | focal_loss | done | 70.70 | 13.12 |

## 8. Discussion (Thảo luận)

- Đưa ra các đánh giá nhận định từ kết quả, làm nổi bật kết quả tốt nhưng cũng không che giấu những hạn chế mô hình.
- Đề xuất công việc tương lai cải thiện hạn chế hiện tại.
