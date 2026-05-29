# 1. PHÂN TÍCH INPUT / OUTPUT
# - Input: 
#   + Danh sách 'product_list' (chứa thông tin mã, tên, giá, số lượng).
#   + Biến 'option': Số nguyên từ 1 đến 5 do người dùng chọn menu.
#   + Dữ liệu nhập thêm: Mã SP (chuỗi), Tên (chuỗi), Giá và Số lượng (số nguyên).
# - Output:
#   + Menu hiển thị và bảng danh sách chi tiết các sản phẩm hiện có.
#   + Phản hồi trạng thái: Thêm/Sửa/Xóa thành công hoặc báo lỗi trùng mã, sai mã.
#
# 2. THIẾT KẾ GIẢI PHÁP & THUẬT TOÁN
# - Sử dụng .strip().upper() để chuẩn hóa mã SP, tránh lỗi gõ chữ thường/khoảng trắng.
# - Dùng vòng lặp `while` lồng bên trong để bắt buộc nhập Giá/Số lượng phải >= 0.

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

option = ''

while option != '5':
    print()
    print('===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====')
    print('1. Hiển thị danh sách sản phẩm')
    print('2. Thêm sản phẩm mới')
    print('3. Cập nhật thông tin sản phẩm')
    print('4. Xóa sản phẩm theo mã')
    print('5. Thoát chương trình')
    
    option = input('Nhập lựa chọn của bạn (1-5): ').strip()
    match option:
        case '1':
            print()
            if product_list == []:
                print('Danh sách sản phẩm hiện đang trống.')
            else:
                print('Danh sách sản phẩm hiện tại:')
                print(f"{'STT':<4} | {'Mã SP':<7} | {'Tên sản phẩm':<18} | {'Giá bán':<10} | {'Số lượng'}")
                print("-" * 60)
                for i, item in enumerate(product_list, start=1):
                    print(f"{i:<4} | {item['product_id']:<7} | {item['product_name']:<18} | {item['price']:<10,} | {item['quantity']}")
            print()
            
        case '2':
            print()
            found = False
            input_pro_id = input('Mời bạn nhập vào mã sản phẩm: ').strip().upper()

            for item in product_list:
                if input_pro_id == item['product_id']:
                    print('Mã sản phẩm đã tồn tại!')
                    found = True
                    break
                    
            if found == False:
                input_pro_name = input('Mời bạn nhập vào tên sản phẩm: ').strip()
                
                while True:
                    price_str = input('Mời bạn nhập giá sản phẩm: ').strip()
                    if price_str.isdigit():
                        input_pro_price = int(price_str)
                        break
                    print('Lỗi: Giá sản phẩm phải là số nguyên dương, vui lòng nhập lại!')
                
                while True:
                    qty_str = input('Nhập vào số lượng sản phẩm: ').strip()
                    if qty_str.isdigit():
                        input_pro_quantity = int(qty_str)
                        break
                    print('Lỗi: Số lượng sản phẩm phải là số nguyên dương, vui lòng nhập lại!')

                new_pro = {
                    "product_id": input_pro_id,
                    "product_name": input_pro_name,
                    "price": input_pro_price,
                    "quantity": input_pro_quantity
                }
                product_list.append(new_pro)
                print('Đã thêm sản phẩm thành công!')
            print()
            
        case '3':
            print()
            found = False
            input_id_search = input('Mời bạn nhập vào mã sản phẩm muốn cập nhật: ').strip().upper()

            for item in product_list:
                if input_id_search == item['product_id']:
                    found = True
                    item['product_name'] = input('Mời bạn nhập vào tên sản phẩm mới: ').strip()
                    
                    while True:
                        price_str = input('Mời bạn nhập giá sản phẩm mới: ').strip()
                        if price_str.isdigit():
                            item['price'] = int(price_str)
                            break
                        print('Lỗi: Giá sản phẩm phải là số nguyên dương, vui lòng nhập lại!')

                    while True:
                        qty_str = input('Nhập vào số lượng sản phẩm mới: ').strip()
                        if qty_str.isdigit():
                            item['quantity'] = int(qty_str)
                            break
                        print('Lỗi: Số lượng sản phẩm phải là số nguyên dương, vui lòng nhập lại!')
                        
                    print('Đã cập nhật thông tin sản phẩm thành công!')
                    break
                    
            if found == False:
                print('Không tìm thấy sản phẩm cần cập nhật!')
            print()
            
        case '4':
            print()
            found = False
            input_id_search = input('Mời bạn nhập vào mã sản phẩm muốn xóa: ').strip().upper()

            for item in product_list:
                if input_id_search == item['product_id']:
                    found = True
                    product_list.remove(item)
                    print(f'Đã xóa sản phẩm có mã {input_id_search} thành công!')
                    break
            
            if not found:
                print('Không tìm thấy mã sản phẩm cần xoá!')
            print()
        
        case '5':
            print('Đã thoát chương trình')
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
