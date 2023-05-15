import tldextract

def func():
    url = input("Ввести URL: ")
    if url != "":
        extracted_info = tldextract.extract(url)
        print("Результат после экстракции:", extracted_info)
        print("Доменное имя", extracted_info.domain)
    else:
        print("Пустая строка")
        url = "https://github.com/W83w?tab=repositories"
        return url

