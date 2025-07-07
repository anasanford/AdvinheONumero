# Adivinhe o Número
Olá! Esse é um projeto simples em Python para que eu aprenda a usar os comandos básicos do Git.
O projeto foi baseado no vídeo "12 Beginner Python Projects - Coding Course" da Kylie Ying
Link para o vídeo: https://www.youtube.com/watch?v=8ext9G7xspg

## Explicando o jogo Adivinhe o Número!
O jogo funciona em duas etapas:
- Na primeira parte, o computador gera um número aleatório entre 1 e 1000 para você advinhar e vai lhe dando dicas se o seu chute está muito alto ou muito baixo.
- Na segunda parte, você é quem escolhe um número aleaório entre 1 e 1000 para o computador advinhar. O computador vai chutar um número e você deve dar um feedback à ele, dizendo se o número está muito alto, muito baixo ou se o número está correto!

## Explicando o código:
- A biblioteca random foi importada para o uso da função randint(a, b), que seleciona um inteiro aleatório entre os parâmetros "a" e "b". Essa função foi usada tanto para o computador gerar um número aleatório para o usuário advinhar, como para ele gerar os números para chutar.
- Foram criadas duas funções, sendo a função advinhe(x) para o usuário advinhar o número do computador e a função computador_advinha(x) para o computador advinhar o número do usuário.
- O loops em cada função foram usados para que o jogo continue até o usuário e o computador acertem o número
- As condicionais foram usadas em duas situações: nas duas funções, foram usados para dar as dicas se os chutes estão altos/baixos e somente na função computador_advinha(x) foi usado para criar uma exceção quando os valores que servem de parâmetro à função random.radint() são iguais
