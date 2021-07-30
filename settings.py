import texto as txt

#############################  Estruturas do jogo  ###############################

################################### Inventario ###################################
class Node: #no da lista
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: #estrutura de lista encadeada
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range") #return None
        return pointer

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Retorna o índice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data.nome == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(elem))

    # Retorna o objeto e valor logico True se encontrar o item pedido na lista
    def busca(self, elem):
        pointer = self.head
        for i in range(len(self)):
            if pointer.data.nome == elem:
                return pointer.data, True
            pointer = pointer.next
        return pointer, False

    # Retorna objeto e valor logico com base no nome e na presenca do item
    def retorna_objeto(self, name):
        name = name.lower()

        if self.busca(name)[1] == True:  # confere se o elemento existe na lista do cenario
            index = self.index(name)  # retorna o indice do elemento desejado
            objeto = self[index]  # retorna o objeto da lista
            return objeto, True
        else:
            return name, False

    # Vale ressalta que esse "elem" que esta n parametro da funcao ainda nao eh um objeto, mas apenas o nome de um objeto
    def pegar_objeto(self, inventario_personagem, name):
        objeto, verificacao = self.retorna_objeto(name)
        if verificacao == True and objeto.coletavel == True:
            print(f"Você pegou {name.capitalize()}")
            self.remove(objeto)
            inventario_personagem.append(objeto)
        else:
            print("Você não pode pegar esse objeto.")
        return

class Inventario(LinkedList):
    def __repr__(self):
        r = ""
        pointer = self.head
        counter = 1
        while(pointer):
            r = r + str(counter) + " " + str((pointer.data.nome).capitalize()) + "\n"
            pointer = pointer.next
            counter += 1
        if r == "":
            return("Inventario de Lancelot: vazio\n")
        else:
            return (f"Inventario de Lancelot: \n{r[0:len(r)-1]}\n") # remove o "-" do final da string

    def __str__(self):
        return self.__repr__()

################################### Cenario ###################################
#Cenarios do jogo
class Cenario(LinkedList):
    def __init__(self, msg_inicial = None, norte=None, sul=None, leste=None, oeste=None, ir_norte = None, ir_sul = None, ir_oeste = None, ir_leste = None, can_previous=False, can_next=False):
        super().__init__()
        self.msg_inicial = msg_inicial
        self.norte = norte
        self.sul = sul
        self.leste = leste
        self.oeste = oeste
        self.ir_norte = ir_norte
        self.ir_sul = ir_sul
        self.ir_leste = ir_leste
        self.ir_oeste = ir_oeste
        self.can_previous = can_previous
        self.can_next = can_next

    def look(self, direcao):

        if direcao == "norte":
            print(self.norte)

        elif direcao == "sul":
            print(self.sul)

        elif direcao == "leste":
            print(self.leste)

        elif direcao == "oeste":
            print(self.oeste)

    def __repr__(self):
        r = ""
        pointer = self.head
        counter = 1
        while(pointer):
            r = r + str(counter) + " " + str((pointer.data.nome).capitalize()) + "\n"
            pointer = pointer.next
            counter += 1
        if r == "":
            return("Objetos no cenario : vazio\n")
        else:
            return (f"Objetos no cenario : \n{r[0:len(r)-1]}\n") # remove o "-" do final da string

    def __str__(self):
        return self.__repr__()

################################### Objeto ###################################
#Objetos do jogo
class Objeto:

    def __init__(self, hp, nome, descricao, codigo_interacao, coletavel):
        self.hp = hp
        self.nome = nome
        self.descricao = descricao
        self.codigo_interacao = codigo_interacao
        self.coletavel = coletavel

    def descricao(self):
        print(self.descricao)

################################### Arvore de decisao ###################################

#Arvore que armazena e lida com as interações do jogador com o cenário.

