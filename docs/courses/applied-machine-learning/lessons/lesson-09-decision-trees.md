---
title: Decision Trees
hide:
---

#<center>Decision Trees</center>
<img class="banner" 
       src="../../../../assets/images/aml_l08_banner.png" 
       alt="">
</img>

## 1. Theoretical Foundations
---

Cây Quyết Định (Decision Tree) là một thuật toán Học Máy có thể thực hiện cả hai tác vụ phân loại và hồi quy, thậm chí là các tác vụ phân loại đa lớp. Thuật toán này rất mạnh mẽ, có khả năng học tốt trên các tập dữ liệu phức tạp. Đặc biệt, Cây quyết định chính là thành phần nền tảng để xây dựng nên mô hình Rừng Ngẫu Nhiên (Random Forest).

### 1.1 Structure of a Decision Tree
---

Cấu trúc của Cây quyết định hình thành dựa trên bản chất của chiến lược chia để trị. Chúng biến một tập dữ liệu phức tạp thành một loạt các quy tắc logic đơn giản thông qua 4 thành phần chính:

<div class="figure-environment">
    <div class="subfigure-container"> <figure class="subfigure">
            <img src="" alt="image01" style="width: 70%; height: auto;">
        </figure>
    </div>
</div>

/// caption
**Hình 1:**.
///

- **Root Node (Nút gốc):** Nắm giữ toàn bộ tập dữ liệu ban đầu. Đây là nơi thuật toán đánh giá và tìm ra đặc trưng (feature) có khả năng phân chia dữ liệu tốt nhất ngay ở bước đầu tiên.
- **Decision Nodes (Nút quyết định):** Các điểm trung gian đánh giá điều kiện. Tại đây, dữ liệu tiếp tục bị xé nhỏ thành các nhóm có tính đồng nhất cao hơn dựa trên các câu hỏi logic.
- **Leaf Nodes (Nút lá):** Điểm dừng cuối cùng. Nút này đưa ra kết luận phân loại tuyệt đối và không thể chia tách thêm.
- **Branches (Nhánh):** Các luồng dữ liệu đại diện cho các điều kiện IF-THEN logic, dẫn hướng dòng chảy của dữ liệu từ gốc đến lá.

Bên trong mỗi Node, thuật toán sẽ tính toán và lưu trữ 3 thuộc tính cốt lõi để theo dõi quá trình phân chia:

- **sample:** Số lượng mẫu dữ liệu huấn luyện hiện đang nằm tại nút đó.
- **value:** Số lượng mẫu tương ứng với từng phân lớp có trong nút.
- **gini:** Điểm số đo lường mức độ pha tạp của nút.

### 1.2 Impurity Measures
---

Để quyết định cách chia tách dữ liệu tốt nhất tại mỗi nút, thuật toán cần một thước đo để định lượng mức độ lộn xộn của dữ liệu. Có hai độ đo phổ biến nhất được sử dụng:

**Gini Impurity (Độ vẩn đục Gini).**
Về mặt học thuật, đây là thước đo đánh giá tần suất một phần tử bị gán nhãn sai nếu chúng được phân loại ngẫu nhiên theo tỷ lệ phân bố nhãn. Tuy nhiên, để dễ hình dung nhất hãy coi Gini là điểm số đo lường mức độ lộn xộn của một nhóm dữ liệu.

- Nếu mọi mẫu trong nút đều thuộc về cùng một lớp duy nhất, nút đó hoàn toàn thuần khiết ($\text{Gini} = 0$).
- Nếu dữ liệu trong nút lộn xộn (ví dụ chia đều 50/50 cho 2 lớp), $\text{Gini}$ sẽ đạt mức tối đa.

Mục tiêu của thuật toán là liên tục chia tách để tìm ra các phân vùng dữ liệu thuần khiết nhất ($\text{Gini}$ tiến về 0). Công thức tính Gini tại một nút như sau:

$$
\begin{equation}
\text{Gini} = 1 - \sum_{i=1}^C p_{i}^2
\end{equation}
$$

Trong đó:

- $C$ là tổng số lớp (nhãn) của bài toán.
- $p_i$ là tỷ lệ (xác suất) các mẫu thuộc về lớp $i$ trong nút đó.

