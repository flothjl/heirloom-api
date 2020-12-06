from typing import List
import inspect
from HeirloomApi.models.ingredients.base_ingredient import Ingredient


class Recipe:
    def __init__(self, ingredients: List[Ingredient], title: str, description: str = None, instructions: str = None):
        self.ingredients = self._build_ingredient_list(ingredients)
        self.title = title
        self.description = description
        self.instructions = instructions

    @staticmethod
    def build_from_json(input_dict: dict):
        attributes = inspect.getfullargspec(Recipe)[0]
        try:
            attributes.remove('self')
        except ValueError:
            pass
        for key in input_dict:
            try:
                assert key in attributes
            except AssertionError:
                raise Exception('INVALID DATA')
        recipe = Recipe(ingredients=input_dict['ingredients'],
                        title=input_dict['title'],
                        description=input_dict.get('description'),
                        instructions=input_dict.get('instructions'))
        return recipe

    def _build_ingredient_list(self, input_list: list):
        return [Ingredient(ingredient['name'],
                           ingredient.get('amount'),
                           ingredient.get('uom')).__dict__ for ingredient in input_list]
