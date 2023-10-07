from typing import Any


class store_results:
    _FILE_NAME = "results.txt"

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any) -> str:
        with open(store_results._FILE_NAME, "a") as file:
            file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
