import requests
from tkinter import *
from time import time
from random import randint
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from io import BytesIO


def get_soup_from_link(page: int = 0, res_x: int = 1920, res_y: int = 1080):
    base = f"https://anime-pictures.net/pictures/view_posts/{page}?res_x={res_x}&res_y={res_y}&lang=en"
    content = requests.get(base).content
    soup = BeautifulSoup(content, "lxml")  # # get base link and transform it to soup
    return soup


# get total amount of available pages
# go to page chosen from total scope, i.e. 0 - max
# look for all the posts, choose one at random and return final link to the img post
def get_rndm_img_page(res_x: int = 1920, res_y: int = 1080):
    soup = get_soup_from_link(res_x=res_x, res_y=res_y)
    pages = [page.string for page in soup.body.p.contents if page.string.isdigit()]  # all pages

    rndm_page = get_soup_from_link(randint(0, int(pages[-1])), res_x=res_x, res_y=res_y)  # roll a page
    img_links = []
    for img_link in rndm_page.find_all('a'):
        i = img_link.get("href")  # get all links
        if "view_post" in i and i[21] != "0" and "view_posts" not in i:  # skip falsy links
            index = i[21:i.find("?")]  # get ID of the image
            if (index, i) not in img_links:  # skip duplicates
                img_links.append((index, i))

    random_link_appendix = img_links[randint(0, len(img_links))]  # roll 1 random image
    random_link = "https://anime-pictures.net" + random_link_appendix[1]  # make final link
    return random_link


def get_image(link: str):
    soup = get_soup_from_link(link)  # TODO: implement image return
    pass

get_rndm_img_page(3200, 5000)


# test_img = "https://images.anime-pictures.net/686/6860ac3e69d773d950679c3e473575d2.png?if=ANIME-PICTURES.NET_-_777379-1883x4500-re%3Azero+kara+hajimeru+isekai+seikatsu-white+fox-echidna+%28re%3Azero%29-jun+%28aousa0328%29-single-long+hair.png"


# root = Tk()
# root.geometry("1920x1080")

# scroll = Scrollbar(root)
# scroll.pack(side=RIGHT, fill=Y)

# a = requests.get(test_img).content  # get image content
# img = Image.open(BytesIO(a))  # is it streamed to bytes or wtf?
# img_x = img.size[0]
# img_y = img.size[1]
# resized_img = img.resize((int(img_x / 100 * 10), int(img_y / 100 * 10)))
# img_tk = ImageTk.PhotoImage(resized_img)

# label = Label(image=img_tk)
# label.pack()

# root.mainloop()