import requests
import collections

Realm = collections.namedtuple("Realm", ("name", "href", "house_id"))


class BaseScraper:
    url = None
    data_class = None

    def get_realm_data(self):
        raise NotImplementedError

    def parse(self, realm_data):
        raise NotImplementedError


class RealmScraper(BaseScraper):
    url = "https://theunderminejournal.com/api/realms.php"
    data_class = Realm

    def get_realm_data(self):
        return requests.get(self.url).json()['realms'][1]  # second list element contains information about EU realms

    def parse(self, realm_data):
        data = {
            "name": realm_data.get("name"),
            "href": realm_data.get("slug"),
            "house_id": realm_data.get("house"),
        }
        return self.data_class(**data)