class Arvore_decisao:
    '''
    Construtor. Armazena um valor em "valor", cria uma
    lista vazia de filhos e armazena a condição
   '''
    def __init__(self, condicao, valor):
        self.valor = valor
        self.filhos = []
        self.condicao = condicao

    # Monta string para impressao da arvore, printando noh e sua condicao
    def __str__(self, nivel=0):
        if (self == None):
            return
        else:
            if self.condicao == None: #nao printa condicao para a raiz
                saida = "  " * nivel + str(self.valor) + "\n"
                for filho in self.filhos:
                    saida += filho.__str__(nivel + 1)
                return saida
            else:
                saida = "  " * nivel + str(self.valor) + " | cond: " + str(self.condicao) + "\n"
                for filho in self.filhos:
                    saida += filho.__str__(nivel + 1)
                return saida

    # Insere uma arvore "filho" como filha de uma outra arvore.
    def insere(self, filho):
        self.filhos.append(filho)

    # Busca "valor" na arvore.
    def busca(self, valor):
        if (self.valor == valor):
            return True

        for filho in self.filhos:
            if (filho.busca(valor) == True):
                return True
        return False

    #busca nos filhos a condicao passada e retorna o objeto filho
    def busca_cond(self,obj1, obj2): 
        for filho in self.filhos: #busca o filho que satisfaz a condicao
            if obj1 in filho.condicao:
                for j in filho.filhos:
                    if obj2 in j.condicao:
                        return j.valor


    #Função principal do jogo, recebe:
    # - input do jogador
    # - lista contendo todos os cenario
    # - index do cenario no qual o jogador está
    # - inventario do personagem
    # - arvore cenario - arvore contendo interações não obrigatórias, interações apenas de texto entre jogador e cenario
    def decisao(self, input1, cenarios, index_cenario, inventario_personagem, arvore_cenario):
        filhos = self.filhos
        comando = 0
        for i in filhos:
            if input1[0] in i.condicao:  # se a primeira palavra do jogador estiver no nós de altura 1:
                if len(i.filhos) == 0:
                    comando = i.valor

                else: #caso contrário, procura-se condição que satisfaça no filhos dos nós de altura 1
                    for j in i.filhos:
                        if len(input1) <= 1:
                            print(f"Digite uma direcao após {input1[0]}. Digite 'help' para obter ajuda")  # caso o usuario digite 'ir' sem uma direcao, retorna esse erro
                            return
                        elif input1[1] in j.condicao:
                            comando = j.valor


        #Olhar + direção retorna o atributo dessa direção do cenário no qual o jogador está
        if comando == "Olhar norte":
            print(cenarios[index_cenario].norte)


        elif comando == "Olhar sul":
            print(cenarios[index_cenario].sul)

        elif comando == "Olhar leste":
            print(cenarios[index_cenario].leste)

        elif comando == "Olhar oeste":
            print(cenarios[index_cenario].oeste)

        #Ir + direção trabalha de maneira análoga ao olhar, oferecendo informações mais específicas ao jogador.
        elif comando == "Ir norte":
            print(cenarios[index_cenario].ir_norte)

        elif comando == "Ir sul":
            print(cenarios[index_cenario].ir_sul)

        elif comando == "Ir leste":
            print(cenarios[index_cenario].ir_leste)

        elif comando == "Ir oeste":
            print(cenarios[index_cenario].ir_oeste)

        #Pegar retira um objeto do cenario e o coloca no inventario do jogador
        elif comando == "Pegar":
            cenarios[index_cenario].pegar_objeto(inventario_personagem, input1[1])

        #Volta para o cenario anterior, está definido no while de cada cenário
        elif comando == "Voltar":
            pass

        elif comando == "Help":
            print("Comandos disponiveis:\n\n"
                  "Olhar <direcao> - Descreve brevemente essa direcao\n"
                  "Inventario - Lista os itens no inventario de Lancelot\n"
                  "Ir <direcao>\n"
                  "Pegar <item do cenario>\n"
                  "Usar <item do inventario> <item do cenario>\n"
                  "Combinar <item do inventario> <item do inventario>\n"
                  "Voltar - Retorna ao cenário anterior\n"
                  "Entrar - Entra no próximo cenário\n")

        #Análogo ao "Voltar"
        elif comando == "Entrar":
            pass

        #Interação entre itens do inventario do jogador com os itens no cenário
        elif comando == "Usar":

            try: #quando o jogador tentar usar um objeto do inventário em um objeto do cenário

                if len(input1) == 2: # se o jogador escrever usar + objeto sem especificar aonde ele vai usar
                    print(f"Usar {input1[1]} aonde?")

                elif len(input1) == 1: # se o jogador digitar apenas usar
                    print("Usar o que?")
                else:


                    objeto_chave, verificacao1 = inventario_personagem.retorna_objeto(input1[1])
                    objeto_fechadura, verificacao2 = cenarios[index_cenario].retorna_objeto(input1[2])

                    #CODIGOS DE INTERACAO DOS ITENS
                    item_a = objeto_chave.codigo_interacao
                    item_b = objeto_fechadura.codigo_interacao

                    if verificacao1 == False: #se o primeiro item nao estiver no inventario do jogador
                        print("Você não possui esse item.")

                    if item_a == item_b: #se ambos tiverem mesmo codigo
                        return "Evento chave-fechadura" #um evento que permite o jogador progredir nos cenários
                    else: #objetos com codigo de interacao diferente, procura-se a interação entre eles na arvore de interações de texto
                        interacao_texto = arvore_cenario.busca_cond(input1[1], input1[2])
                        if interacao_texto != None: #se a interacao entre os objetos estiver definida na arvore do cenario
                            print(interacao_texto)
                        else:
                            print("Não há nada o que fazer.")

            except AttributeError:
                objeto_chave, verificacao1 = inventario_personagem.retorna_objeto(input1[1]) #testa a presenca do item no inventario
                objeto_fechadura, verificacao2 = cenarios[index_cenario].retorna_objeto(input1[2])

                if verificacao1 == False:
                    print("Você não possui esse item.")

                elif verificacao1 == True and verificacao2 == False: # se o objeto não estiver no cenario
                    interacao_texto = arvore_cenario.busca_cond(input1[1], input1[2])
                    if interacao_texto != None:  # se a interacao entre os objetos estiver definida na arvore do cenario
                        print(interacao_texto)

                    else:
                        print("Não há nada o que fazer.")

                else:
                    print("Não há nada a se fazer.")

        #Interações entre dois objetos presentes no inventario do jogador
        elif comando == "Combinar":


            verificacao1 = inventario_personagem.retorna_objeto(input1[1])[0].codigo_interacao
            verificacao2 = inventario_personagem.retorna_objeto(input1[2])[0].codigo_interacao

            if verificacao1 == verificacao2:
                return "Evento chave-fechadura"


            else:
                print("Esses itens não combinam")

        #Apresenta o inventario do jogador e permite a ele acessar as descrições dos itens.
        elif comando == "Olhar inventario":
            print(inventario_personagem)
            ver = -1
            while ver != "0":
                ver = input("Digite o nome do item para ver sua descrição ou 0 para sair: ")
                print("")
                try:
                    if ver == "0":
                        break

                    print(inventario_personagem.busca(ver)[0].descricao) #busca e printa a descricao do item pelo nome
                    print("")

                except AttributeError: #caso o nome passado nao exista nao esteja no inventario do jogador
                    print("Esse item não está no seu inventário")

        else:
            print("Comando desconhecido. Digite 'help' para exibir os comandos disponiveis")
            print("")

