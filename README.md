# Interpretador de CNAB

## 1. Sobre a aplicação

Essa aplicação tem o intuito de ler e interpretar arquivo com código(s) CNAB, trazendo um retorno visual para que torne a leitura e entendimento mais simples.

---

## 2. Passo a passo

Para testar a aplicação você terá que seguir os seguintes passos:

1. Fazer o clone do repositório;
2. Iniciar o ambiente virtual (Venv);
3. Na pasta raiz do projeto rodar o seguinte comando no terminal para instalar as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Ainda na pasta raiz rodar os seguintes comandos para gerar as tabelas do banco de dados:

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

5. Após instalá-las basta rodar o seguinte comando para startar a aplicação:

   ```bash
   python manage.py runserver
   ```

E ainda, caso queira ver os testes para testar as validações da model basta rodar o seguinte comando:

```bash
python manage.py transactions.tests
```

---

## 3. Como deve ser o código CNAB

- **Cada código CNAB deve conter exatamente 80 dígitos/caracteres.**
- Caso ocorra de o nome do representante e/ou nome da loja não pegue a quantidade de caracteres necessária deixa espaços em branco.
- Exemplos de código CNAB permitido: `5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ`
- **Como os códigos devem ser separados em um arquivo:**
  Deve conter apenas uma quebra de linha, separando um código do outro
- **No próprio repositório deixei um arquivo de exemplo, o cnab_example.txt.**

---

## 4. Como utilizar a aplicação

1. Na aba de “Envie seu arquivo” selecione o arquivo de texto (.txt) desejado para que possa ser interpretado
2. Após realizar o envio o resultado das transações aparecerá na aba “Resultados” juntamente com o saldo final

---

## 5. Tecnologias e Bibliotecas

- Python;
- Django Rest Framework;

---

### Desenvolvido Por Gisela Mariano ;)
