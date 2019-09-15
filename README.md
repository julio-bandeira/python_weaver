# pyhton_weaver
Forme imagens por meio de linhas

Algoritmo Desenvolvido em Python 3.7 , utilizando PyCharm como IDE com o intuito de aprendizado

Programa realizado com base no video sobre o mesmo porem em c++ do canal Universo Programado

Link: https://www.youtube.com/watch?v=YZtx4jNNbx8&t=234s

## Bibliotecas
As bibliotecas utilizadas foram OpenCV, Math e Tkinter

## Imagem
O programa abrira uma janela para selecionar uma imagem

A imagem em si deve ter certos requisitos...

Afim de manter a uniformidade do circulo, a imagem deve ter altura e largura identicas

Para melhor experiencia utilize imagens entre 500x500 a 1000x1000 pixels
![alt text](https://github.com/julio-bandeira/pyhton_weaver/blob/master/demonstration.jpg)

## Pregos
O algoritimo lhe permitira escolher o numero de pregos a serem utilizados o recomendavel são 210 pregos

## Processo
O programa levara um tempo para processar toda a imagem o que pode variar conforme o arquivo

O algoritimo irá ler a partir de um ponto, uma linha de pixels até outro ponto, fara isso para todos os outro pontos, será traçada um linha até o ponto que mais tiver pixels preto e o processo irá se repetir apartir deste novo ponto e assim seguira até não haver mais pixels pretos entre os pontos ou atingir o numero de 1800 linhas

O limite de linhas atualmente é fixo em 1800...

## Salvamento
Após o processo ser finalizado o será informado o termino no terminal e uma janela identica será aberta, identificando o final do processo para poder observalo, apertando qualquer tecla ou propriamente fechando a imagem, será aberta uma janela para salvar os caminhos de ponto a ponto, escolha o local e digite o nome do arquivo, não há necessidade de informar a extensão, a extensão .txt já está configurada como padrão.
