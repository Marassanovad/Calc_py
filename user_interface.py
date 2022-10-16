def Interface(i:str):
    match i:
        case "Welcome":
            print('---------------------------------------------')
            print('Здравствуйте')
        case "Menu":
            print('---------------------------------------------')
            print('Варианты работы программы')
            print('1. Калькулятор для работы с рациональными числами')
            print('2. Калькулятор для работы с комплексными числами')
            print('3. Выход из программы')
        case "Action":
            print('---------------------------------------------')
            print('Варианты работы программы')
            print('1. Введите "+" чтобы a+b')
            print('2. Введите "-" чтобы a-b')
            print('3. Введите "*" чтобы выбрать действия умножения')
            print('4. Введите "/" чтобы выбрать действие деления')
            print('5. Выход из программы')
        
        case "Mistake":
            print('---------------------------------------------')
            print('------ Ошибка -------')
            

        
        case "Mult":
            print('---------------------------------------------')
            print('Варианты работы программы')
            print('1. Введите "1" чтобы a*b')
            print('2. Введите "2" чтобы a**b')
            print('3. Выход из программы')
        
        case "Div":
            print('---------------------------------------------')
            print('Варианты работы программы')
            print('1. Введите "1" чтобы a/b')
            print('2. Введите "2" чтобы a//b')
            print('2. Введите "3" чтобы a"%"b')
            print('2. Выход из программы')
                
        case "End":
            print('----------------------------------------------')
            print('Выберите дальнейшее действие')
            print('1. Выход в главное меню')
            print('2. Выход из программы')