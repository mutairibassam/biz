import requests as r

def httpThreads():
    # for future automation we can simple change `biz` to any Board name
    # response stored in [sample.json] file
    res = r.get("https://a.4cdn.org/biz/threads.json")



