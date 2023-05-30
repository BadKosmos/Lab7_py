from PIL import Image, ImageDraw, ImageFont

def proc1():
    with Image.open("postcard.jpg") as img:
        img.load()

    cropped_img = img.crop((135, 230, 635, 470))
    cropped_img.save("cropped_postcard.jpg")
    img.close()

def proc2():
    card_list = {1: "postcard.jpg", 2: "23f.jpg", 3: "8m.jpg", 4: "dr.jpg"}
    print("1 - New year\n 2 - 23 of february\n 3 - 8 of march\n 4 - Birth day")
    ans = int(input("Please, enter holiday numb : "))
    filename = card_list[ans]
    name = input("Please enter name: ")
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial_bold.ttf", 25)
    draw_text = ImageDraw.Draw(img)
    draw_text.text((img.width // 2 - 100, 15),name + ", congratulations!",font=font,fill=('#FAACAC'))
    img.show()
    img.save(filename.strip(".jpg")+"_"+name+".jpeg")
    img.close()


