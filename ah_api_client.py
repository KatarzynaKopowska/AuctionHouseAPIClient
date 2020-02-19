import requests


class RealmScraper:
    url = "https://theunderminejournal.com/api/realms.php"
    realm_names_list = []

    def get_realm_information(self):
        return requests.get(self.url).json()['realms'][1]  # second list element contains information about EU realms

    def get_realm_names_list(self, realm_information):
        for name in realm_information.values():
            self.realm_names_list.append(name['slug'])
        return self.realm_names_list
