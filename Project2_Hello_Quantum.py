#################################################
##  Catarina Sofia dos Santos Sousa, Nº 93695  ##
##         PROJETO 2 - HELLO QUANTUM           ##
#################################################

########################
#  FUNCOES AUXILIARES  #
########################


def transforma(t):
    '''
    transforma: tuplo -> lista
    Funcao que transforma um tuplo numa lista e verifica se e uma lista composta por 3 listas de elementos
    iguais a -1, 0 ou 1
    :param t: tuplos
    :return: lista
    '''

    lst = [ii for i in t for ii in i]
    lst = [lst[:3], lst[3:6], lst[6:]]
    if isinstance(lst, list) and len(lst) == 3 and \
        all((isinstance(e, list)) for e in lst) and \
        all(len(e) == 2 if i == 2 else len(e) == 3 for i, e in enumerate(lst))\
       and all((a in (-1, 0, 1) for e in lst for a in e)):
            return lst
    return False


def primeiro_vetor(t):
    '''
    primeiro_vetor: tabuleiro -> vetor
    Funcao que recebe um tabuleiro e devolve o seu primeiro vetor
    :param t: tabuleiros
    :return: vetor
    '''
    return t[0]


def segundo_vetor(t):
    '''
    segundo_vetor: tabuleiro -> vetor
    Funcao que recebe um tabuleiro e devolve o seu segundo vetor
    :param t:tabuleiros
    :return: vetor
    '''
    return t[1]


def terceiro_vetor(t):
    '''
    primeiro_vetor: tabuleiro -> vetor
    Funcao que recebe um tabuleiro e devolve o seu terceiro vetor
    :param t: tabuleiros
    :return: vetor
    '''
    return t[2]


def portas_aux(t, l, c):
    t = tabuleiro_inverte_estado(t, cria_coordenada(l, c))
    return t


####################################
#  FUNCOES DE OPERACOES  BASICAS   #
####################################


##################################### CELULAS ###############################################

def cria_celula (valor):
    '''
    cria_celula: valor -> string
    Funcao que retorna "ativo", "inativo, "incerto" consoante o valor recebido
    :param valor: numero
    :return: string
    '''
    if valor not in (-1, 0, 1):
        raise ValueError("cria_celula: argumento invalido.")

    if valor == 1:
        return ["ativo"]
    elif valor == 0:
        return ["inativo"]
    else:
        return ["incerto"]


def obter_valor(celula):
    '''
    obter_valor: string -> valor
    Funcao que retorna um valor (-1, 1 ou 0) consoante a string recebida
    :param celula: string
    :return: numero
    '''
    return 0 if celula == ["inativo"] else 1 if celula == ["ativo"] else -1


def inverte_estado(celula):
    '''
    inverte_estado: celula -> celula
    Funcao que inverte o estado de uma celula: retorna "ativo" se a celula for "inativo",
    retorna "inativo" se a celula for "ativo" e mantem a celula "inativo" como "inativo"
    :param celula: celula
    :return: celula
    '''

    if obter_valor(celula) == 1:
        celula[0] = "inativo"
    elif obter_valor(celula) == 0:
        celula[0] = "ativo"
    return celula


def eh_celula(uni):
    '''
    eh_celula: universal -> Booleano
    Funcao que verifica se o universal recebido e do tipo celula
    :param universal: universal que representa uma possivel celula
    :return: Booleano
    '''
    return isinstance(uni, list) and len(uni) == 1 and obter_valor(uni) in (-1, 0, 1)


def celulas_iguais(c1, c2):
    '''
    celulas_iguais: celula x celula -> Booleano
    Funcao que verifica se os argumentos recebidos sao celulas e que verifica se sao iguais
    :param c1: celula
    :param c2: celula
    :return: Booleano
    '''
    return eh_celula(c1) and eh_celula(c2) and obter_valor(c1) == obter_valor(c2)



def celula_para_str(celula):
    '''
    celula_para_str: celula -> string
    Funcao que converte a celula recebida numa cadeia de caracteres e converte o -1 a "x"
    :param celula: celula
    :return: string(cadeia de caracteres)
    '''
    return "x" if obter_valor(celula) == -1 else str(obter_valor(celula))


##################################### COORDENADAS ##########################################


def cria_coordenada(l, c):
    '''
    cria_coordenada: linha x coluna -> tuplo
    Funcao que recebe a linha e a coluna e retorna a coordenada correspondente
    :param l: valor
    :param c: valor
    :return: tuplo
    '''
    if not isinstance(l, int) or not isinstance(c, int) or l not in (0, 1, 2) or c not in (0, 1, 2):
        raise ValueError("cria_coordenada: argumentos invalidos.")
    return l, c


