import pytest
import requests

# Chave da OMDb API
API_KEY = "986a0144"  # Sua chave da API

@pytest.mark.parametrize("titulo_filme, expected_year", [
    ("Inception", "2010"),
    ("The Matrix", "1999"),
    ("Interstellar", "2014"),
])
def test_omdb_api(titulo_filme, expected_year):
    # Requisição para obter dados do filme
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={titulo_filme}"
    response = requests.get(url)

    # Verificando o status da resposta
    assert response.status_code == 200, f"Falha no status da resposta para {titulo_filme}. Código retornado: {response.status_code}"

    # Validando o ano do filme
    data = response.json()
    assert data["Year"] == expected_year, f"Falha no ano do filme. Esperado: {expected_year}, mas retornado: {data['Year']}"

    # Requisição para obter o poster do filme
    poster_url = f"http://img.omdbapi.com/?apikey={API_KEY}&t={titulo_filme}"
    poster_response = requests.get(poster_url)

    # Verificando o status da requisição do poster
    assert poster_response.status_code == 200, f"Falha ao buscar o poster para {titulo_filme}. Código retornado: {poster_response.status_code}"

    # Se o teste passar, esta mensagem será exibida
    print(f"Teste para {titulo_filme} passou com sucesso!")
