import requests
from bs4 import BeautifulSoup
import json

def get_data(url):

    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101Firefox/123.0"
    }

    # response = requests.get(url, headers)
    #
    # with open("projects.html", "w") as file:
    #     file.write(response.text)

    with open("projects.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'html.parser')
    cards = soup.find_all('div', class_='card-content')

    project_cards = []

    for card in cards:
        project_url = card.find('a', class_='card-footer-item', string='Apply').get('href')
        project_cards.append(project_url)

    project_data_list = []

    for project_card in project_cards:
        req = requests.get(project_card, headers)
        project_name = project_card.split('/')[-1]

        with open(f'data/{project_name}', 'w') as file:
            file.write(req.text)

        with open(f'data/{project_name}') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'html.parser')
        project_data = soup.find('section', class_='section')

        try:
            project_title = project_data.find('h1', class_='title is-2').text
        except Exception:
            project_title = 'No title'

        try:
            project_company = project_data.find('h2', class_='subtitle is-4 company').text
        except Exception:
            project_company = 'No company'

        try:
            project_description = project_data.find('div', class_='content').find('p').text
        except Exception:
            project_description = 'No description'

        try:
            project_location = project_data.find('div', class_='content').find('p', id='location').text.split(':')[-1].strip()
        except Exception:
            project_location = 'No location'

        try:
            project_post_time = project_data.find('div', class_='content').find('p', id='date').text.split(':')[-1].strip()
        except Exception:
            project_post_time = 'No post time'

        project_data_list.append(
            {
                'Vacancy name: ': project_title,
                'Vacancy company: ': project_company,
                'Vacancy description: ': project_description,
                'Vacancy location: ': project_location,
                'Vacancy post date: ': project_post_time
            }
        )

    with open('data/projects_data.json', 'a', encoding='utf-8') as file:
        json.dump(project_data_list, file, indent=4)

def main():
    get_data("https://realpython.github.io/fake-jobs/")
if __name__=='__main__':
    main()
