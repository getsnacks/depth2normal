from PIL import Image

# JPG dosyasını aç
with Image.open("test_image.jpg") as img:
    # PNG olarak kaydet
    img.save("test_image.png", format="PNG")

print("Dönüştürme tamamlandı.")
