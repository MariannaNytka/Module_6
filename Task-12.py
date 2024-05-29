class IDException(Exception):
    pass

def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Employee ID must start with '01'.")
    id_list.append(employee_id)
    return id_list

# Приклад використання:
id_list = ['01001', '01002', '02001']
try:
    id_list = add_id(id_list, '01003')  # Додаємо коректний employee_id
    print(id_list)  # ['01001', '01002', '02001', '01003']
    id_list = add_id(id_list, '02002')  # Генеруємо виключення, тому що '02002' не починається з '01'
except IDException as e:
    print(f"Error: {e}")
    