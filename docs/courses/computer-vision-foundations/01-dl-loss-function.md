---
title: Loss Function in Deep Learning
icon: material/numeric-2
tags:
  - classification
  - cross-entropy
  - focal-loss
  - deep-learning
  - likelihood
---

#<center>Lesson xxx. Loss Functions Theory</center>
<img class="banner" 
       src="../../../../assets/images/dl_lxx_loss_function.png" 
       alt="Loss Function in Deep Learning">
</img>

## Concepts
---
Giả sử ta có một mẫu dữ liệu training $\{x_i, y_i\}$ là một cặp $\{\text{input}, \text{output}\}$. Hàm **loss function** (hàm mất mát) hay **cost function** (hàm chi phí) kí hiệu là $L[\phi]$ trả về một giá trị duy nhất. Giá trị này phản ánh sai số giữa giá trị dự đoán $\textbf{f}[x_i, \phi]$ và nhãn thật (ground-truth) tương ứng $y_{i}$. Training model (huấn luyện mô hình), chính là quá trình mà chúng ta đi tìm kiếm các parameters $\phi$ sao cho hàm mất mát đạt giá trị nhỏ nhất, tức là giá trị dự đoán phải sát với giá trị thực tế.

## 🚀 Maximum likelihood
---
Xét mô hình $\textbf{f}[\textbf{x}, \phi]$ với tham số $\phi$ học được từ dữ liệu huấn luyện. Ta xem mô hình là thứ tính phân phối xác suất $\text{Pr}(y|x)$ với mỗi đầu vào $x$, chúng chấm điểm xác suất cho từng câu trả lời $y$. Hàm mất mát phạt mô hình khi xác suất dành cho nhãn đúng $y$ còn thấp và tối thiểu hóa loss tương đương kéo xác suất đó lên cao.

Câu hỏi được đặt ra là **"Làm thế nào để output của mạng $\textbf{f}(\textbf{x}, \phi)$"  ta dựng được phân phối xác suất?"**. Việc cần làm đầu tiên là ta cần chọn họ phân phối $\text{Pr}(y|\theta)$ phù hợp với miền đầu ra $y$, việc này giống như việc bạn chọn hàm loss trong thư viện (mse, cross-entropy...). Sau đó dùng mạng neural để tính $\theta$ từ $x$. Ví dụ đầu ra là số thực $(y \in \mathbb{R})$, ta sẽ chọn phân phối được đinh nghĩa bởi mean $\mu$ và phương sai $\sigma$, nên $\theta = \{\mu, \sigma\}$. Mô hình sẽ dự đoán $\mu$, còn $\sigma$ coi là hằng số chưa biết. 

Mạng sinh ra một bộ tham số phân phối riêng cho từng mẫu $\theta_i = \textbf{f}[x_i, \phi]$. Với mỗi mẫu, nhãn thật $y_i$ phải có xác suất cao dưới phân phối riêng đó. Vì vậy, ta cần chỉnh trọng số mạng $\phi$ sao cho tích xác suất của toàn bộ mẫu $\textbf{I}$ là lớn nhất:

$$
\begin{equation}
\begin{aligned}
\hat{\phi} &= \mathop{\operatorname{argmax}}_{\phi} \left[ \prod_{i=1}^{I} \Pr\left(y_i \mid x_i\right) \right] \\
&= \mathop{\operatorname{argmax}}_{\phi} \left[ \prod_{i=1}^{I} \Pr\left(y_i \mid \theta_i\right) \right] \\
&= \mathop{\operatorname{argmax}}_{\phi} \left[ \prod_{i=1}^{I} \Pr\left(y_i \mid \mathbf{f}[x_i, \phi]\right) \right]
\end{aligned}
\end{equation}
$$

**Công thức 1** chính là **likelihood** của các tham số, hay được gọi là **maximum likelihood** (tiêu chuẩn hợp lý cực đại). Một điều nên nhớ rằng, muốn nhân được các xác suất mẫu với nhau, phải giả định chúng cùng dạng phân phối và độc lập có điều kiện **(independent and identically distributed - i.i.d)**.

