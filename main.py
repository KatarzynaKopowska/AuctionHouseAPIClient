from auction_house_scraper import BattlePetsScraperManager


if __name__ == "__main__":
    scraper_manager = BattlePetsScraperManager()
    realm_data = scraper_manager.run()
