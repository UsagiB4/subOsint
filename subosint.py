import requests as req
from Wappalyzer import Wappalyzer, WebPage
print('''
                  dP       MMP"""""YMM MP""""""`MM M""M M"""""""`YM M""""""""M 
                  88       M' .mmm. `M M  mmmmm..M M  M M  mmmm.  M Mmmm  mmmM 
.d8888b. dP    dP 88d888b. M  MMMMM  M M.      `YM M  M M  MMMMM  M MMMM  MMMM 
Y8ooooo. 88    88 88'  `88 M  MMMMM  M MMMMMMM.  M M  M M  MMMMM  M MMMM  MMMM 
      88 88.  .88 88.  .88 M. `MMM' .M M. .MMM'  M M  M M  MMMMM  M MMMM  MMMM 
`88888P' `88888P' 88Y8888' MMb     dMM Mb.     .dM M  M M  MMMMM  M MMMM  MMMM 
                           MMMMMMMMMMM MMMMMMMMMMM MMMM MMMMMMMMMMM MMMMMMMMMM 
                                                                               
''')

urlList = []
with open('subdomains.txt', 'r') as readData:
    a = readData.readlines()

# print(a)
for i in range(len(a)):
    singleURL = a[i]
    if singleURL.startswith('http'):
        urlList.append(singleURL.replace('\n', ''))
        i += 1
    else:
        addProtocol = "http://"+singleURL
        urlList.append(addProtocol.replace('\n', ''))
        i += 1
#print(urlList)

for url in urlList:
    try:
        getReq = req.get(url, timeout=100)
        statUS = getReq.status_code
        print(f"{url} status ----> {statUS}")
        contentLen = len(getReq.content)
        if statUS == 200:
            wappalizer = Wappalyzer.latest()
            web = WebPage.new_from_url(url)
            res = wappalizer.analyze(web)
            goodCont = open("liveDomains.txt", "a")
            goodCont.write(f"{url}\t has ---> {res} \n")
    except (KeyboardInterrupt, SystemExit):
        raise
        
    except:
        print(f"{url} timed out")
        continue