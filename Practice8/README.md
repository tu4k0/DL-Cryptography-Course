# Practice #8. Написання обгортки для зручного використання бібліотеки, що працює з алгеброю на еліптичних кривих.

## Опис завдання:  
Програмна реалізація бібліотечних модулів для перетворень в групі точок еліптичної кривої, а також встановлення параметрів кривої.    

## Технології:   
1. Мова програмування: Python;
2. IDE: PyCharm;
3. Автоматизоване тестування: unittest;  
4. Бібліотеки: cryptography.hazmat.backends, cryptography.hazmat.primitives.asymmetric, ecpy.curves. 

## Особливості реалізації:
1. eliptic_curve - містить клас, який містить обгортки до бібліотечних функцій, що виконують основні перетворення з точками еліптичної кривої;
2. tests - містить Unit-тести перевірки на правильність роботи перетворень точок еліптичної кривої;
3. main.py - містить демонстрацію роботи програми, яка генерує точки на еліптичній кривій secp256k1 та здійсеює відповідні алгебраїчні перетворення в групі точок еліптичної кривої.    


## Інструкція щодо запуску коду:  
У cmd або IDE (які мають модуль для роботи з Python) за розташуванням проекту (..\Practice8) набрати команду python main.py  

## Результати виконання програми:  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice8/images/main_screenshot.png) 

## Результати тестів:  
![Image text](https://github.com/tu4k0/DL-Cryptography-Course/blob/master/Practice8/images/test_screenshot.png)
