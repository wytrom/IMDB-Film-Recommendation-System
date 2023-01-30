# IMDB-Film-Recommendation-System
"Sistema de Recomendação de Filmes baseado em Dados do IMDB: Uma Aproximação com Similaridade Cosseno"

🚀 Este código é uma implementação de um sistema de recomendação de filmes baseado em dados do IMDB.

💻 Utilização: basta rodar o arquivo main.py em um ambiente Python com as bibliotecas Pandas e Numpy instaladas. O código fará a leitura dos dados de um arquivo .csv chamado data.csv, que deve estar na mesma pasta do código.

🧹 Limpeza: os dados lidos serão limpados, retirando dados ausentes e a coluna title desnecessária.

📈 Similaridade: será calculada a similaridade cosseno entre todos os filmes para determinar quais filmes são mais semelhantes.

🎥 Recomendação: a função recommend permite recomendar filmes semelhantes a um filme específico, dado o seu movieId. Por padrão, a função retorna as 10 recomendações mais próximas.

📚 Dependências: o código utiliza as bibliotecas Pandas e Numpy. Certifique-se de tê-las instaladas antes de executar o código.


💻 Para utilizar o código:

Certifique-se de ter o Python instalado em seu ambiente.
Instale as dependências (bibliotecas Pandas e Numpy) caso ainda não as tenha.
Coloque o arquivo data.csv com os dados do IMDB na mesma pasta do código.
Execute o arquivo main.py com o Python.
🎥 Para recomendar filmes:

Chame a função recommend passando como argumento o movieId do filme desejado.
A função retornará uma lista com as recomendações de filmes mais semelhantes ao filme escolhido.
📈 O cálculo da similaridade entre os filmes é feito utilizando o cosseno.

👍 Divirta-se recomendando filmes!
