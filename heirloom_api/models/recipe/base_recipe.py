import inspect
from typing import List

from heirloom_api.models.exceptions import InvalidRequestBody
from heirloom_api.models.ingredients.base_ingredient import Ingredient


class Recipe:
    '''
    Base class for recipe model
    '''
    def __init__(
        self,
        ingredients: List[Ingredient],
        title: str,
        description: str = None,
        instructions: str = None,
    ):
        self.ingredients = self.build_ingredient_list(ingredients)
        self.title = title
        self.description = description
        self.instructions = instructions

    @staticmethod
    def build_from_json(input_dict: dict):
        """
        Args:
            input_dict: dictionary to parse. Must contain only valid attributes.

        Returns:
            Recipe object.

        InvalidRequestBody exception raised in event an
        invalid attribute is passed in the body of the request
        """

        attributes = inspect.getfullargspec(Recipe)[0]
        try:
            attributes.remove("self")
        except ValueError:
            pass
        for key in input_dict:
            if key not in attributes:
                raise InvalidRequestBody(
                    "An invalid attribute was passed in the recipe body"
                )
        recipe = Recipe(
            ingredients=input_dict["ingredients"],
            title=input_dict["title"],
            description=input_dict.get("description"),
            instructions=input_dict.get("instructions"),
        )
        return recipe

    @staticmethod
    def build_ingredient_list(input_list: list):
        '''
        builds ingredient list to store the ingredient list as a dictionary
        '''
        return [
            Ingredient(
                ingredient["name"], ingredient.get("amount"), ingredient.get("uom")
            ).__dict__
            for ingredient in input_list
        ]
