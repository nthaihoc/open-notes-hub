---
title: Lesson 01. FastAPI Overview and Project Setup
---

# ❄️ Lesson 01. FastAPI Overview and Project Setup
---
!!! tip ""
    Nội dung trong bài này cung cấp các kiến thức, cấu trúc cơ bản và vững chắc về FastAPI. Bạn sẽ có thể thiết lập một dự án mới, định nghĩa được các endpoint API, nắm bắt được cách xử lý dữ liệu với FastAPI.

## Technical requirements

Để triển khai thành công một dự án với FastAPI, cần thiết lập một môi trường hỗ trợ phát triển Python và các chức năng của FastAPI. Một số thành phần kỹ thuật quan trọng cần cài đặt:

- Python: FastAPI được xây dựng trên Python, vì vậy cần một phiên bản Python tương thích với phiên bản FastAPI tương ứng.

- FastAPI: Cài đặt bằng pip, trình quản lý gói của Python.

- Uvicorn: FastAPI cần một ASGI server (Asynchronous Server Gateway Interface), và Uvicorn là một triển khai ASCI cực kì nhanh.

- IDE (Integrated Development Environment): Một IDE như Visual Studo Code (VS Code), PyCharm,..., hỗ trợ phát triển Python trong việc viết mã và kiểm thử code.

- Postman hoặc Swagger UI: Dùng để kiểm thử API endpoints. FastAPI tự động tạo và host Swagger UI, có thể sử dụng ngay mà không cần cần cấu hình gì thêm.

- Git: Là công cụ được sử dụng rộng rãi cho phép quản lý phiên bản.

## Setting up development environment

**Cài đặt Python trên Windows.** FastAPI họat động với Python, vì vậy cần kiểm tra phiên bản Python trước khi sử dụng, đây là bước quan trọng để thiết lập FastAPI.

