from factories import Factory
from models import Bill
from payment_strategies import ExactPaymentStrategy
from split_strategies import EqualSplitStrategy, SplitStrategy


class BillService:

    def create_bill(self, users, total_amount, payment_info, split_info):
        split_strategy: SplitStrategy = Factory.get_strategy(users, split_info.get("split_type"), split_info)
        expenses = split_strategy.split_amount()

        payment_strategy = ExactPaymentStrategy(payment_info)
        payments = payment_strategy.get_payment()

        bill = Bill(users, total_amount, expenses, payments)

        # insert
        return bill
        # self.bills.append(bill)

    #         Bill:
#         i.users
#         involved.
#         ii.total
#         amount.
#         iii.expense:
#         users
#         strategy
#         i.equal
#         ii.percentage
#         < user, percentage >
#
#
# iv.payment:
# < user, amount >


# Rs. 600 bill
# user1 : 450
# user2 : 150
# user3
# user4
# user5
# user6

# user settlement:
