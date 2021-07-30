######################### Textos usados para a criação do jogo #########################

######################### Mensagens, listas auxiliares, atributos para inicialização ###############################

msg_inicial0 = "Você é o cavaleiro Sir Lancelot, que foi enviado pelo Rei Artur em uma missão para derrotar Morgana, a feiticeira extremamente poderosa que vêm causando problemas ao reino à décadas. Depois de uma longa jornada árdua cruzando a floresta que rodeia o esconderijo da feiticeira, você finalmente chega ao seu destino"  + 2*"\n"  + "Pressione help para obter ajuda."

######################### Descrições do Cenário #########################

#### Cenario 0
cenario0_leste = "Aparentemente é a entrada do calabouço de Morgana, há uma porta de aço bloqueando sua passagem"
cenario0_oeste = "A escuridão é grande, mas você nota um brilho de relance, será só imaginação?"
cenario0_norte = "Você vê a longa e sombria floresta que você teve que percorrer para chegar ao calabouço. Seu cavalo relincha suavemente."
cenario0_sul = "Está muito escuro para poder ver qualquer coisa."

ir_oeste_cenario0 = "Em meio a terra você avista uma pequena chave enferrujada."
ir_leste_cenario0 = "Olhando mais de perto, é possivel ver que a porta de aço está entreaberta. Porém ela é muito pesada para você conseguir abrir por conta própria"
ir_norte_cenario0 = "Há uma pequena árvore, mas sua madeira parece resistente"
ir_sul_cenario0 = "Aparentemente não há nada aqui, esta muito escuro"

espada_nomes = ["espada","sword"]
arvore_nomes = ["arvore", "tree"]
galho_nomes = ["galho","stick"]
porta_nomes = ["porta", "door"]

#### Cenario 1
cenario1_leste = "Há um goblin dormindo ao lado de seu gigantesco porrete no meio da passagem, seria arriscado acordá-lo sem ter arma alguma para lutar contra ele."
cenario1_oeste = "Há uma estante cheia de livros e ao lado uma lareira acesa. É possível voltar para a floresta."
cenario1_norte = "A parede de pedras está coberta de teias de aranha...há também uma estranha fenda atrás do tamanho de uma chave"
cenario1_sul = "Há um baú de madeira trancado ao lado da parede."
msg_inicial1 = "Você passa pela porta e entra no calabouço. Você está passando por um estreito corredor iluminado por tochas, quando de repente você sente uma espécie de choque percorrendo por seu corpo...você olha para frente desnorteado e vê uma pessoa com um manto roxo e chapéu pontiagudo desaparecendo na escuridão. Quando você se da conta, percebe que suas preciosas espada e armadura reais desapareceram...você está completamente desarmado..."

ir = ["ir", "go"]

ir_oeste_cenario1 = "Você está em frente a lareira"
ir_leste_cenario1 = "Não é possivel ir por aqui pois o Goblin está bloqueando o caminho."
ir_norte_cenario1 = "Não há nada aqui, além da parede."
ir_sul_cenario1 = "Você está em frente a um baú de madeira."

bau_nomes = ["bau", "chest"]
lareira_nomes = ["lareira", "fireplace"]
lamparina_nomes = ["lamparina", "lamp"]

#### Cenario 2
cenario2_leste = "Uma parede, aparentemente é o fim da linha."
cenario2_oeste = "Há uma prateleira na entrada da sala, nela há um frasco com pedrinhas azuis."
cenario2_sul = "Há uma grande pilha de pedras no chão nesse canto da sala."
cenario2_norte = "Este canto da sala está muito mal iluminado, não é possível ver nada."
msg_inicial2 = "Você percorre mais um corredor mal iluminado por tochas nas paredes e chega à uma nova sala, escura e com cristais coloridos brilhando no telhado, porém desta vez a sala parece não ter saída. No meio da sala há uma pilha de grandes pedras cinza-claro"

ir_oeste_cenario2 = "Você se aproxima da prateleira e você pode ver que dentro do frasco há um estranho sal azul."
ir_leste_cenario2 = "Quando você se aproxima mais da parede você pode notar que uma parta dela é falsa, as pedras estão soltas. Você remove as pedras e dentro da parede você encontra um misterioso livro."
ir_norte_cenario2 = "Você esbarra em um estátua de bronze a desmontando por inteiro. O capacete, as luvas e o peitoral caem no chão."
ir_sul_cenario2 = "Quando você se aproxima da pilha de pedras você percebe que ela na verdade é um Golem, imóvel."

###Cenario 3
msg_inicial3 = "Você chega a uma iluminada por uma luz roxa"

ir_oeste_cenario3 = "Você está em frente ao painel, em frente dele há varios quadrinhos com símbolos escritos neles."
ir_leste_cenario3 = "Não é possível passar por aqui. Há um enorme cristal no caminho"
ir_norte_cenario3 = "Ao se aproximar da pessoa você nota que ela na verdade está morta, aparentemente não a muito tempo. No bolso de suas vestes você vê uma chave"
ir_sul_cenario3 = "Você nota que uma parte do chão parece meio frágil, há uma rachadura."

cenario3_sul = "Há uma série de crânios pendurados na parede."
cenario3_norte = "Ao lado da escada por onde você veio há uma pessoa sentada, imóvel."
cenario3_leste = "Há um grande cristal lilás impedindo sua passagem por completo."
cenario3_oeste = "Há um painel emitindo luzes estranhas nesse lado da sala. Acima dele há um alvo."

msg_final = "Armado do arco e flechas você vai para o ambiente final do calabouço, onde Morgana lhe espera..."

######################### Listas de Comandos Aceitos #########################
norte = ["norte","frente", "cima", "north", "up"]
sul = ["sul","atrás", "baixo", "south", "back", "down"]
leste = ["leste", "direita", "east", "right"]
oeste = ["oeste", "esquerda", "left", "west"]

olhar =  ["olhar norte", "olhar sul", "olhar oeste", "olhar leste"]
interagir_obj = ["usar", "abrir", "fechar", "combinar", "use", "open", "close", "combine"]

voltar = ["voltar", "back"]
entrar = ["entrar", "enter"]

combinar = ["combine", "combinar"]

pegar = ["pegar", "get"]
inventario = ["inventario", "inventory", "h"]

numeros = ["1","2","3","4","5","6","7", "8", "9", "10"]