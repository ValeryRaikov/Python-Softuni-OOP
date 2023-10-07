from loans.base_loan import BaseLoan

class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50000.0 
    
    def __init__(self) -> None:
        super().__init__(MortgageLoan.INTEREST_RATE, MortgageLoan.AMOUNT)
        
    def increase_interest_rate(self) -> None:
        self.interest_rate += 0.5