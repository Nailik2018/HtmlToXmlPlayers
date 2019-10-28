from Collections.WebsiteReader import WebsiteReader
class Application():

    def __init__(self, url):
        self.__url = url

    def run(self):
        player = WebsiteReader(self.__url)
        print("URL: " + str(player.getUrl()))
        output = player.getHtml()
        print(output)

