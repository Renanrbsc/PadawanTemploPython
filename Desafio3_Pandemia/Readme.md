⚠️ O mundo está em quarentena! Há uma nova pandemia que luta contra a humanidade. Cada continente é isolado, mas as pessoas infectadas se espalham antes do aviso. ⚠️

🗺️ Você receberia um mapa do mundo em um tipo de string:

string s = "01000000X000X011X0X"

'0': não infectado

'1': infectado

«X»: oceano

O vírus não pode se espalhar no outro lado do oceano.
Se uma pessoa é infectada, todas as pessoas neste continente também são infectadas.
Sua tarefa é encontrar a porcentagem da população humana que foi infectada no final.
Retorne a porcentagem% da população total que foi infectada.
O primeiro e o último continente não estão conectados!

Por exemplo:
início: map1 = "01000000X000X011X0X"
fim: map1 = "11111111X000X111X0X"
total_pessoas = 15
infectados = 11
porcentagem = 100 * 11/15 = 73.33333333333333

Para mapas sem oceanos "X", o mundo inteiro está conectado.
Para mapas sem "0" e "1", retorne 0, pois não há população.