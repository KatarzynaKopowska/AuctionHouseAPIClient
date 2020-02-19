import collections
import requests


PetInformation = collections.namedtuple("Pet", ("name", "realm", "price")
                                        )


class RealmScraper:
    url = "https://theunderminejournal.com/api/realms.php"

    def get_realm_information(self):
        realm_information = requests.get(self.url).json()['realms'][1]
        return realm_information

    def get_realm_list(self, realm_information):
        realm_list = []
        for key, value in realm_information.items():
            realm_list.append(value['name'])
        return realm_list


if __name__ == "__main__":
    realm_scraper = RealmScraper()

    realm_info = realm_scraper.get_realm_information()
    x = realm_scraper.get_realm_list(realm_info)
    print(x)
