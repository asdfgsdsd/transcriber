import subprocess

import pornhub
import youtube_dl

NUM_VIDEOS = 7
DOWNLOAD = False

search_keywords = []

client = pornhub.PornHub(keywords=search_keywords, pro=True, sort="mv", timeframe="a")

ydl_opts = {'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav'
    }], "outtmpl": "%(id)s.%(ext)s"}

filenames = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for video in client.getVideos(NUM_VIDEOS, page=1):
        vid_url = video['url']
        filename = vid_url.split("=")[-1] + ".wav"
        if DOWNLOAD:
            try:
                ydl.download([vid_url])
                filenames.append(filename)
            except youtube_dl.utils.DownloadError:
                print("Download failed for "+vid_url)
        else:
            filenames.append(filename)

for filename in filenames:
    out_file = open(filename.replace(".wav", "-out.json"), "w")
    print(filename)
    subprocess.run(['deepspeech', '--model', 'deepspeech-0.6.1-models/output_graph.pbmm',
                    '--lm', 'deepspeech-0.6.1-models/lm.binary', '--trie', 'deepspeech-0.6.1-models/trie', '--audio',
                    filename, '--json'], stdout=out_file)