## 🍕 Maximum log-likelihood
---
Trong thực tế, việc tối đa hoá trực tiếp tích các xác suất theo công thức **5.1** là không tối ưu. Vì mỗi xác suất $\Pr(y_i|\mathbf{f}[x_i,\phi])$ đều nằm trong khoảng $[0,1]$, tích của chúng trên toàn bộ tập dữ liệu sẽ rất nhỏ. Điều này khiến việc biểu diễn đại lượng này bằng số học độ chính xác hữu hạn trở nên khó khăn hơn (dễ underflow về 0). Vì vậy, trong thực tế ta tối đa hoá logarit của likelihood thay vì chính likelihood. Hai bài toán tương đương chính xác vì log là hàm đơn điệu tăng, nên vị trí cực đại không đổi:

$$
\begin{equation}
\begin{aligned}
\hat{\phi} &= \mathop{\text{argmax}}_{\phi} \left[ \prod_{i=1}^{I} \Pr(y_i \mid \mathbf{f}[x_i,\phi]) \right] \\
&= \mathop{\text{argmax}}_{\phi} \left[ \log \left[ \prod_{i=1}^{I} \Pr(y_i \mid \mathbf{f}[x_i,\phi]) \right] \right] \\
&= \mathop{\text{argmax}}_{\phi} \left[ \sum_{i=1}^{I} \log \left[ \Pr(y_i \mid \mathbf{f}[x_i,\phi]) \right] \right]
\end{aligned}
\end{equation}
$$
     
Vì $\log(a \cdot b) = \log(a) + \log(b)$, tích trong **công thức 5.2** được khai triển thành tổng trong công thức (5.3). Việc dùng log cũng làm cho việc tính đạo hàm trở nên đơn giản hơn, vì ta làm việc với một chuỗi các phép cộng thay vì phép nhân.

## 🎸 Negative log-likelihood
---
Theo quy ước, để mô hình đạt hiệu suất tối ưu ta cần tối thiểu hoá hàm mất mát. Vì vậy, bài toán **maximum log-likelihood** có thể được chuyển thành bài toán **minimizing negative log-likelihood** bằng cách nhân với $-1$:

$$
\begin{equation}
\begin{aligned}
\hat{\phi} &= \mathop{\operatorname{argmin}}_{\phi} \bigl[ -\sum_{i=1}^{I} \log \bigl[ \Pr(y_i \mid \mathbf{f}[x_i,\phi]) \bigr] \bigr]
\end{aligned}
\end{equation}$$

## 🐱 Inference
---
Các mô hình không đưa ra trực tiếp giá trị dự đoán $y$, thay vào đó, chúng thường trả về một phân phối xác suất trên các giá trị mà $y$ có thể nhận. Trong thực tế, người dùng thường mong muốn nhận ngay một giá trị dự đoán cố định thay vì cả phân phối xác suất. Điều này đồng nghĩa với việc chọn giá trị $y$ có xác suất lớn nhất:

$$
\hat{y} = \mathop{\text{argmax}}_{y} \left[ \Pr(y \mid \mathbf{f}[x_i,\hat{\phi}]) \right]
$$

## 🎨 Binary Cross-Entropy
---
Trong bài toán **binary classification** (phân loại nhị phân), đầu ra của một dữ liệu $x$ luôn thuộc một trong hai lớp $y \in \{0,1\}$. Trong xác suất thống kê, ta dùng phân phối **Bernoulli** để biểu diễn vì $y$ chỉ nhận giá trị trong miền $\{0,1\}$. Tham số $\lambda$ của phân phối Bernoulli biểu diễn xác suất để $y=1$.

$$
\begin{equation}
\Pr(y \mid \lambda) =
\begin{cases}
1 - \lambda, & y = 0, \\
\lambda, & y = 1.
\end{cases}
\end{equation}
$$

