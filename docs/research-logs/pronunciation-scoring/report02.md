---
title: Triển khai mô hình cơ bản, đánh giá và phân tích lỗi 
icon: material/tools
---

# Triển khai mô hình cơ bản, đánh giá và phân tích lỗi 
---

!!! danger "Mô tả"
    - Nhiệm vụ này thuộc **[Phase01 - Nghiên cứu tổng quan và chuẩn bị dữ liệu]**

        [Phase01 - Nghiên cứu tổng quan và chuẩn bị dữ liệu]: README.md/#ke-hoach-nhiem-vu-chi-tiet

    - Lựa chọn, thu thập và tiền xử lý bộ dữ liệu phù hợp cho bài toán PS theo chuẩn IPA (1)
      {.annotate}

        1. IPA là một hệ thống ký hiệu ngữ âm học quốc tế, dùng để ghi lại cách phát âm của các âm thanh trong ngôn ngữ nói — một cách chính xác, nhất quán và không phụ thuộc vào chính tả của bất kỳ ngôn ngữ nào.
    
    - Lựa chọn mô hình AI phù hợp, tinh chỉnh (fine-tune) mô hình trên bộ dữ liệu đã được xử lý với hai mục luồng chính:
        1. Mô hình đưa ra được điểm đánh giá tổng thể trên một đoạn âm thanh đầu vào của người học.
        2. Mô hình liệt kê chi tiết và đánh giá đúng sai cho toàn bộ các âm vị (phone-level) khi người học phát âm.
    
    - Đánh giá mô hình, phân tích lỗi cơ bản và dựng API

> Bấm vào (1) trên đầu mỗi từ khóa để xem thêm thông tin chú thích.
>{.annotate}
>
>1. "Chú thích được viết ở đây"

## 1. Bộ dữ liệu
---

Sử dụng bộ dữ liệu **[l2-arctic]** làm bộ dữ liệu chính để triển khai thực nghiệm và đánh giá cơ bản cho mô hình. Đây là một tập dữ liệu tiếng Anh không phải người bản địa (non-native English speech corpus), được thiết kế phục vụ cho nghiên cứu ở một số lĩnh vực như chuyển đổi giọng nói (voice conversion), phát hiện lỗi phát âm (mispronunication scoring detection), v.v. 

### __1.1 Mô tả chi tiết__

Thành phần chính của tập dữ liệu bao gồm âm thanh của 24 người nói tiếng Anh không phải là bản xứ, và họ đến từ đa dạng các quốc gia khác nhau như Hindi, Hàn Quốc, Trung Quốc, Tây Ban Nha, Ả Rập và cả Việt Nam. Dữ liệu âm thanh được thu thập trên cả nam và nữ cho từng quốc gia. Thu âm khoảng 1 giờ các câu tiếng Anh được lấy từ một tập các câu chuẩn __[CMU ARCTIC prompts]__ trên mỗi người nói. Mỗi đoạn thu tâm đều có bản phiên âm chính tả đi kèm (transciption) và phiên âm ngữ âm (forced-aligned phonetic transciption) theo chuẩn __[ARPAbet]__. Ngoài ra còn được chú thích thủ công lỗi phát âm như lỗi thay thế (substitution), lỗi bỏ sót (detection), lỗi thêm thừa (addition). 

[l2-arctic]: https://psi.engr.tamu.edu/l2-arctic-corpus/
[CMU ARCTIC prompts]: https://
[ARPAbet]: https://en.wikipedia.org/wiki/ARPABET

### __1.2 Cấu trúc bộ dữ liệu__

```python
l2arctic_v5/
|
|-- ABA/ #(1)!
|  |-- wav/ #(2)!             
|  |  |-- arctic_a0001.wav
|  |  |-- arctic_a0002.wav
|  |  |-- ...
|  |-- transcripts/ #(3)!  
|  |  |-- arctic_a0001.txt
|  |  |-- arctic_a0002.txt
|  |  |-- ...
|  |-- TextGrid/ #(4)!
|  |  |-- arctic_a0001.TextGrid
|  |  |-- arctic_a0002.TextGrid
|  |  |-- ...
|  |-- annotations/ #(5)!
|     |-- arctic_a0001.TextGrid
|     |-- arctic_a0002.TextGrid
|     |-- ...
|
|-- SKA/
|-- BWC/
|-- ...
```

