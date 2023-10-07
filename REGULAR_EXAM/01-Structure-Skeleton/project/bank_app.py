from typing import List

from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    LOAN_TYPES = {
        "StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan
    }
    CLIENT_TYPES = {
        "Student": Student, "Adult": Adult
    }
    
    GRANTED_LOANS = 0
    GRANTED_LOANS_SUM = 0
    
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
        
        BankApp.GRANTED_LOANS += 1
        BankApp.GRANTED_LOANS_SUM += loan.amount
        
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
    
    def remove_client(self, client_id: str) -> str:
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
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
        result = f"Active Clients: {len(self.clients)}\n" \
                 f"Total Income: {sum([c.income for c in self.clients]):.2f}\n" \
                 f"Granted Loans: {BankApp.GRANTED_LOANS}, Total Sum: {BankApp.GRANTED_LOANS_SUM:.2f}\n" \
                 f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n" \
                 f"Average Client Interest Rate: {sum([c.interest for c in self.clients]) / len(self.clients) if len(self.clients) else 0.00:.2f}"
                 
        return result