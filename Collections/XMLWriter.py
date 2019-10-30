
###################################################################################################################
###################################################################################################################
###################################################################################################################
###                                                                                                             ###
###                                                                                                             ###
###                                                                                                             ###
###                                        @Autor Ki-LIAN                                                       ###
###                                        @Date 30.10.2019                                                     ###
###                                        @XMLReader                                                           ###
###                                        Schreibt Daten in XML                                                ###
###                                                                                                             ###
###                                                                                                             ###
###                                                                                                             ###
###################################################################################################################
###################################################################################################################
###################################################################################################################

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET

class XMLWriter():

    def __init__(self, xml_filename):
        self.__xml_filename = xml_filename

    def get_filename(self):
        return self.__xml_filename

    def set_filename(self, xml_filename):
        self.__xml_filename = xml_filename

    def write(self, data_sets):
        root = Element('player')
        tree = ElementTree(root)


        str_my_elo = 'my_elo'
        ver = SubElement(root, str_my_elo)
        my_elo = data_sets[0][str_my_elo]
        ver.text = my_elo

        str_date_of_match = 'date_of_match'
        str_elo_of_victim = 'elo_of_victim'
        str_name_of_victim = 'name_of_victim'
        str_match_place = 'match_place'

        for data in data_sets:
            date_of_match = data[str_date_of_match]
            elo_of_victim = data[str_elo_of_victim]
            name_of_victim = data[str_name_of_victim]
            match_place = data[str_match_place]

            ver = SubElement(root, str_date_of_match)
            ver.text = date_of_match
            ver = SubElement(root, str_elo_of_victim)
            ver.text = elo_of_victim
            ver = SubElement(root, str_name_of_victim)
            ver.text = name_of_victim
            ver = SubElement(root, str_match_place)
            ver.text = match_place

        tree.write(open(self.get_filename(), 'w'), encoding='unicode')



