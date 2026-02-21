import requests
import json

class ListarPessoas:
    def __init__(self):
        self.base_url = "http://localhost:8080"

    def listar_pessoas(self):
        #endpoint para a operação de listagem
        endpoint_listar = f"{self.base_url}/pessoas"
    
         # Faz uma requisição HTTP GET usando a biblioteca requests
        response_listar = requests.get(endpoint_listar)
        # Converte a resposta JSON para dicionário Python
        dados_json = response_listar.json()

        print("=" * 30)
        print("RESULTADO LISTA DE PESSOAS:")
        for pessoa in dados_json:
            print(
                f"Nome: {pessoa['nome']},"
                f"email:{pessoa['email']}," 
                f"idade: {pessoa['idade']}," 
                f"altura: {pessoa['altura']}")
        print("=" * 30)

    def listar_email(self):
        endpoint_email = f"{self.base_url}/email"
    
         # Faz uma requisição HTTP GET usando a biblioteca requests
        response_listar_email = requests.get(endpoint_email)
        # Converte a resposta JSON para dicionário Python
        dados_json = response_listar_email.json()

        print("=" * 30)
        print("RESULTADO LISTA DE EMAIL:")
        for pessoa in dados_json:
            print(f"Email:{pessoa['email']}")
        print("=" * 30)

    def buscar_email(self, email):
        endpoint_pessoa = f"{self.base_url}/pessoa"
        dados = f'?email={email}'
        response_pessoa = requests.get(endpoint_pessoa + dados)
        dados_json = response_pessoa.json()

        print("=" * 30)
        print("RESULTADO:")
        print(
            f"Nome: {dados_json['nome']},"
            f"email:{dados_json['email']}," 
            f"idade: {dados_json['idade']}," 
            f"altura: {dados_json['altura']}")
        print("=" * 30)

if __name__ == "__main__":
    pessoa = ListarPessoas()
    pessoa.listar_pessoas()
    pessoa.listar_email()
    pessoa.buscar_email("sara@gmail.com")
   