
###################################################################################################################
###################################################################################################################
###################################################################################################################
###                                                                                                             ###
###                                                                                                             ###
###                                                                                                             ###
###                                        @Autor Ki-LIAN                                                       ###
###                                        @Date 30.10.2019                                                     ###
###                                        @WebsiteReader                                                       ###
###                                        Liest clickTT Webseite aus und stellt Struktur zurverfügung          ###
###                                                                                                             ###
###                                                                                                             ###
###                                                                                                             ###
###################################################################################################################
###################################################################################################################
###################################################################################################################

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

    # ------------------------------------------------------------------------------------------------------------------
    # Funktion liest Webseite ab classname aus
    # Relevante Daten werden in liste welche aus Dictionarys besteht geschrieben und zurück gegeben
    # ------------------------------------------------------------------------------------------------------------------
    def changeHtmlToList(self, classname):
        url = self.__url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        result_of_player = soup.find_all(class_=classname)
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