import os
import requests
from bs4 import BeautifulSoup
from src.config import select_category
import shutil


class OframParser:
    """Класс для получения и сохранения данных"""

    def __init__(self):
        self.__header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0 (Edition Yx 05)"}
        self.door_url = []
        self.card = []

    def get_door_url(self):
        """
        Парсинг ссылок на товары
        :return:
        Список ссылок товаров выбранной категории
        """
        response = requests.get(select_category(), headers=self.__header)
        soup = BeautifulSoup(response.text, "lxml")

        for link in soup.find_all("a", {"class": "door-item-link"}):
            self.door_url.append(link.get("href"))
        return self.door_url

    def parse_card(self):
        """
        Парсинг карточки товара
        """
        for link in self.get_door_url():
            response = requests.get(link, headers=self.__header)
            soup = BeautifulSoup(response.text, "lxml")
            title = soup.find("h2", {"class": "door-cart-title"}).text
            article = soup.find("span", {"class": "door-cart-attrs-title"}).text
            price = soup.find("h3", {"class": "price-new"}).text
            description = soup.find("div", {"class": "door-descr"}).text
            os.mkdir(title)

            for img in soup.find_all("img", {"class": "door-item-gallery-item"}):
                if img.get("src") != '':
                    image = img.get("src")
                    self.download_images(image, title)

            for img in soup.find_all("a", {"class": "gallery-popup-link"}):
                if img.get("href") != '':
                    image = img.get("href")
                    self.download_images(image, title)

            if price == "":
                price = "Нет цены"
            if description == "":
                description = "Нет описания"

            self.card.append({"article": article,
                              "title": title,
                              "description": description,
                              "price": price})

        return self.card

    @staticmethod
    def download_images(image, title):
        resp = requests.get(image, stream=True)
        image_name = os.path.basename(image)
        with open(os.path.join(title, image_name), 'wb') as file:
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, file)



