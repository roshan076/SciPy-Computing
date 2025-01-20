class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        total = f"Total: {self.get_balance()}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    for category in categories:
        spent = sum([item["amount"] for item in category.ledger if item["amount"] < 0])
        category_spent.append(spent)
        total_spent += spent

    percentages = [int(spent / total_spent * 100) for spent in category_spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            chart += "o" if percentage >= i else " "
            chart += "  "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"

    max_len = max([len(category.name) for category in categories])
    
    for i in range(max_len):
        chart += "     "
        for category in categories:
            chart += category.name[i] if i < len(category.name) else " "
            chart += "  "
        chart += "\n"

    return chart.strip()

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

entertainment = Category('Entertainment')
entertainment.deposit(500, 'initial deposit')
entertainment.withdraw(150, 'movies')

print(food)
print(clothing)
print(entertainment)
print(create_spend_chart([food, clothing, entertainment]))