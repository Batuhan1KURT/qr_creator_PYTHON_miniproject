# Import the qrcode library
import qrcode

# Install  | pip install qrcode[pil] |  library to change the colors etc.

# Get the URL from user input
url_input = input("Enter the link to create QR code: ")

# Create a QRCode instance with customized options
qrc = qrcode.QRCode(
    version=2,  # Adjust the QR code version (controls the size)
    error_correction=qrcode.ERROR_CORRECT_L,  # Error correction level
    box_size=5,  # Size of each box in the QR code
    border=2  # Width of the border around the QR code
)

# Add the data (URL) to the QR code
qrc.add_data(url_input)

# Generate the QR code image with custom colors
qr_img = qrc.make_image(fill_color="red", back_color="black")

# Save the QR code image as "git_qr.png"
qr_img.save("git_qr.png")

# Print a message to indicate successful QR code creation and saving
print("QR code generated and saved as git_qr.png")

