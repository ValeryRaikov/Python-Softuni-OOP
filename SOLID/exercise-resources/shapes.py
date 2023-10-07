from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> int or float:
        pass


class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    def calculate_area(self) -> int or float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, height_side) -> None:
        self.side = side
        self.height_side = height_side
        
    def calculate_area(self) -> int or float:
        return self.side * self.height_side / 2


class AreaCalculator:

    def __init__(self, shapes) -> None:
        self.shapes = shapes
        
    @property
    def shapes(self):
        return self.__shapes
    
    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")
        
        self.__shapes = value

    @property
    def total_area(self) -> int or float:
        total = 0
        
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)