import json


from parser_folder.parser import OframParser


def main():
    parser = OframParser()
    parser.parse_card()
    json_string = json.dumps(parser.card, ensure_ascii=False)
    with open("product_card.json", "w", encoding="utf-8") as f:
        f.write(json_string)
    print(json_string)
    print("Картинки сохранены в .../ofram-parser/название товара")


if __name__ == "__main__":
    main()

