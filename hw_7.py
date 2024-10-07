import sqlite3

conn = sqlite3.connect('bank_system.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INTEGER,
            address VARCHAR(100),
            email VARCHAR(100),
            balance REAL DEFAULT 0.0
        )
    ''')
    conn.commit()

def open_account(first_name, last_name, age, address, email):
    cursor.execute('''
        INSERT INTO accounts (first_name, last_name, age, address, email)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, age, address, email))
    conn.commit()
    print(f"Счет успешно открыт для {first_name} {last_name}.")

def deposit(account_id, amount):
    if amount <= 0:
        print("Сумма должна быть положительной.")
        return
    
    cursor.execute('''
        UPDATE accounts SET balance = balance + ? WHERE id = ?
    ''', (amount, account_id))
    conn.commit()
    print(f"Счет ID {account_id} пополнен на {amount}. Новая сумма: {get_balance(account_id)}.")

def withdraw(account_id, amount):
    current_balance = get_balance(account_id)
    if amount <= 0:
        print("Сумма должна быть положительной.")
        return
    if amount > current_balance:
        print("Недостаточно средств для снятия.")
        return
    
    cursor.execute('''
        UPDATE accounts SET balance = balance - ? WHERE id = ?
    ''', (amount, account_id))
    conn.commit()
    print(f"Счет ID {account_id} снят на {amount}. Остаток: {get_balance(account_id)}.")

def get_balance(account_id):
    cursor.execute('''
        SELECT balance FROM accounts WHERE id = ?
    ''', (account_id,))
    result = cursor.fetchone()
    return result[0] if result else None

if __name__ == "__main__":
    create_table()

    open_account('amigo', 'matazim', 17, 'kirov', 'фьшпщ@gmail.com')
    open_account('alex', 'pereyra', 25, 'new york', 'alex@gmail.com')

    account_id = 1  
    print(f"Баланс счета ID {account_id}: {get_balance(account_id)}")

    deposit(account_id, 1000)

    withdraw(account_id, 500)

    print(f"Баланс счета ID {account_id} после операций: {get_balance(account_id)}")

conn.close()
