---
title: Lesson 01. Overview and Project Setup
---

<center markdown># Lesson 01. Overview and Project Setup</center>

## 🛠️ Technical Requirements
---

Để triển khai dự án FastAPI, hệ thống cần đáp ứng các thành phần nền tảng sau:

- **Python 3.9+**: Ngôn ngữ lập trình cốt lõi.
- **FastAPI**: Web framework chính.
- **Uvicorn**: Asynchronous Server Gateway Interface (ASGI) server tốc độ cao, dùng để khởi chạy ứng dụng.
- **IDE**: Integrated Development Environment (IDE) như VS Code, PyCharm, hoặc bất kỳ trình soạn thảo mã nguồn nào hỗ trợ Python.
- **API Client**: [Postman](https://www.postman.com/) (hoặc có thể dùng trực tiếp **Swagger UI** được tích hợp sẵn của FastAPI).
- **Git**: Công cụ quản lý phiên bản mã nguồn.

## 💻 Environment Setup
---

### Cài đặt Python

Tùy thuộc vào hệ điều hành, hãy thực hiện các bước dưới đây để cài đặt Python. Sau khi hoàn tất, luôn kiểm tra lại phiên bản để đảm bảo hệ thống đã nhận diện chính xác.

=== "Windows"

    - Truy cập [python.org](https://python.org) và tải file cài đặt phù hợp.
    - Mở file vừa tải. Tại màn hình cài đặt đầu tiên, **bắt buộc** đánh dấu chọn **Add Python to PATH** trước khi nhấn **Install Now**. Điều này cho phép chạy Python từ bất kỳ đâu trong **Command Prompt**.
    - Mở Command Prompt (`cmd`) và chạy lệnh kiểm tra. Nếu hiển thị phiên bản Python, quá trình cài đặt đã thành công:
    
    ```cmd
    python --version
    pip --version
    ```

=== "macOS"
    
    - Mở **Terminal** và chạy lệnh:
    
    ```bash
    brew install python
    ```
    
    - Kiểm tra phiên bản Python sau khi cài đặt:
    
    ```bash
    python3 --version
    pip3 --version
    ```

=== "Linux (Ubuntu/Debian)"
   
    - Cập nhật hệ thống và cài đặt:
    
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
    ```
    
    - Kiểm tra phiên bản Python sau khi cài đặt:
    
    ```bash
    python3 --version
    pip3 --version
    ```

### Khởi tạo Project & Môi trường ảo

Môi trường ảo (virtual environment) giúp cô lập các thư viện (dependencies) của từng dự án, tránh xung đột với hệ thống. Cụ thể, nó tạo ra một thư mục riêng chứa các thư viện cần thiết, tách biệt hoàn toàn với các dự án khác. Điều này giúp việc quản lý phiên bản thư viện trở nên dễ dàng và an toàn hơn.

=== "Windows"

    ```cmd
    mkdir fastapi-project
    cd fastapi-project
    python -m venv .venv
    .venv\Scripts\activate
    ```

=== "macOS / Linux"

    ```bash
    mkdir fastapi-project
    cd fastapi-project
    python3 -m venv .venv
    source .venv/bin/activate
    ```

Khi kích hoạt thành công, giao diện dòng lệnh (terminal) sẽ xuất hiện tiền tố `(.venv)` ở đầu dòng.

### Cài đặt FastAPI & Uvicorn

Chạy lệnh sau để cài đặt FastAPI cùng toàn bộ các thư viện phụ trợ được khuyến nghị (bao gồm cả `uvicorn`):

```bash
pip install "fastapi[all]"
```

## 📂 Project Structure
---

FastAPI không bắt buộc một cấu trúc thư mục cụ thể nào, nhưng dưới đây là chuẩn thiết kế phân lớp được khuyến nghị cho các dự án có khả năng mở rộng (scalable):

```text
fastapi-project/
├── src/                    # Chứa toàn bộ mã nguồn ứng dụng
│   ├── core/               # Cấu hình chung (config, security, database)
│   ├── models/             # Định nghĩa Database Models (SQLAlchemy, v.v.)
│   ├── schemas/            # Pydantic Models (Validate Data / Response)
│   ├── api/                # Chứa các Routers, Endpoints
│   ├── services/           # Logic nghiệp vụ (Business logic)
│   └── main.py             # File khởi chạy ứng dụng (Entry point)
├── tests/                  # Mã kiểm thử (Unit tests, Integration tests)
├── docs/                   # Tài liệu dự án
├── .venv/                  # Môi trường ảo (không commit lên Git)
├── .gitignore              # Các file/thư mục bỏ qua khi dùng Git
└── requirements.txt        # Danh sách thư viện phụ thuộc
```

## 🧠 Core Concepts
---

### Lập trình Bất đồng bộ (Asynchronous)

Nếu sử dụng hàm `def` thông thường, ứng dụng sẽ xử lý tuần tự. Điều này trở nên kém tối ưu khi có nhiều requests cần xử lý cùng lúc (ví dụ: request 2 phải đợi request 1 hoàn tất). FastAPI hỗ trợ mạnh mẽ `async / await`, cho phép xử lý hàng ngàn request đồng thời mà không chặn luồng chính, mang lại hiệu năng vượt trội. Về bản chất:

- `async`: Đặt từ khóa này trước hàm (`async def`) để báo cho Python biết đây không phải là hàm chạy tuần tự thông thường, mà là hàm có khả năng tạm dừng để nhường tài nguyên cho các tác vụ khác.
- `await`: Khi gặp từ khóa `await` bên trong hàm `async`, Python sẽ tạm dừng thực thi hàm đó, chuyển sang xử lý tác vụ khác cho đến khi tác vụ đang chờ hoàn tất.

**Lưu ý**: Khi viết một endpoint với `async def`, bên trong hàm nên có ít nhất một lệnh `await`. Nếu khai báo `async` nhưng không có `await`, hệ thống sẽ lãng phí tài nguyên vì đã kích hoạt chế độ bất đồng bộ mà không thực sự tận dụng nó.

### Endpoints

Endpoint là các điểm giao tiếp nơi các tương tác API diễn ra. Trong FastAPI, một endpoint được định nghĩa bằng cách gắn decorator (ký hiệu `@`) trước một hàm. Ví dụ, `@app.get("/")` tạo ra một endpoint cơ bản trong file `src/main.py`:

```python linenums="1"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```

Sử dụng lệnh `uvicorn` để khởi chạy server, với cú pháp `uvicorn <tên_module>:<tên_biến_app> --reload`:

```bash
uvicorn src.main:app --reload
```

Tùy chọn `--reload` giúp server tự động khởi động lại mỗi khi có thay đổi trong mã nguồn. Tính năng này rất hữu ích, nhưng chỉ nên dùng trong môi trường phát triển (development). 

FastAPI tự động sinh tài liệu API dựa trên chuẩn OpenAPI. Bạn có thể truy cập **Swagger UI** tại [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – một giao diện trực quan cho phép kiểm thử trực tiếp các API.

## 🔀 Routing & Parameters
---

### APIRouter

Khi ứng dụng phát triển lớn hơn, việc khai báo toàn bộ API trong `main.py` là không khả thi. `APIRouter` giúp phân chia và nhóm các endpoints thành các module riêng biệt.

Tạo file `src/api/items.py`:

```python linenums="1"
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
async def get_items():
    return ["Item 1", "Item 2"]
```

Gắn (include) router vừa tạo vào file chính `src/main.py`:

```python linenums="1"
from fastapi import FastAPI
from src.api import items

app = FastAPI()
app.include_router(items.router)
```

### Path & Query Parameters

Trong thực tế, **Path Parameters** và **Query Parameters** thường được kết hợp để giải quyết các bài toán truy vấn dữ liệu phức tạp.

- **Path Parameters**: Dùng để xác định một đối tượng hoặc danh mục cụ thể. Chúng mang tính định danh và **bắt buộc** phải có mặt trên URL.
- **Query Parameters**: Dùng để lọc (filter), sắp xếp (sort), hoặc phân trang (paginate). Chúng là **tùy chọn** và nằm sau dấu `?` trên URL.

**Ví dụ:** Xây dựng API cho hệ thống E-commerce, cần lấy danh sách sản phẩm thuộc danh mục `5` (`category_id = 5`), nhưng người dùng muốn:
- Lọc sản phẩm có giá tối thiểu (`min_price`).
- Chỉ hiện sản phẩm còn hàng (`in_stock=true`).
- Phân trang kết quả (`skip`, `limit`).

URL thực tế sẽ có dạng:  
`GET /categories/5/products?min_price=100&in_stock=true&skip=0&limit=20`

```python linenums="1"
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/categories/{category_id}/products")
async def get_products_by_category(
    category_id: int,                # Path Parameter: Trỏ đích xác vào danh mục số 5
    min_price: Optional[float] = 0,  # Query Parameter: Lọc giá tối thiểu
    in_stock: bool = True,           # Query Parameter: Lọc trạng thái còn hàng (mặc định True)
    skip: int = 0,                   # Query Parameter: Phân trang (bỏ qua X sản phẩm đầu)
    limit: int = 20                  # Query Parameter: Giới hạn số lượng trả về
):
    return {
        "category_id": category_id,
        "filters_applied": {
            "min_price": min_price,
            "in_stock": in_stock,
            "skip": skip,
            "limit": limit
        },
        "data": ["Product A", "Product B"] 
    }
```

Ở ví dụ này, `category_id` là thành phần bắt buộc của URL, trong khi các tham số sau dấu `?` giúp tinh chỉnh kết quả trả về một cách linh hoạt mà không cần tạo thêm các endpoints khác.

## 🛡️ Data Validation với Pydantic
---

**Pydantic** là cốt lõi của FastAPI trong việc định nghĩa cấu trúc, kiểm tra tính hợp lệ (validation) và ép kiểu dữ liệu cho request/response. Bằng cách khai báo kiểu dữ liệu một lần, Pydantic sẽ đảm nhận toàn bộ quá trình kiểm lỗi.

```python linenums="1"
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str
    year: int = Field(..., gt=1900, lt=2100) 

class BookResponse(BaseModel):
    title: str
    author: str

@app.post("/books", response_model=BookResponse)
async def create_book(book: BookCreate):
    return book 
```

**Phân tích kỹ thuật:**

- **`BookCreate`**: Định nghĩa cấu trúc dữ liệu người dùng gửi lên. `Field` được dùng để thêm các ràng buộc như giới hạn độ dài (`min_length`, `max_length`), hoặc khoảng giá trị (`gt` - lớn hơn, `lt` - nhỏ hơn).
- **`BookResponse`**: Định nghĩa cấu trúc dữ liệu trả về. Bằng cách không khai báo trường `year`, chúng ta có thể kiểm soát và ẩn thông tin này khỏi kết quả trả về.
- **Endpoint**: Tham số `book` tự động được xác thực theo `BookCreate`. Nếu client gửi thiếu dữ liệu hoặc sai kiểu (vd: `year` là chuỗi thay vì số), FastAPI sẽ ngắt quy trình và trả về lỗi **422 Unprocessable Entity** kèm chi tiết lỗi.

## ⚠️ Error Handling
---

FastAPI cung cấp ngoại lệ `HTTPException` để chủ động báo lỗi. Đồng thời, nó cho phép tùy biến (Custom Handlers) các lỗi mặc định để đảm bảo định dạng dữ liệu trả về luôn đồng nhất trên toàn hệ thống.

```python linenums="1"
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item không tồn tại")
    return {"item": item_id}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Dữ liệu đầu vào không hợp lệ", 
            "details": exc.errors()
        },
    )
