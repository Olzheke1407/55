from fractions import Fraction

def calculate_fraction_operations(fraction_str1, fraction_str2):
    try:
        
        fraction1 = Fraction(fraction_str1)
        fraction2 = Fraction(fraction_str2)

        
        sum_result = fraction1 + fraction2
        product_result = fraction1 * fraction2

        return sum_result, product_result
    except ValueError:
        return "Ошибка: Неверный формат дроби. Используйте формат 'a/b'."


fraction_str1 = input("Введите первую дробь (в формате a/b): ")
fraction_str2 = input("Введите вторую дробь (в формате a/b): ")

result = calculate_fraction_operations(fraction_str1, fraction_str2)


if isinstance(result, tuple):
    print(f"Сумма: {result[0]}")
    print(f"Произведение: {result[1]}")
else:
    print(result)
