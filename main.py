from ah_api_client import RealmScraper


if __name__ == "__main__":
    realm_scraper = RealmScraper()
    realm_data = realm_scraper.get_realm_data()
    data_list = []

    for data in realm_data.values():
        realm = realm_scraper.parse(data)
        data_list.append(realm)

    for realm in data_list:
        if realm.house_id == 180:
            print(f'{realm.name}, {realm.href}, {realm.house_id}')
