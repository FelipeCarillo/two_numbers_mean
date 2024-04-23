# README

## Membros

- César Shoity Kumakura | Github: CesarKumakura	RA: 23.01564-0 

- Felipe Carillo | Github: FelipeCarillo RA: 23.00765-6      

- Felipe Costa Muniz | Github: felip-000 RA: 23.01459-8

## Continuous Integration com GitHub Actions

Este repositório utiliza GitHub Actions para implementar testes de Continuous Integration (CI) automatizados.

### Passos para Clonar o Repositório

1. Abra o terminal ou prompt de comando.

2. Clone o repositório para o seu computador utilizando o seguinte comando:

   ```
   https://github.com/FelipeCarillo/two_numbers_mean.git
   ```

3. Navegue até o diretório clonado:

   ```
   cd two_numbers_mean
   ```

### Criar e Ativar um Ambiente Virtual

1. No diretório do repositório, crie um ambiente virtual utilizando o comando adequado para o seu sistema operacional:

   Para sistemas Unix/Linux/Mac:

   ```
   python3 -m venv venv
   ```

   Para Windows:

   ```
   python -m venv venv
   ```

2. Ative o ambiente virtual:

   No Unix/Linux/Mac:

   ```
   source venv/bin/activate
   ```

   No Windows:

   ```
   venv\Scripts\activate
   ```

### Instalar Dependências

1. Com o ambiente virtual ativado, instale as dependências do projeto executando o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

   Isso instalará todas as dependências listadas no arquivo `requirements.txt`.

### Executar testes BDD

   ```
   behave BDD/
   ```

### Executar testes TDD

   ```
   pytest TDD/
   ```

---