**Entropy Impurity (Độ vẩn đục Entropy).** Bên cạnh Gini, chúng ta có thể sử dụng Entropy - một khái niệm xuất phát từ Lý thuyết Thông tin (Information Theory) của Claude Shannon. Entropy đo lường mức độ bất định (uncertainty) của hệ thống. 

Cũng giống như Gini, Entropy bằng $0$ khi nút hoàn toàn thuần khiết (không có sự bất định vì chắc chắn 100% mẫu thuộc về lớp nào), và đạt giá trị cao nhất khi các lớp phân bố đều nhau. Công thức của Entropy được biểu diễn như sau:

$$
\begin{equation}
\text{Entropy} = - \sum_{i=1}^C p_i \log_2 \left(p_i\right)
\end{equation}
$$

Nhìn chung, Gini và Entropy không tạo ra sự khác biệt quá lớn về mặt cấu trúc cây cuối cùng. Tuy nhiên, chúng có sự khác biệt nhỏ về mặt vi mô tác động đến hiệu suất:

- **Tốc độ tính toán:** Gini là thước đo mặc định trong hầu hết các thư viện (như Scikit-Learn) vì tính toán nhanh hơn. Gini chỉ yêu cầu phép nhân và cộng, trong khi Entropy đòi hỏi tính hàm logarit ($\log_2$), gây tiêu tốn tài nguyên tính toán hơn.
- **Hành vi tạo cây:** Gini có xu hướng cô lập lớp chiếm đa số ra một nhánh riêng biệt. Ngược lại, do tính chất của hàm logarit phạt nặng các sai số nhỏ, Entropy có xu hướng tạo ra các cây cân bằng hơn và thường hoạt động tốt hơn một chút khi đối mặt với các tập dữ liệu mất cân bằng (imbalanced data).

### 1.3 CART Algorithm
---

Classification and Regression Tree (CART) là thuật toán xương sống đằng sau các Cây phân loại và hồi quy.

Đầu tiên, thuật toán sẽ chọn ra một đặc trưng $k$ (ví dụ: *Thu nhập*) và một ngưỡng $t_k$ (ví dụ: *15 triệu*) để chia tập dữ liệu thành hai tập con (Nhánh trái: *Thu nhập $\le$ 15 triệu* và Nhánh phải: *Thu nhập > 15 triệu*). 

CART sẽ quét nghiệm toàn diện để tìm ra cặp $(k, t_k)$ tối ưu nhất sao cho độ vẩn đục của hai tập con sau khi chia là thấp nhất. Lúc này, hàm chi phí (Cost Function) mà thuật toán cần cực tiểu hóa có dạng:

$$
\begin{equation}
J \left(k, t_k\right) = \frac{m_\text{left}}{m} G_\text{left} + \frac{m_\text{right}}{m} G_\text{right}
\end{equation}
$$

Trong đó:

- $G_\text{left/right}$ là độ vẩn đục Gini của nhánh trái/phải.
- $m_\text{left/right}$ là số lượng mẫu của nhánh trái/phải.
- $m$ là tổng số mẫu của nút đang được chia.

Sau khi chia thành công ở nút gốc, CART tiếp tục áp dụng cùng một logic đệ quy để xé nhỏ các tập con thành các nhánh sâu hơn. Quá trình này chỉ dừng lại khi cây đạt đến chiều sâu tối đa (max_depth) hoặc không thể tìm được cách chia nào giúp làm giảm Gini thêm nữa.

Thực chất CART là một thuật toán tham lam (Greedy Algorithm). Chúng chỉ tìm kiếm cách chia tối ưu mang lại điểm Gini thấp nhất ngay tại bước hiện tại (local optimum), mà hoàn toàn không có tầm nhìn xa để tính toán xem liệu cách chia đó có giúp đạt Gini thấp nhất ở các mức sâu phía dưới hay không. Nhờ vậy, thuật toán vận hành rất nhanh, nhưng cái giá phải trả là thường tìm ra một nghiệm đủ tốt chứ không đảm bảo luôn tìm được cấu trúc cây tối ưu tuyệt đối (global optimum).

