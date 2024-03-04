catalog_urls = {
    1: "https://ofram.ru/good-category/mezhkomnatnye-dveri/",
    2: "https://ofram.ru/good-category/protivopozharnye-dveri/",
    3: "https://ofram.ru/good-category/zvukoizolyacionnye-dveri/",
    4: "https://ofram.ru/good-category/furnitura/",
    5: "https://ofram.ru/good-category/plintus/",
    6: "https://ofram.ru/good-category/mebel/",
    7: "https://ofram.ru/good-category/boiserie/"
}


def select_category():
    """Выбор категории"""
    choice = int(input("Выберите категорию: \n"
                       "1 - МЕЖКОМНАТНЫЕ ДВЕРИ\n"
                       "2 - ПРОТИВОПОЖАРНЫЕ ДВЕРИ\n"
                       "3 - ЗВУКОИЗОЛЯЦИОННЫЕ ДВЕРИ\n"
                       "4 - ФУРНИТУРА\n"
                       "5 - ПЛИНТУС\n"
                       "6 - МЕБЕЛЬ\n"
                       "7 - БУАЗЕРИ ПАНЕЛИ\n"
                       "Любая другая цифра - выход из программы\n"))
    for key, value in catalog_urls.items():
        if choice == key:
            print(f"Ссылка категории - {value}")
            return value
    if choice != catalog_urls.keys():
        exit("Выход из программы")




