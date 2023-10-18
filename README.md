
## О данном проекте 
* Для просмотра тестового задаяния

### Запуск
1. Клонируем проект с репозитория
```python
git clone https://github.com/yottabufer/test_task.git
```
2. Переходим в папку созданную папку
```python
cd test_task
```
3. Создаём виртуально окружение для работы с проектом
```python
python -m venv venv_testtask
```
4. Активируем виртуальное окружение
	
+ Linux
```python
source venv_testtask/bin/activate
```
+ Windows
```python
venv_testtask\Scripts\activate.ps1
```
5. Устанавливаем зависимости
```python
pip install -r requirements.txt
```
6. Заполняем БД
```python
python manage.py migrate
```
7. Заполняем тестовые заказы
```python
python manage.py order_create
```
8. Выводи в консоль заказы сгрупированные по стелажам
```python
python manage.py out_order
```