### 1.4 Parametric vs Nonparametric Models
---

Khi đánh giá cách một thuật toán học từ dữ liệu, chúng ta thường phân loại chúng dựa trên mức độ tự do của cấu trúc mô hình.

**Mô hình tham số (Parametric Models).**
Các mô hình này (ví dụ: Hồi quy tuyến tính) yêu cầu dữ liệu phải tuân theo một phương trình toán học cố định (như $y = ax + b$). Số lượng tham số ($a$ và $b$) được xác định trước khi huấn luyện. Vì cấu trúc bị khóa chặt, chúng rất cứng nhắc và ép mối quan hệ giữa đầu vào và đầu ra phải tuân theo một giả định khắt khe.

**Mô hình phi tham số (Nonparametric Models).**
Ngược lại, Cây quyết định (Decision Tree) đặt rất ít giả định về dữ liệu nền tảng. Chúng được coi là các mô hình phi tham số với những đặc tính cốt lõi sau:

- Không có bất kỳ một dạng hàm toán học định sẵn nào được giả định. Cấu trúc của cây (số lần chia tách, độ sâu, cách bố trí nhánh và các ngưỡng đặc trưng) không được cố định từ trước mà phụ thuộc hoàn toàn vào dữ liệu.
- Độ phức tạp của mô hình được quyết định bởi kích thước tập dữ liệu huấn luyện và không gian đặc trưng. Khi khối lượng dữ liệu tăng lên và phức tạp hơn, cây quyết định sẽ tự động phát triển sâu hơn, phân chia các ngưỡng tinh tế hơn để thích ứng.

Khả năng tự thích ứng sao cho khớp dữ liệu nhất có thể chính là con dao hai lưỡi của Cây quyết định. Nếu không có các ràng buộc nhân tạo, thuật toán sẽ liên tục chẻ nhánh cho đến khi học thuộc lòng từng điểm dữ liệu (bao gồm cả dữ liệu nhiễu). Điều này dẫn đến hiện tượng Overfitting. Do đó, để kiểm soát sức mạnh của mô hình phi tham số, chúng ta bắt buộc phải sử dụng các kỹ thuật giới hạn sự phát triển của cây như regularization (điều chuẩn) hoặc pruning (cắt tỉa).

### 1.5 Regularization in Decision Trees
---

Cây quyết định có xu hướng phát triển độ sâu và độ phức tạp vô hạn để khớp với từng điểm dữ liệu huấn luyện, dẫn đến hiện tượng quá khớp (overfitting). Để ngăn chặn điều này và cải thiện khả năng tổng quát hóa (generalization) của mô hình trên dữ liệu thực tế, chúng ta bắt buộc phải áp dụng các kỹ thuật điều chuẩn (regularization). Đối với Cây quyết định, điều chuẩn thực chất là quá trình cắt tỉa (pruning) để giới hạn sự phát triển của cây.

**Pre-pruning (Cắt tỉa trước).**
Thay vì để cây mọc tự do, chúng ta thiết lập các rào cản kỹ thuật (siêu tham số) ngay từ trước khi thuật toán bắt đầu huấn luyện. Nếu quá trình chẻ nhánh vi phạm các rào cản này, nút đó sẽ buộc phải dừng lại và biến thành nút lá. Ví dụ như giới hạn chiều sâu tối đa của cây (`max_depth`), số mẫu tối thiểu cần có để một nút được phép chẻ nhánh (`min_samples_split`), hoặc số mẫu tối thiểu bắt buộc phải tồn tại ở một nút lá (`min_samples_leaf`).

**Post-pruning (Cắt tỉa sau).**
Trái ngược với pre-pruning, kỹ thuật này cho phép cây phát triển toàn diện đến mức tối đa. Sau đó, thuật toán sẽ đi ngược từ dưới lá lên gốc, đánh giá và chặt bỏ những nhánh cồng kềnh nhưng đóng góp quá ít vào việc giảm sai số. Trong thực tiễn triển khai, quá trình này thường được kiểm soát bằng cách sử dụng tham số phạt độ phức tạp chi phí (`ccp_alpha`).

### 1.6 Decision Tree Regression
---

