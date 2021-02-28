# -----------
# NEEDS SOME WHITESPACE TO BE WORK
# -----------
def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier


def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded = list(map(lambda x: truncate(x / total), breakdown))
    return rounded


def create_spend_chart(categories):
    """
    create_spend_chart that takes a list fo categories as an argument
    It should return a string that is a bar chart
    """

    res = "Percentage spent by category\n"
    i = 100
    totals = get_totals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o "
            else:
                cat_spaces += "  "
        res += str(i).rjust(3) + "|" + cat_spaces + "\n"
        i -= 10

    dashes = "-" + "---" * len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        name_str = '    '
        for name in names:
            if x >= len(name):
                name_str += "  "
            else:
                name_str += name[x] + " "

        if x != len(maxi) - 1:
            name_str += '\n'

        x_axis += name_str

    res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
    return res


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        """
        A deposit method that accepts the
        amount and description
        The ledger list is in the form of :
        {'amount':amount,'description': description}
        """

        self.ledger.append({'amount': amount, 'description': description})

        return None

    def withdraw(self, amount, description=""):
        """
        A withdraw method that is similar to the deposit method
        but the amount passed in should be stored in the ledger as a negative number
        """

        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        """
        The get_balance method returns the current balance of the budget
        """

        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]

        return total_cash

    def transfer(self, amount, category):
        """
        A transfer method that accepts an amount
        and another budget category as arguments.
        """

        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        """
        A check method that accepts an amount as argument
        It returns False if the amount is greater than the balance of the budget category
        """

        if self.get_balance() >= amount:
            return True
        return False

    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total
