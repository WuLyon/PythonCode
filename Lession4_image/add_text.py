from PIL import Image, ImageDraw, ImageFont
import os

def add_text(image):
    draw_obj = ImageDraw.Draw(image)
    width, height = image.size
    font_path = r"C:\Windows\Fonts\Gabriola.ttf"
    font = ImageFont.truetype(font_path, size=100)
    color = "red"
    draw_obj.text((width/2, height/2), 'This is P7i', font=font, fill=color)
    image.save('result.jpg', 'jpeg')  # Saving in current working directory

if __name__ == "__main__":
    image = Image.open(os.path.join(os.path.dirname(__file__),'image.jpg'))
    add_text(image)