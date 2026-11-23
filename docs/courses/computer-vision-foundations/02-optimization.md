---
title: Optimization
tags:
  - deep leanring
  - adam
  - gradient-descent
  - classification
  - cervical cancer cytology
---

# </center>Optimization</center>

## Premilinaries

Hàm mất mát của mô hình phụ thuộc hoàn toàn vào các tham số của mô hình vì việc tìm ra các tham số làm cho hàm mất mát đạt giá trị nhỏ nhất là bài toán cần được giải quyết. Nói một cách đơn giản quá trình tối ưu hoá mô hình có thể mô tả qua hai bước:

- Tính toán đạo hàm (derivatives) của hàm loss liên quan đến các tham số.
  
- Cập nhật tham số dựa vào gradients để làm hàm chi phí nhỏ lại.

Các bước này được lặp đi lặp lại và chúng ta hi vọng rằng có thể tìm thấy một cực tiểu toàn cục khiến cho hàm loss đạt giá trị nhỏ nhất.

## Gradient Descent

Để dữ liệu có thể khớp với mô hình, giả sử ta có một training set $(\mathbf{x}_i, \mathbf{y}_i)$ là các cặp input/output. Ta cần tìm bộ tham số $\phi$ cho mô hình $\mathbf{f}[\mathbf{x}_i, \phi]$ để ánh xạ đầu vào $\mathbf{x}_i$ tới giá trị đầu ra $\mathbf{y}_i$. Hàm mất mát $L[\phi]$ của mô hình trả về giá trị sai số của mô hình. Mục tiêu của thuật toán tối ưu là tìm kiếm bộ tham số $\phi$ để cho hàm loss đạt giá trị nhỏ nhất:

$$
\begin{equation}
\hat{\phi} = \mathop{\operatorname{argmin}}_{\phi} \bigl[L[\phi]\bigr]
\end{equation}
$$

Có rất nhiều thuật toán tối ưu hoá, nhưng đa số chúng dều có xu hướng tìm kiếm bằng việc lặp đi lặp lại trong qúa training. Một phương pháp đơn gỉan nhất trong số này đó là **gradient descent**. Về cơ bản thuật toán này sẽ lặp đi lặp lại 2 bước với bộ tham số khởi tạo $\phi = [\phi_0, 
\phi_1, \dots, \phi_N]^{T}$

- **Step 1.** Tính toán đạo hàm của loss với các tham số:
  
$$
\begin{equation}
\frac{\partial L}{\partial \phi} = 
\begin{bmatrix}
\frac{\partial L}{\partial \phi_0} \\[1.5ex]
\frac{\partial L}{\partial \phi_1} \\[1.5ex]
\vdots \\[1.5ex]
\frac{\partial L}{\partial \phi_N}
\end{bmatrix}
\end{equation}
$$

- **Step 2.** Cập nhật các tham số bằng rule:

$$
\begin{equation}
\phi_j \leftarrow \phi_j - \alpha \cdot \frac{\partial L}{\partial \phi_j}; \quad \text{với}~j \in \{0, 1\}
\end{equation}
$$

Trong đó $\alpha$ là một số dương vô hướng xác định mức độ cập nhật của tham số. Đầu tiên ta sẽ tính toán gradient của loss function ở vị trí hiện tại, điều này xác định độ lớn (độ cao) của chúng. Sau đó, di chuyển một khoảng cách nhỏ $\alpha$ để đẩy loss xuống dốc. Tham số $\alpha$ này chính là **learning rate**. Trong quá trình training chúng có thể cố định hoặc có thể thay đổi tuỳ thuộc vào chiến luọc tinh chỉnh nhằm tìm ra một gía trị giúp cho loss fucntion tốt nhất.

## Gradient Descent for Linear Regression

Trong bài toán hồi quy tuyến tính với dữ liệu là 1D mô hình $\mathbf{f}[x, \phi]$ ánh xạ dầu vào vô hướng $x$ thành đầu ra vô hướng $y$ với vector tham số $\phi = [\phi_0, \phi_1]^T$ lần lượt là **intercept** (hệ số chặn) và **slope** (hệ số góc):

$$
\begin{equation}
y = \mathbf{f}[x, \phi] = \phi_0 + \phi_1 x
\end{equation}
$$

Hàm loss của Linear Regression được biểu diễn bằng tổng sai số bình phương của $I$ điểm dữ liệu $\{x_i, y_i\}$:

$$
\begin{equation}
\begin{align*}
L[\phi] = \sum_{i=1}^I l_i 
&= \sum_{i=1}^I \left(\mathbf{f}[x_i, \phi] - y_i\right)^2 \\
&= \sum_{i=1}^{I} (\phi_0 + \phi_ix_1 - y_i)^2
\end{align*}
\end{equation}
$$

Đạo hàm của toàn bộ hàm loss (gradient) chính là tổng đạo hàm riêng của từng mẫu dữ liệu:

$$
\begin{equation}
\frac{\partial L}{\partial \phi} = \sum_{i=1}^{I} \frac{\partial l_i}{\partial \phi}
\end{equation}
$$

Đạo hàm riêng của từng mẫu dữ liệu theo vector tham số $\phi$ được tính bởi:

$$
\begin{equation}
\frac{\partial l_i}{\partial \phi} =
\begin{bmatrix}
\frac{\partial l_i}{\partial \phi_1} \\[1.5ex]
\frac{\partial l_i}{\partial \phi_1}
\end{bmatrix} =
\begin{bmatrix}
2(\theta_0 + \theta_1x_i - y_i) \\[1.5ex]
2x_i(\theta_0 + \theta_1x_i - y_i) \\
\end{bmatrix}
\end{equation}
$$

**Chain Rule - Đạo hàm theo quy tắc chuỗi.** Đặt $u = (\theta_0 + \theta_1x_i - y_i)$, khi đó $l_i = u^2$. Theo quy tắc chuỗi, đạo hàm của $u^2$ theo một biến $j$ là: $\frac{\partial (u^2)}{\partial j} = 2u \cdot \frac{\partial u}{\partial j}$. Vì vậy:

- Đạo hàm của $u$ theo $\phi_0$ sẽ bằng 1.
  
- Đạo hàm của $u$ theo $\phi_1$ sẽ bằng $x_i$.

Thế vào ta thu được công thức 7. Sau khi có vector gradient tổng $\frac{\partial L}{\partial \phi}$, thuật toán gradient descent sẽ cập nhật từng tham số độc lập theo công thức 3.

## Convex Problems

Hàm chi phí (loss function) của mô hình hồi quy tuyến tính luôn luôn có một điểm cực tiểu duy nhất (global minimum). Về bản chất, đạo hàm của hồi quy tuyến tính có hình dạng giống như một chiếc bát (hàm lồi - convex). Dù cho các tham số có được khởi tạo ngẫu nhiên ở bất kỳ vị trí nào, thuật toán tối ưu cũng sẽ luôn hội tụ về đáy của chiếc bát đó.

Tuy nhiên, hàm loss của các mô hình phi tuyến (bao gồm cả mạng nơ-ron nông và mạng nơ-ron sâu) lại không may mắn như vậy, vì chúng không phải là hàm lồi (non-convex).

Hãy tưởng tượng rằng, hình dáng hàm chi phí của các mô hình **phi tuyến** giống như các ngọn núi cao thấp nhấp nhô được xếp sát nhau. Việc tìm kiếm nghiệm tối ưu lúc này là một bài toán cực kỳ khó khăn vì bề mặt này chứa rất nhiều điểm cực tiểu địa phương (local minimum) và các điểm yên ngựa (saddle points). 

Ba khái niệm cơ bản cần phân biệt:

*   **Global Minimum (Cực tiểu toàn cục):** Đây là điểm thấp nhất trên toàn bộ bề mặt tối ưu. Đây là đích đến lý tưởng nhất của quá trình huấn luyện.
  
*   **Local Minimum (Cực tiểu địa phương):** Đây là những điểm trũng nằm trên sườn núi. Tại đó, nó thấp hơn tất cả các điểm xung quanh, nhưng không phải là điểm thấp nhất của toàn bộ bề mặt. Thuật toán rất dễ bị kẹt tại đây.
  
*   **Saddle Points (Điểm yên ngựa):** Đây là một điểm đặc biệt. Trong không gian 2D, nó giống như trung tâm của một chiếc cầu trượt bốn hướng (hai hướng dốc lên và hai hướng dốc xuống). Tại điểm này, đạo hàm bằng 0, nhưng nó không phải là điểm cực tiểu (vì có hướng vẫn dốc xuống) cũng không phải là cực đại (vì có hướng vẫn dốc lên). Trong không gian đa chiều của mạng Nơ-ron, Saddle Points xuất hiện thường xuyên hơn rất nhiều so với Local Minimum.

## Stochastic, Batch and Mini-Batch Gradient Descent

Với các mô hình đơn giản có ít tham số, chúng ta có thể tìm được global minimum thông qua hai cách tiếp cận cơ bản:

- **Grid Search / Random Search:** Tìm kiếm vét cạn hoặc ngẫu nhiên các giá trị tham số trên không gian tối ưu.
  
- **Random Restarts:** Lặp đi lặp lại quá trình khởi tạo Gradient Descent tại nhiều vị trí xuất phát khác nhau, sau đó chọn ra bộ tham số mang lại giá trị hàm loss nhỏ nhất.

Tuy nhiên, mạng nơ-ron sâu có tới hàng triệu, thậm chí hàng tỷ tham số, việc tiếp cận theo cách trên là hoàn toàn không khả thi. Việc sử dụng Gradient Descent để tìm kiếm cực tiểu toàn cục cho hàm loss trong không gian đa chiều là một thách thức lớn.