Như đã đề cập, Decision Tree không chỉ dùng để phân loại mà còn có thể giải quyết các bài toán hồi quy (dự đoán một giá trị liên tục như Giá nhà, Nhiệt độ). Cấu trúc cây vẫn giữ nguyên, nhưng có hai điểm khác biệt cốt lõi về cách đưa ra kết quả và cách lựa chọn đặc trưng $k$ cùng ngưỡng $t_k$ để phân chia dữ liệu:

**Kết quả dự đoán tại nút lá.** 
Thay vì dự đoán một nhãn phân loại, mỗi nút lá trong Cây hồi quy sẽ dự đoán một giá trị số thực. Giá trị này chính là trung bình cộng của tất cả các giá trị mục tiêu $y$ thuộc các mẫu huấn luyện rơi vào nút đó.

$$
\begin{equation}
\hat{y}_{node} = \frac{1}{m_{node}} \sum_{i \in node} y_i
\end{equation}
$$

**Tiêu chí phân chia (Hàm chi phí).** 
Vì không có nhãn phân loại, thuật toán không thể dùng Gini hay Entropy. Thay vào đó, nó sẽ cực tiểu hóa Độ lỗi bình phương trung bình (MSE - Mean Squared Error). Về bản chất, thuật toán cố gắng chia dữ liệu thành các nhóm sao cho các mẫu trong cùng một nhóm có giá trị mục tiêu xấp xỉ nhau (phương sai thấp nhất). Công thức tính MSE tại một nút (đại diện cho độ phân tán của dữ liệu quanh giá trị trung bình):

$$
\begin{equation}
\text{MSE}_{node} = \frac{1}{m_{node}} \sum_{i \in node} (y_i - \hat{y}_{node})^2
\end{equation}
$$

Thuật toán CART sẽ thử mọi đặc trưng $k$ và ngưỡng $t_k$ để tìm ra cách phân tách tối ưu hóa hàm chi phí sau:

$$
\begin{equation}
J\left(k, t_k\right) = \frac{m_\text{left}}{m} \text{MSE}_\text{left} + \frac{m_\text{right}}{m} \text{MSE}_\text{right}
\end{equation}
$$

Chính vì Cây hồi quy đưa ra dự đoán dựa trên giá trị trung bình tại từng vùng dữ liệu độc lập, đường hồi quy mà nó tạo ra không phải là một đường cong liên tục, mà có hình dạng bậc thang rất đặc trưng. 

Tuy nhiên, tương tự như bài toán phân loại, mô hình này đối mặt với rủi ro rất lớn. Nếu không áp dụng các kỹ thuật Điều chuẩn (regularization) hoặc Cắt tỉa (pruning), Cây hồi quy sẽ dễ dàng rơi vào trạng thái overfitting tự do phân nhánh và uốn nắn cấu trúc bậc thang của nó để đi qua chính xác từng điểm dữ liệu nhiễu.

## 2. Implementation
---

```python
#todo
```

## 3. Assessment
---

**Question 1.** Độ pha tạp Gini của nút con thường thấp hơn hay cao hơn độ pha tạp Gini của nút cha?

**Question 2.** Nếu việc huấn luyện cây quyết định trên tập dữ liệu chứa 1 triệu mẫu mất một tiếng, sẽ mất khoảng bao lâu để huấn luyện một cây quyết định khác trên tập huấn luyện chứa 10 triệu mẫu?

**Question 3.** Nếu cây quyết định đang underfitting thì có nên thử co giãn đặc trưng đầu vào không?


## 4. FAQs
---

<u>^^FAQ 1.^^</u>

**Q: Mô hình Decision Trees có tinh chỉnh được không?**

**A:** Về bản chất, cây quyết định không có khả năng học tăng cường nội tại. Điều này có nghĩa là chúng không thể dễ dàng được tinh chỉnh hoặc cập nhật thêm kiến thức khi có dữ liệu mới giống như các thuật toán khác. Bất kì có sự thay đổi nào về mô hình hoặc dữ liệu, mô hình Decsion Trees đều phải huấn luyện lại toàn bộ cây từ đầu. Để hiểu rõ tại sao mô hình này lại thiếu đi sự linh hoạt, chúng ta cần xem xét lại cơ chế hoạt động và những đặc thù giới hạn cốt lõi của chúng:

