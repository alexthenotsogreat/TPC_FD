run coder.py  

Sempre que pedido o nome o u caminho de um ficheiro, introduzir sempre a extensão também, por exemplo, output.txt.  

Outputs:  

1 - Encoding:  
  1.1 -> ficheiro output codificado por código cíclico.  
  1.2 -> ficheiro com os bytes resultantes da leitura da imagem (_OriginalBytes.txt)  
  
2 - Decoding:  
  2.1 -> ficheiro output com o resultado da descodificação (imagem) que, no caso de não ter sido corrompida para além das capacidades de correção do decoder, pela função chanel, será aberta.  
  2.2 -> ficheiro output com o resultado da descodificação (.txt) --> para comparação na opção 3  
  
3 - Compare:  
  3.1 -> resultado do cálculo do BER dos ficheiros introduzidos. Ficheiros estes que são, respetivamente, os 1.2 e 2.2.  
  
