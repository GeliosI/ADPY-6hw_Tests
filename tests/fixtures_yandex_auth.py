FIXTURES_BAD_PASSWD = [
    ('test', 'admin', 'Неверный пароль'),
    ('qwerty', 'elephant', 'Неверный пароль'),
]

FIXTURES_BAD_LOGIN = [
    ('admin', 'Логин введен некорректно или удален'),
    ('elephant@', 'Такой логин не подойдет'),
]

FIXTURES_CORRECT_LOGIN_AND_PASSWD = [
    ('correct_login', 'correct_passwd', 'https://passport.yandex.ru/auth/welcome'),
]