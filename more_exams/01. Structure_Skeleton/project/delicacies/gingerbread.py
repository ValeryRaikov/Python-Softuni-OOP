from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200
    
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, Gingerbread.PORTION, price)
        
    def details(self) -> str:
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."