def coordenada_linha(coordenadas):
    '''
    coordenada_linha: coordenada -> valor
    Funcao que recebe uma coordenada e retorna a linha da coordenada (primeiro valor)
    :param coordenadas: coordenada
    :return: valor
    '''
    return coordenadas[0]


def coordenada_coluna(coordenadas):
    '''
    coordenada_coluna: coordenada -> valor
    Funcao que recebe uma coordenada e retorna a coluna da coordenada (segundo valor)
    :param coordenadas: coordenada
    :return: valor
    '''
    return coordenadas[1]


def eh_coordenada(c):
    '''
    eh_coordenada: universal -> Booleano
    Funcao que verifica se o argumento recebido corresponde a uma coordenada
    :param c: universal que representa uma possivel coordenada
    :return: Booleano
    '''

    return isinstance(c, tuple) and len(c) == 2 \
        and coordenada_linha(c) in (0, 1, 2) and coordenada_coluna(c) in (0, 1, 2)


def coordenadas_iguais(c1, c2):
    '''
    coordenadas_iguais: coordenada X coordenada -> Booleano
    Funcao que verifica se o argumentos recebidos sao coordenadas e verifica se sao iguais
    :param c1: coordenada
    :param c2: coordenada
    :return: Booleano
    '''
    return eh_coordenada(c1) and eh_coordenada(c2) and coordenada_linha(c1) == coordenada_linha(c2)\
        and coordenada_coluna(c1) == coordenada_coluna(c2)


def coordenada_para_str(coor):
    '''
    coordenada_para_str: coordenada -> string
    Funcao que retorna a cadeia de caracteres correspondente a coordenada recebida
    :param coordenada: coordenada
    :return: string (cadeia de caracteres)
    '''
    return "({}, {})".format(coordenada_linha(coor), coordenada_coluna(coor))


########################################## TABULEIROS ################################################


def tabuleiro_inicial ():
    '''
    :return: tabuleiro inicial do jogo
    '''
    return [[cria_celula(-1), cria_celula(-1), cria_celula(-1)],
            [cria_celula(0), cria_celula(0), cria_celula(-1)],
            [cria_celula(0), cria_celula(-1)]]

def eh_tabuleiro_p1(tab):
    '''
        eh_tabuleiro: universal -> booleano
        Funcao que recebe um argumento qualquer e devolve um booleano
        Retorna True se o argumento for um tuplo com 3 tuplos de tamanho 3, 3 e 2, respetivamente e se os elementos
        dos tuplos for -1, 1 ou 0, caso contrario retorna False
        :param t: Universal que representa um possivel tabuleiro
        :return: Booleano
        '''
    if isinstance(tab, tuple) and len(tab) == 3:
        if isinstance(tab[0], tuple) and isinstance(tab[1], tuple) and isinstance(tab[2], tuple):
            if len(tab[0]) == 3 and len(tab[1]) == 3 and len(tab[2]) == 2:
                for e in range(len(tab)):
                    for i in range(len(tab[e])):
                        if tab[e][i] != 0 and tab[e][i] != 1 and tab[e][i] != -1:
                            return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def str_para_tabuleiro(cadeia):
    '''
    str_para_tabuleiro: cadeia de caracteres -> tabuleiro
    Funcao que retorna o tabuleiro corresponde a cadeia de caracteres recebida.
    :param cadeia: string (cadeia de caracteres)
    :return: tabuleiro
    '''
    if isinstance(cadeia, str):
        tup_tab = eval(cadeia)
        if eh_tabuleiro_p1(tup_tab):
            tab = tabuleiro_inicial()
            for l in range(3):
                for col in range(3):
                    c = cria_coordenada(l, col)
                    if coordenada_linha(c) != 2:
                        tab = tabuleiro_substitui_celula(tab, cria_celula(tup_tab[l][col]), c)
                    else:
                        if coordenada_coluna(c) in (0, 1):
                            tab = tabuleiro_substitui_celula(tab, cria_celula(tup_tab[l][col]),
                                                             cria_coordenada(l, col + 1))
            return tab
        raise ValueError("str_para_tabuleiro: argumento invalido.")
    raise ValueError("str_para_tabuleiro: argumento invalido.")


def tabuleiro_dimensao(t):
    '''
    :param t: tabuleiro
    :return: Valor (dimensao do tabuleiro recebido)
    '''
    return 3


