import PIL
from PIL import Image,ImageDraw
import csv



with open('user_actions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # line_count = 0
    source_img = Image.open('img/level_test_bg.png')
    for row in csv_reader:
        if int(row[0]) == 32:
            draw = ImageDraw.Draw(source_img)
            draw.rectangle(((int(row[1]), int(row[2])), (int(row[1])+80, int(row[2])+80)), fill="red")
        if int(row[0]) == 275:
            draw = ImageDraw.Draw(source_img)
            draw.rectangle(((int(row[1]), int(row[2])), (int(row[1])+80, int(row[2])+80)), fill="blue")
        if int(row[0]) == 276:
            draw = ImageDraw.Draw(source_img)
            draw.rectangle(((int(row[1]), int(row[2])), (int(row[1])+80, int(row[2])+80)), fill="yellow")
        if int(row[0]) == 273:
            draw = ImageDraw.Draw(source_img)
            draw.rectangle(((int(row[1]), int(row[2])), (int(row[1])+80, int(row[2])+80)), fill="purple")
        if int(row[0]) == 114:
            draw = ImageDraw.Draw(source_img)
            draw.rectangle(((int(row[1]), int(row[2])), (int(row[1])+80, int(row[2])+80)), fill="green")
        # draw.text((20, 70), "something123", font=ImageFont.truetype("font_path123"))

        source_img.save('heat_map.jpeg', "JPEG")