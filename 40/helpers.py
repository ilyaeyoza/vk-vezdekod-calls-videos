import vk_api
import datetime
import json

count = 100

class Helper(object):
    def __init__(self):
        file = open('./access_token.txt', 'r')
        token = file.read()
        self.vk_session = vk_api.VkApi(token=token)

    def comments(self, owner_id, video_id, page):
        thisComments = self.vk_session.method('video.getComments', dict(owner_id=owner_id, video_id=video_id, count = count, offset = page*count))
        return thisComments

def counter(d, keys):
    _d = {}
    for key in keys:
        _d[key] = 0

    for c in d:
        if c['text'] in keys:
            i = keys.index(c['text'])
            _d[keys[i]] += 1

    return _d

def include_counter(d, keys):
    _d = {}
    for key in keys:
        _d[key] = 0

    for c in d:
        for key in keys:
            if c['text'] in key:
                _d[key] += 1

    return _d

def save(d, res):
    timestamp = int(datetime.datetime.now().timestamp())
    path = f'./saves/{timestamp}.json'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(
            json.dumps(dict(items=d, res=res), indent=4)
        )
