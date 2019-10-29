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

    def changeHtmlToList(self):
        url = self.__url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        result_of_player = soup.find_all(class_="border-light-light-gray-bottom")
        i = 0

        output = []

        for single in result_of_player:
            date_of_match = single.contents[1].get_text().strip()
            match_place = single.contents[3].get_text().strip()
            my_elo = single.contents[5].get_text().strip()
            #classing_of_victim = single.contents[7].get_text().split(",")
            #print(classing_of_victim)
            name_of_victim = single.contents[7].get_text().strip()
            elo_of_victim = single.contents[9].get_text().strip()
            #win_chance = single.contents[11].get_text()
            #new_elos = single.contents[13].get_text()
            win_chance = ''

            i += 1

            player = {
                "date_of_match": date_of_match,
                "elo_of_victim": elo_of_victim,
                "name_of_victim": name_of_victim,
                #"classing_of_victim": classing_of_victim,
                "my_elo": my_elo,
                "win_chance": win_chance,
                #"new_elos": new_elos,
                "match_place": match_place,
            }
            output.append(player)
        return output

    def htmlSeperatorByID(self, id):
        output = []
        soup = BeautifulSoup(self.page_content, 'html.parser')
        event_month = soup.find(id=id)
        return event_month