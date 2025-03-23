import sqlite3


connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

cursor.execute('ALTER TABLE animals ADD COLUMN room INTEGER')
cursor.execute("DELETE FROM animals WHERE name = 'Лев'")

cursor.execute("INSERT INTO animals (name, species, age, room) VALUES ('Лев', 'Хищник', 5, 25)")

connection.commit()

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
