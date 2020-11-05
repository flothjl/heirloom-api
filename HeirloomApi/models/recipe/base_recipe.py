from typing import List
from HeirloomApi.models.ingredients.base_ingredient import Ingredient


class Recipe:
    def __init__(self, ingredients: List[Ingredient]):
        self.ingredients = ingredients
