import sqlite3
from flask import Flask, request

app    = Flask(__name__)
conn   = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Prediction (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INT NOT NULL,
    class_name VARCHAR(64) NOT NULL,
    probability FLOAT NOT NULL
    );"""
)
conn.commit()
cursor.close()
conn.close()

@app.route('/add', methods=['POST'])
def add():
    if request.method != 'POST':
        return
    
    data = request.json
    data['probability'] = 100*float(f"{data['probability']:.4}")
    
    conn   = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO Prediction (class_id, class_name, probability)
        VALUES (?, ?, ?)
        ;""",
        (data['class_id'], data['class_name'], data['probability'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Success!", 200

if __name__ == '__main__':
    app.run(port=5001)