**Công thức 4** tương đương với:

$$
\begin{equation}
\Pr(y \mid \lambda) = (1-\lambda)^{1-y} \cdot \lambda^{y}
\end{equation}
$$

Mô hình $\mathbf{f}[x,\phi]$ cho ra một giá trị có thể là số thực bất kỳ. Tuy nhiên, tham số phân phối $\lambda$ chỉ có thể nằm trong khoảng $[0,1]$, và ta không thể đảm bảo đầu ra của mô hình luôn nằm trong khoảng này. Do đó, ta đưa đầu ra của mô hình qua một hàm ánh xạ số thực $\mathbb{R}$ về khoảng $[0,1]$. Hàm này là **logistic sigmoid**:

$$
\begin{equation}
\operatorname{sig}[z] = \frac{1}{1 + \exp[-z]}
\end{equation}
$$

Vì vậy, ta dự đoán tham số phân phối là $\lambda = \operatorname{sig}[\mathbf{f}[x,\phi]]$. Công thức likelihood bây giờ có dạng:

$$
\begin{equation}
\Pr(y \mid x;\phi)
=
(1 - \operatorname{sig}[\mathbf{f}[x,\phi]])^{1-y}
\cdot
\operatorname{sig}[\mathbf{f}[x,\phi]]^{y}
\end{equation}
$$

Hàm mất mát trên toàn bộ tập dữ liệu huấn luyện là **negative log-likelihood**:

$$
\begin{equation}
L[\phi]
=
\sum_{i=1}^{I}
\bigl[
-(1-y_i) \log \left(1-\operatorname{sig}[\mathbf{f}[x_i,\phi]]\right)
-
y_i\log\left(\operatorname{sig}[\mathbf{f}[x_i,\phi]]\right)
\bigr]
\end{equation}
$$

Công thức (5.9) chính là hàm **binary cross-entropy loss**. Đầu ra $\operatorname{sig}[\mathbf{f}[x,\phi]]$ dự đoán tham số $\lambda$ của phân phối Bernoulli, tức xác suất $y=1$, do đó $1-\lambda$ là xác suất $y=0$. Khi thực hiện suy luận, nếu cần một điểm dự đoán, ta đặt $\hat{y}=1$ nếu $\lambda > 0.5$ và $\hat{y}=0$ nếu ngược lại.

## ⚡ Cross-Entropy
---
Không giống với binary classification, mục tiêu của multi-class classification (phân loại đa lớp) với một mẫu dữ liệu $x$ là gán $x$ vào một trong $K>2$ lớp, tức $y \in \{1,2,\dots,K\}$. 

Với bài toán phân loại đa lớp, ta lựa chọn **categorical distribution** để mô hình hoá nhãn thay vì sử dụng phân phối Bernoulli. Lúc này có $K$ tham số $\lambda_1,\lambda_2,\dots,\lambda_K$ tương ứng với xác suất của từng nhãn. Các tham số này không chỉ nằm trong khoảng $[0,1]$ mà tổng của chúng phải bằng $1$ để đảm bảo là một phân phối xác suất hợp lệ. Tuy nhiên, tương tự như binary classification, ta không thể đảm bảo mô hình sẽ trả về các giá trị tuân theo phân phối đã chọn. Vì vậy, ta cần một hàm ép các giá trị thô đầu ra của mô hình thành các phần tử trong khoảng $[0,1]$ và có tổng bằng $1$. Hàm này là **softmax**:

$$
\begin{equation}
\operatorname{softmax}_{k}[z]
=
\frac{\exp[z_k]}{\sum_{j=1}^{K}\exp[z_j]}
\end{equation}
$$

Likelihood của $\phi$ khi giá trị $y=k$ từ đầu vào $x$ có dạng là:

$$
\begin{equation}
\Pr(y=k \mid x)
=
\operatorname{softmax}_{k}\bigl[\mathbf{f}[x,\phi]\bigr].
\end{equation}
$$

