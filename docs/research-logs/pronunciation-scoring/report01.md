---
title: Tổng quan về Pronunciation Scoring - PS
icon: material/information
---

# Tổng quan về Pronunciation Scoring - PS
---

!!! danger "Mô tả"
    - Nhiệm vụ này thuộc [Phase01 - Nghiên cứu tổng quan và chuẩn bị dữ liệu]

        [Phase01 - Nghiên cứu tổng quan và chuẩn bị dữ liệu]: README.md/#ke-hoach-nhiem-vu-chi-tiet

    - Nghiên cứu, khảo sát tổng quan các công trình liên quan đến bài toán PS trong và ngoài nước.
    - Tìm hiểu một số kiến trúc PS tổng thể, hệ thống end-to-ends.

## 1. Giới thiệu chung
---

Hệ thống hỗ trợ học ngôn ngữ bằng máy tính (Computer-Assisted Language Learing - CALL) mang lại nhiều lợi ích thiết thực trong giáo dục, đặc biệt là đối với giáo viên và học sinh. Những hệ thống này cho phép cung cấp phản hồi liên tục cho người học mà không cần sự giám sát thường trực của giáo viên, hỗ trợ việc tự học, khuyến khích sử dụng ngôn ngữ một cách tương tác thay vì phụ thuộc vào các phương pháp học truyền thống như học thuộc lòng hay ghi chép. Bên cạnh đó, CALL cũng góp phần đơn giản hóa và tự động hóa các quy trình đánh giá năng lực ngôn ngữ.

Một trong những thành phần cốt lõi và đầy thác thức trong hệ thông CALL là chấm điểm phát âm (Pronuncation Scoring). Đây là nhiệm vụ quan trọng nhằm đánh giá mức độ chĩnh xác trong các phát âm của người học so với chuẩn của người bản ngữ. Hệ thống chầm điểm phát âm hiệu quả không chỉ giúp phát hiện và sửa lỗi kịp thời mà còn cung cấp phản hồi mang tính dài hạn về năng lực phát âm của người học.

Trong nhiều năm qua, đã có rất nhiều các nghiên cứu, hướng tiếp cận chính như:

- Phương pháp dựa trên mô hình nhận dạng tiếng nói (ASR-based methods): Đây là một trong những phương pháp cổ điển và rất phổ biến, trong đó hệ thống nhận dạng giọng nói thường sử dụng mô hình Markov ẩn (Hidden Markow Model) nhằm so sánh phát âm của người học với các mô hình âm học chuẩn. Một trong những kỹ thuật nổi bật là thuật toán Goodness of Pronunciation (GOP) cho phép tính điểm phát âm ở cấp độ âm vị (phone-level).

- Đánh giá dựa trên so sánh với mẫu người bản ngữ (Template-based / Reference-based methods): Các phương pháp này so sánh trực tiếp tín hiệu âm thanh của người học với bản ghi âm từ người bản ngữ. Chúng thường yêu cầu dữ liệu huấn luyện riêng cho từng từ hoặc cụm từ, khiến hệ thống trở nên text-dependent và rất khó để có thể mở rộng.

- Mô hình học máy và học sâu (Machine Learning / Deep Learning-based methods): Gần đây, các mô hình học sâu như CNN, RNN và đặc biệt là các mô hình transformer-based (wav2vec, HuBERT, v.v.) đước sử dụng để trích xuất đặc trưng âm học và xây dựng bộ chấm điểm phát âm mà không cần phải phụ thuộc hoàn toán vào pipeline của hệ thống nhận dạng truyền thống.

Ngoài ra, các nghiên cứu khác cũng khai thác triệt để những yếu tố đặc trưng của âm thanh như trường độ, ngữ điệu, v.v, nhằm đánh giá chất lượng phát âm một cách toán diện hơn. Tuy nhiên, chúng vấn đang gặp phải rất nhiều những thách thức liên quan đến sự phụ thuộc vào dữ liệu, sự nhất quát và công bằng trong đánh giá và sự thích nghi khi dữ liệu giọng nói đa dạng. 

## 2. Một số phương pháp nổi bật
---
### __2.1 Goodness of Pronuncation__

