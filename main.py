import texto as txt
import settings as st


################################### Objetos ###################################
# Vale lembrar que nem todos objetos são objetos colecionáveis, 
# alguns apenas servem para interagir com o jogador

################################### Cenario 0 ###################################

espada_cenario0 = st.Objeto(3, "espada", "Espada longa e afiada confiada a Lancelot pelo Rei Arthur", 0.1, coletavel= True)
armadura_cenario0 = st.Objeto(3, "armadura", "Armadura em aço branco e polido. O porquê de Lancelot: O Cavaleiro Branco ser chamado de Lancelot: Cavaleiro Branco.", 0.2, coletavel= True)
arvore_cenario0 = st.Objeto(3, "arvore", "Uma pequena árvore, mas sua madeira parece resistente", 0.1, coletavel= False )
galho_cenario0 = st.Objeto(3, "galho", "É um pedaço resistente de madeira.", 0.4, coletavel= True)
chave_cenario0 = st.Objeto(1, "grampo", "Pequeno grampo metal geralmente usado por ladrões.", 0.5 ,coletavel= True)
faca_cenario0 = st.Objeto(1, "faca", "É uma pequena adaga, mas em bom estado.", 0.6, coletavel= True)
porta_cenario0 = st.Objeto(3, "porta", "Porta de aço escovado", 0.4, coletavel = False )
sul_cenario0 = st.Objeto(3,"sul", "escuridao ao sul do cenario 1 para se interagir com a lamparina", 1.5, coletavel=False)


################################### Cenario 1 ###################################
corpo_goblin_cenario1 = st.Objeto(3, "corpo", "O corpo do goblin descansa no chão.", 1.2, coletavel= False)
lareira_cenario1 = st.Objeto(3, "lareira", "lareira feita com tijolos acesa", 0.8, coletavel= False)

lamparina_cenario12 = st.Objeto(3, "lamparina", "Lamparina acesa. Agora o escuro não é mais problema.", 1.5, coletavel= True )
lamparina_cenario1 = st.Objeto(3, "lamparina", "Lamparina apagada.", 0.8, coletavel= True )
bau_cenario1 = st.Objeto(2, "bau", "bau de ferro ", 0.5, coletavel= False)
arco_cenario1 = st.Objeto(2, "arco", "Arco ornamentado com rubis. Pra quê uma bruxa precisaria de um arco?", 1, coletavel= True)
goblin_cenario1 = st.Objeto(1, "goblin", "apenas um goblin dormindo", 0.6, coletavel= False)
rachadura_cenario1 = st.Objeto(3, "fenda", "fenda na parede do cenario 1", 1.1 , coletavel= False)



################################### Cenario 2 ###################################
parede_cenario2 = st.Objeto(3,"parede", "parede contendo a palavra do feitiço", 0.8, coletavel= False)
livro_cenario2 = st.Objeto(3,"livro", "é um livro de feitiços, provavelmente pertence à Morgana. Com o livro em mãos você pode conjurar feitiços escrevendo-os no terminal.", 1.3, coletavel= True)
pedra_cenario2 = st.Objeto(3, "pedra", "É uma grande pedra que antes pertencia ao corpo do Golem. Ela não parece ter propriedades mágicas mas de qualquer forma pode ser útil.", 1.4, coletavel= True)
tapete_cenario2 = st.Objeto(3,"tapete", "É um tapete vermelho feito de um tecido aparentemente nobre e caro. Não parece ter muita utilidade no momento.", 1.5, coletavel=True)

norte_cenario2 = st.Objeto(3, "norte", "norte do cenario 2 para interagir com a lamparina acesa", 1.5, coletavel= True)
lamparina_cenario2 = st.Objeto(3,"lamparina", "A lamparina está agora acesa com um chama azulada.", 1.5, coletavel= True )
sal_azul_cenario2 = st.Objeto(3, "sal", "Sal de uma cor azulada e fluorescente.",1.5, coletavel=True)
golem_cenario2 = st.Objeto(3, "golem", "golem do cenario 2", 1.3, coletavel= False)

################################### Cenario 3 #########################
chave_cenario3 = st.Objeto(3,"chave", "é uma chave de prata muito bem forjada", 1.1 , coletavel= True)
flechas_cenario3 = st.Objeto(3, "flechas", "São bonitas flechas de madeira com ponta feita de bronze. Porém sem um arco elas não tem muita utilidade", 1, coletavel= True)
alvo_cenario3 = st.Objeto(3,"alvo", "alvo no cenário 3", 1.6, coletavel= False)
rachadura_cenario3 = st.Objeto(3,"rachadura", "rachadura no cenario 3", 1.4, coletavel= False)


