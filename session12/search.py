from youtube_dl import YoutubeDL
import json
options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False )
with open('data.json', 'w') as outfile:
    json.dump(search_result, outfile)