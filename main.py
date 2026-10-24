
import qrcode

text = input("Enter text or website URL: ")
filename = input("Enter filename: ")

qr = qrcode.make(text)
qr.save(filename + ".png")

print("QR Code generated successfully!")
print("Saved as:", filename + ".png")
