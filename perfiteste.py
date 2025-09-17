import streamlit as st

st.title("Questionário API PreviBayer")
st.write("Responda as perguntas para descobrir seu perfil de investidor.")

total = 0

# Pergunta 1
idade = st.radio("1 - Qual a sua faixa etária?",
                 ["De 18 a 35 anos",
                  "De 36 a 45 anos",
                  "De 46 a 55 anos",
                  "Mais de 56 anos"])

if idade == "De 18 a 35 anos":
    total += 20
elif idade == "De 36 a 45 anos":
    total += 10
elif idade == "De 46 a 55 anos":
    total += 5
else:
    total += 0

# (Aqui você segue o mesmo padrão para as demais perguntas...)

# Botão para calcular
if st.button("Calcular Perfil"):
    if total <= 30:
        perfil = "Conservador"
    elif total <= 60:
        perfil = "Moderado"
    elif total <= 90:
        perfil = "Agressivo"
    else:
        perfil = "Arrojado"
    
    st.success(f"Seu perfil de investimento é: **{perfil}**")
