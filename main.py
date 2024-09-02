"""
Kochbuch
"""
import json


def load_recipe(data_json):
    return json.loads(data_json)


def adjust_recipe(recipe_info, persons):
    factor = persons / recipe_info['servings']
    adjusted_ingredients = {
        ingredient: int(amount * factor) for ingredient, amount in recipe_info['ingredients'].items()
    }
    return {
        'title': recipe_info['title'],
        'ingredients': adjusted_ingredients,
        'servings': persons
    }


if __name__ == '__main__':
    recipe_json = (
        '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, '
        '"Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    )

    recipe_data = load_recipe(recipe_json)

    adjusted_recipe = adjust_recipe(recipe_data, 2)

    print('Angepasstes Rezept:')
    print(json.dumps(adjusted_recipe, indent=4))
