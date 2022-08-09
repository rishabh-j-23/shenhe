import requests


class genshin_data:

    url = 'https://api.genshin.dev/'

    def __articall__(self, url):
        return self.url + 'artifacts/'
    
    def __nameParser__(self, name: str):
        return name.lower().replace(" ", "-").replace("'", '-')

    def get_arti_data(self, name):
        url = self.__articall__(self.url) + f'{self.__nameParser__(name)}'

        return requests.get(url).json()
    
    def getSetBonuses(self, name):
        set = self.get_arti_data(name)
        return f'''
{set['name']}
{set['2-piece_bonus']}
{set['4-piece_bonus']}'''

print(genshin_data().getSetBonuses("shimenawa's reminiscence"))