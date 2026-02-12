from abc import ABC, abstractmethod


# Product class ---------------------------------------------------
class Sandwich:
    """
    The final object that will be built step by step by builders.
    It stores ingredients and knows how to display itself.
    """
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """Add a single ingredient to the sandwich."""
        self.ingredients.append(ingredient)

    def display(self):
        """Print sandwich ingredients in a readable format."""
        print("Sandwich with the following ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def __str__(self):
        """Readable string representation when printed."""
        return f"Sandwich({', '.join(self.ingredients)})"


# Abstract Builder ------------------------------------------------
class SandwichBuilder(ABC):
    """
    Abstract builder that defines the construction steps.
    Concrete builders must implement bread and filling logic.
    """
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        """Create a fresh sandwich instance."""
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        """Add bread to the sandwich."""
        pass

    @abstractmethod
    def add_filling(self):
        """Add fillings to the sandwich."""
        pass

    def get_results(self):
        """Return the finished sandwich."""
        return self.sandwich


# Concrete Builder (Veggies) -------------------------------------
class VeggiesSandwichBuilder(SandwichBuilder):
    """Builds a vegetarian sandwich."""

    def add_bread(self):
        self.sandwich.add_ingredient("Wheat Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Lettuce")
        self.sandwich.add_ingredient("Tomato")
        self.sandwich.add_ingredient("Cucumber")


# Concrete Builder (Ham) -----------------------------------------
class HamSandwichBuilder(SandwichBuilder):
    """Builds a ham sandwich."""

    def add_bread(self):
        self.sandwich.add_ingredient("White Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Ham")
        self.sandwich.add_ingredient("Cheese")
        self.sandwich.add_ingredient("Mayonnaise")


# Director --------------------------------------------------------
class SandwichDirector:
    """
    Controls the building process.
    It doesn't know sandwich details, only the steps.
    """
    def __init__(self, builder: SandwichBuilder):
        self.builder = builder

    def build_sandwich(self):
        """Execute building steps in order."""
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_results()


# ---------------------------------------------------------------
# Example usage

veggies_builder = VeggiesSandwichBuilder()
director = SandwichDirector(veggies_builder)

veggies_sandwich = director.build_sandwich()

print(veggies_sandwich)   # uses __str__
veggies_sandwich.display()



ham_builder = HamSandwichBuilder()
director = SandwichDirector(ham_builder)
ham_sandwitch = director.build_sandwich()
print(ham_sandwitch)
ham_sandwitch.display()
