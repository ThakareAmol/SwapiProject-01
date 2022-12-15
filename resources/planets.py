from resources.base import ResourceBase
from utils.fetch_data import fetch_data


class Planets(ResourceBase):
    """
    Resource class plural
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/planets/"  # plural
        self.__planets_range = [1, 60]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def range(self):
        return self.__planets_range

    @range.setter
    def range(self, new_range):
        self.__planets_range = new_range

    def get_count(self):
        plural_planets_url = self.home_url + self.relative_url
        response = fetch_data(plural_planets_url)
        return response.get("count")

    def get_resource_urls(self):
        resource_url = self.home_url + self.relative_url
        return resource_url

    def get_sample_data(self, id_="1"):
        sample_url = self.get_resource_urls() + id_
        return fetch_data(sample_url)


p = Planets()
print(p.get_resource_urls())
print(p.range)
p.range = [4, 15]
print(p.range)
