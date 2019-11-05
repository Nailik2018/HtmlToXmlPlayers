
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

class Application():

    def __init__(self, url, classname, firstname, lastname):
        self.__url = url
        self.__classname = classname
        self.__firstname = firstname
        self.__lastname = lastname

    # ------------------------------------------------------------------------------------------------------------------
    # Ausfüren der Anwendung.
    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        player = WebsiteReader(self.__url)
        print("URL: " + str(player.getUrl()))
        data_of_player = player.changeHtmlToList(self.__classname)
        print(data_of_player)
        xml_player = XMLWriter(self.__firstname + "-" + self.__lastname + ".xml")
        xml_player.write(data_of_player)
        print(xml_player.get_filename())




