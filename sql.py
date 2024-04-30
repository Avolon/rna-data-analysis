import mysql.connector

# Параметры подключения к базе данных
db_config = {
    'host': 'mysql-rfam-public.ebi.ac.uk',
    'port': 4497,
    'user': 'rfamro',
    'password': '',
    'database': 'Rfam'
}

# Функция для выполнения запроса и вывода результатов
def execute_query(query):
    try:
        # Подключение к базе данных
        connection = mysql.connector.connect(**db_config)
        
        # Создание курсора
        cursor = connection.cursor()
        
        # Выполнение запроса
        cursor.execute(query)
        
        # Получение результатов запроса
        result = cursor.fetchall()
        
        # Вывод результатов
        for row in result:
            print(row)
            
        # Закрытие курсора и соединения
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

# Запрос 1: выбор первой строки из таблицы fr.fram_acc
query1 = "SELECT * FROM fr.fram_acc LIMIT 1"
print("Result of Query 1:")
execute_query(query1)
print()

# Запрос 2: выбор всех РНК крыс
query2 = """
    SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end
    FROM full_region fr, rfamseq rf, taxonomy tx
    WHERE rf.ncbi_id = tx.ncbi_id
    AND fr.rfamseq_acc = rf.rfamseq_acc
    AND tx.ncbi_id = 10116
    AND is_significant = 1
"""
print("Result of Query 2:")
execute_query(query2)
