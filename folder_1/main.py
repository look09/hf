import requests, json, time


mydict = {}
nekos = [
        'baka', 'bite', 'blush', 'bored', 'cry', 'cuddle',
        'dance', 'facepalm', 'feed', 'happy', 'hug', 'kiss',
        'laugh', 'pat', 'shrug', 'slap', 'sleep', 'smile',
        'smug', 'stare', 'think', 'thumbsup', 'tickle', 'wave',
        'wink'
    ]

nekos.sort(key=str.lower)

for i in nekos:
	k = []
	for n in range(50):
		res = requests.get(f'https://nekos.best/api/v1/{i}').json()
		print(n,i,":", res['url'])
		if res['url'] in k:
			pass
		else:
			k.append(res['url'])
		time.sleep(5)
	dic = {i:k}
	mydict.update(dic)
f = open('emotes-url.json','a+')
json.dump(mydict, f, indent=4)
f.close()
print("Done")
