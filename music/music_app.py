from youtube_dl import YoutubeDL
import json
from pyglet.media import Source, Player, load
player = Player()
menu = {
    '1.' : 'show all song:',
    '2.' : 'show detail of a song',
    '3.' : 'play a song',
    '4.' : 'search and download songs',
    '5.' : 'exit'
}
while True:
    for k,v in menu.items():
        print(k,v)
    x = input('ban muon lam gi:')
    if x =='5':
        break
    if x =="4":
        search = input('ten bai hat:')
        options = {
        'default_search': 'ytsearch5'
        }

        ydl = YoutubeDL(options)
        search_result = ydl.extract_info(search, download=False )
        with open('app.json', 'w') as outfile:
            json.dump(search_result, outfile)
        with open('app.json') as json_data:
            d = json.load(json_data)
        n = 0
        for items in d['entries']:
            n +=1
            print(n,'.',items['title'])
        pick = input('pick a song:')
        if pick == '1':
            ydl_opts = {
                'outtmpl': '%(id)s', # lấy tên file đown về là id của video
  	            'postprocessors': [{
                    'key': 'FFmpegExtractAudio', # Tách lấy audio
                    'preferredcodec': 'mp3', # Format ưu tiên là mp3
                    'preferredquality': '192', # Chất lượng bitrate
                }],

            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([d['entries'][0]['webpage_url']])
        if pick == '2':
            ydl_opts = {
                'outtmpl': '%(id)s', # lấy tên file đown về là id của video
  	            'postprocessors': [{
                    'key': 'FFmpegExtractAudio', # Tách lấy audio
                    'preferredcodec': 'mp3', # Format ưu tiên là mp3
                    'preferredquality': '192', # Chất lượng bitrate
                }],
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([d['entries'][1]['webpage_url']])
        if pick == '3':
            ydl_opts = {
                'outtmpl': '%(id)s', # lấy tên file đown về là id của video
  	            'postprocessors': [{
                    'key': 'FFmpegExtractAudio', # Tách lấy audio
                    'preferredcodec': 'mp3', # Format ưu tiên là mp3
                    'preferredquality': '192', # Chất lượng bitrate
                }],
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([d['entries'][2]['webpage_url']])
        if pick == '4':
            ydl_opts = {
                'outtmpl': '%(id)s', # lấy tên file đown về là id của video
  	            'postprocessors': [{
                    'key': 'FFmpegExtractAudio', # Tách lấy audio
                    'preferredcodec': 'mp3', # Format ưu tiên là mp3
                    'preferredquality': '192', # Chất lượng bitrate
                }],
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([d['entries'][3]['webpage_url']])
        if pick == '5':
            ydl_opts = {
                'outtmpl': '%(id)s', # lấy tên file đown về là id của video
  	            'postprocessors': [{
                    'key': 'FFmpegExtractAudio', # Tách lấy audio
                    'preferredcodec': 'mp3', # Format ưu tiên là mp3
                    'preferredquality': '192', # Chất lượng bitrate
                }],
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([d['entries'][4]['webpage_url']])
    if x =='3':
        source = load('AOAtz8xWM0w.mp3')
        player.queue(source)
        player.play()
        abc = input('Press any key to exit')
        player.stop()
        
        
        

            
       



        



    