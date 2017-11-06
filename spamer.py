import re
import requests
def urlcheck(URL, mainURL, HTMLs):
    checker = 0
    r = requests.get(URL)
    HTML_code = r.content.decode('UTF-8')
    Badhtmls = re.findall("href=\"(http[s]?://[\w+\.]+\w+[[\/\w+]+]?)\"", HTML_code)
    for n in range(len(Badhtmls)):
        if re.match(URL, Badhtmls[n]) != None:
            checker+=1
    if checker == 0:
        Badhtmls = re.findall("<a href=\"(/.+/)\">", HTML_code)
        for n in range(len(Badhtmls)):
            temp = URL + Badhtmls[n]
            if temp not in HTMLs:
                HTMLs.append(temp)
                urlcheck(temp, mainURL, HTMLs)
    else:
        for n in range(len(Badhtmls)):
            temp = Badhtmls[n]
            if re.match(mainURL, temp) != None:
                if temp not in HTMLs:
                    HTMLs.append(temp)
                    urlcheck(temp, mainURL, HTMLs)

def emails_check(HTMLs, BadEmails, Emails):
    for n in range (len(HTMLs)):
        r = requests.get(HTMLs[n])
        HTML_code = r.content.decode('utf-8')
        BadEmails = re.findall("\w+@\w+\.\w+", HTML_code)
    for n in range (len(BadEmails)):
        if BadEmails[n] not in Emails:
            Emails.append(BadEmails[n])

BadEmails=[]
HTMLs = []
Emails=[]
GoodHTMLs = []

url = 'http://www.csd.tsu.ru/'
urlcheck(url, url, GoodHTMLs)
emails_check(GoodHTMLs, BadEmails, Emails)
print(GoodHTMLs)
print(Emails)