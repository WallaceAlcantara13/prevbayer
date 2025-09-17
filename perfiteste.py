import streamlit as st
import pandas as pd
from pathlib import Path

# Configuração inicial
st.title("Questionário API PreviBayer")
st.write("Responda as perguntas abaixo para descobrir seu perfil de investidor.")

# Dados do usuário
nome = st.text_input("Digite seu nome completo:")
email = st.text_input("Digite seu e-mail:")

# Só mostrar o questionário se nome e email estiverem preenchidos
if nome and email:
    total = 0

    # Pergunta 1
    idade = st.radio("1 - Qual a sua faixa etária?", 
                     ["De 18 a 35 anos", "De 36 a 45 anos", "De 46 a 55 anos", "Mais de 56 anos"])
    total += {"De 18 a 35 anos": 20, "De 36 a 45 anos": 10, "De 46 a 55 anos": 5, "Mais de 56 anos": 0}[idade]

    # Pergunta 2
    momento = st.radio("2 - Como você definiria o seu momento de vida?",
                       ["Estou apenas arcando com as despesas e compromissos financeiros",
                        "Estou construindo meu patrimônio, tenho compromissos financeiros, mas posso guardar parte da minha renda",
                        "Já construí meu patrimônio, estou realizando meus sonhos e objetivos, mas ainda mantenho despesas fixas elevadas",
                        "Já tenho um patrimônio consolidado que considero suficiente para preservar meu estilo de vida e agora é a hora de usufruir o que tenho guardado"])
    total += {0:20,1:10,2:5,3:0}[ ["Estou apenas arcando com as despesas e compromissos financeiros",
                                    "Estou construindo meu patrimônio, tenho compromissos financeiros, mas posso guardar parte da minha renda",
                                    "Já construí meu patrimônio, estou realizando seus sonhos e objetivos, mas ainda mantenho despesas fixas elevadas",
                                    "Já tenho um patrimônio consolidado que considero suficiente para preservar seu estilo de vida e agora é a hora de usufruir o que tem guardado"].index(momento)]

    # Pergunta 3
    conhecimento = st.radio("3 - Qual das alternativas melhor descreve seu conhecimento do mercado financeiro?",
                            ["Tenho baixo conhecimento sobre mercado financeiro.",
                             "Tenho algum conhecimento e costumo discutir o assunto com amigos e familiares",
                             "Já fiz alguns cursos sobre mercado financeiro.",
                             "Minha formação e minha profissão são diretamente relacionadas ao mercado financeiro"])
    total += {"Tenho baixo conhecimento sobre mercado financeiro.":0,
              "Tenho algum conhecimento e costumo discutir o assunto com amigos e familiares":5,
              "Já fiz alguns cursos sobre mercado financeiro.":10,
              "Minha formação e minha profissão são diretamente relacionadas ao mercado financeiro":20}[conhecimento]

    # Pergunta 4
    tempo = st.radio("4 - Quanto tempo pretende investir?",
                     ["0","Entre 1 e 5 anos","Entre 6 e 10 anos","Acima de 10 anos"])
    total += {"0":0,"Entre 1 e 5 anos":5,"Entre 6 e 10 anos":10,"Acima de 10 anos":20}[tempo]

    # Pergunta 5
    queda = st.radio("5 - O que você faria ao ver uma queda de 10% nos seus investimentos?",
                     ["Resgataria todos os meus recursos",
                      "Troca de perfil para um de menor risco",
                      "Manteria os investimentos nas mesmas classes de ativos",
                      "Avaliaria a oportunidade para aumentar minha exposição em ativos de mais risco"])
    total += {"Resgataria todos os meus recursos":0,
              "Troca de perfil para um de menor risco":5,
              "Manteria os investimentos nas mesmas classes de ativos":10,
              "Avaliaria a oportunidade para aumentar minha exposição em ativos de mais risco":20}[queda]

    # Pergunta 6
    objetivo = st.radio("6 - Qual seu objetivo ao investir?",
                        ["Ainda não tenho objetivo(s)","Preservar o valor investido",
                         "Combinação entre preservar o valor investido e uma valorização de patrimônio assumindo certo risco",
                         "Maximizar os ganhos sobre o capital investido, assumindo o risco"])
    total += {"Ainda não tenho objetivo(s)":0,
              "Preservar o valor investido":5,
              "Combinação entre preservar o valor investido e uma valorização de patrimônio assumindo certo risco":10,
              "Maximizar os ganhos sobre o capital investido, assumindo o risco":20}[objetivo]

    # Pergunta 7
    planejamento = st.radio("7 - Você realiza algum tipo de planejamento financeiro em suas finanças pessoais?",
                            ["Não realizo planejamento algum",
                             "Realizo planejamento para objetivos de curto prazo (ex. troca de celular, viagem, etc)",
                             "Apenas organizo as finanças do mês para não ficar no vermelho",
                             "Realizo planejamento para objetivos de médio e longo prazo (ex. casa própria, aposentadoria, faculdade dos filhos, etc)"])
    total += {"Não realizo planejamento algum":0,
              "Realizo planejamento para objetivos de curto prazo (ex. troca de celular, viagem, etc)":5,
              "Apenas organizo as finanças do mês para não ficar no vermelho":10,
              "Realizo planejamento para objetivos de médio e longo prazo (ex. casa própria, aposentadoria, faculdade dos filhos, etc)":20}[planejamento]

    # Pergunta 8
    poupanca = st.radio("8 - Quanto você poupa em relação aos seus rendimentos mensais (salário, bônus, renda extra, etc.)?",
                        ["Mais de 20%","Até 20%","Até 10%","Não poupo"])
    total += {"Mais de 20%":20,"Até 20%":10,"Até 10%":5,"Não poupo":0}[poupanca]

    # Pergunta 9
    outros_invest = st.radio("9 - Além do Plano de Previdência, você tem ou pretende ter outros investimentos?",
                             ["Não, somente o plano",
                              "Sim, um valor abaixo do plano",
                              "Sim, um valor próximo que tenho no plano",
                              "Possuo a maior parte dos meus investimentos fora do plano de aposentadoria"])
    total += {"Não, somente o plano":0,
              "Sim, um valor abaixo do plano":5,
              "Sim, um valor próximo que tenho no plano":10,
              "Possuo a maior parte dos meus investimentos fora do plano de aposentadoria":20}[outros_invest]

    # Pergunta 10
    aplicacao = st.radio("10 - Atualmente como estão sendo aplicados os seus recursos financeiros?",
                         ["Não possuo investimentos financeiros no momento.",
                          "A maior parte está aplicada em imóveis, outros bens ou em renda fixa de baixo risco (ex.: poupança)",
                          "A maior parte está aplicada em renda fixa (poupança, fundos, CDB, etc.) e uma pequena parte está direcionada para renda variável (ações, câmbio, etc.)",
                          "Boa parte está investida no segmento de renda variável (ações e fundos de ações) e também já investi em opções ou outros derivativos"])
    total += {"Não possuo investimentos financeiros no momento.":0,
              "A maior parte está aplicada em imóveis, outros bens ou em renda fixa de baixo risco (ex.: poupança)":5,
              "A maior parte está aplicada em renda fixa (poupança, fundos, CDB, etc.) e uma pequena parte está direcionada para renda variável (ações, câmbio, etc.)":10,
              "Boa parte está investida no segmento de renda variável (ações e fundos de ações) e também já investi em opções ou outros derivativos":20}[aplicacao]

    # Botão para calcular perfil
    if st.button("Calcular Perfil"):
        if total >= 95:
            perfil = "AGRESSIVO"
        elif total > 65:
            perfil = "MODERADO"
        elif total > 35:
            perfil = "CONSERVADOR"
        else:
            perfil = "SUPERCONSERVADOR"

        st.success(f"Seu perfil recomendado é: {perfil}")

        # Salvar resultado no Excel
        file_path = Path("resultados.xlsx")
        if file_path.exists():
            df = pd.read_excel(file_path)
        else:
            df = pd.DataFrame(columns=["Nome","E-mail","Perfil Recomendado"])
        
        df = pd.concat([df, pd.DataFrame([[nome,email,perfil]], columns=df.columns)], ignore_index=True)
        df.to_excel(file_path, index=False)
        st.info("Resultado salvo em 'resultados.xlsx'.")
