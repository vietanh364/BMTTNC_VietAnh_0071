# lab-04 > hash > md5_library.py

import hashlib

def calculate_md5(input_string):
  """
  Hàm này tính toán mã băm MD5 cho một chuỗi đầu vào bằng thư viện hashlib.

  Args:
    input_string: Chuỗi ký tự cần băm.

  Returns:
    Chuỗi hex biểu diễn giá trị băm MD5.
  """
  # Tạo một đối tượng băm MD5 mới
  md5_hash = hashlib.md5()
  
  # Cập nhật đối tượng băm với chuỗi đầu vào đã được mã hóa thành utf-8
  md5_hash.update(input_string.encode('utf-8'))
  
  # Trả về giá trị băm dưới dạng chuỗi hex
  return md5_hash.hexdigest()

# Chương trình chính
if __name__ == "__main__":
  # Yêu cầu người dùng nhập chuỗi
  input_string = input("Nhập chuỗi văn bản: ")
  
  # Tính toán mã băm MD5
  md5_hash = calculate_md5(input_string)
  
  # In kết quả
  print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")