**Batch Gradient Descent (BGD).** 
Giả sử ta có một tập dữ liệu gồm $\operatorname{I}$ mẫu. BGD chính là việc tính đạo hàm và cập nhật trọng số một lần duy nhất trên toàn bộ tập dữ liệu. Do được tính đạo hàm trên toàn bộ dữ liệu nên đường đi của thuật toán là hoàn toàn xác định. Tuy nhiên, nếu không may rơi vào một điểm local minimum, chúng sẽ bị kẹt ở đó mãi mãi. Thuật toán chỉ biết đi xuống, không thể tự nhảy ra ngoài để tìm đến những vùng trũng sâu hơn.

**Stochastic Gradient Descent (SGD) và Mini-batch GD.** 
Phương pháp này khắc phục hạn chế của BGD bằng việc chỉ tính đạo hàm trên một mẫu dữ liệu duy nhất (SGD thuần túy) hoặc một nhóm nhỏ dữ liệu (mini-batch). Vì chỉ nhìn vào một phần nhỏ dữ liệu nên hướng đi được tính toán chỉ là ước lượng gần đúng. Trong các mẫu dữ liệu này có thể chứa nhiễu (noise).

Nhìn chung về tổng thể, hướng di chuyển của đạo hàm vẫn là đi xuống dốc. Nhưng ở từng bước cập nhật, do chứa nhiễu nên đường đi của chúng không bằng phẳng mà sẽ **zig-zag**. Điều này vô tình lại là một điều có lợi, giúp cho thuật toán đang bị kẹt ở một local minimum có thể thoát ra khỏi điểm đó để rơi xuống một hố sâu hơn, và mang lại hy vọng tìm được global minimum.

**Batches and Epoch Concept.** 
Tại mỗi một lần lặp iteration $(t)$, thuật toán lựa chọn ra một tập con ngẫu nhiên (minibatch) từ tập dữ liệu huấn luyện và tính toán đạo hàm trên toàn bộ mẫu thuộc tập con này. Với mỗi subset, tham số $\phi$ của model được cập nhật tại vòng lặp thứ $t$ là:

$$
\begin{equation}
\phi_{t+1} \leftarrow \phi_t - \alpha \cdot \sum_{i \in \mathcal{B}_t} \frac{\partial \ell_i[\phi_t]}{\partial \phi}
\end{equation}
$$

Trong đó:
- $\mathcal{B}_t$ là tập hợp chứa chỉ số (indices) của các cặp dữ liệu trong batch hiện tại $(t)$.
  
- $\ell_i$ là giá trị loss của mẫu dữ liệu thứ $(i)$.
   
- $\sum_{i \in \mathcal{B}_t} \ell_i$ chính là loss của toàn bộ mini-batch.

Các batch thường được lấy mẫu không hoàn lại (without replacement) - tức là không trùng lặp. Thuật toán sẽ duyệt qua các mẫu cho đến khi sử dụng hết toàn bộ dữ liệu, sau đó mới xáo trộn và bắt đầu lấy mẫu lại từ đầu. Mỗi một lượt mô hình di qua hết toàn bộ tập training được gọi là một **epoch**.

**Features of SGD.**

- **Hiệu quả & Tổng quát hóa:** Tính đạo hàm trên mini-batch giúp tiết kiệm chi phí tính toán so với việc dùng toàn bộ dữ liệu. Dù có nhiễu, các bước cập nhật vẫn có ý nghĩa, và thực tế chứng minh mô hình dùng SGD thường khái quát hóa (generalization) tốt hơn trên dữ liệu mới.

- **Vượt qua các bẫy của hàm Loss:** Yếu tố nhiễu giúp mô hình thoát khỏi các hố lõm nông (Local Minimum). Tại điểm yên ngựa (Saddle Point) nơi gradient toàn cục bằng 0, xác suất để một batch ngẫu nhiên có gradient lớn vẫn rất cao, tạo cú hích giúp mô hình tiếp tục di chuyển.
  
- **Tính công bằng & Hội tụ thực tế:** Việc bốc mẫu không hoàn lại trong 1 epoch đảm bảo mọi dữ liệu đều đóng góp công bằng. SGD không hội tụ tuyệt đối (đứng yên hoàn toàn) do nhiễu, nhưng khi gần đáy, gradient rất nhỏ khiến tham số dần ổn định và thường tìm được các Local Minimum rất tốt (gần Global Minimum).
  
- **Lịch trình Tốc độ học (Learning Rate Schedule):** Tốc độ học $\alpha$ thường giảm dần theo thời gian. Giai đoạn đầu giữ $\alpha$ cao để khám phá (explore) các vùng trũng hợp lý; giai đoạn sau giảm $\alpha$ thấp để tinh chỉnh (fine-tune) tham số quanh vùng tối ưu.