import json
import srt
from datetime import timedelta

MAX_WORD_TIME = 10
MIN_SUB_TIME = 1.5
MAX_SUB_TIME = 3


def gen_subs(filename):
    with open(filename+"-out.json", "r") as in_file:
        words = json.loads(in_file.read())["words"]
        print(words)

    index = 0
    subtitle = ""
    start_time = 0
    end_time = 0
    subtitles = []

    for word in words:
        print(word)
        word["end_time"] = word["start_time "] + word["duration"]
        if word["duration"] < MAX_WORD_TIME:
            if start_time + MAX_SUB_TIME >= word["end_time"] and subtitle:
                subtitle += " "
                subtitle += word["word"]
                end_time = max(word['end_time'], start_time + MIN_SUB_TIME)
            elif subtitle:
                index += 1
                subtitles.append(srt.Subtitle(index, timedelta(seconds=start_time), timedelta(seconds=end_time), subtitle))
                subtitle = ""

            if not subtitle:
                start_time = word['start_time ']
                subtitle += word['word']
                end_time = max(word['end_time'], start_time + MIN_SUB_TIME)

    if subtitle:
        subtitles.append(srt.Subtitle(index, timedelta(seconds=start_time), timedelta(seconds=end_time), subtitle))

    # subtitles = list(srt.sort_and_reindex(subtitles))

    with open(filename+".srt", "w") as f:
        f.write(srt.compose(subtitles, reindex=True, start_index=1, strict=True))
