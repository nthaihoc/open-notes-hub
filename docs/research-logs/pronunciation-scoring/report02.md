---
title: Triển khai mô hình cơ bản, đánh giá và phân tích lỗi 
icon: material/tools
hide:
    -navigation
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


## 2. Đánh giá hiệu suất mô hình

**Đánh giá hiệu suất mô hình dựa trên thước đo phân lọai cơ bản.** Đánh giá các mô hình dựa trên bộ dữ liệu l2arctic, sử dụng F1-score.

| Model | Description | F1-score |
| :---- | :---------- | :------: |
| **MLP**         | 3 tầng fully-connected |  *0.78* |
| **BiLSTM**      | 2 tầng BiLSTM + pooling/attention |  *0.83* |
| **GOP-based**   | Tính GOP từ ASR (likelihood/posterior) sau đó classifier trên GOP và kết hợp feature | *0.71* |
| **Mini-Transformer** | 4 lớp Transformer encoder | *0.82* |

**Đánh giá hiệu suất trên bộ dữ liệu khác.** So sánh khả năng khái quát hóa của mô hình trên miền dữ liệu tiếng nói khác. 

| Model             | Dataset        | F1-score       |
| :---------------- | :------------- | :------------: |
| **MLP**           | l2arctic       | **0.78**       |
|                   | Speechocean762 | 0.65 |
|                   | EpaDB          | 0.61 |
| | | |
| **BiLSTM**        | l2arctic       | **0.83** |
|                   | Speechocean762 | 0.72 |
|                   | EpaDB          | 0.68 |
| | | |
| **GOP-based**     | l2arctic       | **0.75** |
|                   | Speechocean762 | 0.60 |
|                   | EpaDB          | 0.54 |
| | | | 
| **Mini-Transformer** | l2arctic    | **0.85** |
|                   | Speechocean762 | 0.65 |
|                   | EpaDB          | 0.75 |


---