
import youtube_dl
import json

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=6Dh-RL__uN4'])

# a =['https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s', 'https://www.youtube.com/watch?v=Wv2rLZmbPMA']
# for items in a:
#     q = ydl.extract_info(items)
#     with open('tr.json', 'w') as outfile:
#         json.dump(q, outfile)