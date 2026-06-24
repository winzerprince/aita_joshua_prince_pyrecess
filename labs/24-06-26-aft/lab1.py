# Create a method overloading and method overiding that completes a banking system
# The parent class must be transaction and the child class can be deposit withdraw and transfer
# Demonstrate and employer depositing, withdrawing, and transfering
#


class Transaction:
    def __init__(self, account_number):
        self.account_number = account_number

    def process(self, amount, target_account=None):
        raise NotImplementedError("Subclasses must implement this method")


class Deposit(Transaction):
    def process(self, amount, target_account=None):
        if isinstance(amount, float) and amount > 0:
            print(f"Depositing ${amount} to account {self.account_number}")
        elif isinstance(amount, int) and amount > 0:
            print(f"Depositing ${amount} to account {self.account_number}")


class Withdraw(Transaction):
    def process(self, amount, target_account=None):
        if isinstance(amount, float) and amount > 0:
            print(f"Withdrawing ${amount} from account {self.account_number}")
        elif isinstance(amount, int) and amount > 0:
            print(f"Withdrawing ${amount} from account {self.account_number}")


class Transfer(Transaction):
    def process(self, amount, target_account=None):
        if isinstance(amount, float) and amount > 0:
            print(
                f"Transferring ${amount} from account {self.account_number} to account {target_account}"
            )
        elif isinstance(amount, int) and amount > 0:
            print(
                f"Transferring ${amount} from account {self.account_number} to account {target_account}"
            )


deposit = Deposit("234434")

deposit.process(100.0)

withdraw = Withdraw("234434")

withdraw.process(50)

transfer = Transfer("234434")
transfer.process(25.0, "987654")