###################################Árvore de decisao - criação ###################################
#Cria a arvore com os comandos principais do jogo

Arvore = Arvore_decisao(None,"Arvore") #raiz da arvore

Olhar = Arvore_decisao(["olhar", "look"], "Olhar") #filho 2
Arvore.insere(Olhar) #insere filho 2 na raiz

norte = Arvore_decisao(txt.norte, "Olhar norte") #filho 2.1
sul = Arvore_decisao(txt.sul, "Olhar sul") #filho 2.2
leste = Arvore_decisao(txt.leste, "Olhar leste") #filho 2.3
oeste = Arvore_decisao(txt.oeste, "Olhar oeste") #filho 2.4

Olhar.insere(norte) #insere filho 2.1
Olhar.insere(sul) #insere filho 2.2
Olhar.insere(leste) #insere filho 2.3
Olhar.insere(oeste) #insere filho 2.4

Usar = Arvore_decisao(txt.interagir_obj, "Usar") #filho 3
Arvore.insere(Usar)

Pegar = Arvore_decisao(txt.pegar, "Pegar") #filho 4
Arvore.insere(Pegar)

Olhar_Inventario = Arvore_decisao(txt.inventario, "Olhar inventario")
Arvore.insere(Olhar_Inventario)

Help = Arvore_decisao(["help"], "Help")
Arvore.insere(Help)



