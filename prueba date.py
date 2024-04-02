from date import Date

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