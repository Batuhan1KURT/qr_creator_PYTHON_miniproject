# Import the qrcode library
import qrcode

# Get the URL from user input
url_input = input("Enter the link to create QR code: ")

# Generate the QR code image
qr_img = qrcode.make(url_input)

# Save the QR code image as "git_qr.jpg"
qr_img.save("git_qr.jpg")

# Print a message to indicate successful QR code creation and saving
print("QR code generated and saved as git_qr.jpg")