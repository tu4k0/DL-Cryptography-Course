# Practice #9. Реалізація алгоритму цифрового підпису ECDSA.

## Опис завдання:  
Програмна реалізація алгоритму цифрового підпису на еліптичних кривих.    

## Технології:   
1. Мова програмування: Python;
2. IDE: PyCharm;
3. Автоматизоване тестування: unittest;  
4. Бібліотеки: Practice5.hashing_algorithms.SHA1_own, Practice8.eliptic_curve, Practice9.ECDH. 

## Особливості реалізації:  
1. ECDSA - містить клас, який містить набір методів та атрибутів для формування цифрового підпису за алгоритмом ECDSA;  
2. tests - містить Unit-тести перевірки на правильність роботи протоколу ECDSA;  
3. main.py - містить демонстрацію роботи протоколу, генерує приватні та публічні ключі, виконує підпис повідомлення та перевірки підпису.      


## Інструкція щодо запуску коду:  
У cmd або IDE (які мають модуль для роботи з Python) за розташуванням проекту (..\Practice10) набрати команду python main.py  

## Результати виконання програми:  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice10/images/main_screenshot.png) 

## Результати тестів:  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice10/images/test_screenshot.png)
