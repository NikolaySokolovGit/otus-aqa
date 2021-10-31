from typing import List

from pydantic import BaseModel, validator


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: str = None
    address_2: str = None
    address_3: str = None
    city: str = None
    state: str = None
    county_province: str = None
    postal_code: str = None
    country: str = None
    longitude: str = None
    latitude: str = None
    phone: str = None
    website_url: str = None
    updated_at: str = None
    created_at: str = None

    @validator('brewery_type')
    def check_brewery_type(cls, value):
        possible_values = ('micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract',
                           'proprietor', 'closed')
        assert value in possible_values

class BreweryList(BaseModel):
    __root__: List[Brewery]