[**GOP (Goodness of Pronunciation)**](http://svr-www.eng.cam.ac.uk/~sjy/papers/wiyo00.pdf) là phương pháp là một trong những kỹ thuật nổi bật, với mục tiêu đo lường mức độ khớp giữa phát âm của người học và cách phát âm chuẩn của người bản ngữ, tính tại mức âm vị (phone-level). Gỉa sử khi chúng ta phát âm từ **cat** nó sẽ có hai âm vị là **/ka/** và **/et/**. GOP sẽ chấm điểm xem người dùng đã phát âm **/ka/** tốt đến đâu và **/et/** tốt đến đâu. 

!!! info "**Công thức GOP**"

    $$
    \textbf{GOP} = \frac{1}{NF_\text{(p)}} \cdot \left| \text{log} \left( \frac{p(O^\text{(p)}) | p}{\max_{q \in \mathbf{Q}} p(O^\text{(p)}) | q} \right) \right|
    $$

    ^^Trong đó:^^

    - Tử số $p(O^\text{(p)}) | p$: Đây là khả năng đoạn âm thanh $O(p)$ được tạo ra bởi đúng âm vị $p$. Chúng cho biết âm thanh thực tế khớp với âm vị mà chúng ta mong đợi nghe thấy đến mức nào.

    - Mẫu số $\max_{q \in \mathbf{Q}} p(O^\text{(p)}) | q$: Đây là khả năng đoạn âm thanh $O(p)$ được tạo ra bởi âm vị khớp tốt nhất trong tất cả các âm vị $q$. Cho biết âm thanh thực tế giống với âm vị nào nhất trong tất cả các âm vị, bất kể đúng hay sai.

Nếu tỷ lệ $\frac{p(O^\text{(p)}) | p}{\max_{q \in \mathbf{Q}} p(O^\text{(p)}) | q}$ tiến đến gần 1, có nghĩa là âm vị đích khớp rất tốt, và không có âm vị nào khác khớp tốt hơn. Điều này chứng tỏ người đọc đã phát âm rất tốt. Ngược lại, có nghĩa là có một hoặc nhiều âm vị khác khớp với đoạn âm thanh đó hơn so với âm vị đích, đồng nghĩa với người dùng phát âm chưa chuẩn. 

**Hệ thống Pronunciation Scoring:** 

Sơ đồ khối của cơ chế chấm điểm dựa trên phương pháp GOP được thể hiện như trong hình. Cụ thể sẽ trải qua 4 giai đoạn:

![](../images/gop_system_baseline.png)
/// caption
Hình 1.1: Biểu đồ minh họa các thành phần chính trong hệ thống chấm điểm dựa trên phương pháp GOP truyền thống. 
///

- Front-end Feature Extraction: Đây là giai đoạn đầu tiên, dữ liệu âm thanh đầu vào được xử lý để trích xuất các đặc trưng quan trọng của giọng nói thường là MFCC (Mel-frequency Cepstral Coefficients). Đây là cách biểu điễn âm thanh dưới dạng số.

- Two Recognition Pass: Tiếp theo các transcipts và đặc trưng âm thanh tương ứng sẽ trải qua hai lượt nhận dạng:
    - Forced Alignment Pass: Sử dụng bản ghi đã biết để ép các đặc trưng MFCC khớp với chuỗi phone đúng (đây chính là việc tính toán tử số của công thức GOP). Ví dụ hệ thống nhận đầu vào tín hiệu âm thanh của người đọc là **cat**, hệ thống sẽ sử dụng một từ điển phát âm (pronunciation dictionary), từ điển này chứa cách phát âm chuẩn theo IPA của mỗi từ trong ngôn ngữ. Từ **cat** sẽ được ánh xạ thành chuỗi âm vị chuẩn là **/k/ /ae/ /t/**. Sau đó quá trình ép khung diễn ra, giai đoạn này sẽ xác định thời điểm bắt đầu và kết thúc của từng âm vị trong lời nói của người học và đồng thời gán cho mỗi đoạn âm thanh một âm vị $p$ đúng theo bản ghi chuẩn. Đầu ra của giai đoạn này sẽ có dạng:

    ```yaml title="example.json" linenums="1"
    [
        { "phone": "/k/", "start_time": 0.05, "end_time": 0.18 },
        { "phone": "/æ/", "start_time": 0.18, "end_time": 0.35 },
        { "phone": "/t/", "start_time": 0.35, "end_time": 0.48 }
    ]
    ```

    - Phone Recognition Pass: Sử dụng một "phoneme loop" để nhận dạng đoạn âm thanh $O^{\text{(p)}}$ mà không có ràng buộc về từ vựng. Chúng tìm ra âm vị nào (trong tất cả các âm vị có thể có trong ngôn ngữ) khớp tốt nhất với đoạn âm thanh đó (tính toán mẫu số của GOP).

- GOP scores: Tính toán các điểm GOP riêng lẻ cho từng phone dựa trên các kết quả thu được từ hai lượt nhận dạng.

- Threshold: Sau khi có được điểm GOP cho mỗi phone, lựa chọn một ngưỡng tùy chỉnh nhằm phân loại, nếu điểm GOP của một phone thấp hơn ngưỡng thì âm đó được coi là phát âm kém và ngược lại.

**Hạn chế của phương pháp GOP:**

- Phụ thuộc quá nhiều vào Forced Alignment và HMM (Hidden Markov Model) truyền thống. GOP phụ thuộc hoàn toàn vào độ chính xác của quá trình ép khung để xác định ranh giới của từng âm vị và tính toán likelihood. Nếu quá trình căn chỉnh này không chính xác sẽ dẫn đến điểm GOP không đáng tin cậy.

- Không có mô hình riêng biệt cho lỗi phát âm: GOP truyền thống so sánh âm thanh đầu vào với mô hình của âm vị đúng và tất cả các âm vị khác trong ngôn ngữ đích. Tuy nhiên chúng bỏ qua và không quan tâm đến các loại lỗi phát âm cụ thể thường gặp.

- Không xem xét ngữ cảnh: GOP thường đánh giá từng âm vị một cách tương đối độc lập. Chúng ít khi xét đến ngữ cảnh âm vị xung quanh hoặc ngữ cảnh từ/câu, điều này cũng ảnh hưởng đến cách phát âm và nhận thức về lỗi của con người.

### __2.2 Deep Neural Networks based GOP__

Các hệ thống chấm điểm phát âm thường được huấn luyện chỉ với dữ liệu giọng nói của người bản xứ. Trong khi đó, giọng nói của người học ngôn ngữ (phi bản xứ) lại có nhiều khác biệt, đặc biệt là khi họ phát âm sai. Nhiều nghiên cứu chỉ ra rằng việc huấn luyện hệ thống trực tiếp bằng dữ liệu giọng nói của người học phi bản xứ giúp cho hệ thống tốt hơn. Tuy nhiên việc thu thập dữ liệu và gán nhãn chi tiết dữ liệu giọng nói phi bản xứ là một thách thức lớn gây tốn kém và mất thời gian. Phương pháp này được tiếp cận dựa trên transfer learning [**DNN-based GOP**](https://arxiv.org/pdf/2111.00976) để giải quyết những thách thức này, cụ thể: 

- Tận dụng mô hình đã được huấn luyện cho nhiệm vụ nhận dạng giọng nói trên một lượng lớn dữ liệu người bản xứ.
- Tinh chỉnh mô hình đã được huấn luyện trước với lượng nhỏ dữ liệu phi bản xứ có nhãn.

**Mở rộng công thức tính GOP với DNN:**

So với phương pháp tính toán GOP truyền thống như được trình bày ở [**(1)**](#1-goodness-of-pronunciation), trong đó GOP được tính dựa trên các mô hình âm học GMM (Gausian Mixture Models). Trong những năm gần đây, một loạt các nghiên cứu đã chỉ ra những cải thiện đáng kể khi sử dụng các mô hình âm học dựa trên DNN (Deep Neural Networks). DNN có khả năng học và mô hình hóa các đặc trưng âm thanh phức tạp tốt hơn nhiều so với GMM.

Khi sử dụng các mô hình âm học dựa trên DNN, điểm GOP của một âm vị đích $p$ bắt đầu từ khung thời gian $\text{T}$ và có độ dài $\text{D}$ được tính như sau:

$$
\textbf{GOP}_{p} = -\frac{1}{D} \sum^{\text{T+D-1}}_\text{t=T} \log P_{t}(p|O)
$$

Trong đó:

- $\text{D}$ là độ dài của âm vị, tính bằng số lượng khung thời gian$p$
- $\text{T}$ là khung thời gian bắt đầu của âm vị $p$
- $O$ là toàn bộ chuỗi đặc trưng, được trính xuất từ dạng sóng âm sang các đặc trưng để có thể tính toán, đại diện cho tất cả các dữ liệu âm thanh mà mô hình có thể sử dụng
- $\sum^{\text{T+D-1}}_\text{t=T}$ tổng các giá trị cho tất cả các khung thời gian t nằm trong khoảng từ khung bắt đầu $\text{T}$ đến khung kết thúc $\text{T + D - 1}$ của âm vị $p$.
- $\log P_{t}(p|O)$ là xác xuất hâu nghiệm của âm vị $p$ tại khung thời gian $t$, với điều kiện là toàn bộ chuỗi đặc trưng âm học $O$ đã được quan sát

Sự khác biệt lớn giữa việc tính toán giữa GOP truyền thống và GOP dựa trên DNN là việc chuyển từ likelihood sang posterior. Cụ thể:

- Đối với GOP truyền thống: Đoạn âm thanh $O^{(p)}$ của âm vị $p$ được đưa vào mô hình sinh (generative model) của âm vị $p$. Mô hình này sẽ tính toán khả năng chúng sinh ra $O^{(p)}$.

- Đối với GOP dựa trên DNN: Thay vì tính toán tỉ lệ giữa các likelihood, mô hình DNN trực tiếp đưa ra xác suất hậu nghiệm $P_t(p|O)$ cho âm vị $p$ tại mỗi khung thời gian $t$. 

**Cấu trúc mô hình đề xuất:**

Nhìn chung phương pháp này cũng tương tự như GOP basline truyền thống, cả hai đều tuân thủ theo nhiều quy trình riêng lẻ, từ việc xử lý dữ liệu âm thanh cho đến đưa ra điểm số phát âm cho từng âm vị.

![](../images/gop_dnn_system.png)

- Giai đoạn tiền xử lý và căn chỉnh ép buộc (Forced Aligner): Đầu vào là một tín hiệu âm thanh (waveform) mà người học phát ra và bản ghi (transcipt) tương ứng. Sau đó vẫn sử dụng bộ căn chỉnh ép buộc để xác định tính chính xác thời điểm bắt đầu và kết thúc của từng âm vị trong lời nói của người học.

- Giai đoạn tạo điểm cấp khung (Frame-level score Generation): Sau khi có các đoạn âm thanh được căn chỉnh cho từng âm vị, các đặc trưng âm học đã được trích xuất cho từng khung nhỏ của toàn bộ tín hiệu âm thanh được đưa vào một mô hình DNN, mô hình này sẽ đưa ra điểm số cho mỗi âm vị có thể có trong ngôn ngữ tại khung đó.

- Lựa chọn điểm cấp khung (Frame-level score selection): 

    - Như đã được đề cập, mô hình DNN trong các hệ thống cơ sở đuọc huấn luyện để đưa ra xác suất hậu nghiệm cho từng senone tại mỗi khung thời gian (nhánh phía trên của khối màu xám). Để có được điểm số cho mỗi âm vị tại mỗi khung, các xác suất hậu nghiệm của tất cả các senone thuộc về cùng một âm vị đó sẽ được tổng hợp lại. Mục đích là chuyển đổi đầu ra chi tiết của DNN (cấp senone) về cấp độ âm vị (phone) để tính toán GOP.

    - Mô hình đề xuất (nhánh phía dưới khối màu xám), thay vì phải đi qua các senone trung gian rồi tổng hợp, mô hình DNN được thiết kế và huấn luyện trực tiếp để đưa ra xác suất hậu nghiệm cho từng âm vị tại mỗi khung thời gian. 

    - Sau khi DNN đã tạo ra điểm số cho tất cả các âm vị tại mỗi khung, bước này sẽ chọn ra điểm số của âm vị đúng $p$ tại từng khung. Ví dụ nếu Forced Aligner cho rằng khung $t$ thuộc về âm vị **/k/** thì ta sẽ lấy giá trị P_t(**/k/**|O) từ đầu ra của DNN tại khung đó.

- Giai đoạn tính toán điẻm phát âm: Đối với mỗi âm vị $p$ đã được xác định bởi Forced Aligner, lấy tất cả các điểm số cấp khung đã được lựa chọn ở bước trước. Các điểm số này sau đó được trung bình hóa trên toàn bộ các khung mà âm vị đó chiếm giữ. Giả sử âm vị **/k/** kéo dài 10 khung từ ($f_1$ đến $f_{10})$, điểm GOP của **/k/** sẽ được tính bằng cách lấy trung bình của $[P_{f1}(/k/|O),...,P_{f10}(/k/|O)]$. 

### 2.3 GOPT-PAII

### 2.4 E2E-R

### 2.5 3MH

---