################################### Funções ###################################
def inicializa_cenario(lista_cenario, cenario): #adiciona todos os itens e atributos ao cenario passado
    if cenario == 0:
        lista_cenario.msg_inicial = txt.msg_inicial0
        lista_cenario.norte = txt.cenario0_norte
        lista_cenario.sul = txt.cenario0_sul
        lista_cenario.leste = txt.cenario0_leste
        lista_cenario.oeste = txt.cenario0_oeste
        lista_cenario.append(porta_cenario0)
        lista_cenario.append(arvore_cenario0)
        lista_cenario.append(galho_cenario0)
        lista_cenario.append(chave_cenario0)
        lista_cenario.append(faca_cenario0)
        lista_cenario.append(sul_cenario0)
        lista_cenario.ir_sul = txt.ir_sul_cenario0
        lista_cenario.ir_norte = txt.ir_norte_cenario0
        lista_cenario.ir_leste = txt.ir_leste_cenario0
        lista_cenario.ir_oeste = txt.ir_oeste_cenario0

    elif cenario == 1:
        lista_cenario.msg_inicial = txt.msg_inicial1
        lista_cenario.norte = txt.cenario1_norte
        lista_cenario.sul = txt.cenario1_sul
        lista_cenario.leste = txt.cenario1_leste
        lista_cenario.oeste = txt.cenario1_oeste
        lista_cenario.append(lareira_cenario1)
        lista_cenario.append(lamparina_cenario1)
        lista_cenario.append(lamparina_cenario12)
        lista_cenario.append(bau_cenario1)
        lista_cenario.append(arco_cenario1)
        lista_cenario.append(goblin_cenario1)
        lista_cenario.append(rachadura_cenario1)
        lista_cenario.ir_sul = txt.ir_sul_cenario1
        lista_cenario.ir_norte = txt.ir_norte_cenario1
        lista_cenario.ir_leste = txt.ir_leste_cenario1
        lista_cenario.ir_oeste = txt.ir_oeste_cenario1

    elif cenario == 2:
        lista_cenario.msg_inicial = txt.msg_inicial2
        lista_cenario.norte = txt.cenario2_norte
        lista_cenario.sul = txt.cenario2_sul
        lista_cenario.leste = txt.cenario2_leste
        lista_cenario.oeste = txt.cenario2_oeste
        lista_cenario.append(pedra_cenario2)
        lista_cenario.append(tapete_cenario2)
        lista_cenario.append(livro_cenario2)
        lista_cenario.append(golem_cenario2)
        lista_cenario.append(sal_azul_cenario2)
        lista_cenario.append(parede_cenario2)
        lista_cenario.append(norte_cenario2)
        lista_cenario.ir_sul = txt.ir_sul_cenario2
        lista_cenario.ir_norte = txt.ir_norte_cenario2
        lista_cenario.ir_leste = txt.ir_leste_cenario2
        lista_cenario.ir_oeste = txt.ir_oeste_cenario2

    elif cenario == 3:

        lista_cenario.msg_inicial = txt.msg_inicial3
        lista_cenario.norte = txt.cenario3_norte
        lista_cenario.sul = txt.cenario3_sul
        lista_cenario.leste = txt.cenario3_leste
        lista_cenario.oeste = txt.cenario3_oeste
        lista_cenario.append(chave_cenario3)
        lista_cenario.append(flechas_cenario3)
        lista_cenario.append(alvo_cenario3)
        lista_cenario.append(rachadura_cenario3)
        lista_cenario.ir_sul = txt.ir_sul_cenario3
        lista_cenario.ir_norte = txt.ir_norte_cenario3
        lista_cenario.ir_leste = txt.ir_leste_cenario3
        lista_cenario.ir_oeste = txt.ir_oeste_cenario3

    return

