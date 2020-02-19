import pornhub

search_keywords = ["pro"]

client = pornhub.PornHub(search_keywords)

with open("urls.txt", "w") as file:
    for video in client.getVideos(10, page=0):
        file.write(video['url'] + "\n")
