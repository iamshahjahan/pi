import abc
import enum
from abc import ABC

from splitwise.models import Expense


class SplitType(enum.Enum):
    EQUAL, PERCENTAGE, EXACT = 1, 2, 3


class SplitStrategy(ABC):
    @abc.abstractmethod
    def split_amount(self):
        pass


class EqualSplitStrategy(SplitStrategy):
    expenses = []
    users = []
    amount = 0

    def __init__(self, users, amount):
        super().__init__()
        self.users = users
        self.amount = amount
        self.split_type = SplitType.EQUAL
        self.expenses = []

    def split_amount(self):
        for user in self.users:
            self.expenses.append(Expense(user, self.amount))
        return self.expenses


class PercentageSplitStrategy():
    def __init__(self):
        self.split_type = SplitType.PERCENTAGE

        pass


class ExactSplitStrategy():
    def __init__(self):
        pass
