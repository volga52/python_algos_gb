"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


def processing1(dict_test):         # O!(n*log(n))
    login, pas = input('Введите логин: '), input('Введите пароль: ')    # O +(1)
    if login in dict_test:                              # O n*log(n)
        if pas == dict_test.get(login)[0]:              # O n*log(n)
            if dict_test.get(login)[1]:                 # O n*log(n)
                print('ok')                             # O +(1)
            else: print('Активируйте учетную запись')   # O(1)
        else: print('Не верный пароль')                 # O(1)
    else: print('Не верный логин')                      # O(1)
    return


def processing2(dict_test):         # O!(n*log(n))
    login = input('Введите логин: ')                    # O +(1)
    test_list = (input('Введите пароль: '), 1)          # O +(1)
    err_list = ('Не верный логин или пароль', 'Активируйте аккаунт')    # O +(1)
    for i, j in enumerate(test_list):                   # O 3*(1)
        if j != dict_test.get(login, "*")[i]:           # O n*log(n)
            print(err_list[i])                          # O(1)
            return
    print('ok')                                         # O +(1)
    return


users = {
    'a': ('1', 1),
    'b': ('2', 1),
    'c': ('3', 1),
    'd': ('4', 0)
}

# processing2(users)
# processing1(users)

"""
2. Описание сложности в комментариях кода по каждой строчке
3. Сложность функций примерно одинаковая. 3*n*log(n)
"""
