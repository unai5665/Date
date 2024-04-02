from datetime import datetime, timedelta

class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        # Validar día, mes y año
        if year < 1900 or year > 2050:
            year = 1900
        if month < 1 or month > 12:
            month = 1
        if day < 1 or day > self.days_in_month(month, year):
            day = 1

        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year: int) -> bool:
        '''Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, y también si es divisible entre 400.'''
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.is_leap_year(year) and month == 2:
            return 29
        else:
            return days[month-1]

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha.'''
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        
        delta_days = (self.year - 1900) * 365
        for y in range(1900, self.year):
            if self.is_leap_year(y):
                delta_days += 1

       
        for m in range(1, self.month):
            delta_days += days_in_month[m - 1]
            if m == 2 and self.is_leap_year(self.year):
                delta_days += 1
        delta_days += self.day - 1

        return delta_days

    @property
    def weekday(self) -> int:
        fecha = datetime(self.year, self.month, self.day)
        return fecha.weekday()

    @property
    def is_weekend(self) -> bool:
        '''Devuelve True si la fecha corresponde a un sábado, False de lo contrario.'''
        return self.weekday == 6

    @property
    def short_date(self) -> str:
        return "{:02d}/{:02d}/{:04d}".format(self.day, self.month, self.year)

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        weekdays = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
        month_names = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        day_of_week = datetime(self.year, self.month, self.day).weekday()
        return f"{weekdays[day_of_week]} {self.day} DE {month_names[self.month - 1]} DE {self.year}"

    def __add__(self, days: int):
        '''Sumar un número de días a la fecha'''
        date_obj = datetime(self.year, self.month, self.day) + timedelta(days=days)
        return Date(date_obj.day, date_obj.month, date_obj.year)

    def __sub__(self, other):
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días de la fecha -> Nueva fecha'''
        if isinstance(other, Date):
            delta = datetime(self.year, self.month, self.day) - datetime(other.year, other.month, other.day)
            return delta.days
        elif isinstance(other, int):
            date_obj = datetime(self.year, self.month, self.day) - timedelta(days=other)
            return Date(date_obj.day, date_obj.month, date_obj.year)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Date' and '{}'".format(type(other)))

    def __lt__(self, other):
        '''Menor que (<)'''
        if isinstance(other, Date):
            return (self.year, self.month, self.day) < (other.year, other.month, other.day)
        raise TypeError("Unsupported operand type(s) for <: 'Date' and '{}'".format(type(other)))

    def __gt__(self, other):
        '''Mayor que (>)'''
        if isinstance(other, Date):
            return (self.year, self.month, self.day) > (other.year, other.month, other.day)
        raise TypeError("Unsupported operand type(s) for >: 'Date' and '{}'".format(type(other)))

    def __eq__(self, other) -> bool:
        '''Compara si dos fechas son iguales.'''
        if isinstance(other, Date):
            return (self.year, self.month, self.day) == (other.year, other.month, other.day)
        return False

fecha = Date(21, 3, 2024)
print(Date.is_leap_year(2024))
print(Date.days_in_month(3, 2024))
print(fecha.get_delta_days())
print(fecha.weekday)
print(fecha.is_weekend)
print(fecha.short_date)
print(fecha)
nueva_fecha = fecha + 10
print(nueva_fecha.short_date)
fecha_anterior = fecha - 3
print(fecha_anterior.short_date)
otra_fecha = Date(1, 1, 2024)
diferencia = fecha - otra_fecha
print(diferencia)
print(otra_fecha < fecha)
print(fecha > otra_fecha)
print(otra_fecha == fecha)