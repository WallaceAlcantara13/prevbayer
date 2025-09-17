import streamlit as st
import pandas as pd
from pathlib import Path

# CSS para imagem de fundo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/your_image.jpg");  /* Substitua pelo link direto da imagem */
        background-size: cover;
        background-position: center;
    }
    .stRadio>div, .stTextInput>div, .stButton>div {
        background-color: rgba(255,255,255,0.8);
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Questionário API PreviBayer")
st.write("Responda as perguntas abaixo para descobrir seu perfil de investidor.")

# Session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "nome" not in st.session_state:
    st.session_state.nome = ""
if "email" not in st.session_state:
    st.session_state.email = ""

# Função para avançar para a próxima pergunta
def proxima_pergunta(pontos=0):
    st.session_state.total += pontos
    st.session_state.step += 1

# Função helper para radio sem seleção inicial
def pergunta_radio(texto, opcoes):
    return st.radio(texto, opcoes, index=-1)

# Tela inicial: nome e e-mail
if st.session_state.step == 0:
    st.session_state.nome = st.text_input("Digite seu nome completo:")
    st.session_state.email = st.text_input("Digite seu e-mail:")
    if st.button("Iniciar Questionário") and st.session_state.nome and st.session_state.email:
        st.session_state.step = 1

# Perguntas
elif st.session_state.step == 1:
    resposta = pergunta_radio("1 - Qual a sua faixa etária?", 
                              ["De 18 a 35 anos", "De 36 a 45 anos", "De 46 a 55 anos", "Mais de 56 anos"])
    if st.button("Próxima") and resposta:
        pontos = {"De 18 a 35 anos":20, "De 36 a 45 anos":10, "De 46 a 55 anos":5, "Mais de 56 anos":0}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 2:
    resposta = pergunta_radio("2 - Como você definiria o seu momento de vida?",
                              ["Estou apenas arcando com as despesas e compromissos financeiros",
                               "Estou construindo meu patrimônio, tenho compromissos financeiros, mas posso guardar parte da minha renda",
                               "Já construí meu patrimônio, estou realizando meus sonhos e objetivos, mas ainda mantenho despesas fixas elevadas",
                               "Já tenho um patrimônio consolidado que considero suficiente para preservar seu estilo de vida e agora é a hora de usufruir o que tem guardado"])
    if st.button("Próxima") and resposta:
        pontos = {"Estou apenas arcando com as despesas e compromissos financeiros":20,
                  "Estou construindo meu patrimônio, tenho compromissos financeiros, mas posso guardar parte da minha renda":10,
                  "Já construí meu patrimônio, estou realizando seus sonhos e objetivos, mas ainda mantenho despesas fixas elevadas":5,
                  "Já tenho um patrimônio consolidado que considera suficiente para preservar seu estilo de vida e agora é a hora de usufruir o que tem guardado":0}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 3:
    resposta = pergunta_radio("3 - Qual das alternativas melhor descreve seu conhecimento do mercado financeiro?",
                              ["Tenho baixo conhecimento sobre mercado financeiro.",
                               "Tenho algum conhecimento e costumo discutir o assunto com amigos e familiares",
                               "Já fiz alguns cursos sobre mercado financeiro.",
                               "Minha formação e minha profissão são diretamente relacionadas ao mercado financeiro"])
    if st.button("Próxima") and resposta:
        pontos = {"Tenho baixo conhecimento sobre mercado financeiro.":0,
                  "Tenho algum conhecimento e costumo discutir o assunto com amigos e familiares":5,
                  "Já fiz alguns cursos sobre mercado financeiro.":10,
                  "Minha formação e minha profissão são diretamente relacionadas ao mercado financeiro":20}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 4:
    resposta = pergunta_radio("4 - Quanto tempo pretende investir?",
                              ["0","Entre 1 e 5 anos","Entre 6 e 10 anos","Acima de 10 anos"])
    if st.button("Próxima") and resposta:
        pontos = {"0":0,"Entre 1 e 5 anos":5,"Entre 6 e 10 anos":10,"Acima de 10 anos":20}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 5:
    resposta = pergunta_radio("5 - O que você faria ao ver uma queda de 10% nos seus investimentos?",
                              ["Resgataria todos os meus recursos",
                               "Troca de perfil para um de menor risco",
                               "Manteria os investimentos nas mesmas classes de ativos",
                               "Avaliaria a oportunidade para aumentar minha exposição em ativos de mais risco"])
    if st.button("Próxima") and resposta:
        pontos = {"Resgataria todos os meus recursos":0,
                  "Troca de perfil para um de menor risco":5,
                  "Manteria os investimentos nas mesmas classes de ativos":10,
                  "Avaliaria a oportunidade para aumentar minha exposição em ativos de mais risco":20}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 6:
    resposta = pergunta_radio("6 - Qual seu objetivo ao investir?",
                              ["Ainda não tenho objetivo(s)","Preservar o valor investido",
                               "Combinação entre preservar o valor investido e uma valorização de patrimônio assumindo certo risco",
                               "Maximizar os ganhos sobre o capital investido, assumindo o risco"])
    if st.button("Próxima") and resposta:
        pontos = {"Ainda não tenho objetivo(s)":0,
                  "Preservar o valor investido":5,
                  "Combinação entre preservar o valor investido e uma valorização de patrimônio assumindo certo risco":10,
                  "Maximizar os ganhos sobre o capital investido, assumindo o risco":20}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 7:
    resposta = pergunta_radio("7 - Você realiza algum tipo de planejamento financeiro em suas finanças pessoais?",
                              ["Não realizo planejamento algum",
                               "Realizo planejamento para objetivos de curto prazo (ex. troca de celular, viagem, etc)",
                               "Apenas organizo as finanças do mês para não ficar no vermelho",
                               "Realizo planejamento para objetivos de médio e longo prazo (ex. casa própria, aposentadoria, faculdade dos filhos, etc)"])
    if st.button("Próxima") and resposta:
        pontos = {"Não realizo planejamento algum":0,
                  "Realizo planejamento para objetivos de curto prazo (ex. troca de celular, viagem, etc)":5,
                  "Apenas organizo as finanças do mês para não ficar no vermelho":10,
                  "Realizo planejamento para objetivos de médio e longo prazo (ex. casa própria, aposentadoria, faculdade dos filhos, etc)":20}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 8:
    resposta = pergunta_radio("8 - Quanto você poupa em relação aos seus rendimentos mensais?",
                              ["Mais de 20%","Até 20%","Até 10%","Não poupo"])
    if st.button("Próxima") and resposta:
        pontos = {"Mais de 20%":20,"Até 20%":10,"Até 10%":5,"Não poupo":0}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 9:
    resposta = pergunta_radio("9 - Além do Plano de Previdência, você tem ou pretende ter outros investimentos?",
                              ["Não, somente o plano",
                               "Sim, um valor abaixo do plano",
                               "Sim, um valor próximo que tenho no plano",
                               "Possuo a maior parte dos meus investimentos fora do plano de aposentadoria"])
    if st.button("Próxima") and resposta:
        pontos = {"Não, somente o plano":0,
                  "Sim, um valor abaixo do plano":5,
                  "Sim, um valor próximo que tenho no plano":10,
                  "Possuo a maior parte dos meus investimentos fora do plano de aposentadoria":20}[resposta]
        proxima_pergunta(pontos)

elif st.session_state.step == 10:
    resposta = pergunta_radio("10 - Atualmente como estão sendo aplicados os seus recursos financeiros?",
                              ["Não possuo investimentos financeiros no momento.",
                               "A maior parte está aplicada em imóveis, outros bens ou em renda fixa de baixo risco (ex.: poupança)",
                               "A maior parte está aplicada em renda fixa (poupança, fundos, CDB, etc.) e uma pequena parte está direcionada para renda variável (ações, câmbio, etc.)",
                               "Boa parte está investida no segmento de renda variável (ações e fundos de ações) e também já investi em opções ou outros derivativos"])
    if st.button("Finalizar") and resposta:
        pontos = {"Não possuo investimentos financeiros no momento.":0,
                  "A maior parte está aplicada em imóveis, outros bens ou em renda fixa de baixo risco (ex.: poupança)":5,
                  "A maior parte está aplicada em renda fixa (poupança, fundos, CDB, etc.) e uma pequena parte está direcionada para renda variável (ações, câmbio, etc.)":10,
                  "Boa parte está investida no segmento de renda variável (ações e fundos de ações) e também já investi em opções ou outros derivativos":20}[resposta]
        proxima_pergunta(pontos)

# Resultado final
if st.session_state.step == 11:
    total = st.session_state.total
    if total >= 95:
        perfil = "AGRESSIVO"
    elif total > 65:
        perfil = "MODERADO"
    elif total > 35:
        perfil = "CONSERVADOR"
    else:
        perfil = "SUPERCONSERVADOR"

    st.success(f"Seu perfil recomendado é: {perfil}")