```

**Phân tích kỹ thuật:**

- **Ném lỗi chủ động (`HTTPException`)**: Dùng khi dữ liệu đầu vào đúng kiểu, nhưng không hợp lệ về mặt nghiệp vụ (vd: yêu cầu `item_id` 105 trong khi kho chỉ có 100 món). Lệnh `raise HTTPException` lập tức dừng thực thi và trả về mã lỗi **404 Not Found** cho người dùng.
- **Tùy biến lỗi hệ thống (`exception_handler`)**: Khi người dùng gửi sai kiểu dữ liệu, Pydantic mặc định trả về lỗi 422 với cấu trúc khá phức tạp. Hàm `validation_exception_handler` sẽ "bắt" các lỗi này (`RequestValidationError`) và đóng gói lại thành định dạng JSON chuẩn hóa với mã lỗi **400 Bad Request**, tuân thủ theo thiết kế của dự án.

## 📚 Resources
---

1. [Creation of virtual environments](https://docs.python.org/3/library/venv.html)
2. [Git simple guide](https://rogerdudler.github.io/git-guide/)
3. [Concurrency and async / await](https://fastapi.tiangolo.com/async/)
4. [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
5. [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
6. [Pydantic](https://docs.pydantic.dev/latest/)
7. [Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/)
8. [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)


---

---