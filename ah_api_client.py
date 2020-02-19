import requests
import collections

Realm = collections.namedtuple("Realm", ("name", "href", "house_id")
                               )
BattlePet = collections.namedtuple("Pet", ("name", "price", "species_id")
                                   )


class BaseScraper:
    url = None
    data_class = None

    def get(self, **kwargs):
        raise NotImplementedError

    def parse(self, realm_data):
        raise NotImplementedError


class RealmScraper(BaseScraper):
    url = "https://theunderminejournal.com/api/realms.php"
    data_class = Realm

    def get(self, **kwargs):
        return requests.get(self.url).json()['realms'][1]  # second list element contains information about EU realms

    def parse(self, data):
        realm_data = {
            "name": data.get("name"),
            "href": data.get("slug"),
            "house_id": data.get("house"),
        }
        return self.data_class(**realm_data)


class BattlePetScraper(BaseScraper):
    url = "https://theunderminejournal.com/api/category.php?"
    data_class = BattlePet

    def get(self, **kwargs):
        kwargs.update(**{"id": "battlepets"})
        url = "{}{}={}&{}={}".format(self.url, kwargs, kwargs, kwargs, kwargs)
        battle_pet_data = requests.get(url, params=kwargs).json().get("results")[0]["data"].get("9")
        return battle_pet_data

    def parse(self, data):
        battle_pet_data = {
            "name": data.get("name_enus"),
            "price": data.get("price"),
            "species_id": data.get("species"),
        }
        return self.data_class(**battle_pet_data)


class BattlePetsScraperManager:
    def __init__(self):
        self.realms = []
        self.realm_class = RealmScraper()
        self.battle_pet_class = BattlePetScraper()

    def run(self):
        realm_data = self.realm_class.get()

        battle_pets = []
        for data in realm_data.values():
            realm_information = self.realm_class.parse(data)
            battle_pet_json = self.battle_pet_class.get(house=realm_information.house_id)
            print(f"\nInformation about battle pet prices for {realm_information.name}: ")
            for data in battle_pet_json.values():
                battle_pet_data = self.battle_pet_class.parse(data)
                battle_pets.append(battle_pet_data)
                print(f"{battle_pet_data.name}, {battle_pet_data.price/1000}")
        return battle_pets

