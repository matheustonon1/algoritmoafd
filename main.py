# Função que representa a função de transição δ
def transition_function(estado_atual, input_symbol, transicao):
    # Verifica se há uma transição definida para o estado atual e símbolo de entrada
    if estado_atual in transicao and input_symbol in transicao[estado_atual]:
        return transicao[estado_atual][input_symbol]
    return None  # Retorna None se não houver uma transição definida

# Função que executa o AFD
def run_afd(input_string, estado_inicial, estado_final, transicao):
    # Inicializa o estado atual com o estado inicial
    estado_atual = estado_inicial

    # Itera sobre cada símbolo na cadeia de entrada
    for symbol in input_string:
        # Verifica se o símbolo de entrada está no alfabeto (se necessário)
        if symbol not in transicao.get(estado_atual, {}):
            return False  # Símbolo de entrada inválido
        
        # Atualiza o estado atual usando a função de transição
        estado_atual = transition_function(estado_atual, symbol, transicao)
        
        # Se não há transição definida, rejeita a cadeia
        if estado_atual is None:
            return False

    # Verifica se o estado atual é um dos estados finais
    return estado_atual in estado_final

# Definição dos estados do AFD
estados = {'q0', 'q1', 'q2'}  # Conjunto de estados
alfabeto = {'a', 'b'}        # Alfabeto

# Função de transição δ
transicao = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

# Estado inicial
estado_inicial = 'q0'

# Conjunto de estados finais
estado_final = {'q1'}

# Cadeia de entrada
input_string = 'bbaa'

# Executa o AFD e exibe o resultado
if run_afd(input_string, estado_inicial, estado_final, transicao):
    print("Aceita")
else:
    print("Rejeita")