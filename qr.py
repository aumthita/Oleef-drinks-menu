# สร้างไฟล์ QR จาก URL
# วิธีใช้:
#   pip install qrcode[pil]
#   python qr.py "https://your-domain.example"
import sys, qrcode
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        url = sys.argv[1].strip()
    else:
        url = input("URL สำหรับเข้าชมเว็บ: ").strip()
    if not url:
        raise SystemExit("กรุณาระบุ URL")
    img = qrcode.make(url)
    img.save("qr.png")
    print("สร้างไฟล์ qr.png เรียบร้อย")
