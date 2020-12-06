import inspect
from typing import List

from ...models.exceptions import InvalidRequestBody
from ..ingredients.base_ingredient import Ingredient

class Recipe:
    def __init__(
        self,
        ingredients: List[Ingredient],
        title: str,
        description: str = None,
        instructions: str = None,
    ):
        self.ingredients = self._build_ingredient_list(ingredients)
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

        InvalidRequestBody exception raised in event that an invalid attribute is passed in the body of the request
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

    def _build_ingredient_list(self, input_list: list):
        return [
            Ingredient(
                ingredient["name"], ingredient.get("amount"), ingredient.get("uom")
            ).__dict__
            for ingredient in input_list
        ]
