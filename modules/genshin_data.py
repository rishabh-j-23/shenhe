import requests
import json
import os

class genshin_artifact_data:

    url = 'https://api.genshin.dev/'

    def __articall__(self, url):
        return url + 'artifacts/'

    def __nameParser__(self, name: str):
        return name.lower().replace(" ", "-").replace("'", '-')

    def get_arti_data(self, name):
        url = self.__articall__(self.url) + f'{self.__nameParser__(name)}'

        return requests.get(url).json()

    def getSetBonuses(self, name):
        set = self.get_arti_data(name)
        return f'''{set['name']} \n{set['2-piece_bonus']} \n{set['4-piece_bonus']}'''


class genshin_character_data:

    url = 'https://api.genshin.dev/'

    def __charCall__(self, url):
        return url + 'characters/'

    def __nameParser__(self, name: str):
        return name.lower().replace(' ', '-')

    def getCharName(self, name):
        return self.getCharData(name)['name']

    def getCharData(self, name):
        name = self.__nameParser__(name)
        charData = requests.get(self.__charCall__(self.url) + name)

        return charData.json()

    def getCharBaseDetails(self, name):
        name = self.__nameParser__(name)
        charData = self.getCharData(name)

        return f"""**Name :** {charData['name']}
**Vision :** {charData['vision']}
**Weapon :** {charData['weapon']}
**Nation :** {charData['nation']}
**Affiliation :** {charData['affiliation']}
**Rarity :** {charData['rarity']}
**Constellation :** {charData['constellation']}
**Birthday :** {charData['birthday']}       
**Description :** {charData['description']}


        """

    def getCharNormalAttack(self, name):

        name = self.__nameParser__(name)
        charSkillsData = self.getCharData(name)['skillTalents']

        return f""" 
**__{charSkillsData[0]['name']}__**
*{charSkillsData[0]['description']}*
"""
    
    def getCharEleSkill(self, name):
        name = self.__nameParser__(name)
        charSkillsData = self.getCharData(name)['skillTalents']
        return f"""
**__{charSkillsData[1]['name']}__**
*{charSkillsData[1]['description']}*        
        """

    def getCharBurstSkill(self, name):
        name = self.__nameParser__(name)
        charSkillsData = self.getCharData(name)['skillTalents']
        return f"""
**__{charSkillsData[2]['name']}__**
*{charSkillsData[2]['description']}*
        """


def getCharIcon(name):
        folder_dir = "res/images/genshin/character_icons/"
        folder_dir = '/workspaces/shenhe/res/images/genshin/character_icons/'
        name = name.capitalize().replace(" ", "_")
        icon = []
        try:
            for images in os.listdir(folder_dir):
                if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
                    icon.append(images)
        except Exception as e:
            print(e)

        for i in range(len(icon)):
            if str(icon[i]) == str(f'Character_{name}_Thumb.png'):
                return icon[i]
        
        return None