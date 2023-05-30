import sympy
from sympy import symbols, integrate, latex, SympifyError

import streamlit as st

# Estilo CSS personalizado
st.markdown(
    """
    <style>
    .header {
        background-color: #f63366;
        padding: 1rem;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }

    .subheader {
        margin-top: 1rem;
        font-size: 18px;
        font-weight: bold;
    }

    .footer {
        margin-top: 2rem;
        text-align: center;
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
st.markdown(
    """
    <div class="header">
    Calculadora de Integrais
    </div>
    """,
    unsafe_allow_html=True
)

# Instruções para o usuário
if st.checkbox("Instruções"):
    st.markdown(
        """
        # Bem-vindo à Calculadora de Integrais!
        ====================================

        A Calculadora de Integrais é uma ferramenta que permite calcular diferentes tipos de integrais de maneira simples e rápida. Com ela, você pode obter resultados de integrais indefinidas, integrais por partes, integrais por substituição e integrais definidas.

        ## Passo a passo para usar a Calculadora de Integrais:
        ---------------------------------------------------

        1. Digite a expressão: No campo de texto "Digite a expressão", insira a expressão matemática da qual você deseja calcular a integral. Você pode usar as operações matemáticas básicas, como adição (+), subtração (-), multiplicação (*), divisão (/), exponenciação (^) e parênteses para definir a ordem das operações. Por exemplo, você pode digitar "x^2 + 3*x + 2" para calcular a integral dessa função.

        2. Inserindo raízes e frações: Para inserir uma raiz quadrada, você pode usar a função `sqrt()`. Por exemplo, para inserir a raiz quadrada de x, você pode digitar "sqrt(x)". Para inserir uma fração, você pode usar a barra (/). Por exemplo, para inserir a fração 1/2, você pode digitar "1/2".

        3. Selecione o tipo de integral: No menu suspenso "Selecione o tipo de integral", escolha o tipo de integral que você deseja calcular. Você pode escolher entre "Indefinida", "Por Partes", "Por Substituição" e "Definida".

        4. Integrais Indefinidas: Se você selecionou "Indefinida", a ferramenta irá calcular a integral indefinida da expressão fornecida. O resultado será exibido no campo "Resultado" como a integral indefinida da função.

        5. Integrais por Partes: Se você selecionou "Por Partes", a ferramenta irá calcular a integral por partes da expressão fornecida. O resultado será exibido no campo "Resultado" como a integral por partes da função.

        6. Integrais por Substituição: Se você selecionou "Por Substituição", a ferramenta irá calcular a integral por substituição da expressão fornecida. O resultado será exibido no campo "Resultado" como a integral por substituição da função.

        7. Integrais Definidas: Se você selecionou "Definida", será necessário fornecer os limites inferior e superior da integral. Digite os valores correspondentes nos campos "Limite inferior" e "Limite superior". A ferramenta irá calcular a integral definida da expressão entre esses limites. O resultado será exibido no campo "Resultado" como a integral definida da função nos limites especificados.

        8. Passos Intermediários: No campo "Passos Intermediários", você encontrará os passos realizados para calcular a integral, incluindo substituições, cálculos intermediários e avaliação nos limites, quando aplicável. Nem todas as integrais mostrarão os passos intermediários, pois alguns cálculos podem ser complexos ou impossíveis de serem exibidos passo a passo.

        9. Experimente diferentes expressões e tipos de integrais: Sinta-se à vontade para digitar diferentes expressões matemáticas, incluindo raízes e frações, e explorar os diferentes tipos de integrais oferecidos. A Calculadora de Integrais está aqui para ajudá-lo a compreender e calcular integrais de forma interativa.

        A Calculadora de Integrais é uma ferramenta educacional poderosa para estudantes, professores e entusiastas da matemática. Use-a para praticar cálculos de integrais, verificar seus resultados e entender os passos intermediários envolvidos.

        Esperamos que a Calculadora de Integrais seja útil em suas explorações matemáticas e facilite o seu trabalho com integrais. Aproveite a ferramenta e desfrute da matemática!

        Se você tiver mais dúvidas ou precisar de mais ajuda, não hesite em entrar em contato.
        """
    )


# Entrada de dados
expression = st.text_input("Digite a expressão:", value="x^2 + 2*x + 1")
integral_type = st.selectbox("Selecione o tipo de integral:", ["Indefinida", "Por Partes", "Por Substituição", "Definida"])
variable = symbols('x')

# Cálculo da integral
try:
    if integral_type == "Indefinida":
        result = integrate(expression, variable)
        st.subheader("Resultado")
        st.latex("\\int " + latex(sympy.sympify(expression)) + " dx = " + latex(result))

    elif integral_type == "Por Partes":
        result = integrate(expression, variable, parts=True)
        st.subheader("Resultado")
        st.latex("\\int " + latex(sympy.sympify(expression)) + " dx = " + latex(result))

    elif integral_type == "Por Substituição":
        result = integrate(expression, (variable, symbols('u')))
        st.subheader("Resultado")
        st.latex("\\int " + latex(sympy.sympify(expression)) + " dx = " + latex(result.subs(symbols('u'), symbols('x'))))

    elif integral_type == "Definida":
        lower_limit = st.number_input("Limite inferior:", value=0.0)
        upper_limit = st.number_input("Limite superior:", value=1.0)
        result = integrate(expression, (variable, lower_limit, upper_limit))
        st.subheader("Resultado")
        st.latex("\\int_{" + latex(lower_limit) + "}^{" + latex(upper_limit) + "} " + latex(sympy.sympify(expression)) + " dx = " + latex(result))

    # Mostrar passos intermediários para todas as integrais
    st.subheader("Passos Intermediários")
    try:
        intermediate_steps = integrate(expression, variable, conds='none', steps=True).doit()
        st.latex(intermediate_steps)
    except Exception as e:
        st.write("Passos intermediários não disponíveis para esta integral.")

except SympifyError:
    st.error("Erro: Expressão matemática inválida. Certifique-se de que a expressão esteja correta.")

# Rodapé
st.markdown(
    """
    <div class="footer">
    Desenvolvido por Pedro Henrique Rodrigues da Silva - 2023
    </div>
    """,
    unsafe_allow_html=True
)