Hàm mất mát lúc này là negative log-likelihood trên toàn bộ tập dữ liệu huấn luyện:

$$
\begin{equation}
\begin{aligned}
L[\phi]
&=
-\sum_{i=1}^{I}
\log\left[
\operatorname{softmax}_{y_i}\bigl[\mathbf{f}[x_i,\phi]\bigr]
\right] \\
&=
-\sum_{i=1}^{I}
\left[
\text{f}_{y_i}[x_i,\phi]
-
\log\left[
\sum_{j=1}^{K}\exp\bigl[\text{f}_j[x_i,\phi]\bigr]
\right]
\right]
\end{aligned}
\end{equation}
$$

**Công thức 11** chính là **multi-class cross-entropy loss**. Trong quá trình inference để lấy giá trị dự đoán cuối cùng ta chọn lớp có xác suất lớn nhất với $\hat{y}=\mathop{\operatorname{argmax}}_{k}\Pr(y=k \mid x;\hat{\phi})$

## 🏖️ Focal Loss
---

<div class="figure-environment">
    <div class="subfigure-container">
        <figure class="subfigure">
            <img src="../../../../assets/images/dl_lxx_focal_loss.png" alt="">
        </figure>
    </div>
</div>

/// caption
**Hình 1:** Biều đồ hàm Focal Loss khi training với nhiều hệ số $\lambda$ khác nhau.
///

**Hạn chế của Cross-Entropy.** Cross-entropy đối xử công bằng với mọi mẫu,
gây vấn đề khi dữ liệu mất cân bằng:

- **Mẫu dễ áp đảo**: số lượng lớn easy negatives (ví dụ background trong
  object detection) cộng dồn loss lớn, lấn át tín hiệu từ mẫu khó.
- **Mẫu khó bị chìm**: gradient từ mẫu khó bị pha loãng bởi tổng gradient
  từ vô số mẫu dễ.

Focal Loss (Lin et al., 2017) giải quyết bằng cách **giảm trọng số mẫu dễ**,
giúp mô hình **tập trung học mẫu khó**.

Công thức tổng quát:

$$
\text{FL}(p_t)=-\alpha_t\,(1-p_t)^{\gamma}\log(p_t)
$$

Trong đó:

- $p_t$ là xác suất mô hình gán cho **lớp đúng** ($p_t=p$ nếu $y=1$. Nếu $p_t=1-p$ nếu $y=0$), $p_t$ cao thì mẫu dễ; $p_t$ thấp thì mẫu khó.
- $\alpha_t$ là **trọng số cố định theo lớp** ($\alpha$ cho $y=1$, $1-\alpha$ cho $y=0$), dùng để cân bằng lớp và chứng không phụ thuộc $p_t$.
- $\gamma$ là **focusing parameter**, nếu $\gamma=0$ thì Focal Loss chính là Cross-Entropy. $\gamma$ càng lớn, mẫu dễ càng bị giảm trọng số mạnh.

**Binary classification.** Khai triển theo $y$:

$$
\begin{equation}
\text{FL}(p)=-\alpha\,y\,(1-p)^{\gamma}\log(p)
-(1-\alpha)\,(1-y)\,p^{\gamma}\log(1-p)
\end{equation}
$$

**Multi-class classification** (softmax, $K$ lớp):

$$
\begin{equation}
\text{FL}(p_t)=-\alpha_t\,(1-p_t)^{\gamma}\log(p_t)
\end{equation}
$$

rong đó $t$ là chỉ số lớp đúng, $\alpha_t$ là trọng số cho lớp $t$ và $p_t=\operatorname{softmax}(x_t)$.

## 📚 Futher Reading
---
- [Understanding Deep Learning book (Prince, Chapter 05)](https://udlbook.github.io/udlbook/).
- [Focal Loss (Lin et al.)](https://arxiv.org/pdf/1708.02002) 

---