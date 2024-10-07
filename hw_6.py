import sqlite3

conn = sqlite3.connect('wizards.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wizards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            age INTEGER,
            house VARCHAR(20),
            magic_level INTEGER CHECK(magic_level BETWEEN 1 AND 100),
            special_ability VARCHAR(50)
        )
    ''')
    conn.commit()

def add_wizard(first_name, last_name, age, house, magic_level, special_ability):
    cursor.execute('''
        INSERT INTO wizards (first_name, last_name, age, house, magic_level, special_ability)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, age, house, magic_level, special_ability))
    conn.commit()
    print(f"Волшебник {first_name} {last_name} добавлен.")

def find_wizard_by_ability(ability):
    cursor.execute('''
        SELECT first_name, last_name FROM wizards WHERE special_ability = ?
    ''', (ability,))
    results = cursor.fetchall()
    
    if results:
        print(f"Волшебники с способностью '{ability}':")
        for row in results:
            print(f"{row[0]} {row[1]}")
    else:
        print(f"Нет волшебников с способностью '{ability}'.")

def list_wizards_by_house(house):
    cursor.execute('''
        SELECT first_name, last_name FROM wizards WHERE house = ?
    ''', (house,))
    results = cursor.fetchall()
    
    if results:
        print(f"Волшебники из дома '{house}':")
        for row in results:
            print(f"{row[0]} {row[1]}")
    else:
        print(f"Нет волшебников из дома '{house}'.")

def update_magic_level(wizard_id, new_level):
    cursor.execute('''
        UPDATE wizards SET magic_level = ? WHERE id = ?
    ''', (new_level, wizard_id))
    conn.commit()
    print(f"Уровень магии волшебника с ID {wizard_id} обновлен на {new_level}.")

def delete_wizard(wizard_id):
    cursor.execute('''
        DELETE FROM wizards WHERE id = ?
    ''', (wizard_id,))
    conn.commit()
    print(f"Волшебник с ID {wizard_id} удален.")

if __name__ == "__main__":
    create_table()

    add_wizard('amigo', 'matazim', 17, 'kirov', 85, 'neckromant')
    add_wizard('asko', 'madamin', 17, 'kara cuu', 95, 'fire boll')
    add_wizard('jumi', 'ayti', 18, 'ak orgo', 75, 'amaterasu')

    user_input_ability = input("Введите название способности для поиска: ")
    find_wizard_by_ability(user_input_ability)

    user_input_house = input("Введите название дома для вывода волшебников: ")
    list_wizards_by_house(user_input_house)

    wizard_id = int(input("Введите ID волшебника для обновления уровня магии: "))
    new_level = int(input("Введите новый уровень магии (1-100): "))
    update_magic_level(wizard_id, new_level)

    wizard_id_to_delete = int(input("Введите ID волшебника для удаления: "))
    delete_wizard(wizard_id_to_delete)

conn.close()
