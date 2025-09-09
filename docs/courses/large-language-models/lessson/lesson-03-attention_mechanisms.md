---
title: Lesson 03. Attention Mechanisms Knowledge Base
icon: material/numeric-3-circle
---

# Lesson 03: Attention Mechanisms Knowledge Base
---

### Types for attention mechanisms

Chúng ta sẽ tìm hiểu và triển khai bốn biến thể khác nhau của cơ chế attention, những biến thể attention này được xây dựng dựa trên nhau với các mục tiêu khác biệt.

| Type | Description |
| :--- | :---------- |
| **Simplified self-attention** (attention đơn giản) | Đây là kỹ thuật self-attention đơn giản để giới thiệu ý tưởng tổng quát |
| **Self-attention** (attention tự học) | Self-attention với các trọng số có thể huấn luyện, là cơ sở của cơ chế được dùng trong các LLM.
| **Causal attention** (attention nhân quả) | Một dạng self-attention được dùng trong LLM, cho phép mô hình chỉ xem xét các đầu vào hiện tại và trước đó trong một chuỗi, đảm bảo thứ tự thời gian trong quá trình sinh văn bản |
| **Multi-head-attention** (attention đa đầu) | Mở rộng self-attention và causal attention, cho phép mô hình đồng thời chú ý đến thông tin từ nhiều không gian biểu diễn khác nhau |

Bắt đầu từ phiên bản simplified self-attention giúp chúng ta hình dung được khái niệm cơ bản nhất, trước khi thêm các trọng số có thể huấn luyện ở phiê bản self-attention. Cơ chế causal attention thêm một mask vòa self-attention, cho phép LLM sinh từng từ một. Cuối cùng, multi-head attention tổ chức cơ chế attention thành nhiều head, giúp mô hình nắm bắt nhiều khía cạnh khác nhau của dữ liệu đầu vào cùng lúc.

### The birth of attention mechanism

Trước khi đi sâu vào cơ chế self-attention, trái tim của các mô hình LLM hiện nay, cần xem xét vấn đề của các kiến trúc trước đây mà không có cơ chế attention. Giả sử chúng ta muốn xây dựng một mo hình dịch ngôn ngữ, mục tiêu là dịch văn bản từ một ngôn ngữ này sang một ngôn ngữ khác. Chúng ta không thể dịch từng từ một cách trực tiếp (word-by-word) do cấu trúc ngữ pháp khác nhau giữa ngôn ngữ nguồn và ngôn ngữ đích.

Ví dụ:

- Câu gốc tiếng Việt: "Bạn có thể giúp tôi dịch câu này được không". 
- Dịch từng từ trực tiếp: "You can help me translate this sentence" -> câu này sai ngữ pháp trầm trọng.
- Dịch chính xác: Một số từ trong câu dịch cần tham chiếu đến các từ xuất hiện trước hoặc sau trong câu gốc, đòi hỏi hiểu  ngữ cảnh và cấu trúc ngữ pháp chứ không thể dịch theo từng từ riêng lẻ.

Để giải quyết vấn đề này, thường sử dụng mạng nơ-ron sâu với hai thành phần là encoder và decoder. Encoder đọc và xử lý toàn bộ văn bản đầu vào, trong khi decoder dựa trên thông tin từ encoder để tạo ra văn bản đích. Trước khi có transformer, RNN là kiến trúc encoder-decoder phổ biến nhất cho dịch ngôn ngữ. RNN là loại mạng nơ-ron mà đầu ra của bước trước được làm đầu vào của bước hiện tại, rất phù hợp cho dữ liệu tuần tự như văn bản hay giọng nói. 

Trong encoder-decoder của RNN, văn bản đầu vào được đưa vào encoder, xử lý tuần tự, encoder cập nhật hidden state tại mỗi bước, cố gắng nén toàn bộ ý nghĩa của câu đầu vào trong hidden state cuối cùng. Decoder sử dụng hidden state cuối cùng này để bắt đầu tạo từng câu dịch, từng từ một, và cũng cập nhật hidden state tại mỗi bước để giữ ngữ cảnh cần thiết cho việc dự đoán từ tiếp theo. Tuy nhiên hạn chế lớn của encoder-decoder RNN là:

- Khi đang decode, RNN không thể truy cập trực tiếp các nhóm hidden state trước đó của encoder.
- Decoder chỉ dựa vào hidden state hiện tại, vốn phải chứa toàn bộ thông tin quan trọng của cả một chuỗi. Điều này có thể gây mất ngữ cảnh, đặc biệt với các câu dài hoặc có nhiều phụ thuộc phức tạp.

Những hạn chế này của RNN là cơ sở, động lực để giải thích cho sự ra đời của transformer và attention trong LLM.

### Bahdanau attention

Mặc dù RNN hoạt động khá tốt khi dịch những câu ngắn, nhưng chúng lại không hiệu quả với các văn bản dài vì chúng không có khả năng truy cập trực tiếp vào những từ trước đó trong đầu vào. Một điểm hạn chế lớn của phương pháp này là RNN phải ghi nhớ toàn bộ đầu vào đã được mã hóa trong một trạng thái ẩn duy nhất trước khi truyền nó cho bộ giải mã.

