from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    assert len(result) == 15

    # Verifica se todos os empregos possuem as chaves corretas
    keys = ["title", "salary", "type"]
    assert all(all(key in job for job in result) for key in keys)

    # Verifica se as chaves incorretas não estão presentes nos empregos
    assert all("titulo" not in job for job in result)
    assert all("salario" not in job for job in result)
    assert all("tipo" not in job for job in result)

    # Verifica se o primeiro emprego tem os valores corretos
    assert result[0]["title"] == "Maquinista"
    assert result[0]["salary"] == "2000"
    assert result[0]["type"] == "trainee"
