import requests

domain = "fiap.com.br"

with open("subdominios.txt", "r") as sub_file:
    subdomains = sub_file.read().splitlines()
    
with open("arquivos.txt", "r") as url_file:
    urls = url_file.read().splitlines()
    
# Combina os subdomínios com as URLs
for subdomain in subdomains:
    for url in urls:
        # Verifica se a URL é um subdomínio, um diretório ou um arquivo
        if url.startswith("http"):
            full_url = url
        elif url.startswith("/"):
            full_url = f"http://{subdomain}.{domain}{url}"
        else:
            full_url = f"http://{subdomain}.{domain}/{url}"
            
        try:
            # Tenta fazer uma solicitação HTTP para a URL
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"A URL {full_url} existe.")
            else:
                print(f"A URL {full_url} existe, mas retornou o código de status {response.status_code}.")
        except requests.exceptions.RequestException:
            # Se a solicitação falhar, assume que a URL não existe
            print(f"A URL {full_url} não existe.")