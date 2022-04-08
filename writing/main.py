import requests
from bs4 import BeautifulSoup
import json
listAlpha = [
    "lv1",
    "lv2",
    "lv3"
]
for alpha in listAlpha:
    f = open('essays/'+alpha+'/index.json', encoding="utf8")
    data = json.load(f)
    print(len(data))
    init = data[0:100]
    print(len(init))
    done = data[100:]
    print(len(done))
    with open('essays/'+alpha+'/init.json', 'w', encoding='utf-8') as f:
        json.dump(init, f, ensure_ascii=False, indent=4)

    with open('essays/'+alpha+'/done.json', 'w', encoding='utf-8') as f:
        json.dump(done, f, ensure_ascii=False, indent=4)

