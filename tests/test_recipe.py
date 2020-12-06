import pytest
from heirloom_api.models.ingredients.base_ingredient import Ingredient
from heirloom_api.models.recipe.base_recipe import Recipe


def test_ingredient():
    new_ing = Ingredient('Apple')
    assert new_ing.name == 'Apple'


def test_recipe():
    new_rec = Recipe(ingredients=[Ingredient('apple')])
    assert new_rec.ingredients[0].name == 'apple'
