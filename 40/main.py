from helpers import Helper, count, counter, include_counter, save
import math
import time

timeout = 0.5

def main():
    start = h.comments(owner_id=owner_id, video_id=video_id, page=0)
    count_comments = start['count']
    more = count_comments-count

    if more < 0:
        if mode == 1:
            res = counter(start['items'], searches)

        res = include_counter(start['items'], searches)
        save(start['items'], res)
        return res

    all = start['items']

    i = math.ceil(more/count)
    for n in range(1, i+1):
        c = h.comments(owner_id=owner_id, video_id=video_id, page=n)
        all += c
        time.sleep(timeout)

    if mode == 1:
        res = counter(all, searches)

    res = include_counter(all, searches)
    save(all, res)
    return res

def beauty(d):
    print('------------------------')
    for k in d.keys():
        print(f'{k}: {d[k]}')
        print('------------------------')

if __name__ == '__main__':
    h = Helper()
    ids = input('Введите идентификатор видео в формате <owner_id>_<video_id>: ')
    owner_id, video_id = [int(i) for i in ids.split('_')]
    searches = []
    i = 1
    while True:
        try:
            s = input(f'Введите вариант ответа {i} (enter для продолжения): ')
            if len(s) == 0:
                break
            searches.append(s)
            i+=1
        except:
            break

    mode = int(input('Режим счётчика, введите 1 - если нужно искать по полному совпадению ключей, 2 - если по содержанию ключа в комментарии: '))
    if mode < 1 or mode > 2:
        mode = 1

    if len(searches) > 0:
        beauty(main())