1. Folder chứa dữ liệu âm thanh của tất cả người nói trong cùng một quốc gia.
2. Folder chứa các đoạn thanh của người nói
3. Folder bao gồm các văn bản chú thích tương ứng với file âm thanh
4. Folder chú thích căn chỉnh sau khi trải qua quá trình ép khung
5. Folder gán nhãn thủ công các lỗi phát âm cho đoạn âm thanh

Trong đó:

- `ABA:` Folder chứa dữ liệu âm thanh của tất cả người nói trong cùng một quốc gia.
- `wav:` Folder chứa các đoạn thanh của người nói
- `transcipts:` Folder bao gồm các văn bản chú thích tương ứng với file âm thanh
- `TextGrid:` Folder chú thích căn chỉnh sau khi trải qua quá trình ép khung
- `annotations:` Folder gán nhãn thủ công các lỗi phát âm cho đoạn âm thanh

Mỗi một đoạn âm thanh đều được đưa vào một công cụ căn chỉnh dựa trên transcipts tương ứng. Các thông tin này được lưu trữ dưới dạng `.TextGrid`(1).
{.annotate}

1. Là một định dạng tệp văn bản được sử dụng trong phầm mềm Praat để gán nhãn thời gian cho âm thanh. Chúng lưu trữ thông tìn như từ, âm tiết, nhãn âm vị... tương ứng với các đoạn thời gian trong file âm thanh. 

Cấu trúc chính của một file `.TextGrid` cơ bản được hiển thị như trong `example.TextGrid`, chứa một số thông tin quan trọng:

- `xmin`, `xmax`: thời gian bắt đầu và kết thúc của một file âm thanh.

- `tier`: là các tầng dữ liệu chính như `name="words"`, `name="phones"`. 

- Tại mỗi tầng, mỗi đoạn âm thanh đều được gán nhãn tương ứng với từ/âm vị tại thời điểm đó. 

```json title="example.TextGrid" linenums="1"
File type = "ooTextFile"
Object class = "TextGrid"

xmin = 0 
xmax = 2.39 
tiers? <exists> 
size = 3 
item []: 
    item [1]:
        class = "IntervalTier" 
        name = "words" 
        xmin = 0 
        xmax = 2.39 
        intervals: size = 10 
        intervals [1]:
            xmin = 0 
            xmax = 0.05 
            text = "" 
        intervals [2]:
            xmin = 0.05 
            xmax = 0.42 
            text = "will" 
        intervals [3]:
            xmin = 0.42 
            xmax = 0.64 
            text = "we" 
        ...

    item [2]:
        class = "IntervalTier" 
        name = "phones" 
        xmin = 0 
        xmax = 2.39 
        intervals: size = 22 
        intervals [1]:
            xmin = 0 
            xmax = 0.05 
            text = "sil" 
        intervals [2]:
            xmin = 0.05 
            xmax = 0.28 
            text = "W" 
        intervals [3]:
            xmin = 0.9 
            xmax = 1.07 
            text = "ER0,AH0,s" 
        ...
```

Thông tin quan trọng nhất của tập dữ liệu này, đó là những labels được gán nhãn thủ cộng phục vụ cho bài toán mispronunciation detect ở mức phone-level. Ở tầng `phones`, mỗi đoạn âm thanh tương ứng sẽ được đi kèm với thông tin gán nhãn. Chúng được gán nhãn theo một số định dạng cụ thể như sau, ví dụ: 

- Âm vị `text = "ERO"` sẽ giữ nguyên nếu người dùng phát âm đúng.
- Nếu phát hiện lỗi phát âm sai nhãn sẽ được đổi thành `text = "ER0,AH0,s"`.
    - `ERO` (correct phoneme label) là âm đúng lẽ ra người đọc phải phát âm.
    - `AHO` (perceived phoneme lable) là âm thực tế mà người nói đã phát âm. Bên cạnh đó `err` sẽ được dùng nếu người dùng phát âm không rõ. 
    - `s` (substitution) đánh đấu là lỗi thay thế, ngoài ra còn có `a` (addition) lỗi thêm âm và `d` (detection) lỗi bỏ âm.

