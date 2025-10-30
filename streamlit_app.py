import streamlit as st
import webbrowser

# Teste CSS PERSONALIZADO 
st.markdown("""
    <style>
            /* Corpo da pagina */
        body { background-color: #2F4F4F; color: #FFFFFF; }  
            /* Corpo da aplicação */
        .stApp { background-color: #2F4F4F; } 
             /* Título */
        .titulo { font-size: 50px; font-weight: bold; text-align: center; color: #FFFFFF; margin-bottom: 10px; }
            /* Subtítulo */
        .subtitulo { text-align: center; color: #D8BFD8; margin-bottom: 40px; } 

        /* CARD COM ANIMAÇÃO */
        .card {
            background-color: #008080;
            /*Preenchimento*/
            padding: 25px;
            /*Cantos arredondados*/
            border-radius: 25px;
            /*Margem*/
            margin-top: 20px;
            /*Transição suave*/
            transition: all 0.2s ease-in-out;
            /*Borda esquerda*/
            border-left: 6px solid #7FFFD4;
        }
            /*Efeito hover de mover quando passa o mouse*/
        .card:hover {
            transform: scale(1.03);
            border-left: 6px solid #D8BFD8;
        }

        
    </style>
"""
, unsafe_allow_html=True)

# TÍTULO 
st.markdown("<div class='titulo'>🏗️ Fornecedores de Aços</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Escolha o tipo de aço e entre em contato diretamente com o fornecedor.</div>", unsafe_allow_html=True)

# DADOS
fornecedores = {
    "Aço Carbono": {
        "empresa": "Empresa A",
        "descricao": "Aço carbono de alta resistência, ideal para estruturas metálicas e construção civil.",
        "email": "contatoA@empresa.com"
    },
    "Aço Inox 304": {
        "empresa": "Empresa B",
        "descricao": "Aço inox 304 com excelente resistência à corrosão, ideal para utensílios e equipamentos industriais.",
        "email": "contatoB@empresa.com"
    },
    "Aço Inox 316": {
        "empresa": "Empresa C",
        "descricao": "Aço inox 316 de qualidade superior, utilizado em ambientes marítimos e químicos.",
        "email": "contatoC@empresa.com"
    },
    "Aço Galvanizado": {
        "empresa": "Empresa D",
        "descricao": "Aço galvanizado com alta durabilidade, indicado para estruturas expostas e coberturas.",
        "email": "contatoD@empresa.com"
    }
}

# SELEÇÃO 
st.subheader("Selecione o tipo de aço para ver os detalhes do fornecedor:")
opcao = st.selectbox("Escolha um tipo de aço:", list(fornecedores.keys()))
st.write(fornecedores.keys())
if opcao:
    dados = fornecedores[opcao]
    st.markdown(f"""
        <div class='card'>
            <h3>{opcao} - {dados['empresa']}</h3>
            <p>{dados['descricao']}</p>
            <p>📧 <b>Contato:</b> {dados['email']}</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Deseja entrar em contato com este fornecedor?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sim"):
          gmail_url = "https://mail.google.com/"
          st.markdown(f'<meta http-equiv="refresh" content="0; url={gmail_url}">', unsafe_allow_html=True)
        st.success("Abrindo seu aplicativo de e-mail...")

    with col2:
        if st.button("❌ Não, obrigado.", key="nao"):
            st.info("Tudo bem! Você pode escolher outro tipo de aço acima 😊")

