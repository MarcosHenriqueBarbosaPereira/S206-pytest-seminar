import pytest
import requests


class TestAPI:
    # TESTE DE API
    @pytest.mark.parametrize(
        "pokemon, expected_name",
        [
            ("bulbasaur", "bulbasaur"),
            ("charmander", "charmander"),
            ("squirtle", "squirtle"),
        ],
    )
    def test_PokemonSucesso(self, pokemon, expected_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)

        # Verificando o status da resposta
        assert response.status_code == 200

        # Validando o nome do Pokémon
        data = response.json()
        assert data["name"] == expected_name