### __1.3 Tiền xử lý & Chuẩn bị dữ liệu__

Để đảm bảo dữ liệu phù hợp với mô hình và mục tiêu của bài toán mà chúng ta mong muốn. Bộ dữ liệu __[L2-ARCTIC]__ sẽ được thiết kế một cách cụ thể hơn phục vụ cho bài toán mispronunciation detect. Dễ dàng quan sát thấy tất cả các file `.TextGrid` trong bộ dữ liệu này đã chứa những thông tin rất chi tiết về thời gian bắt đầu và kết thúc của từng từ, từng âm vị trong một file `.wav` âm thanh. Tuy nhiên, các mô hình yêu cầu đầu vào phải là các đặc trưng âm học, giúp mô hình biết được vector đặc trưng âm học này thuộc về âm vị nào và nhãn của chúng ra sao. Như đã đề cập ở nội dung 1.2, có bốn định dạng đánh nhãn cơ bản cho từng âm vị, trong đó có một định dạng dành cho phát âm đúng và ba định dạng cho phát âm sai. Nếu người học phát âm đúng ta có thể coi là nhãn 0, nếu phát âm sai nhãn sẽ được gán theo 3 lỗi chính `s` (1 - lỗi thay thế), `a` (2 - lỗi thêm âm) và `d` (3 - lỗi bỏ âm). Do vậy, chúng ta cần phải định nghĩa lại bộ dữ liệu để đảm bảo đầu vào có đầy đủ những yếu tố trên.

[L2-ARCTIC]: https://

Trước tiên, hãy hình dung một output mà ta mong muốn mô hình trả về mỗi khi nhận được một file âm thanh bất kì. Giả sử, với một file âm thanh có tên `test0001.wav` với transcipts là `scoring`, mô hình sẽ trả về kết quả như sau:

```python title="test001.json" linenums="1"
{
    "file": "test001.wav",
    "transcipts": "scoring",
    "x_min": 0,
    "x_max": 1.2,
    "total_score": 0.7,
    "type": "IPA",
    "phones": {
        "s": 2,
        "k": 1,
        "ɔː": 0,
        "r": 1,
        "i": 1,
        "ŋ": 3
    }
}
```

Từ kết quả này, dễ dàng có thể giúp người học biết được `total_score` - người học phát âm đúng bao nhiêu phần trăm so với người bản địa, và liệt kê một `phones` - danh sách bao gồm các âm vị và nhãn tương ứng mà mô hình dự đoán ra. Để đảm bảo mô hình học được mối liên hệ giữa các đặc trưng âm học và các âm vị tương ứng cũng như lỗi phát âm, quy trình tiền xử lý dữ liệu sẽ bao gồm các bước chính như sau:

__Bước 1: Trích xuất đặc trưng âm học__

- Mỗi file âm thanh `.wav` được đưa qua mô hình __[wav2vec 2.0]__ (đây là mô hình tôi chưa lựa chọn cho quá trình này), có thể sử dụng các mô hình âm học tương đương khác để trích xuất đặc trưng.

- Kết quả đầu ra sau khi trích xuất là một tensor có kích thước thường có dạng `[1, T, D]` với `T` là số lượng khung đặc trưng (frame) và `D` là chiều của vector đặc trưng. Mỗi khung âm thanh tương ứng với một đoạn thời gian cố định (thường kéo dài khoảng 20ms/frame, phụ thuộc vào từng mô hình).

__Bước 2: Lấy thông tin nhãn từ file `.TextGrid`__

- Lấy toàn bộ các thông tin như các khoàng thời gian (`xmin`, `xmax`) của từng âm vị trong tier `phones` trong các file `.TextGrid` tương ứng.

