import requests as req
from Wappalyzer import Wappalyzer, WebPage

urlList = []
with open('subdomains.txt', 'r') as readData:
    a = readData.readlines()

print(a)
for i in range(len(a)):
    singleURL = a[i]
    addProtocol = "http://"+singleURL
    urlList.append(addProtocol.replace('\n', ''))
    i += 1
#print(urlList)

for apiURL in urlList:
    try:
        getReq = req.get(apiURL, timeout=20)
        statUS = getReq.status_code
        print(f"{apiURL} status ----> {statUS}")
        contentLen = len(getReq.content)
        if statUS == 200:
            wappalizer = Wappalyzer.latest()
            web = WebPage.new_from_url(apiURL)
            res = wappalizer.analyze(web)
            with open("liveDomains.txt", "a") as goodCont:
                goodCont.write(f"{apiURL}\t has ---> {res} \n")
    except:
        print(f"{apiURL} timed out")
        continue

