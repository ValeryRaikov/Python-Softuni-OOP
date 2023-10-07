from typing import List

from loans.base_loan import BaseLoan
from loans.student_loan import StudentLoan
from loans.mortgage_loan import MortgageLoan
from clients.base_client import BaseClient
from clients.student import Student
from clients.adult import Adult


class BankApp:
    LOAN_TYPES = {
        "StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan
    }
    CLIENT_TYPES = {
        "Student": Student, "Adult": Adult
    }
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        
    def add_loan(self, loan_type: str) -> str:
        if loan_type not in BankApp.LOAN_TYPES.keys():
            raise Exception("Invalid loan type!")
        
        loan = BankApp.LOAN_TYPES[loan_type]()
        
        self.loans.append(loan)
        
        return f"{loan_type} was successfully added."
    
    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in BankApp.CLIENT_TYPES.keys():
            raise Exception("Invalid client type!")
        
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        
        client = BankApp.CLIENT_TYPES[client_type](client_name, client_id, income)
        
        self.clients.append(client)
        
        return f"{client_type} was successfully added."
    
    def grant_loan(self, loan_type: str, client_id: str) -> str:
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
        client = [c for c in self.clients if c.client_id == client_id][0]
        
        if loan_type == "StudentLoan":
            if not isinstance(client, Student):
                raise Exception("Inappropriate loan type!")
            
        if loan_type == "MortgageLoan":
            if not isinstance(client, Adult):
                raise Exception("Inappropriate loan type!")
            
        self.loans.remove(loan)
        client.loans.append(loan)
        
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
    
    def remove_client(self, client_id: str) -> str:
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except StopIteration:
            raise Exception("No such client!")
        
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        
        self.clients.remove(client)
        
        return f"Successfully removed {client.name} with ID {client_id}."
    
    def increase_loan_interest(self, loan_type: str) -> str:
        loan_type = BankApp.LOAN_TYPES[loan_type]
        
        changed_loans = 0

        for loan in self.loans:
            if isinstance(loan, loan_type):
                loan.increase_interest_rate()
                changed_loans += 1

        return f"Successfully changed {changed_loans} loans."
    
    def increase_clients_interest(self, min_rate: float) -> str:
        changed_client_rates = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates += 1

        return f"Number of clients affected: {changed_client_rates}."
    
    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)

        loans_count_granted_to_clients = sum(1 for loan in self.loans if any(client for client in self.clients if loan in client.loans))
        granted_sum = sum(loan.amount for loan in self.loans if any(client for client in self.clients if loan in client.loans))

        loans_count_not_granted = sum(1 for loan in self.loans if not any(client for client in self.clients if loan in client.loans))
        not_granted_sum = sum(loan.amount for loan in self.loans if not any(client for client in self.clients if loan in client.loans))

        avg_client_interest_rate = sum(client.interest for client in self.clients) / total_clients_count if total_clients_count > 0 else 0.0

        return f"Active Clients: {total_clients_count}\n" \
               f"Total Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"