- Tại mỗi âm vị tiến hành xử lý nhãn theo bốn định dạng đã được phân tích ở phần trước (ví dụ `text = "AH1", "T", "S"`) sẽ gán là 1, tương tự với các mẫu khác và nhãn khác.

- Tính toán `total_score` của toàn câu để mô tả mức độ chính xác trong phát âm của người học. Công thức tính như sau:

$$
\text{total_score} = \frac{A}{N}
$$

- Trong đó $A$ là số lượng âm vị phát âm đúng (nhãn 0) và $N$ là tổng số âm vị có trong câu theo transcipts. 

__Bước 3: Đối chiếu thời gian với chỉ số frame__

- Để thực hiện việc gán nhãn chính xác cho từng đoạn đặc trưng, cần ánh xạ mỗi `xmin`, `xmax` sang chỉ số frame tương ứng trong tensor đặc trưng có được trong bước 1. Bằng cách sử dụng công thức sau, có thể dễ dàng xác định được chỉ số frame:

$$\text{start_frame} = [\frac{x_\min}{\text{stride}}]; \quad \text{end_frame} = [\frac{x_\max}{\text{stride}}]$$

- Trong đó tham số `stride` là khoảng thời gian giữa hai khung liên tiếp (đối với mô hình __[wav2vec 2.0]__ là 0.02 giây).

__Bước 4: Gán nhãn cho mỗi đoạn đặc trưng__

- Sau khi tách được mỗi đoạn (`start_frame`, `end_frame`), tiến hành cắt đoạn đặc trưng tương ứng với chỉ số này từ tensor đặc trưng gốc sau khi trích xuất và gán nhãn theo quy tắc (đã được xử lý trong bước 2).

- Vì các `phones` trong bộ dữ liệu **[L2-ARCTIC]** được chú thích theo chuẩn **[ARPAbet]**, mà bài toán ta mong muốn mô hình học được phát âm theo chuẩn **[IPA]**, chính vì vậy các kí tự âm vị sẽ được chuyển đổi sang chuẩn này.

[wav2vec 2.0]: https://arxiv.org/pdf/2006.11477
[ARPAbet]: **https://en.wikipedia.org/wiki/ARPABET
[IPA]: https://vi.wikipedia.org/wiki/B%E1%BA%A3ng_m%E1%BA%ABu_t%E1%BB%B1_ng%E1%BB%AF_%C3%A2m_qu%E1%BB%91c_t%E1%BA%BF

## 2. Lựa chọn và tinh chỉnh mô hình

Như đã được đề cập ở những phần trước đó, bài toán này sử dụng mô hình __[wav2vec 2.0]__ để trích xuất đặc trưng âm thanh phục vụ quá trình frame-label và huấn luyện một mô hình có khả năng nhận diện và phân loại chi tiết cho từng âm vị. Mô hình này là một phương pháp hiệu quả và hiện đại nhằm mục đích xây dựng hệ thống nhận dạng tiếng nói thông qua học tự giám sát, giúp giải quyết vấn đề thiếu dữ liệu có nhãn. Chúng học cách mã hóa âm thanh thành các biểu diễn tiềm ẩn, sau đó che đi một phần và sử dụng kiến trúc Transformer tạo ra các biểu diễn ngữ cảnh hóa và phân biệt chúng với các yếu tố gây nhiễu, đồng thời học được các đơn vị tiếng nói rời rạc. Phương pháp này đạt được hiệu suất rất tốt, đặc biệt ấn tượng ở các trường hợp có rất ít dữ liệu có nhãn.

[wav2vec 2.0]: https://arxiv.org/pdf/2006.11477

### __2.1 Kiến trúc của mô hình__

Kiến trúc của mô hình __[wav2vec 2.0]__ (__Hình 2.1__) tập trung vào ba thành phần chính: Bộ mã hóa đặc trưng (feature encoder), mạng Transformer để tạo biểu diễn ngữ cảnh (contextualized representations with transformers), và lượng tử hóa (quantization module).

![](../images/framework_wav2vec.png)

/// caption
__Hình 2.1: Kiến trúc thành phần cơ bản của mô hình wav2vec__
///

__a. Bộ mã hóa đặc trưng (feature encoder)__

