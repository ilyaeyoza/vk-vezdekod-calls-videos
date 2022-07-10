import time
from helper import VK

vk = VK()
upcoming = []
live = []
finished = []

def checker():
    last = vk.videosInGroup(comminuty_id)['items']
    print(last)
    for v in last:
        if 'live' not in v.keys():
            continue

        if 'live_status' not in v.keys():
            continue

        video_id = v['id']
        status = v['live_status']
        if status == 'upcoming':
            if video_id not in upcoming:
                upcoming.append(video_id)
                print(f'В сообществе запланирована трансляция "{v["title"]}"')

        if status == 'started':
            if video_id in upcoming and video_id not in live:
                live.append(video_id)
                print(f'В сообществе начата трансляция "{v["title"]}"')

        if status == 'finished':
            if (video_id in upcoming or video_id in live) and video_id not in finished:
                finished.append(video_id)
                print(f'В сообществе закончена трансляция "{v["title"]}"')

def main():
    while True:
        try:
            checker()
            time.sleep(60)
        except:
            main()


if __name__ == '__main__':
    comminuty_id = int(input('Цифровой идентификатор сообщества, за которым нужно следить: '))
    main()