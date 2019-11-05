# -*- coding: utf-8 -*-

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

        item = 'item'
        str_my_elo = 'my_elo'
        str_date_of_match = 'date_of_match'
        str_elo_of_victim = 'elo_of_victim'
        str_name_of_victim = 'name_of_victim'
        str_match_place = 'match_place'
        str_firstname_of_victim = 'firstname_of_victim'
        str_lastname_of_victim = 'lastname_of_victim'

        for data in data_sets:
            my_elo = data[str_my_elo]
            date_of_match = data[str_date_of_match]
            elo_of_victim = data[str_elo_of_victim]

            #name_of_victim = data[str_name_of_victim]
            match_place = data[str_match_place]

            firstname_of_victim = data[str_firstname_of_victim]
            lastname_of_victim = data[str_lastname_of_victim]

            item = Element(item)
            item = ElementTree(item)

            ver = SubElement(root, str_my_elo)
            ver.text = my_elo
            ver = SubElement(root, str_date_of_match)
            ver.text = date_of_match
            ver = SubElement(root, str_elo_of_victim)
            ver.text = elo_of_victim
            #ver = SubElement(root, str_name_of_victim)
            #ver.text = name_of_victim

            ver = SubElement(root, str_firstname_of_victim)
            ver.text = firstname_of_victim
            ver = SubElement(root, str_lastname_of_victim)
            ver.text = lastname_of_victim
            ver = SubElement(root, str_match_place)
            ver.text = match_place

        #ET.ElementTree(testtag).write('testunicode.xml', encoding="UTF-8", xml_declaration=True)
        tree.write(open(self.get_filename(), 'w'), encoding="unicode")



