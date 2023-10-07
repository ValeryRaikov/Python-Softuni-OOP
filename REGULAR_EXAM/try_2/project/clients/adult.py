from clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST = 4.0
    
    def __init__(self, name: str, client_id: str, income: float) -> None:
        super().__init__(name, client_id, income, Adult.INTEREST)
        
    def increase_clients_interest(self) -> None:
        self.interest += 2.0