Chính vì vậy, vào năm 2014 cơ chế attention Bahdanau cho RNN xuất hiện. Cơ chế này điều chỉnh kiến trúc RNN encoder-decoder sao cho bộ giải mã có thể truy cập chọn lọc các phần khác nhau của chuỗi đầu vào tại mỗi bước sinh đầu ra. Khi sinh ra một từ trong đầu ra, mô hình có cách để truy cập vào tất cả các từ đầu vào. Độ dày của đường chấm thể hiện mức độ quan trọng của từ đầu vào đối với từ đầu ra tương ứng. Điều này có nghĩa là một số từ đầu vào sẽ quan trọng hơn những từ khác cho việc sinh ra một từ đầu ra nhất định. Độ quan trọng được xác định bởi các trọng số attention sẽ được đề cập ở phần tiếp theo.

Chỉ ba năm sau, các nhà nghiên cứu đã phát hiện ra rằng kiến trúc RNN không còn cần thiết để xây dựng mạng nơ-ron sâu cho xử lý ngôn ngữ tự nhiên. Họ đã đề xuất kiến trúc Transformer bao gồm một cơ chế self-attention lấy cảm hứng từ cơ chế attention Bahdanau. Self-attention là một cơ chế cho phép mỗi vị trí trong chuỗi đầu vào có thể xem xét mức độ liên quan của tất cả các vị trí khác trong cùng chuỗi khi tính toán biểu diễn của chuỗi đó. Self-attention là một thành phần cốt lõi của các mô hình ngôn ngữ lớn hiện đại dựa trên kiến trúc Transformer, chẳng hạn như dòng GPT.

### Concept of self-attention

Trong self-attention, chữ “self” ám chỉ khả năng của cơ chế này trong việc tính toán các trọng số attention bằng cách thiết lập mối liên hệ giữa những vị trí khác nhau trong cùng một chuỗi đầu vào. Cơ chế này cho phép mô hình đánh giá và học được các mối quan hệ, sự phụ thuộc giữa các thành phần của chính chuỗi đó, chẳng hạn như giữa các từ trong một câu hoặc giữa các pixel trong một hình ảnh.

Điều này trái ngược với attention truyền thống, nơi trọng tâm là mối quan hệ giữa các phần tử thuộc hai chuỗi khác nhau. Ví dụ, trong mô hình sequence-to-sequence, attention được tính toán giữa một chuỗi đầu vào và chuỗi đầu ra tương ứng.

### A simple self-attention mechanism

Đây là biến thể đơn giản của self-attention, không có bất kỳ trọng số huấn luyện nào, như được mô tả trong **hình 3.1**. Mục tiêu là minh hoạ một số khái niệm chính trong self-attention trước khi thêm các trọng số có thể huấn luyện. 

![](../large-language-models/images/3_1.jpg)

/// caption
**Hình 3.1** Mô tả mục tiêu của self-attention trong việc tính toán một vector ngữ cảnh cho mỗi phần từ đầu vào, bằng cách kết hợp thông tin từ tất cả các phần từ đầu vào khác. Trong ví dụ này, chúng ta đang tính vector ngữ cảnh $z^{(2)}$. Mức độ quan trọng hay sự đóng góp của từng phần tử đầu vào trong việc tính $z^{(2)}$ được xác định bởi các trọng số attention $\alpha_{21}$ đến $\alpha_{2T}$. Khi tính $z^{(2)}$ các trọng số attention được tính toán dựa trên phần từ đầu vào $x^{(2)}$ và tất cả các phần từ đầu vào khác.
///

**Hình 3.1** minh họa một chuỗi đầu vào ký hiệu là $x$, gồm $T$ phần tử từ $x^{(1)}$ đến $x^{(T)}$. Chuỗi này thường biểu diễn văn bản đã được biến đổi thành các token embedding. Chẳng hạn, với câu “The quick brown fox jumps high”, mỗi phần tử trong chuỗi, như $x^{(1)}$, tương ứng với một vector embedding d-chiều đại diện cho một token cụ thể (ví dụ: từ “The”). Trong ví dụ này, ta giả sử các vector đầu vào là embedding ba chiều (xem chú thích I trong hình).

Trong self-attention, mục tiêu là tính toán các vector ngữ cảnh $z^{(i)}$ cho mỗi phần tử $x^{(i)}$ trong chuỗi đầu vào. Vector ngữ cảnh có thể được hiểu là một embedding được làm giàu, bởi nó không chỉ chứa thông tin về $x^{(i)}$ mà còn kết hợp thông tin từ tất cả các phần tử $x^{(j)}$ khác trong cùng chuỗi.

Để minh họa, hãy xét vector embedding của phần tử thứ hai $x^{(2)}$ (tương ứng với token “quick”) và vector ngữ cảnh tương ứng $z^{(2)}$. Vector ngữ cảnh này là một embedding chứa thông tin về $x^{(2)}$ đồng thời gói gọn cả thông tin từ các phần tử khác, từ $x^{(1)}$ đến $x^{(T)}$.

Vector ngữ cảnh giữ vai trò quan trọng trong self-attention. Nhiệm vụ của chúng là tạo ra những biểu diễn làm giàu cho từng phần tử trong chuỗi bằng cách kết hợp thông tin từ tất cả các phần tử còn lại. Đây là yếu tố then chốt trong các mô hình ngôn ngữ lớn, vốn cần nắm bắt được mối quan hệ và mức độ liên quan giữa các từ trong một câu.

