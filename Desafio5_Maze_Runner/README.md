Introdução
 	Bem-vindo aventureiro. Seu objetivo é navegar pelo labirinto e chegar ao ponto de chegada sem tocar em nenhuma parede. Se o fizer, irá matá-lo instantaneamente!
 
Tarefa
 	Você receberá uma matriz 2D do labirinto e uma série de direções. Sua tarefa é seguir as instruções fornecidas. Se você chegar ao ponto final antes que todos os seus movimentos tenham acabado, retorne Concluir . Se você bater em alguma parede ou sair da fronteira do labirinto, retorne Dead . Se você ainda estiver no labirinto depois de usar todos os movimentos, retorne Lost .
 
O array Maze será parecido com

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
..com a seguinte chave

 	0 = Lugar seguro para andar
1 = Parede
2 = Ponto inicial
3 = Ponto final
 
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
Regras
 	1. A matriz Maze sempre será quadrada, ou seja, N x N, mas seu tamanho e conteúdo serão alterados de teste para teste.
2. As posições inicial e final serão alteradas para os testes finais.
3. A matriz de direções estará sempre em maiúsculas e no formato de N = Norte, E = Leste, W = Oeste e S = Sul .
</td>
 
Boa sorte e fique seguro!