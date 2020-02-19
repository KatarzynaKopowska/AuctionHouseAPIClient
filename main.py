from ah_api_client import RealmScraper
from ah_api_client import BattlePetScraper


if __name__ == "__main__":
    realm_scraper = RealmScraper()
    realm_data = realm_scraper.get()
    data_list = []

    for data in realm_data.values():
        realm = realm_scraper.parse(data)
        data_list.append(realm)

    for realm in data_list:
        if realm.house_id == 180:
            print(f'{realm.name}, {realm.href}, {realm.house_id}')

    battle_pet = BattlePetScraper()
    battle_pet_data = battle_pet.get(house=180)

    battle_pet_list = []
    for data in battle_pet_data.values():
        pet = battle_pet.parse(data)
        battle_pet_list.append(pet)

    print("List of battle pets for realm TARREN MILL/DENTARG:")
    for pet_data in battle_pet_list:
        print(f"'{pet_data.name}' price: {pet_data.price/1000}" '\n')