**Cơ chế hoạt động nền tảng.** Cây quyết định là một mô hình phân cấp. Qúa trình xây dựng cây bao gồm:

- Lựa chọn đệ quy đặc trưng (hoặc ngưỡng đặc trưng) tốt nhất để chia nhỏ dữ liệu tại mỗi nút nhằm đạt độ thuần khiết cao nhất.

- Dừng sự phát triển của cây khi đạt đến các tiêu chí nhất định (độ sâu tối đa, số mẫu tối thiểu, hoặc nút đã hoàn toàn thuần khiết).

- Gán nhãn phân loại (hoặc giá trị hồi quy) tại các nút lá.

**Đặc thù cốt lõi.**

- Quyết định chia tách dữ liệu ở đâu và cấu trúc cây như thế nào được chốt ngay trong quá trình huấn luyện ban đầu. Một khi cây đã hoàn thành xong, cấu trúc này bị khoá cứng, khiến việc cập nhật dữ liệu mới mà không phải huấn luyện lại từ đầu là điều bất khả thi.

- Mô hình phi tham số không có cấu trúc hay số lượng tham số cố định. Chúng phát triển hoàn toàn dựa trên dữ liệu. Nếu thêm dữ liệu vào, phân phối của các đặc trưng sẽ thay đổi, đòi hỏi phải thay đổi cả các ngưỡng chia và toàn bộ cấu trúc tổng thể của cây. Việc can thiệp sửa đổi một cấu trúc đã đóng băng là quá phức tạp và rủi ro.

- Bản chất Decision Trees xây dựng cây một cách tham lam, chúng chỉ chọn cách chia tốt nhất ngay tại thời điểm hiện tại ở một nút cụ thể, mà không hề tính toán đến tương lai. Nếu dữ liệu mới chỉ ra rằng cần có một phép chia tốt hơn ở các tầng bên trên, thuật toán không có cơ chế hoàn tác để quay lại sửa chữa các quyết định cũ. 

- Khi có dữ liệu mới, không thể chỉ đơn giản là đắp dữ liệu vào cây cũ. Các mốc chia cắt tối ưu cho dữ liệu mới có thể hoàn toàn khác biệt so với cây hiện tại. Nếu có tình ép dữ liệu mới vào, mô hình sẽ đưa ra những dự đóan sai lệch. Do đó, giải pháp duy nhất và an toàn nhất là đập bỏ mô hình cũ và huấn luyện lại từ đầu.

<u>^^FAQ 2.^^</u>

**Q: Tại sao mô hình Decision Trees không yêu cầu chuẩn hóa hay thu phóng dữ liệu?**

**A:** Mô hình Decision Trees không yêu cầu chuẩn hóa hoặc thu phóng dữ liệu vì chính cách chúng phân chia dữ liệu và đưa ra quyết định. Khác với các mô hình ML khác, cây quyết định không phụ thuộc vào độ lớn hoặc phân phối của các đặc trưng đầu vào để đưa ra dự đoán. Cụ thể:

- **Phân chia dựa trên ngưỡng tương đối:** Cây quyết định đánh giá từng đặc trưng một cách độc lập, chọn một giá trị ngưỡng để phân tách. Quá trình này hoàn toàn dựa trên các phép so sánh tương đối (ví dụ: lớn hơn, nhỏ hơn) giữa các giá trị đặc trưng, chứ không phải độ lớn tuyệt đối của chúng.
- **Miễn nhiễm với thang đo:** Vì sử dụng các ngưỡng để chẻ dữ liệu, thang đo hay khoảng giá trị thực tế của đặc trưng không ảnh hưởng đến thuật toán. Ví dụ, đặc trưng "thu nhập" dù được đo bằng đô la, hàng nghìn hay hàng triệu đô, cây quyết định vẫn sẽ tìm ra cùng một ngưỡng phân tách dữ liệu tốt nhất.
- **Không tính toán khoảng cách/Gradient:** Trong các mô hình như Hồi quy tuyến tính, KNN hay SVM, các giá trị đặc trưng lớn có thể lấn át giá trị nhỏ, buộc ta phải chuẩn hóa để các biến đóng góp bình đẳng. Ngược lại, Cây quyết định xử lý từng trục tọa độ hoàn toàn độc lập nên khoảng giá trị lớn/nhỏ không thể lấn át lẫn nhau.
- **Bản chất phi tham số (Non-parametric):** Cây quyết định không đưa ra bất kỳ giả định nào về hình dáng phân phối của dữ liệu (như phân phối chuẩn). Do đó, chúng hoạt động cực kỳ hiệu quả và tự nhiên ngay cả khi các đặc trưng đầu vào có sự lệch chuẩn hay sở hữu các khoảng giá trị hoàn toàn khác biệt.

