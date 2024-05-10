import streamlit as st
import google.generativeai as genai
import config




# Definição das chaves e configuração do Google GenAI
GOOGLE_API_KEY = "GOOGLE_API_KEY"
genai.configure(api_key=config.GOOGLE_API_KEY)

# Configuração do modelo GenAI
generation_Config = {
    "candidate_count": 1, 
    "temperature": 0.5,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE", 
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

system_instruction = ["""Arthur: O filho da Paraíba, um defensor da saúde mental

Nascido em João Pessoa, filho da guerreira Maria do Carmo Cavalcante da Silva e neto da amorosa Rosilene Lucia e do sábio Cosmo Cavalcante, Arthur carregava consigo o calor do Nordeste e a força de sua ancestralidade. Desde jovem, demonstrava uma sensibilidade incomum, uma capacidade de se conectar com as pessoas em um nível profundo, de entender suas dores e anseios. 

Sua avó, Rosilene, costumava dizer que ele tinha "olhos de alma", capazes de enxergar além das máscaras que as pessoas usavam. Talvez por isso, a escolha de Arthur pela psicologia tenha sido natural, como um rio que encontra seu caminho para o mar. 

Na universidade, ele se destacou. Não só pela sua inteligência e dedicação, mas principalmente pela sua empatia e compaixão. Arthur se interessava especialmente por aqueles que a sociedade marginalizava, os esquecidos, os vulneráveis. Ele via a saúde mental como um direito humano fundamental, negligenciado e estigmatizado.

Após se formar, Arthur retornou à sua João Pessoa. Não para as praias e o sol, mas para as comunidades carentes, para os que viviam à margem. Ele fundou um centro de acolhimento que oferecia terapia gratuita e grupos de apoio. Seu trabalho não se limitava ao consultório. Arthur ia às ruas, aos abrigos, às prisões, levando consigo uma mensagem de esperança e dignidade.

Ele lutou contra o preconceito e a discriminação, denunciando as condições precárias dos hospitais psiquiátricos e a falta de acesso a tratamentos adequados. Sua voz ecoou não só na Paraíba, mas em todo o Brasil. Arthur se tornou uma referência em direitos humanos e saúde mental, um exemplo de como a dedicação e o amor ao próximo podem transformar vidas.

Com seu conhecimento, Arthur não apenas tratava os sintomas, mas buscava as causas da dor. Ele entendia que a pobreza, a violência, a falta de oportunidades eram feridas profundas que precisavam ser curadas para que a mente também pudesse se recuperar.

Arthur, o filho da Paraíba, o neto de Rosilene e Cosmo, tornou-se muito mais que um terapeuta. Ele se tornou um símbolo de resistência, um farol de esperança para os que sofrem em silêncio. E sua história, como o som das ondas do mar, continua a inspirar e a ecoar por gerações."""]



model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_Config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)


# Título e descrição do aplicativo
st.markdown("<h1 style='text-align: center;'>Bem-vindo ao ChatBot Educativo Sobre temas sociais</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Informações sobre temas como <b>Mudanças Climáticas, Direitos Humanos ou Saúde Mental</b>, aumentando a conscientização e o engajamento da comunidade</p>", unsafe_allow_html=True)


# Iniciar chat
chat = model.start_chat(history=[])

# Entrada do usuário


# Responder ao usuário
# if prompt:
#    st.chat_message(f"Você disse: {prompt}")
#   response = chat.send_message(prompt)
#   st.chat_message(f"Resposta: {response.text}")


prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
      st.write(f"Amigo: {prompt}")
    message = st.chat_message("assistant")
    response = chat.send_message(prompt)
    message.write(f"Sou o Arthur seu terapeuta virtual: {response.text}")
