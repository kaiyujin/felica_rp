import requests, json


def post_slack(url, message):
    requests.post(url, data = json.dumps({
        'text': message,
        'username': u'one-building-Bot',
        'icon_emoji': u':smile_cat:',
        'link_names': 1, 
    }))


if __name__ == '__main__':
    post_slack(url, u'test')