def tabuleiro_celula(tab, coor):
    '''
    tabuleiro celula: Tabuleiro X Coordenada -> celula
    Funcao que retorna a celula correspondente a coordenada recebida como argumento.
    :param t: Tabuleiro
    :param coor: Coordenada
    :return: Celula
    '''
    if eh_tabuleiro(tab) and eh_coordenada(coor):
        if coordenada_linha(coor) != 2:
            return tab[coordenada_linha(coor)][coordenada_coluna(coor)]
        else:
            return tab[coordenada_linha(coor)][coordenada_coluna(coor) - 1]

def tabuleiro_substitui_celula(t, cel, coor):
    '''
    tabuleiro_substitui_celula: Tabuleiro X Celula X Coordenada
    Funcao que substitui a celula da coordenada recebida como argumento
    para a celula desejada.
    :param t: Tabuleiro
    :param cel: Celula
    :param coor: Coordenada
    :return: Celula
    '''
    if not (eh_tabuleiro(t) and eh_celula(cel) and eh_coordenada(coor)):
        raise ValueError("tabuleiro_substitui_celula: argumentos invalidos.")
    if coordenada_linha(coor) != 2:
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = cel
    else:
        t[coordenada_linha(coor)][coordenada_coluna(coor) - 1] = cel
    return t


def tabuleiro_inverte_estado (t, coor):
    '''
    tabuleiro_inverte_estado: Tabuleiro X Coordenada
    Funcao que inverte o estado da celula da coordenada recebida no argumento
    :param t: Tabuleiro
    :param coor: Coordenada
    :return: Celula
    '''
    if eh_tabuleiro(t) and eh_coordenada(coor):
        return tabuleiro_substitui_celula(t, inverte_estado(tabuleiro_celula(t, coor)), coor)
    raise ValueError("tabuleiro_inverte_estado: argumentos invalidos.")


def eh_tabuleiro(u):
    '''
    eh_tabuleiro: universal -> Booleano
    Funcao que verifica se o argumento recebido e um tabuleiro recorrendo
    a funcao verificar_tabuleiro
    :param u: universal que representa um possivel tabuleiro
    :return: Booleano
    '''
    if isinstance(u, list) and len(u) == 3:
        if len(u[0]) == 3 and len(u[1]) == 3 and len(u[2]) == 2:
            for el in u:
                if isinstance(el, list):
                    for cel in el:
                        if not eh_celula(cel):
                            return False
                else:
                    return False
            return True
        return False
    return False

def tabuleiros_iguais(tab1, tab2):
    '''
    tabuleiros_iguais: Tabuleiro X Tabuleiro -> Booleano
    Funcao que verifica se os argumentos recebidos sao tabuleiros e verifica se sao iguais
    :param t1: Tabuleiro
    :param t2: Tabuleiro
    :return: Booleano
    '''
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2):
        for e in range(3):
            for i in range(3):
                c = cria_coordenada(e, i)
                if not coordenadas_iguais(c, cria_coordenada(2, 0)):
                    if not celulas_iguais((tabuleiro_celula(tab1, c)),
                       tabuleiro_celula(tab2, c)):
                        return False
        return True
    return False


def tabuleiro_para_str(tab):
    '''
    tabuleiro_para_str: tabuleiro -> cadeia de caracteres
    Funcao que retorna a cadeia de caracteres correspondente ao tabuleiro recebido
    :param t: Tabuleiro
    :return: String (cadeia de caracteres)
    '''
    return "+-------+\n" \
           "|...{}...|\n" \
           "|..{}.{}..|\n" \
           "|.{}.{}.{}.|\n" \
           "|..{}.{}..|\n" \
           "+-------+".format(celula_para_str((tabuleiro_celula(tab, cria_coordenada(0, 2)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(0, 1)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(1, 2)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(0, 0)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(1, 1)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(2, 2)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(1, 0)))),
                              celula_para_str((tabuleiro_celula(tab, cria_coordenada(2, 1)))))

#OPERACOES DE ALTO NIVEL#


def porta_x(tab, lado):
    '''
    porta_x: Tabuleiro x {'E', 'D'} -> tabuleiro
    Funcao que altera o tabuleiro consoante o lado aplicado.
    Se o lado for 'E', inverte o estado das celulas do segundo vetor;
    Se o lado for 'D', inverte o estado das celulas da 1ª posicao de todos os vetores
    :param t: Tabuleiro
    :param lado: 'E', 'D'
    :return: Tabuleiro
    '''

    if eh_tabuleiro(tab) and lado in ("D", "E"):
        if lado == "E":
            for e in range(3):
                tab = portas_aux(tab, 1, e)
        else:
            for e in range(3):
                if e == 2:
                    tab = portas_aux(tab, e, 1)
                else:
                    tab = portas_aux(tab, e, 1)
        return tab
    raise ValueError("porta_x: argumentos invalidos.")


