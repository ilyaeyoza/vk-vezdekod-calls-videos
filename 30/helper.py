import vk_api

class VK(object):
    def __init__(self):
        file = open('./access_token.txt', 'r')
        token = file.read()
        self.vk_session = vk_api.VkApi(token=token)

    def videosInGroup(self, group_id):
        res = self.vk_session.method('video.get', dict(owner_id=group_id, count=5))
        return res