Mục đích của quá trình này là chuyển đổi toàn bộ sóng âm thanh thô thành các biểu diễn tiềm ẩn có ỹ nghĩa. Bộ mã hóa này được cấu tạo bởi nhiều khối, mỗi khối chứa các thành phần như:

- Tích chập thời gian (temporal convolution): Đây là một loại mạng tích chập chuyên dùng cho dữ liệu chuỗi (như âm thanh). Chúng lần lượt quét qua dữ liệu theo thời gian đề trích xuất các đặc trưng cục bộ.

- Chuẩn hóa lớp (layer normalization): Kỹ thuật này giúp ổn định quá trình huấn luyện của mạng nơ-ron bằng cách chuẩn hóa đầu ra của mỗi lớp.

- Hàm kích hoạt GELU: Hàm này giúp mạng học được các mối quan hệ phức tạp trong dữ liệu.

__b. Biểu diễn được ngữ cảnh hóa với Transformer (contextualized representations with transformers)__

Giả sử các âm thanh thô sau khi đi qua feature encoder là các biểu diễn tiềm ẩn $Z$, chúng sẽ được đưa vào các kiến trúc Transformers để tạo ra các biểu diễn $C$ nắm bắt được ngữ cảnh của toàn bộ chuỗi. Có một sự khác biệt nhỏ trong việc nhúng vị trí (positional embeddings), thay vì dùng nhúng vị trí cố định như phương pháp truyền thống, ở giai đoạn này một lớp tích chập được cài đặt để tạo ra nhúng vị trí tương đối. Hiểu một cách nôm na, thay vì nói "phần tử này ở vị trí thứ 10", thì chúng sẽ tập trung vào "phần tử này cách phần từ kia với khoảng cách là bao xa".

__c. Module lượng tử hóa (quantization module)__

Chuyển đổi các biểu diễn tiếng nói tiềm ẩn liên tục $Z$ thành một tập hợp rời rạc (discrete) các biểu diễn. Các biểu diễn rời rạc này được sử dụng làm mục tiêu trong tác vụ học tự giám sát. Trong mô hình này lượng tử hóa tích (product quantization - PQ) được sử dụng. Đây là một kỹ thuật để lượng tử hóa các vector nhiều chiều thành nhiều phần nhỏ (các nhóm hoặc codebook). Giả sử ta có một vector đặc trưng $d$ chiều. PQ sẽ chia $d$ chiều này thành $G$ nhóm, mỗi nhóm có $\frac{d}{G}$ chiều. Với mỗi nhóm, sẽ chứa một codebook riêng và mỗi codebook sẽ chứa nhiều vector con.

Để dễ hình dung hơn, nếu ta có một bức ảnh kỹ thuật số, màu sắc trong bức ảnh được biểu diễn bằng nhiều giá trị số liên tục. Nếu muốn giảm đi dung lượng file hoặc muốn lưu trữ chúng trên một thiết bị có bộ nhớ hạn chế, thì lượng tử hóa màu sắc sẽ được sử dụng. Thay vì có hàng triệu sắc thái màu liên tục, ta chỉ cho phép ảnh sử dụng một tập hợp rời rạc có thể là 100 màu chuẩn hoặc ít hơn. Mỗi điểm ảnh sẽ được làm tròn hoặc quy về một màu gần nhất trong tập hợp màu giới hạn đó.

Biểu diễn tiếng nói tiềm ẩn $Z$ mà bộ mã hóa tạo ra là các giá trị liên tục, vì vậy mục tiêu chính của lượng tử hóa là cố gắng chuyển đổi chúng về một tập hợp hữu hạn rời rạc các mã hoặc đơn vị. Nếu từ một đoạn âm thanh đầu vào, ta mong muốn phân loại từ một chuỗi các âm thanh liên tục đó thành các âm (như a, b, c) rõ ràng, thay vì là một dải âm liên tục không định hình. Việc này giúp mô hình dễ dàng học được các đơn vị cơ bản của tiếng nói.

