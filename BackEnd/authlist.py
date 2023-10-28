# Tạo list các id
auths = []

# Hàm kiểm tra tính trùng lặp
def check_auth(id):
  for n in auths:
    if n == id:
      return False
  return True

# Hàm thêm id vào list
def add_to_authlist(id):
  if check_auth(id):
    auths.append(id)
  else:
    print("Số nguyên đã tồn tại trong list")

# Hàm xóa id khỏi list
def remove_from_authlist(id):
  if id in auths:
    auths.remove(id)
  else:
    print("Số nguyên không tồn tại trong list")

# In danh sách các id
def print_authlist():
  print("Danh sách các số nguyên:")
  for n in auths:
    print(n)