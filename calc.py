class Calculator:
    """Простой калькулятор, выполняющий базовые арифметические операции."""

    def add(self, a, b):
        """Складывает два числа.

        :param a: Первое число.
        :param b: Второе число.
        :type a: int or float
        :type b: int or float
        :raises TypeError: если a или b не являются числами.
        :returns: Сумма a и b.
        :rtype: int or float
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами")
        return a + b

    def subtract(self, a, b):
        """Вычитает одно число из другого.

        :param a: Число, из которого вычитается.
        :param b: Число, которое вычитается.
        :type a: int or float
        :type b: int or float
        :raises TypeError: если a или b не являются числами.
        :returns: Разность a и b.
        :rtype: int or float
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами")
        return a - b

    def multiply(self, a, b):
        """Умножает два числа.

        :param a: Первый множитель.
        :param b: Второй множитель.
        :type a: int or float
        :type b: int or float
        :raises TypeError: если a или b не являются числами.
        :returns: Произведение a и b.
        :rtype: int or float
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами")
        return a * b

    def divide(self, a, b):
        """Делит одно число на другое.

        :param a: Делимое.
        :param b: Делитель.
        :type a: int or float
        :type b: int or float
        :raises TypeError: если a или b не являются числами.
        :raises ZeroDivisionError: если b равно нулю.
        :returns: Результат деления a на b.
        :rtype: int or float
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами")
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        return a / b