Lượng tử hóa giúp cho việc xử lý dữ liệu và lưu trũ dễ dàng hơn và các biểu diễn đã được lượng tử hóa $Q$ được dùng làm mục tiêu (targets) cho tác vụ học tự giám sát. Mô hình phải cố gắng dự đoán hoặc tái tạo lại các đơn vị rời rạc này.

Codebook có thể coi là một tử điển hoặc một bộ sưu tập các mã hoặc mẫu đã được định nghĩa trước. Chúng được xây dựng một cách tự động thông qua quá trình huấn luyện tự giám sát của mô hình. Trong quá trình huấn luyện, codebook được hình thành nhờ sự hỗ trợ bởi các hàm mất mát (contrastive loss, diversity loss) và các kỹ thuật như gumble softmax để trở thành một tập hợp các đơn vị tối ưu, có khả năng biểu diễn hiệu quả các đặc trưng cơ bản của dữ liệu âm thanh không có nhãn.

- Ban đầu khi mô hình chưa được huấn luyện, các vector trong codebook được khởi tạo ngẫu nhiên. Chúng có thể là những tập hợp số vô nghĩa.

- Codebook được học và cập nhật cùng với phần còn lại của mô hình (bộ mã hóa đặc trưng và transformer) thông qua tác vụ tự giám sát. Để có được nhãn cho việc dự đoán mà không cần con người, các biểu diễn tiềm ẩn $Z$ (thường là các phần không bị che từ các khoảng thời gian khác) được đưa ra PQ để tạo ra các đơn vị rời rạc. Chính các đơn vị này đóng vai trò là nhãn tự tạo cho mô hình.

- Khi mô hình dự đoán một biểu diễn ngữ cảnh cho một đoạn âm thanh bị che, chúng sẽ so sánh dự đoán đó với một trong các đơn vị rời rạc từ codebook (đây là mục tiêu/nhãn đúng cho đoạn bị che đó). Nếu dự đoán của mô hình chưa tốt, hàm mất mát (constractive loss) sẽ đưa ra mức độ sai lệch. 


### __2.2 Gumbel Softmax, Contrastive Loss, Diversity Loss__

__a. Gumble Softmax__

Việc chọn lực một vector rời rạc từ một codebook thường không thể khả vi, tức là sẽ không thể tính toán gradient cho quá trình cập nhật trọng số mạng. Gumbel softmax là một kỹ thuật nhằm giải quyết vấn đề này, chúng cho phép chọn các vector rời rạc một cách khả vi hoàn toàn, điều này có nghĩa là ta có thể thực hiện lan truyền ngược qua quá trình lựa chọn rời rạc đề huấn luyện toàn bộ mô hình. Công thức của Gumbel softmax được thiết kế như sau:

$$
P_{g,v} = \frac{exp(l_{g,v} + n_{v}) / \tau}{\sum^{V}_{k=1} exp(l_{g,k} + n_{k}) / \tau}
$$

Công thức này tính toán xác suất để chọn mục nhập thứ $v$ từ sổ mã của nhóm $g$, $l_{g,v}$ là các đầu ra chưa chuẩn hóa của một lớp tuyến tính. Gumbel softmax có sử dụng một tham số nhiệt độ $\tau$ giúp cho quá trình lựa chọn trở nên mềm mại hơn trong quá trình truyền tiến, và sử dụng một bộ ước tính có tên là straight-through để đảm báo gradient truyền ngược chính xác trong quá trình truyền ngược.

__b. Contrastive Loss__

Đây là hàm mất mát tương phản giúp mô hình có thể phân biệt được giữa biểu diễn tiếng nói tiềm ẩn được lượng tử hóa đúng (positive sample) và các biểu diễn sai (negative sample) cho một vị trí bị che. Hàm này được định nghĩa bằng công thức sau:

$$
\mathcal{L}_{m} = -\text{log} \frac{exp(sim(c_{t}, q_{t})/k)}{\sum_{\tilde{q} \sim Q_{t}} exp(sim(c_{t}, \tilde{q}) / k)}
$$

