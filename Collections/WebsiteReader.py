from bs4 import BeautifulSoup
import requests

class WebsiteReader():

    page_content = ''

    def __init__(self, url):
        self.__url = url

    def getUrl(self):
        return self.__url

    def setUrl(self, url):
        self.__url = url

    def getHtml2(self):
        page = requests.get(self.__url)
        self.page_content = page.content
        soup = BeautifulSoup(self.page_content, 'html.parser')
        output = soup.prettify()
        return output

    def getHtml(self):
        url = self.__url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        result_of_player = soup.find_all(class_="border-light-light-gray-bottom")
        i = 0

        output = []

        for single in result_of_player:
            elo_of_victim = ''
            date_of_match = single.td.get_text()
            name_of_victim = ''
            my_elo = ''
            new_elos = ''
            gewinn_wahrscheinlichkeit = ''
            j = 0

            for s in single:
                if j == 5:
                    my_elo = s.get_text().strip()
                if j == 7:
                    name_of_victim = s.get_text().strip()
                if j == 9:
                    elo_of_victim = s.get_text().strip()
                if j == 11:
                    zahl = str(s.get_text().strip())
                    gewinn_wahrscheinlichkeit = zahl
                if j == 13:
                    new_elos = str(s.get_text().strip())
                    print(new_elos)
                j += 1
                #output.append(elo_of_victim)
            i += 1

            player = {
                "date_of_match": date_of_match,
                "elo_of_victim": elo_of_victim,
                "name_of_victim": name_of_victim,
                "my_elo": my_elo,
                "gewinn_wahrscheinlichkeit": gewinn_wahrscheinlichkeit,
                "new_elos": new_elos,
            }

            output.append(player)
        print(result_of_player[1])

        return output

    def htmlSeperatorByID(self, id):
        output = []
        soup = BeautifulSoup(self.page_content, 'html.parser')
        event_month = soup.find(id=id)
        return event_month