<img width="1186" height="420" alt="image" src="https://github.com/user-attachments/assets/0e42ed58-d4f2-49f9-a8d2-9ba295eb438a" />

    MENU: Os dados do tipo de café (preços, ingredientes)

    RESOURCES: Os ingredientes que a máquina possui

    calculate_coins(): 

    Criei essa função para calcular as moedas que o usuário colocou na "máquina"
    e retornei o resultado dessa operação como output

----------------

<img width="1502" height="761" alt="image" src="https://github.com/user-attachments/assets/3f8c6c40-7305-4d66-95b7-77009ef5eaa0" />

    difference_with_price():

    Criei essa função para verificar se o usuário colocou dinheiro suficiente na "máquina"
    e também para ver se tem troco ou não 
    
    Verifico o input do usuário identificando qual café ele quer. Nisso defino o preço do café tomando base
    do dicionário MENU lá em cima e também já faço a subtração da quantidade de dinheiro que colocou com o
    preço do café selecionado. Armazeno essa diferença em uma variável

    Faço uma condição final para ver:

    Se a diferença for maior ou igual a 0, então teve troco ou não. Em seguida entrego o café para o usuário.
    Também retorno como output True, que será importante mais para frente

    Se a diferença for menor que 0, então faltou dinheiro e imprimo na tela o preço total do café e quanto
    o usuário colocou na máquina. Retorno um output False

----------------

<img width="1187" height="804" alt="image" src="https://github.com/user-attachments/assets/f2694dc5-e7f1-4978-9778-e261953a22f5" />

    decrease_original_resources():

    Criei essa função para diminuir os ingredientes originais que estão na máquina

    Peguei referência ao tipo de café com inpput do usuário e com isso pego
    também os ingredientes que esse tipo de café consome usando keys e os armzeno em variáveis

    Faço esse mesmo procedimento para definir a quantidade de ingredientes na lista Resources{}
    que é onde está a quantidade da máquina

    Depois disso subtraio a quantidade de ingredientes do café que o usuário quer com a quantidade
    que está na máquina

    No final passo esses novos valores à lista com a quantidade de ingredientes original, para que
    a máquina armazene a quantidade que ainda tem

----------------

<img width="1078" height="629" alt="image" src="https://github.com/user-attachments/assets/de5e2e01-454d-445c-b8b6-47caa794cfff" />

    Essa função serve para verificar se tem os ingredientes para o café que o usuário digitou

    Se não tiver algum dos ingredientes, então retorno uma mensagem falando o que está faltando

----------------

<img width="1367" height="509" alt="image" src="https://github.com/user-attachments/assets/baa24e16-557c-406e-88ad-f2dabb5ec58b" />

<img width="1058" height="677" alt="image" src="https://github.com/user-attachments/assets/d86552df-dfaa-41a1-b007-577538b30955" />


    Inicio o loop que irá perguntar qual tipo de café quer

    Se digitar "off", a máquina para

    Se não, chamo a função para verificar se está faltando algum ingrediente e passo o input
    do usuário e os recursos da máquina como argumentos

    Se tiver faltando alguma coisa, a máquina avisa

    Se nenhuma das 2 opções acontecer, então:

    Chamo a função de diminuir os recursos da máquina passando o input do usuário e a lista de recursos.
    Essa função irá retornar a quantidade remanescente da máquina dos respectivos ingredientes e os armazeno
    em suas respectivas variáveis

    Peço para o usuário inserir as moedas

    Chamo a função para calcular o quanto que deu de dinheiro e passo as moedas como argumentos

    Chamo a função para verificar se teve troco ou não e depois limpo a tela