def porta_z(tab, lado):
    '''
    porta_z : Tabuleiro x {'E', 'D'} -> Tabuleiro
    Funcao que altera o tabuleiro consoante o lado aplicado.
    Se o lado for 'E', inverte o estado das celulas do primeiro vetor
    Se o lado for 'D', inverte o estado da ultima posicao de todas os vetores
    :param t: Tabuleiro
    :param lado: 'E', 'D'
    :return: Tabuleiro
    '''
    if eh_tabuleiro(tab) and lado in ("D", "E"):
        if lado == "E":
            for e in range(3):
                tab = portas_aux(tab, 0, e)
        else:
            for e in range(3):
                if e == 2:
                    tab = portas_aux(tab, e, 2)
                else:
                    tab = portas_aux(tab, e, 2)
        return tab
    raise ValueError("porta_z: argumentos invalidos.")


def porta_h(tab, lado):
    '''
    porta_h: Tabuleiro x {'E', 'D'} -> Tabuleiro
    Funcao que substitui as celulas das várias posicoes consoante o lado aplicado
    :param t: Tabuleiro
    :param lado: 'E', 'D'
    :return: Tabuleiro
    '''
    if eh_tabuleiro(tab) and lado in ("D", "E"):
        if lado == "E":

            cord_e = [cria_coordenada(0, 0), cria_coordenada(0, 1), cria_coordenada(0, 2)]
            cord_f = [cria_coordenada(1,0), cria_coordenada(1,1), cria_coordenada(1,2)]

            for i in range(len(cord_e)):
                c = cria_celula(obter_valor(tabuleiro_celula(tab, cord_f[i])))

                tab = tabuleiro_substitui_celula(tab, tabuleiro_celula(tab, cord_e[i]) ,cord_f[i])
                tab = tabuleiro_substitui_celula(tab, c, cord_e[i])

        else:

            cord_d = [cria_coordenada(2,2), cria_coordenada(1,2), cria_coordenada(0, 2)]
            cord_f = [cria_coordenada(2,1), cria_coordenada(1,1), cria_coordenada(0,1)]

            for i in range(len(cord_d)):
                c = cria_celula(obter_valor(tabuleiro_celula(tab, cord_f[i])))

                tab = tabuleiro_substitui_celula(tab, tabuleiro_celula(tab, cord_d[i]), cord_f[i])
                tab = tabuleiro_substitui_celula(tab, c, cord_d[i])

        return tab
    raise ValueError("porta_h: argumentos invalidos.")


def hello_quantum(cadeia):
    '''
    hello_quantum: cadeia -> Booleano
    Funcao que permite ao utilizador jogar o jogo em questao
    :param cadeia: string
    :return: Booleano
    '''
    tabuleiro_objetivo = str_para_tabuleiro(cadeia.split(":")[0])
    tabuleiro_inicial_jogo = tabuleiro_inicial()

    print("Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:\n" +
          tabuleiro_para_str(tabuleiro_objetivo) + "\nComecando com o tabuleiro que se segue:\n" +
          tabuleiro_para_str(tabuleiro_inicial_jogo))

    jogadas = 0
    JOGADAS_OBJETIVO = eval(cadeia.split(":")[1])

    while jogadas != JOGADAS_OBJETIVO:

        porta_escolha = str(input("Escolha uma porta para aplicar (X, Z ou H): "))
        qubit_escolha = str(input("Escolha um qubit para analisar (E ou D): "))
        if porta_escolha == "X":
            tabuleiro_inicial_jogo = porta_x(tabuleiro_inicial_jogo, qubit_escolha)
        elif porta_escolha == "Z":
            tabuleiro_inicial_jogo = porta_z(tabuleiro_inicial_jogo, qubit_escolha)
        elif porta_escolha == "H":
            tabuleiro_inicial_jogo = porta_h(tabuleiro_inicial_jogo, qubit_escolha)
        print(tabuleiro_para_str(tabuleiro_inicial_jogo))
        jogadas += 1
    if tabuleiros_iguais(tabuleiro_inicial_jogo, tabuleiro_objetivo):
        print("Parabens, conseguiu converter o tabuleiro em", jogadas, "jogadas!")
        return True
    else:
        return False