Ir = Arvore_decisao(txt.ir, "Ir direção")
Arvore.insere(Ir)

norte = Arvore_decisao(txt.norte, "Ir norte")
sul = Arvore_decisao(txt.sul, "Ir sul")
leste = Arvore_decisao(txt.leste, "Ir leste")
oeste = Arvore_decisao(txt.oeste, "Ir oeste")

Ir.insere(norte)
Ir.insere(sul)
Ir.insere(leste)
Ir.insere(oeste)

combinar = Arvore_decisao(txt.combinar, "Combinar")
Arvore.insere(combinar)

voltar = Arvore_decisao(txt.voltar, "Voltar")
Arvore.insere(voltar)

entrar = Arvore_decisao(txt.entrar, "Entrar")
Arvore.insere(entrar)

############################## Árvore Interações ################################
#Árvores que definem possíveis interações do jogador com objetos coletáveis ou não. 
# Utilizada apenas nos cenários 0 e 1, já que possuem maior riqueza de objetos.

################################### Cenário 0 ###################################
Arvore_cenario0 = Arvore_decisao(None, "Ações")

uso_espada = Arvore_decisao(txt.espada_nomes, "Ações espada")
Arvore_cenario0.insere(uso_espada)

uso_chave = Arvore_decisao(["key", "chave"], "Ações chave")
Arvore_cenario0.insere(uso_chave)

uso_galho = Arvore_decisao(txt.galho_nomes, "Ações galho")
Arvore_cenario0.insere(uso_galho)

espada_arbusto = Arvore_decisao(["arbusto"], "Num rápido corte você confirma que seu escudeiro não se esqueceu de afiar a lâmina desta vez")
espada_porta = Arvore_decisao(txt.porta_nomes, "A espada pode acabar se quebrando contra essa porta. Talvez haja outra forma?")
espada_cavalo = Arvore_decisao(["cavalo", "horse"], "Não seria inteligente matar seu próprio cavalo.")
espada_sapo = Arvore_decisao(["sapo", "frog"], "Você não está com fome suficiente para começar a comer sapos.")

uso_espada.insere(espada_cavalo)
uso_espada.insere(espada_arbusto)
uso_espada.insere(espada_porta)
uso_espada.insere(espada_sapo)

galho_cavalo = Arvore_decisao(["cavalo", "horse"], "Não tem porquê atazanar seu cavalo.")
uso_galho.insere(galho_cavalo)

lamparina = Arvore_decisao(["lamparina", "lamp"], "Ações lamparina")
Arvore_cenario0.insere(lamparina)

lamparina_sul = Arvore_decisao(txt.sul, "Você não consegui iluminar nada com a lamparina apagada.")
lamparina.insere(lamparina_sul)

################################### Cenário 1 ###################################
Arvore_cenario1 = Arvore_decisao(None, "Ações")

uso_grampo = Arvore_decisao(["grampo", "lockpick"], "Ações grampo")
Arvore_cenario1.insere(uso_grampo)

grampo_rachadura = Arvore_decisao(["parede", "fenda"], "Você coloca o grampo na fenda do telhado, porém não é possivel girá-la")
uso_grampo.insere(grampo_rachadura)

uso_lamparina = Arvore_decisao(txt.lamparina_nomes, "Ações lamparina")
Arvore_cenario1.insere(uso_lamparina)

lamparina_goblin = Arvore_decisao(["goblin"], "Um golpe de lamparina não deve ser o suficiente para lidar com o goblin.")
uso_lamparina.insere(lamparina_goblin)


uso_faca = Arvore_decisao(["faca", "knife"], "Ações faca")
Arvore_cenario1.insere(uso_faca)

faca_corpo = Arvore_decisao(["corpse", "corpo"], "Chutando cachorro morto? Isso não parece muito cavaleiresco. ")
uso_faca.insere(faca_corpo)

faca_aranha = Arvore_decisao(["aranha", "spider"], "Você tenta golpear a aranha, mas ela é mais rápida e se esconde em um buraco.")
uso_faca.insere(faca_aranha)

###################################








