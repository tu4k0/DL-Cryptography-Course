# Practice #3. Дослідження S-блоку та P-блоку.

## Опис завдання:  
Програмна реалізація алгоритмів S-блоку та P-блоку (пряме та зворотне перетворення).

## Технології:   
1. Мова програмування: Python;
2. IDE: PyCharm;
3. Автоматизоване тестування: unittest;  
4. Бібліотеки: random.  

## Особливості реалізації:
1. s_box.py - містить константи та методи алгоритму прямого та зворотного симетричного криптографічного перетворення з використанням автоматично згенерованого S-блоку;   
2. p_box.py - містить константи та методи алгоритму прямого та зворотного симетричного криптографічного перетворення з використанням автоматично згенерованого P-блоку;   
3. Довжина вхідних даних - 8 бітів (1 байт), вихідних - 8 бітів;
4. Таблиці S-блоків мають розмір 2х2 (2 inner bits, 2 outer bits), кожна комірка містить унікальне значення від 0-15(F) у двійковому вигляді (4 біти).  


## Інструкція щодо запуску коду:  
У cmd за розташуванням проекту (..\Practice3\SBox_PBox_application\application) набрати команду python s_box.py (для S-блоку) або python p-box.py (для P-блоку) та слідувати настановам інтерфейсу.  

## Результати виконання програми для вхідного значення 200 (тип даних integer):  
S-блок  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice3/SBox_PBox_application/images/S-block_result.png)

P-блок  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice3/SBox_PBox_application/images/P-block_result.png)

## Результати тестів:  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice3/SBox_PBox_application/images/tests.png)
