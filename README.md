# Hướng dẫn cài đặt Anaconda, Python và thiết lập môi trường làm việc

## 1. Giới thiệu

Anaconda là một bộ phân phối Python phổ biến, tích hợp sẵn Python cùng nhiều thư viện khoa học và công cụ quản lý môi trường rất tiện lợi. Sử dụng Anaconda giúp bạn dễ dàng quản lý phiên bản Python, thư viện và môi trường ảo.

---

## 2. Tải và cài đặt Anaconda

1. Truy cập trang chính thức:  
   [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

2. Chọn phiên bản phù hợp với hệ điều hành của bạn (Windows, macOS hoặc Linux).

3. Tải bộ cài và chạy để cài đặt.  
   **Lưu ý:** Trong quá trình cài đặt, chọn thêm tùy chọn “Add Anaconda to my PATH environment variable” (nếu có) để dễ dàng sử dụng `conda` từ terminal.

---

## 3. Kiểm tra cài đặt Anaconda và Python

Sau khi cài xong, mở **Anaconda Prompt** (Windows) hoặc terminal/macOS/Linux, chạy lệnh:

```bash
conda --version
python --version

```

## 4. Tạo môi trường ảo Python với conda

Để quản lý thư viện và dự án tốt hơn, bạn nên tạo một môi trường ảo riêng biệt cho mỗi dự án:

```bash
conda create -n myenv python=3.10

```

Kích hoạt môi trường bằng lệnh:

```bash
conda activate myenv

```

## 5. Cài đặt thư viện cần thiết trong môi trường

Để cài thư viện pydub và công cụ ffmpeg dùng xử lý âm thanh:

```bash
conda install -c conda-forge pydub ffmpeg

```

Nếu thư viện bạn cần không có sẵn trên conda, bạn có thể sử dụng pip trong môi trường conda:

```bash
pip install <tên-thư-viện>

```

## 6. Sử dụng môi trường và chạy script Python

Sau khi kích hoạt môi trường, bạn có thể chạy các script Python bình thường:

```bash
python your_script.py

```

Khi hoàn thành, bạn có thể thoát khỏi môi trường bằng lệnh:

```bash
conda deactivate

```

## 7. Quản lý môi trường conda

Liệt kê tất cả các môi trường đã tạo:

```bash
conda env list

```

Xóa môi trường không còn dùng:

```bash
conda remove -n myenv --all

```

## 8. Tài nguyên hỗ trợ

Trang chủ Anaconda: https://www.anaconda.com/

Tài liệu Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/

Tài liệu Python: https://docs.python.org/3/
