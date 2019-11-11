from bs4 import BeautifulSoup
import requests

class URLRouter():

    def __init__(self, url):
        self.__url = url

    def get_ranking(self, classname):

        url = self.__url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all(class_=classname)

        for element in results:
            ranking = element.contents[3].a['href'].split("ranking=")
            output = ranking[1]

        return output

#classname = "result-set"

#url ="https://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloFilter?sex=WONoSelectionString&federation=STT&rankingDate=10.11.2019&licenceNr=517044"

#url_to_route = URLRouter(url)
#url = url_to_route.get_ranking(classname)
#print(url)
