import cv2

# Địa chỉ IP của camera
camera_ip = "172.24.0.1"

# Thông tin đăng nhập (nếu cần)
username = "0356698045"  # Thay bằng username của camera nếu có
password = "Binh1991#"  # Thay bằng password của camera nếu có

# Tạo URL kết nối
# Định dạng phổ biến: rtsp://username:password@ip_address:port/path
# Hoặc http://ip_address:port/video
rtsp_url = f"rtsp://{username}:{password}@{camera_ip}:554/stream1"
# Hoặc có thể thử:
# http_url = f"http://{camera_ip}/video"

# Tạo đối tượng VideoCapture
cap = cv2.VideoCapture(rtsp_url)

# Kiểm tra xem kết nối có thành công không
if not cap.isOpened():
    print("Không thể kết nối đến camera. Vui lòng kiểm tra:")
    print("- Địa chỉ IP và cổng")
    print("- Thông tin đăng nhập")
    print("- Kết nối mạng")
    exit()

print("Kết nối camera thành công!")

# Đọc và hiển thị video từ camera
while True:
    ret, frame = cap.read()

    if not ret:
        print("Không nhận được frame. Kết thúc...")
        break

    # Hiển thị frame
    cv2.imshow('Camera IP', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()