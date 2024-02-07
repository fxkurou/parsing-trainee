import json
import requests
from bs4 import BeautifulSoup

# url = 'https://realpython.github.io/fake-jobs/'
#
# headers = {
#    ' Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
# }
#
# response = requests.get(url)
# src = response.text
# print(src)
#
# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'html.parser')
all_jobs = soup.find_all(class_='card-footer-item', string='Apply')
all_titles = soup.find_all(class_='title is-5')

all_vacancies_dict = {}

for title, job in zip(all_titles, all_jobs):
    title_text = title.text
    job_href = job.get('href')
    all_vacancies_dict[title_text] = job_href

with open('all_vacancies.json') as file:
    # json.dump(all_vacancies_dict, file, indent=4, ensure_ascii=False)
    all_vacancies = json.load(file)


# all_jobs_list = []
# for item in all_jobs:
#     item_text = item.text
#     item_href = item.get('href')
#     if item_text == 'Learn': continue
#     all_jobs_list.append(item_href)
#
# with open('all_jobs_list.txt', 'w') as file:
#     for item in all_jobs_list:
#         file.write("%s\n" % item)
#
# print(all_jobs_list)

def search(dictionary, key_to_find):
    found_items = []

    for key, value in dictionary.items():
        if key == key_to_find:
            found_items.append(value)
        elif isinstance(value, dict):
            found_items.extend(search(value, key_to_find))

    return found_items

def main():
    inp = input("Enter vacancie name: ")
    res = search(all_vacancies, inp)
    print('Result: ', ' '.join(res))

if __name__ == "__main__":
    main()