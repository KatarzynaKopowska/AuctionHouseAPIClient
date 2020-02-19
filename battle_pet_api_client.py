import collections


PetInformation = collections.namedtuple("Pet", ("name", "realm", "price")
                                        )


class BaseEndpoint:
    base_url = None
    data_class = None

    def get(self, **kwargs):
        raise NotImplementedError


