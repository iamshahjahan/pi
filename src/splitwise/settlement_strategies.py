import enum
from typing import List, Dict

from models import Payment, Bill


class SettlementStrategyType(enum.Enum):
    MINIMUM_TRANSACTION_STRATEGY = 1


class SettlementService:
    def __init__(self, group_bill_mapping):
        self.group_bill_mapping: Dict[str:List[Bill]] = group_bill_mapping

    def do_settlement(self):
        # generating settlement amount per bill
        for group, bills in self.group_bill_mapping.items():
            for bill in bills:
                settlement_dict = {}

                for user in bill.users:
                    settlement_dict[user] = 0

                for expense in bill.expenses:
                    settlement_dict[expense.user] -= expense.expense_amount

                for payment in bill.payments:
                    settlement_dict[payment.user] += payment.payment_amount

                print(settlement_dict)