1. Truy cập trang chính thức của Python: [python.org](https://python.org), tải phiên bản Python mới nhất, hoặc tối thiểu >= 3.9.

2. Chạy file cài đặt, nhớ tích vào ô `Add Python to Path` trước khi bấm `Install Now`.

3. Sau khi cài xong, mở Command Prompt (cmd) và gõ: `python --version` để kiểm tra phiên bản.

**Cài đặt Python trên macOS/Linux.** macOS thường có sẵn Python, nhưng thường là bản cũ, bạn nên cài bản mởi bằng Homebrew.

Cài Homebrew (nếu chưa có):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Sau đó cài Python qua lệnh:

```bash
brew install python
```
Đối với Linux (Ubuntu/Debian) thực hiện cài Python bằng `apt` thông qua lệnh:

```bash
sudo apt-get install python3
```

**Kiểm tra phiên bản sau khi cài đặt.** Trên macOS/Windows chạy `python --version`, trên Linux `python3 --version`. Ngoài ra, kiểm tra pip (trình quản lý gói của Python), trên macOS/Windows chạy `pip --version`, trên Linux `pip3 --version`.

**Cài đặt FastAPI và Uvicorn.** Sau khi cài đặt thành công Python và pip, tiếp theo sẽ cài đặt FastAPI và Uvicorn. Mở terminal/command prompt và chạy `pip install fastapi[all]`. Lệnh này sẽ cài FastAPI cùng tất cả các dependencies được khuyến nghị, bao gồm cả Uvicorn. Kiểm tra cài đặt chạy `uvicorn --version`.

**Thiết lập IDE.** IDE không chỉ là editor, mà còn là nơi viết code, debug, và test ứng dụng. Một số IDE phổ biến cho FastAPI mà bạn có thể tải và dùng là [VS Code](https://code.visualstudio.com) và [PyCharm](https://www.jetbrains.com/pycharm/download).

**Thiết lập Git và Github.** Quản lý phiên bản (Version Control) là một khía cạnh quan trọng của phát triển phầm mềm. Git kết hợp GitHub tạo thành một bộ công cụ mạnh mẽ để theo dõi thay đổi, cộng tác nhóm và duy trì lịch sử dự án. Có thể tìm và cài đặt Git từ trang chính thức [git-scm.com](https://git-scm.com).

Sau khi cài xong, cấu hình Git với tên và email của bạn trong command line:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Creating a FastAPI project

Bắt đầu bằng việc khởi tạo một project folder với tên mà bạn thích (đây sẽ là nơi chứa toàn bộ mã nguồn dự án). Trước hết, bạn cần tạo một môi trường ảo:

```bash
$ python -m venv .venv
```

Để kích hoạt môi trường ảo, nếu bạn sử dụng Mac or Linux:

```bash
$ source .venv/bin/activate
```

Trên hệ điều hành Windows, chạy dòng lệnh sau:

```bash
$ .venv\Scripts\activate
```

Khi môi trường ảo được kích hoạt, bạn sẽ thấy trong terminal có một chuỗi tiền tố như sau: `(.venv) $`. Từ thời điểm này, toàn bộ các module bạn cài đặt bằng pip sẽ được lưu trữ và cài đặt vào thư mục `.venv`, và chỉ sử dụng được khi môi trường này đang hoạt động.

Bây giờ, bạn có thể cài đặt gói fastapi cùng với uvicorn trong môi trường ảo của mình bằng cách chạy lệnh sau:

```bash
$ pip install fastapi uvicorn
```

Sau khi FastAPI đã được cài đặt, hãy mở thư mục dự án và tạo một file có tên là `main.py`. File này sẽ là nơi ứng dụng FastAPI của bạn bắt đầu.

```python
# import module FastAPI
from fastapi import FastAPI

# khởi tạo instance của lớp FastAPI
app = FastAPI()
```

Định nghĩa router đầu tiên trong ứng dụng. Router trong FastAPI giống như biến chỉ đường, giúp điều hướng request đến đúng function.

```python
@app.get("/")
def read_root(): 
    return {"Hello" : "World"}
```

## Structure project

Trong bất kể dự án nào, việc sắp xếp mã nguồn theo một cấu trúc rõ ràng không chỉ là vấn đề gọn gàng mà còn là việc tạo ra một môi trường bền vững và có khả năng mở rộng. Điều này có nghĩa là bạn cần tổ chức dự án theo cách tách biệt các phần khác nhau của ứng dụng một cách logic và hiệu quả.

Không có một cấu trúc duy nhất và hoàn hảo cho mọi dự án FastAPI, tuy nhiên, một cách tiếp cận phổ biến là chia dự án thành một số thư mục chính:

- **/src:** Đây là nơi chứa code chính của ứng dụng, bên trong có thể có các thư mục con cho những module khác nhau. Ví dụ: `models` - chứa các database models; `routes` - chứa các route của FastAPI; `services` - chứa phần logic nghiệp vụ.

- **/tests:** Tách riêng ra khỏi code ứng dụng là một cách tốt, giúp dễ dàng quản lý, dồng thời đảm bảo rằng build production không bao gồm code test.

- **docs:** Tải liệu là rất quan trọng với bất kỳ dự án nào, phần này sẽ bao gồm hướng dẫn cài đặt, hướng dẫn sử dụng,v.v. Việc có một thư mục dành riêng cho tài liệu giúp dự án rõ ràng và dễ duy trì hơn.

## Basic concepts of FastAPI

**Khái niệm và đặc điểm chính của FastAPI.** FastAPI là một framework web hiện đại và nhanh để để xây dựng API với Python, dựa trên type hints tiêu chuẩn của Python. Một số đặc điểm chính của FastAPI:

- Tốc độ: Đây là một trong những framework nhanh nhất để xây dựng API bằng Python, nhờ sử dụng Starlette cho phần web và Pydantic cho xử lý dữ liệu.

- Dễ sử dụng: FastAPI được thiết kế để dễ học, dễ code, giúp tăng tốc độ phát triển.

- Tài liệu tự động: Với FastAPI, tài liệu API được tự động sinh ra, vừa tiết kiệm thời gian, vừa cực kỳ hữu ích cho lập trình viên.

**Asynchronous programming (lập trình bất đồng bộ).** Một trong những tính năng mạnh mẽ nhất của FastAPI là hỗ trợ lập trình bất đồng bộ. Cho phép:

- Ứng dụng xử lý được nhiều request cùng lúc.

- Tránh việc một tác vụ chặn các tác vụ khác.

- Cải thiện hiệu năng tổng thể của ứng dụng.

Lập trình bất đồng bộ là một kiểu lập trình concurrent programming (chạy đồng thời), trong đó các tác vụ được thực hiện mà không chặn luồng xử lý chính.


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

Ở đây, ta dùng `async def` thay cho `def`, hành vi của code vẫn giống như trước, khi bạn truy cập `/`, hàm trả về `{"Hello": "World"}`. Nhưng nếu sau này bạn cần gọi các tác vụ I/O bất đồng bộ (ví dụ: gọi API khác, query DB bất đồng bộ), thì việc dùng `async` sẽ giúp ứng dụng tối ưu và nhanh hơn.

**Endpoints.** Là những điểm mà tại đó diễn ra sự tương tác với API. Trong FastAPI, một endpoint được tạo ra bằng cách trang trí (decorating) một hàm với một HTTP method, chẳng hạn như `app.get("/")`. Điều này có nghĩa là một yêu cầu GET sẽ được gửi tới root `("/")` của ứng dụng.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

Trong đoạn code này, chúng ta đang định nghĩa một endpoint cho URL gốc `("/")`. Khi có một yêu cầu GET được gửi đến URL này, hàm `read_root` sẽ được gọi và trả về một phản hồi dạng JSON.

**Routers.** Khi chúng ta cần xử lý nhiều endpoint nằm ở các file khác nhau, chúng ta có thể tận dụng routers. Routers giúp nhóm các endpoint thành những module riêng biệt, từ đó làm cho codebase dễ bảo trì và dễ hiểu hơn. Ví dụ, chúng ta có thể dùng một router cho các thao tác liên quan đến users và một router khác cho các thao tác liên quan đến products.

Để định nghĩa một router, trước hết hãy tạo một file mới trong thư mục dự án của bạn với tên `router.py`. Sau đó, tạo router như sau:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

Giờ đây bạn có thể tái sử dụng router này và gắn chúng vào instance FastAPI trong file `main.py`.

```python
from fastapi import FastAPI
import routers

app = FastAPI()

app.include_router(routers.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

Lúc này, bạn đã có code để chạy server, trong đó bao gồm router cho endpoint `GET / items` được import từ một module khác.

**Chạy server FastAPI.** Để chạy ứng dụng FastAPI, bạn chỉ cần cho Uvicorn biết instance của ứng dụng. Nếu file của bạn có tên là `main.py` và instance FastAPI được gọi là app, bạn có thể khởi động server ở cấp thư mục bằng lệnh sau:

```bash
$ uvicorn main:app --reload
```

Tham số `--reload` sẽ làm cho server tự động khởi động lại sau mỗi lần thay đổi code, rất hữu ích cho lập trình viên. Khi server đã chạy, bạn có thể truy cập API của mình tại [[http://127.0.0.1.8000](http://127.0.0.1.8000)]. Nếu bạn mở URL trong trình duyệt, bạn sẽ thấy phản hồi JSON từ endpoint `"/"` mà chúng ta vừa tạo.

Một trong những tính năng thú vị nhất của FastAPI là tài liệu tự động. Khi bạn chạy ứng dụng FastAPI, hai giao diện tài liệu sẽ được tạo sẵn:

- Swagger UI: [[http://127.0.0.1.8000/docs](http://127.0.0.1.8000/docs)]

- Redoc: [[http://127.0.0.1.8000/redoc](http://127.0.0.1.8000/redoc)]

Hai giao diện này cung cấp một cách tương tác trực quan để khám phá API và kiểm thử các chức năng của chúng.

## Defining first API endpoint

Khi bạn đã nắm được những kiến thức cơ bản về FastAPI và môi trường phát triển đã sẵn sàng, bây giờ chúng ta sẽ đi chi tiết về việc khởi tạo endpoint đầu tiên. Đây chính là nơi sức mạnh thật sự của FastAPI, bạn có thể xây dựng được một endpoint API hoạt động, sẵn sàng phản hồi các HTTP request một cách dễ dàng. 

Trong web API, GET request có lẽ là phổ biến nhất. Chúng được sử dụng để lấy dữ liệu từ server. Trong FastAPI, việc xử lý một GET request rất đơn giản và trực quan. Giả sử bạn đang xây dựng API cho một cửa hàng sách. Endpoint đầu tiên sẽ cung cấp thông tin về một cuốn sách dựa trên ID.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "Machine Learning Basic",
        "author": "Scott Mc"
    }
```

Trong đoạn mã trên, decorator `@app.get("/books/{book_id}")` báo cho FastAPI rằng hàm này sẽ phản hồi các GET request tại đường dẫn `/books/{book_id}`. Phần `{book_id}` trong path được gọi là path parameter, được dùng để truyền giá trị tự động. FastAPI sẽ tự động lấy giá trị `book_id` từ URL và truyền vào hàm của bạn.

Hãy chú ý đến `book_id: int` đây là một type hints, FastAPI sử dụng type hint này để kiểm tra dữ liệu. Nếu request gửi lên mà `book_id` không phải số nguyên, FastAPI sẽ tự động trả về lỗi kèm thông báo chi tiết. 

Sau khi định nghĩa endpoint GET, bạn có thể chạy ứng dụng FastAPI bằng uvicorn giống như trước. Như đã được đề cập FastAPI tự động sinh tài liệu API dạng tương tác với Swagger UI. Công cụ này cho phép kiểm thử endpoint API trực tiếp từ trình duyệt mà không cần viết thêm code. Bạn có thể dễ dàng kiểm tra ngay endpoint `/books/{book_id}` vừa tạo trong đó.

**Sử dụng Swagger UI.** Truy cập [[http://127.0.0.1.8000/docs](http://127.0.0.1.8000/docs)], ở đó endpoint `/books/{book_id}`. Hãy click vào chúng và thử nhập một `book_id` bất kì, rồi chạy thử. Bạn sẽ thấy reponse API trả về.

**Sử dụng ứng dụng Postman.** Postman là một API client cho phép xây dựng, kiểm thử tài liệu hóa API một cách chi tiết hơn. Tải và cài đặt Postman từ [[https://www.postman.com/downloads/](https://www.postman.com/downloads/)]. Sau khi cài đặt: (1) tạo một request mới; (2) chọn method là GET; (3) đặt URL là endpoint FastAPI của bạn `http://127.0.0.1:8000/books/1`; (4) Nhấn send và nhận phản hồi từ server FastAPI.

## Path parameters and query parameters

Một trong những khía cạnh quan trọng của phát triển API là xử lý paramters. Parameters cho phép API nhận input từ người dùng, giúp endpoints trở nên động và linh hoạt hơn. 

**Path parameters.** Là những phần trong URL được kỳ vọng sẽ thay đổi. Ở đây với endpoint `/authors/{author_id}`, thì `author_id` chính là một parameter. FastAPI cho phép lấy giá trị của parameter này một cách dễ dàng và sử dụng trong hàm của mình. Giá trị `name` không thay đổi, nhưng `author_id` sẽ là giá trị được truyền vào từ request.

```python
@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Nguyen Thai Hoc"
    }
```

**Query parameters.** Được dùng để tinh chỉnh hoặc tùy biến phản hồi của API, chúng được thêm vào URL sau dấu ?. Ví dụ `/books?genre=ai&year=2025` có thể trả về danh sách những sách phát hành năm 2025 và thuộc thể loại AI. 

```python
@app.get("/books")
async def read_book(year: int=None):
    if year:
        return {
            "year" : year,
            "books" : ["Deep Learning", "Computer Vision"]
        }
    
    return {"books": ["All Books"]}
```

Ở đây, `year` là một query parameter tùy chọn, khi gán giá trị mặc định là `None` chúng trở thành optional, nếu người dùng truyền `year` endpoint sẽ trả về danh sách của năm đó, nêu không chúng sẽ trả về tất cả các sách.

## Defining request and respone models

**Pydantic models.** Pydantic models là một tính năng mạnh mẽ cho việc xác thực và chuyển đổi dữ liệu. Chúng cho phép bạn định nghĩa cấu trúc, kiểu dữ liệu, và các ràng buộc của dữ liệu mà ứng dụng xử lý, cả cho request đến và response đi.

**Tạo models.** Tạo một class kế thừa BaseModel của Pydantic cho ứng dụng của bạn trong file có tên là `models.py`.

```python
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int
```

Ở đây, Book là một class kế thừa từ Pydantic BaseModel với ba trường: title, author và year. Mỗi trường được khai báo kiểu dữ liệu riêng, đảm bảo rằng bất kỳ dữ liệu nào tuân theo model này sẽ có các thuộc tính với kiểu dữ liệu đã được chỉ định.

**Request body.** Trong FastAPI, các Pydantic models không chỉ được dùng để xác thực mà còn đóng vai trò là request body.

```python
from models import Book

@app.post("/book")
async def create_book(book: Book):
    return book
```

Trong endpoint này, khi người dùng gửi một POST request đến endpoint `/book` với dữ liệu JSON, FastAPI sẽ tự động phân tích và xác thực dựa trên model Book. Nếu dữ liệu không hợp lệ, người dùng sẽ nhận được một phản hồi lỗi tự động.

**Xác thực dữ liệu request.** Pydantic còn cung cấp các tính năng xác thực nâng cao. Ví dụ, có thể thêm regex validation, giá trị mặc định...

```python
from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=1000)
    author: str = Field(..., min_length=1, max_length=1000)
    year: int = Field(..., gt=1900, lt=2100)
```

Bạn có thể xem chi tiết các tính năng xác thực ở tài liệu chính thức của Pydantic [[https://docs.pydantic.dev/latest/concepts/fields/](https://docs.pydantic.dev/latest/concepts/fields/)]. 

**Quản lý response formats.** FastAPI cho phép định nghĩa response models một cách rõ ràng, đảm bảo dữ liệu được trả về bởi API của bạn khớp với một schema cụ thể. Điều này rất cần thiết trong việc loại bỏ dữ liệu nhạy cảm hoặc tái cấu trúc response.

```python
from pydantic import BaseModel

class BookResponse(BaseModel):
    title: str
    author: str

@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        {"id": 1, "title": "Machine Learning", "author": "Chip Huyen"},
        {"Id": 2, "title": "Computer Vision", "author": "Kaparthy"}
    ]
```

Phần `-> list[BookReponse]` trong khai báo kiểu trả về của hàm cho FastAPI biết rằng phải sử dụng model BookReponse cho response, đảm bảo chỉ có các trường title và author được đưa vào JSON trả về.

Ngoài ra, bạn có thể chỉ định response trực tiếp trong decorator của endpoint như sau:

```python
@app.get("/allbooks", response_model=list[BookResponse])
async def read_all_books() -> Any:
    return [
        {"id": 1, "title": "Machine Learning", "author": "Chip Huyen"},
        {"Id": 2, "title": "Computer Vision", "author": "Kaparthy"}
    ]
```

## Handling errors and exceptions

FastAPI cung cấp và hỗ trợ cho việc xử lý ngoại lệ và lỗi. Khi một lỗi xảy ra, FastAPI trả về một phản hồi JSON chứa chi tiết về lỗi, điều này rất hữu ích cho việc gỡ lỗi. Tuy nhiên, có những tình huống bạn có thể muốn tùy chỉnh các phản hồi lỗi này để mang lại trải nghiệm người dùng tốt hơn hoặc đảm bảo bảo mật.

```python
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "OOPs ! Something went wrong"
        }
    )

```

Trong ví dụ này, hàm `http_exception_handler` sẽ được dùng để xử lý các lỗi `HTTPException`. Bất cứ khi nào một lỗi `HTTPException` được raise ở bất kỳ đâu trong ứng dụng của bạn, FastAPI sẽ dùng bộ xử lý này để trả về một phản hồi tùy chỉnh.

```python
@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)
```

Endpoint này sẽ ném ra phản hồi lỗi HTTP để minh họa thông báo đã được tùy chỉnh ở bước trước đó.

Như đã thảo luận trong phần Pydantic, FastAPI sử dụng cac model của Pydantic để xác thực dữ liệu. Khi một request đươc gửi với dữ liệu không tuân theo model đã định nghĩa, FastAPI sẽ raise một ngoại lệ và trả về phản hồi lỗi. Trong một số trường hợp, bạn có thể muốn tùy chỉnh phản hồi cho các lỗi xác thực.

```python
import json
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import PlainTextResponse

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(
    request: Request,
    exc: ResponseValidationError
):
    return PlainTextResponse(
        "This is a plain text response:"
        f"\n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST
    )
```

Bộ xử lý tùy chỉnh này sẽ bắt bất kỳ lỗi RequestValidationError nào và trả về một phản hồi chi tiết của lỗi. Giả sử bạn thử gọi endpoint `POST /book` với giá trị title là một số thay vì một chuỗi, bạn sẽ nhận được phản hồi với mã lỗi trạng thái 422.

```python
@app.post("/book")
async def create_book(book: Book):
    return ({
        "message": "Book created successfully !",
        "data": book
    })
```

