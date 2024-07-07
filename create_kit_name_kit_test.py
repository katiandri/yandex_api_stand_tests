import sender_stand_request


# Создаю тело запроса
def kkit_body(name):
    body = {
        "name": name
    }
    return body


# Создаю пустое тело
def empty_body():
    return {}


# Функция позитивной проверки
def positive_assert(live):
    kit_body = kkit_body(live)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == live


# Функция негативной проверки
def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


# Тест 1. Допустимое количество символов (1):
# kit_body = {
# "name": "a"
# }
def test_create_kit_name_with_one_symbol():
    positive_assert("a")


# Тест 2. 	Допустимое количество символов (511):
# kit_body = {
# "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
# }
def test_create_kit_name_with_max_symbols():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Количество символов меньше допустимого (0):
# kit_body = {
# "name": ""
# }
def test_create_kit_name_with_zero_symbols():
    body = kkit_body("")
    negative_assert(body)


# Тест 4. Количество символов больше допустимого (512):
# kit_body = {
# "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
# }
def test_create_kit_name_with_more_max_symbols():
    body = kkit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(body)


# Тест 5. Разрешены английские буквы:
# kit_body = {
# "name": "QWErty"
# }
def test_create_kit_name_with_english_letters():
    positive_assert("QWErty")


# Тест 6. Разрешены русские буквы:
# kit_body = {
# "name": "Мария"
# }
def test_create_kit_name_with_russian_letters():
    positive_assert("Мария")


# Тест 7. Разрешены спецсимволы:
# kit_body = {
# "name": ""№%@","
# }
def test_create_kit_name_with_specifical_letters():
    positive_assert("№%@", )


# Тест 8. Разрешены пробелы:
# kit_body = {
# "name": " Человек и КО "
# }
def test_create_kit_name_with_white_spaces():
    positive_assert(" Человек и КО ")


# Тест 9. Разрешены цифры:
# kit_body = {
# "name": "123"
# }
def test_create_kit_name_with_numbers():
    positive_assert("123")


# Тест 10. Параметр не передан в запросе:
# kit_body = {
# }
def test_create_kit_name_with_empty_body():
    kit_body = empty_body()
    negative_assert(kit_body)


# Тест 11. Передан другой тип параметра (число):
# kit_body = {
# "name": 123
# }
def test_create_kit_with_invalid_type():
    body = kkit_body(123)
    negative_assert(body)
