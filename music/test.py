import youtube_dl
import json

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    x = ydl.download('https://www.youtube.com/watch?v=6Dh-RL__uN4')