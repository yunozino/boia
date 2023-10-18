mes = int(input('mês que nasceu: '))
dia = int(input('seu dia: '))
if mes == 1 and dia >= 20  or mes == 2 and dia <= 18:
    print('é de aquários')
else:
    if mes == 2 and dia >= 19 or mes == 3 and dia <= 20:
        print('é de peixes')
    else:
        if mes == 3 and dia >= 21 or mes == 4 and dia <= 19:
            print('é de touro')
        else:
            if mes == 4 and dia >= 20 or mes == 5 and dia <= 20:
                print('é de touro')
            else:
                if mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
                    print('é de gêmeos')
                else:
                    if mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
                        print('é de câncer')
                    else:
                        if mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
                            print('é de leão')
                        else:
                            if mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
                                print('é de virgem')
                            else:
                                if mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
                                    print('é de libra')
                                else:
                                    if mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
                                        print('é de escorpião')
                                    else:
                                        if mes == 11 and dia >= 23 or mes == 12 and dia <= 21:
                                            print('é de sagitário')
                                        else:
                                            if mes == 12 and dia >= 22 or mes == 1 and dia <= 19:
                                                print('é de capricórnio')
                                            else:
                                                print('???????? cade o sentido mano?')