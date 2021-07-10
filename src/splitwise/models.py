class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Group:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class Expense:
    def __init__(self, user, expense_amount):
        self.user = user
        self.expense_amount = expense_amount


class Payment:
    def __init__(self, user, payment_amount):
        self.user = user
        self.payment_amount = payment_amount


# class Settlement:
#     def __init__(self, bill, user, settlement_amount):
#         self.user = user
#         self.settlement_amount = settlement_amount
#         self.bill = bill


class Bill:
    def __init__(self, users, amount, expenses, payments):
        self.users = users
        self.amount = amount
        self.expenses = expenses
        self.payments = payments
