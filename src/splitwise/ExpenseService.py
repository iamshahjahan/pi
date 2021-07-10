from bill_service import BillService
from models import User, Group
from settlement_strategies import SettlementService
from split_strategies import SplitType


class ExpenseService:
    def __init__(self):
        self.group_bill_mapping = {}

    def create_expense(self):
        user1 = User("Shahjahan", "email1")
        user2 = User("Himanshu", "email1")
        user3 = User("Neelesh", "email1")

        my_group1 = Group()
        my_group1.add_user(user1)
        my_group1.add_user(user2)
        my_group1.add_user(user3)

        # my_group2 = Group()
        # my_group2.add_user(user1)
        # my_group2.add_user(user2)

        # Rs. 600 bill
        # user1 : 450
        # user2 : 150
        # user3

        total_amount = 600

        split_info = {
            'split_type': SplitType.EQUAL,
            'split_amount': total_amount / len(my_group1.users)
        }

        payment_info = {
            user1: 450,
            user2: 150
        }

        billService = BillService()

        bill1 = billService.create_bill(my_group1.users, total_amount, payment_info, split_info)

        self.group_bill_mapping[my_group1] = [bill1]

        total_amount = 300

        split_info = {
            'split_type': SplitType.EQUAL,
            'split_amount': total_amount / len(my_group1.users)
        }

        payment_info = {
            user3: 300,
        }

        billService = BillService()
        bill2 = billService.create_bill(my_group1.users, total_amount, payment_info, split_info)
        self.group_bill_mapping[my_group1].append(bill2)

        print(self.group_bill_mapping)

        settlement = SettlementService(self.group_bill_mapping)
        settlement.do_settlement()


if __name__ == "__main__":
    ExpenseService().create_expense()
