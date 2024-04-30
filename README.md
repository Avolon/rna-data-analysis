# rna-data-analysis
В этом примере:

on.push.paths указывает GitHub Actions запускать пайплайн только при изменении файлов, соответствующих указанному пути.
 Здесь sql.py - это ваш SQL-скрипт, который будет запускаться при изменении.
jobs.run_sql_script определяет задачу выполнения SQL-скрипта.
steps содержит последовательность шагов, необходимых для выполнения задачи.
actions/checkout@v2 используется для проверки репозитория.
actions/setup-python@v2 используется для установки Python.
sudo apt-get update && sudo apt-get install -y mysql-client используется для установки клиента MySQL.
python sql.py запускает ваш SQL-скрипт.