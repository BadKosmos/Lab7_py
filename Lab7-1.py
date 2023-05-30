from PIL import Image


def proc1():

    filename = "be_legendary.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode

    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def proc2():

    filename = "be_legendary.jpg"
    with Image.open(filename) as img:
        img.load()
    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("resized_be_legendary.jpg")
    new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.save("rotate_be_legendary.jpg")
    new_img = img.rotate(180)
    new_img.save("180_be_legendary.jpg")

def proc3():

    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for i in range(1, 5):
        file_name = str(i) + ".jpg"
        with Image.open(file_name) as img:
            img.load()
            new_img = img.filter(Image.Filter.FIND_EDGES)
            new_img.show()
            new_img.save("new_" + str(i)+".jpg")

def proc4():

    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    with Image.open("watermark.png") as img_water:
        img_water.load()
    img_water = img_water.convert('RGBA')

    for i in range(1, 6):
        f_name = str(i) + ".jpg"
        with Image.open(f_name) as img:
            img.load()
        img = img.convert('RGBA')

        layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
        img_water = img_water.resize(img.size)
        layer.paste(img_water)
        layer2 = layer.copy()
        layer2.putalpha(128)
        layer.paste(layer2, layer)

        outp = Image.alpha_composite(img, layer)

        outp = outp.convert('RGB')
        outp.save("marked_" + str(i) + ".jpg")
        img.close()

    img_water.close()
