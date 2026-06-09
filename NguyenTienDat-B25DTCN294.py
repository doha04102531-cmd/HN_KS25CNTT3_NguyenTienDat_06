booking = [
    {'id': 'BK001',
     'name_room': 'Phòng Thảo Luận A',
     'name_room_booking': 'Phòng Marketing',
     'time_start': 9,
     'time_end': 12,
     'time' : 3,
     'phan_loai': 'Tiêu chuẩn'
    },
    {'id': 'BK002',
     'name_room': 'Phòng Xuất Bản B',
     'name_room_booking': 'Phòng Sản Xuất',
     'time_start': 5,
     'time_end': 10,
     'time' : 5,
     'phan_loai': 'Dài'
    },
    {'id': 'BK003',
     'name_room': 'Phòng Chiến Lược C',
     'name_room_booking': 'Phòng Idea',
     'time_start': 11,
     'time_end': 12,
     'time' : 2,
     'phan_loai': 'Ngắn'
    }
]
def display_booking(danh_sach):
    print("DANH SÁCH ĐẶT LỊCH")
    if danh_sach == []:
        print('Danh sách đặt lịch hiện đang trống')
    else:
        for lich in danh_sach:
            print(f"Mã BK: {lich['id']:<5} | Tên Phòng: {lich['name_room']:<18} | Người Đặt: {lich['name_room_booking']:<18} | Giờ Bắt Đầu: {lich['time_start']:<2} | Giờ Kết Thúc: {lich['time_end']:<2} | Thời lượng: {lich['time']:<2} | Phân Loại: {lich['phan_loai']}")

def phan_loai(time_bk):
    if int(time_bk) < 2:
        print('Ngắn')
    elif int(time_bk) > 2 and int(time_bk) < 4:
        print('Tiêu chuẩn')
    elif int(time_bk) > 4 and int(time_bk) < 6:
        print('Dài')
    elif int(time_bk) >6:
        print("Quá tải")
 
def add_booking(danh_sach):
    id_input = input('Nhập mã phòng: ')
    if id_input == '':
        print('Không để trống mã phòng')
        return
    else:
        for id in danh_sach:
            if id['id'] == id_input:
                print('Mã phòng đã có')
                return
            else:
                name_room_input = input('Nhập tên phòng:')
                if name_room_input == "":
                    print('Tên phòng không được để trống')
                else: 
                    name_room_booking_input = input('Nhập tên người đặt:')
                    if name_room_booking_input == '':
                        print('Tên người đặt không được để trống')
                        return
                    else:
                        gio_bat_dau = int(input('Nhập giờ bắt đầu:'))
                        if gio_bat_dau < 0 or gio_bat_dau > 24:
                            print('Thời gian trong khoảng 0 đến 24')
                        else:
                            gio_ket_thuc = int(input('Nhập giờ kết thúc:'))
                            if gio_ket_thuc < 0 or gio_ket_thuc > 24:
                                print('Thời gian trong khoảng 0 đến 24')
                            else:
                                time_bk = gio_ket_thuc - gio_bat_dau                
                                new_bk ={
                                    'id': id_input,
                                    'name_room': name_room_input,
                                    'name_room_booking': name_room_booking_input,
                                    'time_start': gio_bat_dau,
                                    'time_end': gio_ket_thuc,
                                    'time': time_bk,
                                    'phan_loai':phan_loai(time_bk)
                                }
                                danh_sach.append(new_bk)
                                print('Đặt lịch thành công')
                                break

def update_booking(danh_sach):
    check = -1
    update_input = input('Nhập mã BK cần cập nhật: ')
    for bk in danh_sach:
        if bk['id'] == update_input:
            bk['name_room']  = input('Nhập tên phòng cần cập nhật: ')
            bk['time_start'] = int(input('Nhập giờ bắt đầu cần cập nhật:'))
            bk['time_end']   = int(input('Nhập giờ kết thúc cần cập nhật:'))
            bk['time'] = bk['time_end'] - bk['time_start']
            bk['phan_loai'] = phan_loai(bk['time'])
            check = 0
    if check == -1 :
        print('Không tìm thấy mã phòng')

def delete_booking(danh_sach):
    del_bk = input("Nhập mã phòng cần xóa:")
    for bk in danh_sach:
        if bk['id'] == del_bk:
            hal = input('Bạn có muốn xóa không (y/n)').lower()
            if hal == 'y':
                danh_sach.remomve(del_bk)

def thong_ke(danh_sach):
    ngan = 0
    tieu_chuan = 0
    dai=0
    qua_tai=0
    for bk in danh_sach:
        if bk['phan_loai'] == 'Ngắn':
            ngan += 1
        elif bk['phan_loai'] == 'Tiêu Chuẩn':
            tieu_chuan += 1
        elif bk['phan_loai'] == 'Dài':
            dai += 1
        else :
            qua_tai += 1
while True :
    choice = input('''
==================================
====  BẢNG CHỨC NĂNG BOOKING  ====
==================================
1.Hiển thị danh sách đặt lịch
2.Đặt ký lịch đặt phòng mới
3.Cập nhật thông tin lịch hẹn
4.Hủy/Xóa lịch đặt phòng
5.Tìm kiếm lịch đặt phòng
6.Thống kê mật độ sử dụng
7.Phân loại khung giờ tự động
8.Thoát
==================================    
Xin mời nhập lựa chọn của bạn: ''')
    
    match choice:
        case '1':
            display_booking(booking)
        case '2':
            add_booking(booking)
        case '3':
            update_booking(booking)
        case '4':
            delete_booking(booking)
        
        case 6:
            thong_ke(booking)

        case '8':
            print('Cảm ơn đã sử dụng')
            break
        case _:
            print('Lựa chọn không hợp lệ')
