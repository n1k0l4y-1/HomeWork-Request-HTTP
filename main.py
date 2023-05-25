import requests


# Задание 1

def smartest_hero(list_name_hero: list):
    api_ = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    j_api = api_.json()
    list_hero = sorted([[hero['powerstats']['intelligence'], hero['name']] for hero in j_api if list_name_hero.count(hero['name'])])
    return print(f'Самый умный супергерой - {list_hero[-1][1]}')


smartest_hero(['Hulk', 'Captain America', 'Thanos'])
print()





# Задание 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load

    def upload(self, disk_file_path, local_file_path):
        href = self.get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(href, data=open(local_file_path, 'rb'))
        if response.status_code == 201:
            print("Success")
            print()


if __name__ == '__main__':
    local_path_to_file = input('Введите локальный адрес файла: ')
    disk_path_to_file = input('Введите адрес Yandex Disk: ')
    TOKEN = input('Введите токен: ')
    uploader = YaUploader(token=TOKEN)
    uploader.upload(disk_path_to_file, local_path_to_file)





# Задание 3

def get_questions(page):
    url = f"https://api.stackexchange.com/2.3/questions?page={page}&pagesize=100&fromdate=1678752000&todate=1678924800&order=desc&sort=activity&tagged=Python&site=stackoverflow"
    response = requests.get(url)
    return response.json()


page = 1
has_more = True
while has_more:
    for question in get_questions(page)['items']:
        print(question['title'])
    page += 1
    has_more = get_questions(page)['has_more']