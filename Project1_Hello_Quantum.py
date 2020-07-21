# Catarina Sofia dos Santos Sousa, nº 93695
def eh_tabuleiro(t):
    '''
    eh_tabuleiro: universal -> booleano
    Funcao que recebe um argumento qualquer e devolve um booleano
    Retorna True se o argumento for um tuplo com 3 tuplos de tamanho 3, 3 e 2, respetivamente e se os elementos
    dos tuplos for -1, 1 ou 0, caso contrario retorna False
    :param t: Universal que representa um possivel tabuleiro
    :return: Booleano
    '''
    if isinstance(t, tuple) and len(t) == 3:
        if isinstance(t[0], tuple) and isinstance(t[1], tuple) and isinstance(t[2], tuple):
            if len(t[0]) == 3 and len(t[1]) == 3 and len(t[2]) == 2:
                for e in range(len(t)):
                    for i in range(len(t[e])):
                        if t[e][i] != 0 and t[e][i] != 1 and t[e][i] != -1:
                            return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def substitui(t):
    '''
    substitui: tabuleiro -> cadeia de caracteres
    Funcao que recebe um tabuleiro e substitui o valor -1 por 'x' em todos os tuplos
    :param t: tabuleiro
    :return: cadeia de caracteres com os valores do tuplo novo
    '''
    t2 = ()
    for i in range(len(t)):
        for e in (range(len(t[i]))):
            if t[i][e] == -1:
                t2 = t2 + ('x',)
            else:
                t2 = t2 + (t[i][e],)
    return "+-------+\n" \
           "|...{}...|\n" \
           "|..{}.{}..|\n" \
           "|.{}.{}.{}.|\n" \
           "|..{}.{}..|\n" \
           "+-------+".format(t2[2], t2[1], t2[5], t2[0],
                              t2[4], t2[7], t2[3], t2[6])


def tabuleiro_str(t):
    '''
    tabuleiro_str: tabuleiro -> cadeia de caracteres
    Funcao que recorre a funcao eh_tabuleiro para verificar se o tabuleiro inserido e valido
    Se o tabuleiro for valido recorre a funcao auxiliar substitui
    :param t: tabuleiro
    :return: cadeia de caracteres
    '''
    if eh_tabuleiro(t) == True:
        return substitui(t)
    else:
        raise ValueError("tabuleiro_str: argumento invalido")


def tabuleiros_iguais(t1, t2):
    '''
    tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    Funcao que recorre a funcao eh_tabuleiro para verificar se ambos os tabuleiros inseridos sao validos
    Retorna True se os dois tabuleiros forem iguais, caso contrário retorna False
    :param t1: tabuleiro
    :param t2: tabuleiro
    :return: Booleano
    '''
    if eh_tabuleiro(t1) == True and eh_tabuleiro(t2) == True:
        if t1 == t2:
            return True
        else:
            return False
    else:
        raise ValueError("tabuleiros_iguais: um dos argumentos nao e tabuleiro")


def porta_x(t, c):
    '''
    porta_x: tabuleiro x {'E', 'D'} -> tabuleiro
    Funcao que recorre a funcao eh_tabuleiro para verificar se o tabuleiro inserido e valido, se não for gera
    erro
    Se o caracter for 'E', troca os valores do 2º tuplo: 1 por 0 e 0 por 1
    Se o caracter for 'D', junta os 3 tuplos num unico tuplo, verifica as posicoes 1, 4 e 6 e troca os valores
    do novo tuplo, 0 por 1 e 1 por 0
    Por fim divide o novo tuplo em 3 tuplos de tamanho 3, 3 e 2, respetivamente
    :param t: tabuleiro
    :param c: 'E', 'D'
    :return: tabuleiro
    '''
    tnovo = ()
    if c == "E" and eh_tabuleiro(t) == True :
        for e in range(len(t[1])):
            if t[1][e] == 1:
                tnovo = tnovo + (0,)
            elif t[1][e] == 0:
                tnovo = tnovo + (1,)
            elif t[1][e] == -1:
                tnovo = tnovo + (-1,)
        tnovo1 = (t[0],) + (tnovo,) + (t[2],)
        return tnovo1
    elif c == "D"and eh_tabuleiro(t) == True:
        tnovo = (t[0] + t[1] + t[2])
        for e in (1, 4, 6):
            if tnovo[e] == 1:
                tnovo = tnovo[0:e] + (0,) + tnovo[e+1:]
            elif tnovo[e] == 0:
                tnovo = tnovo[0:e] + (1,) + tnovo[e+1:]
        tnovo1 = (tnovo[0:3], tnovo[3:6], tnovo[6:])
        return tnovo1
    else:
        raise ValueError("porta_x: um dos argumentos e invalido")


def porta_z (t, c):
    '''
    porta_z: tabuleiro x {'E', 'D'} -> tabuleiro
    Funcao que recorre a funcao eh_tabuleiro para verificar se o tabuleiro inserido e valido, se não for gera
    erro
    Se o caracter for 'E' troca os valores do 1º tuplo, 0 por 1 e 1 por 0
    Se o caracter for 'D' junta os 3 tuplos num unico tuplo, verifica as posicoes 2, 5 e 7 e troca os valores
    do novo tuplo, 0 por 1 e 1 por 0
    Por fim divide o novo tuplo em 3 tuplos de tamanho 3, 3 e 2, respetivamente
    :param t: tabuleiro
    :param c: 'E', 'D'
    :return: tabuleiro
    '''
    if eh_tabuleiro(t) == True:
        if c == "E":
            t1 = ()
            for e in t[0]:
                if e == -1:
                    t1 = t1 + (-1,)
                elif e == 1:
                    t1 = t1 + (0,)
                elif e == 0:
                    t1 = t1 + (1,)
            t1 = (t1, t[1], t[2])
            return t1
        elif c == "D":
            tnovo = (t[0] + t[1] + t[2])
            for e in (2, 5, 7):
                if tnovo[e] == 1:
                    tnovo = tnovo[0:e] + (0,) + tnovo[e+1:]
                elif tnovo[e] == 0:
                    tnovo = tnovo[0:e] + (1,) + tnovo[e+1:]
            t1 = (tnovo[0:3], tnovo[3:6], tnovo[6:])
            return t1
        else:
            raise ValueError("porta_z: um dos argumentos e invalido")
    else:
        raise ValueError("porta_z: um dos argumentos e invalido")


def porta_h(t,c):
    '''
    porta_h: tabuleiro x {'E','D'} -> tabuleiro
    Funcao que recorre a funcao eh_tabuleiro para verificar se o tabuleiro inserido e valido, se não for gera
    erro
    Se o caracter for 'E' troca o 1º tuplo com o 2º
    Se o caracter for 'D' junta os 3 tuplos num unico tuplo e troca a 1ª posicao com a 2ª, a 4ª com a 5ª
    e a 6ª com a 7ª
    :param t: tabuleiro
    :param c: 'E','D'
    :return: tabuleiro
    '''
    if eh_tabuleiro(t) == True:
        if c == "E":
            t1 = (t[1], t[0], t[2])
            return t1
        elif c == "D":
            t1 = (t[0] + t[1] + t[2])
            t2 = (t1[0], t1[2], t1[1])
            t3 = (t1[3], t1[5], t1[4])
            t4 = (t1[7], t1[6])
            tnovo = (t2, t3, t4)
            return tnovo
        else:
            raise ValueError("porta_h: um dos argumentos e invalido")
    else:
        raise ValueError("porta_h: um dos argumentos e invalido")
