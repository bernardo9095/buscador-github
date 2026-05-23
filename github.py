import requests

def repositori(nome, repo):
    url = (f'https://api.github.com/repos/{nome}/{repo}')
    reposta = (requests.get(url))
    return reposta.json()

nome = input('digite o nome do usuario do github: ')
repo = input('digite o nome do repositorio: ')

try:
    resultado = repositori(nome, repo)
    print(resultado['description'])
    print(resultado['stargazers_count'])
    print(resultado['name'])
    print(resultado['language'])
except KeyError:
    print('nao existe')