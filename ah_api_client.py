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
