"""
    La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un
    periodo de tiempo dedo, expresandolo en horas y minutos. Las horas van de 0 a 23 y los
    minutos de 0 a 59. El resultado debe ser mostrado en consola

    Variables
        * hora_inicio_evento = Hora en la que inicia el evento
        * minutos_inicio_evento = Minutos en los que inicia el evento
        * duracion_evento = duración del evento en minutos
        * hora_finalizacion_evento = Hora en la que terminará eñ evento
        * minutos_finalizacion_evento = Los minutos en los cuales terminará el evento
        * h y m = Variables temporales para desglosar (duracion_evento) en horas y minutos
"""
def evento():
    try:
        hora_inicio_evento = int(input('Ingrese la hora en la que inicia el evento.  '))
        minutos_inicio_evento = int(input('Ingrese los minutos en los que inicia el evento. '))
        duracion_evento = int(input('Ingresa en minutos la duración del evento.  '))

        if (hora_inicio_evento >= 0 and minutos_inicio_evento >= 0 and duracion_evento >= 0):
            minutos_finalizacion_evento = duracion_evento + minutos_inicio_evento

            if minutos_finalizacion_evento > 59:
                h = minutos_finalizacion_evento // 60
                m = minutos_finalizacion_evento % 60
                minutos_finalizacion_evento = m
            else:
                h = 0

            hora_finalizacion_evento = hora_inicio_evento + h

            if hora_finalizacion_evento > 23:
                hora_finalizacion_evento -= 24

            print(f'El evento terminará a las {hora_finalizacion_evento}:{minutos_finalizacion_evento}')
        else:
            print('Debe ingresar valores positivos')
            evento()
    except Exception:
        print('Ingresaste datos inválidos, vuelve a intentarlo')
        evento()

evento()

