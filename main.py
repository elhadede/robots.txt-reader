import requests as r

info = []
json = {}
def main(url):
    resp = r.get(url)
    for i in str(resp.text).split("\n"):
        if not i.startswith("#") and i:
            info.append(i)
    for i in info:
        i = i.split(": ")
        if len(i) == 2:
            if not i[0] in json:
                json[i[0]] = [i[1]]
            else:
                json[i[0]].append(i[1])
    
if __name__ == "__main__":
    main("https://youtube.com/robots.txt")
    print(json)