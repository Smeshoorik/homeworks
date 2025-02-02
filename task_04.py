# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

import random 
from datetime import time, timedelta
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

#сделала максимально универсальное решение, чтобы можно было составить случайный плэйлист из разного количества песен
num_songs = 3 
playlist=[0]*num_songs
items_num = 0

# добавила условие отсутствия повторов одной и той же песни в плейлисте
while True:
    playlist_queue = random.choice (my_favorite_songs)
    song_exist = False
    for i in playlist:
        if playlist_queue == i:
            song_exist = True
            break
    if not song_exist:
        items_num += 1
        playlist[items_num-1]=playlist_queue
    if items_num == num_songs:
        break

common_min=0
common_sec=0
for song in playlist:
    duration = str(song[1])
    minsec=duration.split('.')

    if len(minsec[1]) < 2:
        minsec[1]+='0'
    min=int(minsec[0])
    sec=int(minsec[1])
    common_min += min
    common_sec += sec
minplus=common_sec // 60
common_sec %= 60
common_sec=str(common_sec)
if len (common_sec) < 2:
    common_sec = '0'+ str(common_sec)
common_min += minplus
print (playlist) # печать плейлиста, чтобы увидеть созданный плейлист и проверить, правильно ли складываются длительности
print (f"{common_min}.{common_sec}")
