from ah_api_client import RealmScraper

if __name__ == "__main__":
    realm_scraper = RealmScraper()

    realm_information = realm_scraper.get_realm_information()
    realm_names_list = realm_scraper.get_realm_names_list(realm_information)
    print(realm_names_list)
