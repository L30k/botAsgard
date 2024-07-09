def carregarConfiguracoes(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):  # Ignora linhas em branco e comentários
                key, value = line.strip().split('=', 1)
                config[key.strip()] = value.strip()
    return config