from PIL import Image

foreground = Image.open("./images/eth-diamond-glyph.png")
background = Image.open("./images/background.png")

(img_h, img_w) = foreground.size

resize_back =  background.resize((img_h, img_w))

resize_back.paste(foreground, (0, 0), foreground)

resize_back.save("result.png","png")