<u>^^FAQ 3.^^</u>

**Q: Tại sao Decision Trees hiếm khi được sử dụng đơn lẻ?**

**A:** Cây quyết định, mặc dù trực quan và mạnh mẽ, nhưng hiếm khi được sử dụng đơn lẻ trong thực tế do những hạn chế cố hữu. Thay vào đó, các phương pháp học tập kết hợp (ensemble methods) được ưu tiên hơn vì chúng giải quyết triệt để những hạn chế mà Decision Trees gặp phải.

- Hiện tượng Overfitting: Cây quyết định rất dễ bị quá khớp, đặc biệt là khi chúng sâu và phức tạp. Một cây quyết định phát triển tối đa có thể khớp hoàn hảo với dữ liệu huấn luyện bằng cách tạo ra nhiều phép chia để chứa nhiều biến thể nhỏ trong dữ liệu, bao gồm cả nhiễu và các điểm dị biệt. Mặc dù điều này mang lại sai số huấn luyện rất thấp, nhưng lại dẫn đến khả năng tổng quát hoá kém trên dữ liệu chưa từng gặp.
- Phương sai cao trong cây quyết định: Cây quyết định có xu hướng phương sai cao, nghĩa là dự đoán của chúng có thể dao động dáng kể chỉ với những thay đổi nhỏ trong dữ liệu. Điều này xảy ra vì mỗi cây được xây dựng bằng cách chọn các phép chia đặc trưng tốt nhất một cách tham lam, do đó một sự thay đổi nhẹ trong dữ liệu có thể dẫn đến một cấu trúc cây hoàn toàn khác.
- Sự đánh đổi Bias-Variance: Cây quyết định có thể bị quá khớp (phương sai cao) hoặc chưa khóp (thiên lệch cao) tuỳ thuộc vào độ sâu của chúng. Cây nông dễ bị underfit vì không nắm bắt được các mối quan hệ phức tạp, trong khi câu sâu lại overfit vì học cả dữ liệu nhiễu.
- Hiệu suất kém trên dữ liệu phức tạp: Các cây đơn lẻ thường chật vật với các tập dữ liệu phức tạp, đăc biệt khi có sự tương tác chéo giữa các đặc trưng. Thuật toán phân chia dữ liệu bằng cách sử dụng từng đặc trưng một, làm cho chúng kém mạnh mẽ khi đối mặt với các tương tác phức tạp.
- Thiếu ổn định: Sự thay đổi nhỏ trong dữ liệu dẫn đến sự thay đổi lớn trong cấu trúc. Điều này làm cho mô hình khó được tin tưởng khi áp dụng vào thực tế.
- Không thể diễn giải ở các cây sâu: Cây nông thì dễ hiểu, nhưng với cây sâu hàng nghìn nút phân chia sẽ trở thành một hộp đen, gây khó khăn cho việc giải thích logic với các đặc trưng liên quan.

## 5. Resources
---

1. **Blog &. Web**

    1. [Decision Trees](https://machinelearningcoban.com/2018/01/14/id3/).

    2. [Mô hình cây quyết định](https://phamdinhkhanh.github.io/deepai-book/ch_ml/DecisionTree.html).

    3. [Decision Tree Classification Algorithm](https://www.tpointtech.com/machine-learning-decision-tree-classification-algorithm).

    4. [Decision Trees](https://bradleyboehmke.github.io/HOML/DT.html).

