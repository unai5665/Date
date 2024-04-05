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
        diasmes= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.is_leap_year(year) and month == 2:
            return 29
        else:
            return diasmes[month-1]

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha.'''
        dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        delta_days = (self.year - 1900) * 365
        for x in range(1900, self.year):
            if self.is_leap_year(x):
                delta_days += 1

        
        for m in range(1, self.month):
            delta_days += dias_en_mes[m - 1]
            if m == 2 and self.is_leap_year(self.year):
                delta_days += 1
        delta_days += self.day - 1

        return delta_days

    #En el metodo weekday de datetime hubo un problema y es que en este se representa el lunes con el 0 y el domingo con el 6, y el el test nos piden que el domingo sea 0 y el jueves sea 4 en vez de 3 con los cual he modificado el metodo. 

    @property
    def weekday(self) -> int:
        fecha = datetime(self.year, self.month, self.day)
        weekday_orden = fecha.weekday()
    
        ajuste_weekday = (weekday_orden + 1) % 7

        return ajuste_weekday

    @property
    def is_weekend(self) -> bool:
        '''Devuelve True si la fecha corresponde a un sábado, False de lo contrario.'''
        return self.weekday == 6

    
    @property
    def short_date(self) -> str:
        dia = self.day
        mes = self.month
        if self.day < 10:
            dia = "0"+ str(self.day)
        if self.month < 10:
            mes = "0"+ str(self.month)
        return f"{dia}/{mes}/{self.year}"


    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        weekdays = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
        nombremes = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        dias_semana = datetime(self.year, self.month, self.day).weekday()
        return f"{weekdays[day_of_week]} {self.day} DE {month_names[self.month - 1]} DE {self.year}"

    def __add__(self, days: int):
        '''Sumar un número de días a la fecha'''
        date_obj = datetime(self.year, self.month, self.day) + timedelta(days=days)
        return Date(date_obj.day, date_obj.month, date_obj.year)
