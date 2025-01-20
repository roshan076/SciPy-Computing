# Budget App

This project is a basic budget management system using Python that allows users to categorize their spending into different categories (e.g., Food, Clothing, Entertainment), track their deposits and withdrawals, and transfer money between categories. Additionally, it provides a graphical representation of spending by category.

---
## Class: `Category`

### Description:
The `Category` class represents a specific budget category, such as "Food" or "Clothing". It includes methods to manage deposits, withdrawals, transfers, and balances within that category.

### Attributes:
- `name`: The name of the category (e.g., "Food", "Clothing").
- `ledger`: A list to store transactions (deposits and withdrawals) in the category.

### Methods:
1. **`__init__(self, name)`**:
   - Initializes a category with a name and an empty ledger.
   
2. **`deposit(self, amount, description="")`**:
   - Adds a deposit to the category's ledger.
   - `amount`: The amount to deposit.
   - `description`: A brief description of the deposit (default is an empty string).
   
3. **`withdraw(self, amount, description="")`**:
   - Withdraws money from the category's balance.
   - `amount`: The amount to withdraw.
   - `description`: A brief description of the withdrawal (default is an empty string).
   - Returns `True` if the withdrawal is successful (i.e., sufficient funds), otherwise returns `False`.
   
4. **`get_balance(self)`**:
   - Returns the current balance of the category by summing the amounts in the ledger.
   
5. **`transfer(self, amount, category)`**:
   - Transfers money from the current category to another category.
   - `amount`: The amount to transfer.
   - `category`: The target category to which money will be transferred.
   - Returns `True` if the transfer is successful, otherwise returns `False`.
   
6. **`check_funds(self, amount)`**:
   - Checks whether the category has enough funds for a transaction.
   - `amount`: The amount to check.
   - Returns `True` if sufficient funds are available, otherwise `False`.
   
7. **`__str__(self)`**:
   - Returns a string representation of the category, including its name, transactions (with descriptions and amounts), and the total balance.

---

## Function: `create_spend_chart`

### Description:
The `create_spend_chart` function generates a bar chart (as text) showing the percentage of money spent in each category. It visually compares the spending across different categories.

### Arguments:
- `categories`: A list of `Category` objects whose spending is to be charted.

### Method:
1. **Calculates the total amount spent** in each category by summing the negative amounts (withdrawals) in the `ledger` of each category.
2. **Computes the percentage** of the total spending that each category represents.
3. **Generates a bar chart** using these percentages, with the height of each bar representing the percentage of total spending.

### Returns:
- A string representation of a bar chart with each category's percentage of total spending, displayed as a vertical chart with labels.

---