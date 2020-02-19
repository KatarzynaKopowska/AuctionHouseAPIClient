import collections


PetInformation = collections.namedtuple("Pet", ("name", "realm", "price")
                                        )


class BaseEndpoint:
    base_url = None
    data_class = None
    realm_list = None

    def get(self, **kwargs):
        raise NotImplementedError


class BattlePet:
    base_url = "https://theunderminejournal.com/#eu"
    data_class = PetInformation
    realm_list = None

    def get(self, realm_name):
        url = self.base_url + realm_name