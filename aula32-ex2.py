horas = input('Digite as horas atuais: ')

if horas.isnumeric():
    horas = int(horas)
    if 0 <= horas <= 11:
        print('BOM DIA')
    elif 12 <= horas <= 17:
        print('BOA TARDE')
    elif 18 <= horas <= 23:
        print('BOA NOITE')
    else:
        print('HORAS INVÁLIDAS')
