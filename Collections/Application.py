
###################################################################################################################
###################################################################################################################
###################################################################################################################
###                                                                                                             ###
###                                                                                                             ###
###                                                                                                             ###
###                                        @Autor Ki-LIAN                                                       ###
###                                        @Date 30.10.2019                                                     ###
###                                        @Application                                                         ###
###                                        Führt die Anwendung aus                                              ###
###                                        Benötigt die Url und classname des Elements                          ###
###                                                                                                             ###
###                                                                                                             ###
###                                                                                                             ###
###################################################################################################################
###################################################################################################################
###################################################################################################################

from Collections.WebsiteReader import WebsiteReader
from Collections.XMLWriter import XMLWriter
from Collections.PlayerDatabase import PlayerDatabase
from Collections.URLRouter import URLRouter
from datetime import date
from time import time

class Application():

    def __init__(self, classname, ):
        self.__classname = classname

    # ------------------------------------------------------------------------------------------------------------------
    # Ausführen der Anwendung.
    # ------------------------------------------------------------------------------------------------------------------
    def run(self):

        start = time()

        play = PlayerDatabase()
        all_players = play.select_players_from_db()

        today = date.today()
        print(today.day)
        print(today.month)
        print(today.year)

        date_of_ranking = "10.11.2019"

        for player in all_players:
            print(player)
            firstname = player['firstname'].lower()
            lastname = player['lastname'].lower()
            licenceNr = str(player['licenceNr'])

            #url = "https://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloFilter?lastname=" + lastname + "&federation=STT&rankingDate=" + date_of_ranking + "&sex=WONoSelectionString&firstname=" + firstname + "&ranking=355425655"
            #url = "https://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloFilter?lastname=" + lastname + "&federation=STT&rankingDate=" + date_of_ranking + "&sex=WONoSelectionString&firstname=" + firstname

            #url = "https://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloFilter?sex=WONoSelectionString&federation=STT&rankingDate=10.11.2019&licenceNr="+ licenceNr + "&ranking=" + "355426816"
            url = "https://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloFilter?sex=WONoSelectionString&federation=STT&rankingDate=10.11.2019&licenceNr=" + licenceNr

            classname = "result-set"
            url_to_route = URLRouter(url)
            ranking = url_to_route.get_ranking(classname)
            url = "https://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloFilter?sex=WONoSelectionString&federation=STT&rankingDate=10.11.2019&licenceNr=" + licenceNr + "&ranking=" + ranking

            player = WebsiteReader(url)
            print("URL: " + str(player.getUrl()))
            data_of_player = player.changeHtmlToList(self.__classname)
            print(data_of_player)
            xml_player = XMLWriter(firstname + "-" + lastname + ".xml")
            xml_player.write(data_of_player)
            print(xml_player.get_filename())

        print("--- %s Sekunden" % (time() - start))