Mô hình sẽ nhận đầu ra từ mạng transformer là $c_{t}$, tập trung vào một bước thời gian $t$ đã bị che, $c_t$ là biểu diễn ngữ cảnh mà transformer đã tạo ra, cố gắng nắm bắt thông tin từ toàn bộ chuỗi. Sau đó mô hình cần xác định đâu là biểu diễn tiếng nói tiềm ẩm được lượng tử hóa đúng $q_{t}$ cho bước thời gian $t$, $q_{t}$ được tạo ra từ biểu diễn tiềm ẩn gốc (không bị che) tại vị trí $t$, sau khi đi qua module lượng tử hóa. Để làm được điều này, mô hình được đưa ra một tập hợp $K+1$ ứng cử viên cho $\tilde{q}$. Tập hợp này bao gồm:

- $q_{t}$ biểu diễn đúng
- $K$ là phần tử gây nhiễu, các biểu diễn này được lấy mẫu ngẫu nhiên từ các bước thời gian bị che khác trong cùng một file âm thanh. 

__c. Diversity Loss__

Công thức của Diversity Loss (hàm mất mát đa dạng) được biểu diễn như sau:

$$
\mathcal{L}_{d} = \frac{1}{GV} \sum^{G}_{g=1} - H(\overline{p}_{g}) == \frac{1}{GV} \sum^{G}_{g=1} \sum^V_{v=1} \overline{p}_{g,v} \log \overline{p}_{g,v}
$$

Trong đó:

- $H(\overline{p}_{g})$ là ký hiệu cho entropy phân phối của $\overline{p}_{g}$.
- $\sum^V_{v=1} \overline{p}_{g,v} \log \overline{p}_{g,v}$ là công thức tính toán entropy.
- $\frac{1}{GV}$ là hệ số chuẩn hóa, trung bình hóa hàm mất mát trên tất cả $G$ codebook và $V$ vector trong mỗi codebook.

Hàm mất mát đa dạng này được áp dụng khuyến khích mô hình sử dụng tất cả hoặc phần lớn các vector trong các codebook một cách đồng đều, thay vì chỉ tập trung vào một vài vector đặc trưng phổ biến. Nếu không có hàm mất mát này, có thể một số vector trong codebook không bao giờ được sử dụng. Điều này sẽ vô tình làm lãng phí khả năng biểu diễn của codebook và hạn chết tính đa dạng của các đơn vị mà mô hình học được.

### __2.3 Thiết kế fine-tune mô hình__

Sau khi đã có được các cặp (đặc trưng âm học theo khung, nhãn lỗi theo khung) ở __[phần 1.3]__, một mô hình MLP đơn giản được chọn làm baseline để thử nghiệm huấn luyện cho bộ dữ liệu, qua đó nhanh chóng kiểm tra pipeline và làm điểm số tham chiếu, đồng thời chứng yêu cầu tài nguyên tính toán ít hơn. 

[phần 1.3]: #13-tiền-xử-lý--chuẩn-bị-dữ-liệu

## 3. Đánh giá cơ bản mô hình

__Bảng 3.1__ là kết quả đánh giá mô hình mispronunciation detection trên dữ liệu kiểm tra.

| Nhãn | Ghi chú | Precision | Recall | F1-score |
| :--: | :------ | :-------: | :----: | :------: |
| 0 | Phát âm đúng | 0.75 | 0.82 | 0.78 |
| 1 | Lỗi thêm âm | 0.60 | 0.52 | 0.56 |
| 2 | Lỗi bỏ âm | 0.58 | 0.63 | 0.60 |
| 3 | Lỗi thay thế âm | 0.62 | 0.54 | 0.58 |

/// caption
__Bảng 3.1: Bảng kết quả đánh giá hiệu suất mô hình mispronuncation detect trên những nhãn cơ bản.__
///


Nhìn chung mô hình đang đạt hiệu suất ở mức độ trung bình, mô hình nhận diện âm đúng là tương đối tốt, những các lỗi phát âm thì khó có thể phân biệt rõ ràng. Điều  này có thể xuất phát từ dữ liệu, quy trình thiết kế và lựa chọn phương pháp thực nghiệm.

## 4. Xây dựng API cơ bản

==Progress...==

---