def main(): #inicializa o jogo

    running = True

    index_cenario = 0  #isso aqui vai representar qual cenarios estamos
    # Cenario 0
    a = 0
    inventario_personagem = st.Inventario() # inicializa inventario do personagem
    inventario_personagem.append(espada_cenario0) #adiciona espada
    inventario_personagem.append(armadura_cenario0) #adiciona armadura

    lista_cenario0 = st.Cenario() #inicializa cenario
    inicializa_cenario(lista_cenario0, 0) #adiciona todos os itens ao cenario


    # Cenario 1
    b = -1
    lista_cenario1 = st.Cenario()
    inicializa_cenario(lista_cenario1, 1)  # adiciona todos os itens ao cenario
    cenarios = st.LinkedList() # Uma lista encadeada simples eh suficiente para armazenar os os cenarios

    #Cenario 2
    c = -1
    lista_cenario2 = st.Cenario()
    inicializa_cenario(lista_cenario2, 2)  # adiciona todos os itens ao cenario

    #Cenario 3
    d = -1
    lista_cenario3 = st.Cenario()
    inicializa_cenario(lista_cenario3, 3)

    cenarios.append(lista_cenario0)
    cenarios.append(lista_cenario1)
    cenarios.append(lista_cenario2)
    cenarios.append(lista_cenario3)

    armadura = 0

    #Variaveis para definir se o jogador esta entrando pela primeira vez no cenario
    primeira_vez0 = True
    primeira_vez1 = True
    primeira_vez2 = True
    primeira_vez3 = True

    while running == True:

        # Cenario 0 - Contendo todas as interações no cenário.
        # Eventos chave-fechadura ocorrem quando dois objetos interagem (possuem codigo_interacao igual) de modo a prosseguir na história
        # Outras prováveis interações que o usuário possa tentar fazer são definidas na seção Árvores Interações em settings.py
        while a != -1:

            if primeira_vez0 == True:
                print(cenarios[0].msg_inicial)
                cenarios[0].msg_inicial = "A escuridão ainda é forte, você só consegue ouvir o vento. Correr agora seria covardia, você precisa das suas armas de volta."
                primeira_vez0 = False

            n = input(">>>").split()

            if n[0] in txt.voltar: #caso jogador tentar voltar da floresta
                print("Depois de tanto tempo procurando você já vai desistir da sua missão?")

            d = st.Arvore.decisao(n, cenarios, index_cenario, inventario_personagem, st.Arvore_cenario0)

            if d == "Evento chave-fechadura":

                if n[1] in txt.espada_nomes and n[2] in txt.arvore_nomes:
                    print("Você conseguiu cortar um grosso galho da árvore. Talvez ele tenha alguma utilidade.")
                    cenarios[0].pegar_objeto(inventario_personagem, "galho")

                if n[1] in txt.lamparina_nomes and n[2] in txt.sul:
                    print("É possivel ver agora uma faca largada no chão, talvez de algum combate anterior. Será util para você agora que está desarmado.")
                    cenarios[0].pegar_objeto(inventario_personagem, "faca")

                if n[1] in txt.galho_nomes and n[2] in txt.porta_nomes: #so aparece a primeira vez que o jogador passa pro cenario 1
                    print("Você usa a galho como alavanca e consegue abrir um pouco mais a porta, o suficiente para você conseguir passar")
                    inventario_personagem.remove(inventario_personagem.retorna_objeto("galho")[0])

                    cenarios[0].can_next = True
                    cenarios[0].ir_oeste = "A porta está aberta, mas você não consegue enxergar nada dentro."
                    entrar = input("Entrar? (y/n)")
                    print("")
                    if entrar == "y":

                        a = -1  # sai do while
                        b = 0
                        c = -1
                        d = -1
                        index_cenario = 1  # passa pro cenario 1
                        break
                    else:
                        continue

            #Entrar depois de ter solucionado o puzzle da sala
            if n[0] in txt.entrar and cenarios[0].can_next == True: #no caso em que o jogador volta para a floresta e queira voltar para o Cenario 1
                a = -1  # sai do while
                b = 0
                c = -1
                d = -1
                index_cenario = 1  # passa pro cenario 1
                if primeira_vez1 == True: # no while do cenario 1 a msg inicial já é printada
                    pass
                else:
                    print(cenarios[1].msg_inicial) #caso, contrario, printa-se a mensagem aqui
                break

            #Se o jogador tentar entrar antes de abrir a porta
            elif n[0] in txt.entrar and cenarios[0].can_next == False:
                print("A porta não está aberta o suficiente para entrar.")

        #Cenario 1 - Sala do esconderijo da bruxa
        while b != -1:

            if primeira_vez1 == True: #ao entrar na sala pela primeira vez o jogador perde seus itens e a msg inicial da sala muda após ser printada
                inventario_personagem.remove(inventario_personagem.retorna_objeto("espada")[0])
                inventario_personagem.remove(inventario_personagem.retorna_objeto("armadura")[0])
                print(cenarios[1].msg_inicial)
                cenarios[1].msg_inicial = "Você chega em uma espécie de sala iluminada por uma lareira em sua entrada. No final dela há um corredor que leva à sala seguinte. Porém guardando ele há um Goblin dormindo." # muda a mensagem inicial
                primeira_vez1 = False

            n = input(">>>").split()
            d = st.Arvore.decisao(n, cenarios, index_cenario, inventario_personagem, st.Arvore_cenario1)

            #Voltar para a floresta
            if n[0] in txt.voltar:
                b = -1 #sai do while
                a = 0 # torna possivel o while do cenario 0
                c = -1
                d = -1
                index_cenario = 0 #cenario 0 é passado para o jogador
                print(cenarios[0].msg_inicial)
                break

            if d == "Evento chave-fechadura":

                #usar chave - que encontra na sala 3 - rachadura, obtem arco
                if n[1] in ["chave", "key"] and n[2] in ["fenda", "hole"]:
                    print("Você coloca a chave na fenda do telhado e consegue girá-la até ouvir um 'tec'. Nisso um alçapão magicamente se abre no telhado, e dentro dele você encontra um arco.")
                    cenarios[1].pegar_objeto(inventario_personagem, "arco")

                #usar lamparina lareira, acende lamparina
                if n[1] in txt.lamparina_nomes and n[2] in txt.lareira_nomes:
                    print("Você acende a lamparina na lareira")
                    inventario_personagem.retorna_objeto("lamparina")[0].codigo_interacao = 1.5
                    inventario_personagem.retorna_objeto("lamparina")[0].descricao = "Lamparina acesa. Agora o escuro não é mais problema."

                #usar chave bau, pega a lamparina
                if n[1] in ["grampo", "lockpick"] and n[2] in txt.bau_nomes:
                    print("O baú se abre e dentro dele você encontra uma lamparina apagada.")
                    inventario_personagem.remove(inventario_personagem.retorna_objeto("grampo")[0])
                    cenarios[1].pegar_objeto(inventario_personagem, "lamparina")

                #usar faca goblin, mata o goblin e passa para a proxima sala
                if n[1] in ["faca", "knife", "adaga"] and n[2] in ["goblin"]:
                    print("Você se aproxima do Goblin sorrateiramente e o mata com uma facada no pescoço antes que ele possa revidar. Agora você pode prosseguir.")
                    cenarios[1].msg_inicial = "Você chega em uma espécie de sala iluminada por uma lareira em sua entrada. No final dela há um corredor que leva à sala seguinte o corpo do goblin já está começando a feder."
                    cenarios[1].can_next = True
                    cenarios[1].leste = "O corpo do goblin repousa silenciosamente no chão ao lado de seu porrete." # muda a mensagem inicial apos a morte do goblin
                    st.lamparina_goblin.valor = "O goblin já está morto." #depois de tentar usar a lamparina no goblin
                    cenarios[1].remove(cenarios[1].retorna_objeto("goblin")[0]) #retira o goblin do cenario
                    cenarios[1].append(corpo_goblin_cenario1) #adiciona o corpo do goblin
                    entrar = input("Continuar pro próximo cenário? (y/n)")
                    print("")
                    if entrar == "y":
                        b = -1  # sai do while
                        c = 0
                        d = -1
                        a = -1
                        index_cenario = 2  # passa pro cenario 2
                        break

                    else:
                        continue

            if n[0] in txt.entrar and cenarios[1].can_next == True: #no caso em que o jogador volta para o esconderijo e queira voltar para o Cenario 2
                b = -1  # sai do while
                c = 0
                d = -1
                a = -1
                index_cenario = 2  # passa pro cenario 1
                if primeira_vez2 == True: # no while do cenario 1 a msg inicial já é printada
                    pass
                else:
                    print(cenarios[2].msg_inicial) #caso, contrario, printa-se a mensagem aqui
                break

            elif n[0] in txt.entrar and cenarios[1].can_next == False: #no caso em que o jogador tentar entrar sem matar o goblin
                print("O goblin ainda está dormindo, é melhor não acorda-lo.")

        #Cenario 2 - Sala do Golem
        while c != -1:

            if primeira_vez2 == True:  # ao entrar na sala pela primeira vez a msg inicial da sala muda após ser printad
                print(cenarios[2].msg_inicial)
                cenarios[2].msg_inicial = "Você está numa sala escura com cristais coloridos brilhando no telhado."  # muda a mensagem inicial
                primeira_vez2 = False

            n = input(">>>").split()
            d = st.Arvore.decisao(n, cenarios, index_cenario, inventario_personagem, st.Arvore_cenario1)

            #Armadura ao norte do cenario, após esbarrar na armadura o jogador pode tentar pegar suas partes, mas sem sucesso
            if n[0] in txt.ir and n[1] in txt.norte:
                if armadura == 0:
                    cenarios[2].ir_norte = "Os restos da armadura estão no chão."

            if n[0] in txt.pegar and n[1] in ["capacete", "helmet"]:
                print("O capacete se desfaz na sua mão.")
                armadura +=1

            if n[0] in txt.pegar and n[1] in ["chest", "peitoral"]:
                print("O peitoral se desfaz na sua mão.")
                armadura += 1

            if n[0] in txt.pegar and n[1] in ["luvas", "gautlet"]:
                print("As luvas se desfazem na sua mão.")
                armadura += 1

            if armadura == 3:
                cenarios[2].ir_norte = "Só restou poeira onde antes existia uma armadura."

            if d == "Evento chave-fechadura":

                # Caso especial de combinação de dois elementos no inventario do personagem
                #combinar sal lamparina ou combinar lamparina sal
                # Ao combinar o sal com a lamparina sua chama muda.
                if n[1] in ["sal", "salt"] and n[2] in txt.lamparina_nomes or n[2] in ["sal", "salt"] and n[1] in txt.lamparina_nomes :
                    print("Agora a lamparina está com uma cor azulada.")
                    inventario_personagem.remove(inventario_personagem.retorna_objeto("lamparina")[0])
                    inventario_personagem.append(lamparina_cenario2)  # adiciona a lamparina com chama azul

                #usar lamparina norte, o jogador descobre duas palavras do feitiço
                if n[1] in txt.lamparina_nomes and n[2] in txt.norte:

                    #Como ambas as lamparinas tem o mesmo código de interação, para interagir com o norte da sala, diferenciamos as interações pelas descrições.
                    #se o jogador usar a lamparina acesa com chama normal
                    if inventario_personagem.retorna_objeto("lamparina")[0].descricao == "Lamparina acesa. Agora o escuro não é mais problema.":
                        print("Você consegue agora ver uma palavra escrita nessa parede. Mas você não tem certeza oque ela significa.")
                        print("AMORFUS")

                    #se o jogador usar a lamparina com a chama azul
                    elif inventario_personagem.retorna_objeto("lamparina")[0].descricao == "A lamparina está agora acesa com um chama azulada.":

                        print("Você consegue agora ver uma palavra escrita nessa parede. Mas você não tem certeza oque ela significa.")
                        print("EXPONENTIA")

                #usar livro golem, pede as palavras e libera a passagem
                if n[1] in ["livro","book"] and n[2] in ["golem"]:
                    palavra_magica1 = input("Proclame o feitiço >>>")
                    palavra_magica2 = input("Proclame o feitiço >>>")
                    if palavra_magica1 == "EXPONENTIA" and palavra_magica2 == "AMORFUS" or palavra_magica2 == "EXPONENTIA" and palavra_magica1 == "AMORFUS":
                        print("Quando você proclama esse feitiço o Golem simplesmente desintegra como se nunca estivesse lá, deixando apenas uma das pedras que compunham seu corpo. No chão debaixo de onde o Golem estava há um tapete vermelho.")

                    else:
                        print("Nada acontece, talvez você tenha pronunciado a palavra errado?")

            #depois de pegar o tapete e a pedra, o jogador pode prosseguir para o próximo cenário
            if cenarios[2].busca("tapete")[1] == False and cenarios[2].busca("pedra")[1] == False and cenarios[2].can_next == False: #dps do jogador pegar a pedra e o tapete
                print("Há um alçapão no chão, que antes estava escondido pelo tapete. Você o abre e observa uma longa escada de metal descendo até a escuridão.")

                cenarios[1].leste = "O corpo do goblin repousa silenciosamente no chão."
                cenarios[2].can_next = True
                entrar = input("Continuar pro próximo cenário? (y/n)")
                print("")
                if entrar == "y":
                    a = -1
                    b = -1
                    c = -1
                    d = 0
                    index_cenario = 3  # passa pro cenario 2
                    # sai do while
                    if primeira_vez3 == True:
                        pass
                    else:
                        print(cenarios[3].msg_inicial)

                    break
                else:
                    continue

            if n[0] in txt.voltar:
                b = 0  # sai do while
                c = -1
                d = -1
                a = -1
                index_cenario = 1
                print(cenarios[1].msg_inicial)
                break

            if n[0] in txt.entrar and cenarios[2].can_next == True:  # no caso em que o jogador volta para o esconderijo e queira voltar para o Cenario 2
                c = -1  # sai do while
                d = 0
                a = -1
                b = -1
                index_cenario = 3  # passa pro cenario 3
                if primeira_vez3 == True: # no while do cenario 2 a msg inicial já é printada
                    pass
                else:
                    print(cenarios[3].msg_inicial) #caso, contrario, printa-se a mensagem aqui
                break


            elif n[0] in txt.entrar and cenarios[2].can_next == False :
                print("Entrar aonde? Essa sala parece não ter saída.")

        # Cenario 3 - Sala de controle Morgana
        while d != -1:

            if primeira_vez3 == True:
                print(cenarios[3].msg_inicial)
                primeira_vez3 = False

            n = input(">>>").split()

            f = st.Arvore.decisao(n, cenarios, index_cenario, inventario_personagem, st.Arvore_cenario1)

            if n[0] in txt.pegar and n[1] in ["chave", "key"]:
                cenarios[3].ir_norte = "Ao se aproximar da pessoa você nota que ela na verdade está morta, aparentemente não a muito tempo."

            if f == "Evento chave-fechadura":

                #usar pedra rachadura, encontra flechas
                if n[1] in ["pedra", "stone"] and n[2] in ["rachadura", "hole"]:
                    p = 0
                    while p != 3:
                        if p == 0:
                            print("Você golpeia a rachadura, mas nada acontece.")
                        s = input("Pressione S para continuar batendo.")

                        if s == "S" or s == "s":
                            p += 1

                        if p == 1:
                            print("A rachadura se torna maior")
                        elif p == 2:
                            print("Um pequeno buraco se abre.")
                        else:
                            print("O buraco cede e você avista um conjunto de flechas.")

                    if p == 3:
                        cenarios[3].ir_sul = "Só um pequeno buraco no chão."

                #combinar arco flecha, voce pode agora atirar
                if n[1] in ["arco"] and n[2] in ["flecha", "flechas", "arrow", "arrows"]:
                    print("Você pode agora atirar.")
                    inventario_personagem.retorna_objeto("arco")[0].codigo_interacao = 1.6
                    inventario_personagem.retorna_objeto("arco")[0].descricao = "Arco carregado, em quem você vai atirar?"
                    inventario_personagem.remove(inventario_personagem.retorna_objeto("flechas")[0])

                #usar arco alvo, voce libera a passagem e termina o jogo
                if n[1] in ["arco"] and n[2] in ["target", "alvo"]:
                    #Se o arco já estiver carregado
                    if inventario_personagem.retorna_objeto("arco")[0].codigo_interacao == 1.6:
                        print("Você acerta o alvo com uma flecha e ouve um ruído de algo se quebrando do outro lado da sala. O cristal se quebrou, agora você pode prosseguir")
                        entrar = input("Deseja entrar?(y/n)")
                        if entrar == "y":
                            cenarios[3].can_next = True
                            print(txt.msg_final)
                            exit()
                    else:
                        print("Não tem como atirar sem flechas.")

            if n[0] in txt.voltar:
                a = -1
                b = -1
                c = 0  # sai do while
                d = -1  # torna possivel o while do cenario 2
                index_cenario = 2  # cenario 2 é passado para o jogador
                print(cenarios[2].msg_inicial)
                break

            if n[0] in txt.entrar and cenarios[3].can_next == True:  # no caso em que o jogador volta para o esconderijo e queira voltar para o Cenario 2
                cenarios[3].can_next = True
                print(txt.msg_final)
                exit()
                break

            elif n[0] in txt.entrar and cenarios[3].can_next == False:
                print("O cristal ainda está em seu caminho.")

main()
