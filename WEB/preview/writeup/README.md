# Preview
### _WEB_

Nos deparamos com a seguinte página ao acessar o desafio:
![Imagem 1](./preview1.png)

Clicando em "Admin", somos enviados para "/admin" porém a mesma página a cima é renderizada. Olhando os cookies é possível verificar o seguinte:

```
auth=0
```

Alterando o auth para 1, temos acesso ao "/admin":
![Imagem 2](./preview2.png)

Que é nada mais que um "sistema de renderização de imagens". Passando uma url de uma imagem qualquer, ela é renderizada:
![Imagem 3](./preview3.png)

Sendo assim, imagina-se que exista alguma função que acesse a url, baixe o conteúdo do arquivo em questão (a imagem) e faça a "renderização" dessa imagem. Portanto, usando o protocolo file (```file://```) é possível fazer com que a função acesse algum arquivo interno do servidor.
![Imagem 4](./preview4.png)

Então, procurando por "/flag.txt" temos a flag:
![Imagem 5](./preview5.png)

FLAG:
```
DC5551{N1CE_?????}
```
