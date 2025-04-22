class CakeCalculator:
    def __init__(self, recipe=None, available=None):
        self.recipe = recipe
        self.available = available
        
    def max_cakes(self, recipe=None, available=None):
        # Using instance variables if no arguements are passed.
        recipe = recipe or self.recipe
        available = available or self.available
        
        if recipe is None or available is None:
            raise ValueError("Recipe and ingredients must be provided")
        
        return min(available.get(ingredient, 0) // amount for ingredient, amount in recipe.items())