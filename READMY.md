API Servis Deposit

Все необходимые библиотеки в requirements.txt
Основной файл app.py

Запустить проект командой 
python3 -m venv Serv_deposit_venv
source Serv_deposit_venv/bin/activate
pip install -r requirements.txt
python3 app.py

API принимает параметры следующего типа {
       "date": "25.01.2022",
       "period": 3,
       "amount": 10000,
       "rate": 6
       
}

возвращает JSON в виде {
    "25.01.2022": 10050.00,
    "25.02.2022": 10100.25,
    "25.03.2022": 10150.75
}
Учитываются ограничения описаны в task.py

При корректных данных отдает таблицу с данными и расчетами,
При некоректных данных выдает описанную ошибку с кодом 400

Документацию swagger можно посмотреть по ссылке http://127.0.0.1:5000/apidocs/
