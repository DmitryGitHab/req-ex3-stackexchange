import requests
import time


def get_questions():
    url = f"https://api.stackexchange.com/2.3/questions?order=desc&min={round(time.time()-48*60*60)}&" \
          f"max={round(time.time())}&sort=activity&tagged=python&site=stackoverflow"
    response = requests.get(url)
    dict = response.json()['items']
    print('За последние два дня запрошены следующие темы по "Python"')
    for i in dict:
       print(i['title'])


if __name__ == '__main__':
    get_questions()
