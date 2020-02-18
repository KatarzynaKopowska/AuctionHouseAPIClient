import collections
import requests


PetInformation = collections.namedtuple("Pet", ("name", "realm", "price")
                                        )
Realm = collections.namedtuple("Realm", ("name", "region")
                               )

class RealmScraper:
    url = "https://theunderminejournal.com/api/realms.php"
    data_class = Realm

    def get_realm_information(self):
        realm_information = requests.get(self.url).json()['realms'][1]
        return realm_information

    def parse_realm_information(self, realm_information):
        data = {
            "name": realm_information["298"]["name"],
            "region": realm_information["298"]["region"],
        }

        return self.data_class(**data)


if __name__ == "__main__":
    realm_scraper = RealmScraper()

    realm_info = realm_scraper.get_realm_information()
    print(realm_scraper.parse_realm_information(realm_info))




