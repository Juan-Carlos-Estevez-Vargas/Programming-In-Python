"""
    Érase una vez una tierra - una tierra de leche y miel, habitada por gente feliz y 
    próspera. La gente pagaba impuestos, por supuesto, su felicidad tenía límites. El
    impuesto mas importante, denominado 'Impuesto Personal de ingresos(IPI para abreviar)'
    tenia que pagarse una vez al año y se evaluó utilizando la siguiente regla:

        * Si el ingreso del ciudadano no era superior a 85.528 pesos, el impuesto era igual
          al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal)
        * Si el ingreso era superior a esta cantidad, el impuesto era igual a 14.839 pesos y 2 
          centavos, más el 32% del excedente sobre 85528 pesos.
"""


def calculadora_impuestos():
    try:
        ingreso = float(input('Ingrese sus ingresos '))
        impuesto = 0

        if ingreso <= 85528:
            impuesto = ingreso * 0.18 - 556.2        
        else:
            temporal = ingreso - 14834.2
            temporal *= 0.32
            impuesto = temporal + 14834.2

        if impuesto < 0:
            impuesto = 0
        
        ingreso -= impuesto
        print(f'Impuesto: {impuesto}\nSaldo ingresos: {ingreso}')
    except Exception:
        print('Debe ingresar un valor válido')
        calculadora_impuestos()

calculadora_impuestos()
