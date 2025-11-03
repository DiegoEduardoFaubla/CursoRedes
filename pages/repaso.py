import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Función para la animación
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code !=200:
    return None
  return r.json()

#Animaciones
lottie_coding1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0yfsb3a1.json")
#lottie_coding2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ggwq3ysg.json")

#Imagenes a usar
imagen1 = Image.open("CS.jpeg")
imagen2 = Image.open("inicio.jpg")
imagen3 = Image.open("instructor4.png")

st.markdown("""
    <style>
    /* Afecta el contenedor principal de Streamlit */
    section[data-testid="stSidebar"] {
        top: 0;
    }
    div.block-container {
        padding-top: 0rem;   /* 🔹 reduce espacio superior */
        margin-top: 15px;   /* 🔹 sube todo el contenido */
    }
    </style>
""", unsafe_allow_html=True)

#Sección 3 Repaso: Preguntas
st.image(imagen1,width=400)

st.header("Bienvenido a la sección de repaso 🖊")
st.subheader("Aquí podrás poner en práctica tus conocimientos, por medio de preguntas")
st.subheader("Seleccione el módulo que desea repasar")

# --- Lista de Módulos (usada para el Selectbox, bueno ya no estoy usando por el multipages) ---
MODULOS = [
        "Módulo 1: Las redes en nuestros tiempos",
        "Módulo 2: Configuración básica de dispositivos",
        "Módulo 3: Protocolos y Modelos",
        "Módulo 4: Capa Física" ,
        "Módulo 5: Matemáticas de Redes (Sistema binario, hexadecimal)",
        "Módulo 6: Capa Enlace de Datos",
        "Módulo 7: Tecnología Ethernet",
        "Módulo 8: Capa de Red",
        "Módulo 9: ARP",
        "Módulo 10: Configuración de dispositivos router",
        "Módulo 11: IPv4",
        "Módulo 12: IPv6",
        "Módulo 13: Protocolo de mensajes de control del Internet (ICMP)",
        "Módulo 14: Capa de Transporte",
        "Módulo 15: Capa de Aplicación",
        "Módulo 16: Fundamento de seguridad en una red",
        "Módulo 17: Laboratorio final de configuración de dispositivos"             
    ]
# 1. Widget para seleccionar el módulo
modulo_seleccionado = st.selectbox(
        "Módulos disponibles:",
        options=MODULOS
    )
    
st.markdown("---") # Separador para las preguntas
    
    # 2. Lógica para mostrar las preguntas basadas en la selección
    
if modulo_seleccionado == "Módulo 1: Las redes en nuestros tiempos":
    st.subheader("Módulo 1: Preguntas de Repaso")

    st.write("""1. ¿Cuáles de las siguientes son dos funciones de los dispositivos finales en una red? (Escoja dos opciones.):""")
    opciones = {
        "Dan origen a los datos que fluyen por la red.": st.checkbox("Dan origen a los datos que fluyen por la red."),
        "Dirigen los datos por rutas alternativas si fallan los enlaces.": st.checkbox("Dirigen los datos por rutas alternativas si fallan los enlaces."),
        "Filtran el flujo de datos para aumentar la seguridad.": st.checkbox("Filtran el flujo de datos para aumentar la seguridad."),
        "Constituyen la interfaz entre los humanos y la red de comunicación.": st.checkbox("Constituyen la interfaz entre los humanos y la red de comunicación."),
        "Proporcionan el canal por el que viaja el mensaje de red.": st.checkbox("Proporcionan el canal por el que viaja el mensaje de red."),
        }        

    if st.button("Comprobar respuestas",key="btn_enviar1"):
            correctas = opciones["Dan origen a los datos que fluyen por la red."] and opciones["Constituyen la interfaz entre los humanos y la red de comunicación."]
            incorrecta = opciones["Dirigen los datos por rutas alternativas si fallan los enlaces."] and opciones["Filtran el flujo de datos para aumentar la seguridad."] and opciones["Proporcionan el canal por el que viaja el mensaje de red."]
            incorrectas = opciones["Dirigen los datos por rutas alternativas si fallan los enlaces."] or opciones["Filtran el flujo de datos para aumentar la seguridad."] or opciones["Proporcionan el canal por el que viaja el mensaje de red."]
            if correctas  and not incorrectas:
                st.success("✅ ¡Excelente! Todas son correctas.")
            else:
                st.error("❌ Hay algún error. Revisa tus selecciones.")            
            
        
    st.write("2. ¿Qué es Internet")
    pregunta = st.radio("",
        ["Es una red basada en la tecnología Ethernet.", "Proporciona acceso a la red a los dispositivos móviles.", "Proporciona conexiones a través de las redes globales interconectadas.", "Es una red privada para una organización con conexiones LAN y WAN."]
        )

    if st.button("Responder",key="btn_enviar2"):
         if pregunta == "Proporciona conexiones a través de las redes globales interconectadas.":
            st.success("✅ ¡Correcto!")
         else:
            st.error("❌ Respuesta incorrecta.")

    st.write("3. Un empleado desea acceder a la red de la organización de manera remota y de la forma más segura posible. ¿Qué característica de la red le permitiría a un empleado acceder a la red de la empresa de manera remota y de la forma más segura?   ")
    pregunta = st.radio("",
    ["ACL", "IPS", "VPN", "BYOD"]
    )

    if st.button("Responder",key="btn_enviar3"):
        if pregunta == "VPN":
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Respuesta incorrecta.")

    st.write("4.  ¿Cómo cambia BYOD la forma en que las empresas implementan las redes?")
    pregunta = st.radio("",
    ["BYOD requiere que las organizaciones compren PC portátiles en lugar de computadoras de escritorio.", "Los usuarios BYOD son responsables de la seguridad de su red, por lo que se reduce la necesidad de políticas de seguridad dentro de la organización.", "Los dispositivos BYOD son más costosos que los dispositivos que compran las organizaciones.", "BYOD brinda flexibilidad con respecto a cuándo y cómo los usuarios pueden acceder a los recursos de red."]
    )

    if st.button("Responder",key="btn_enviar4"):
        if pregunta == "BYOD brinda flexibilidad con respecto a cuándo y cómo los usuarios pueden acceder a los recursos de red.":
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Respuesta incorrecta.")

    st.write("5. ¿A qué tipo de red debe acceder un usuario doméstico para realizar compras en línea?")
    pregunta = st.radio("",
    ["Una intranet", "El Internet", "Una extranet", "Una red de área local"]
    )

    if st.button("Responder",key="btn_enviar5"):
        if pregunta == "El Internet":
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Respuesta incorrecta.")
        
    st.write("""6. ¿Qué dos opciones de conexión a Internet no requieren que los cables físicos se ejecuten en el edificio? (Escoja dos opciones.)""")
    opciones = {
    "DSL": st.checkbox("DSL"),
    "Red celular": st.checkbox("Red celular"),
    "Red satelital": st.checkbox("Red satelital"),
    "Dial-up": st.checkbox("Dial-up"),
    "Línea arrendada dedicada": st.checkbox("Línea arrendada dedicada"),
    }

    if st.button("Comprobar respuestas",key="btn_enviar6"):
        correctas = opciones["Red celular"] and opciones["Red satelital"]
        incorrecta = opciones["DSL"] and opciones["Dial-up"] and opciones["Línea arrendada dedicada"]
        incorrectas = opciones["DSL"] or opciones["Dial-up"] or opciones["Línea arrendada dedicada"]
            
        if correctas  and not incorrectas:
            st.success("✅ ¡Excelente! Todas son correctas.")
        else:
            st.error("❌ Hay algún error. Revisa tus selecciones.")
        
    st.write("7. ¿Qué dispositivo realiza la función de determinar la ruta que deben tomar los mensajes a través de interredes?")
    pregunta = st.radio("",
    ["Un router", "Un firewall", "Un servidor web", "Un Módem DSL"]
    )

    if st.button("Responder",key="btn_enviar7"):
        if pregunta == "Un router":
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Respuesta incorrecta.")
        
    st.write("""8. ¿Cuáles de las siguientes son dos características de una red escalable? (Escoja dos opciones.)""")
    opciones = {
        "Se sobrecarga fácilmente con el incremento de tráfico.": st.checkbox("Se sobrecarga fácilmente con el incremento de tráfico."),
        "Crece en tamaño sin afectar a los usuarios existentes.": st.checkbox("Crece en tamaño sin afectar a los usuarios existentes."),
        "No es tan confiable como una red pequeña.": st.checkbox("No es tan confiable como una red pequeña."),
        "Es adecuada para los dispositivos modulares que permiten expansión.": st.checkbox("Es adecuada para los dispositivos modulares que permiten expansión."),
        "Ofrece un número limitado de aplicaciones.": st.checkbox("Ofrece un número limitado de aplicaciones."),
        }

    if st.button("Comprobar respuestas",key="btn_enviar8"):
        correctas = opciones["Crece en tamaño sin afectar a los usuarios existentes."] and opciones["Es adecuada para los dispositivos modulares que permiten expansión."]
        incorrecta = opciones["Se sobrecarga fácilmente con el incremento de tráfico."] and opciones["No es tan confiable como una red pequeña."] and opciones["Ofrece un número limitado de aplicaciones."]
        incorrectas = opciones["Se sobrecarga fácilmente con el incremento de tráfico."] or opciones["No es tan confiable como una red pequeña."] or opciones["Ofrece un número limitado de aplicaciones."]
            
        if correctas  and not incorrectas:
            st.success("✅ ¡Excelente! Todas son correctas.")
        else:
            st.error("❌ Hay algún error. Revisa tus selecciones.")
        
    st.write("9. Una universidad construye una nueva residencia estudiantil en su campus. Los trabajadores cavan para instalar las nuevas tuberías de agua de la residencia. Uno de ellos accidentalmente daña el cable de fibra óptica que conecta dos de las residencias existentes al centro de datos del campus. A pesar de que se cortó el cable, los estudiantes de las residencias solo perciben una interrupción muy breve en los servicios de red. ¿Qué característica de la red se demuestra aquí?")
    pregunta = st.radio("",
        ["Calidad de servicio (QoS)", "Escalabilidad", "Seguridad", "Tolerancia a fallas","Integridad"]
        )

    if st.button("Responder",key="btn_enviar9"):
        if pregunta == "Tolerancia a fallas":
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Respuesta incorrecta.")

    st.write("10. ¿Qué característica de una red le permite expandirse rápidamente para admitir a nuevos usuarios y aplicaciones sin afectar el rendimiento del servicio que se les proporciona a los usuarios actuales?")
    pregunta = st.radio("",
        ["Confiabilidad", "Escalabilidad", "Calidad de servicio", "Accesibilidad"]
        )

    if st.button("Responder",key="btn_enviar10"):
        if pregunta == "Escalabilidad":
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Respuesta incorrecta.")
        


elif modulo_seleccionado == "Módulo 2: Configuración básica de dispositivos":
    st.subheader("Módulo 2: Preguntas de Repaso")
    
elif modulo_seleccionado == "Módulo 3: Protocolos y Modelos":
    st.subheader("Módulo 3: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 4: Capa Física":
    st.subheader("Módulo 4: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 5: Matemáticas de Redes (Sistema binario, hexadecimal)":
    st.subheader("Módulo 5: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 6: Capa Enlace de Datos":
    st.subheader("Módulo 6: Preguntas de Repaso")
        
elif modulo_seleccionado == "Módulo 7: Tecnología Ethernet":
    st.subheader("Módulo 7: Preguntas de Repaso")
        
elif modulo_seleccionado == "Módulo 8: Capa de Red":
    st.subheader("Módulo 8: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 9: ARP":
    st.subheader("Módulo 9: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 10: Configuración de dispositivos router":
    st.subheader("Módulo 10: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 11: IPv4":
    st.subheader("Módulo 11: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 12: IPv6":
    st.subheader("Módulo 12: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 13: Protocolo de mensajes de control del Internet (ICMP)":
    st.subheader("Módulo 13: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 14: Capa de Transporte":
    st.subheader("Módulo 14: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 15: Capa de Aplicación":
    st.subheader("Módulo 15: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 16: Fundamento de seguridad en una red":
    st.subheader("Módulo 16: Preguntas de Repaso")

elif modulo_seleccionado == "Módulo 17: Laboratorio final de configuración de dispositivos":
    st.subheader("Módulo 17: Preguntas de Repaso")
else:
    # Esto cubre todos los demás módulos (3 al 16)
    st.info(f"Seleccionaste **{modulo_seleccionado}**. ¡Cargando preguntas pronto!")
    
    # respuesta = st.selectbox(
    # "¿Cuál de estos tipos de datos es mutable?",
    # ["int", "tuple", "list", "str"]
    #     )

    # if respuesta == "list":
    #     st.success("✅ Correcto")
    # else:
    #     st.warning("❌ Incorrecto, las listas son las mutables.")
    # puntuacion = 0

    # q1 = st.radio("1️⃣ ¿Qué imprime `print(2 ** 3)`?", ["5", "6", "8"])
    # if q1 == "8": puntuacion += 1

    # q2 = st.radio("2️⃣ ¿Cuál es el tipo de `{'a':1, 'b':2}`?", ["Lista", "Diccionario", "Tupla"])
    # if q2 == "Diccionario": puntuacion += 1

    # if st.button("Ver resultado"):
    #     st.info(f"Tu puntuación: {puntuacion}/2")

    # # =========================
    # # ESTILO TERMINAL para comandos
    # # =========================
    # st.markdown("""
    # <style>
    #     .stTextInput > div > div > input {
    #         background-color: black;
    #         color: #00ff00;
    #         font-family: monospace;
    #         font-size: 16px;
    #         border: none;
    #     }
    #     .terminal {
    #         background-color: black;
    #         color: #00ff00;
    #         font-family: monospace;
    #         padding: 10px;
    #         border-radius: 5px;
    #         min-height: 250px;
    #         white-space: pre-wrap;
    #     }
    # </style>
    # """, unsafe_allow_html=True)

    # st.title("🧑‍💻 Simulador de Configuración Cisco")

    # st.info("Tarea: Configura el servicio DHCP en la interfaz GigabitEthernet0/0 del router R1.")

    # # Entrada del usuario (como si fuera CLI)
    # comando = st.text_input("Ingresa un comando:", placeholder="R1#")

    # # Lista de comandos esperados (ordenados)
    # comandos_correctos = [
    #     "enable",
    #     "configure terminal",
    #     "ip dhcp pool RED_LOCAL",
    #     "network 192.168.10.0 255.255.255.0",
    #     "default-router 192.168.10.1",
    #     "dns-server 8.8.8.8",
    #     "exit",
    #     "interface gigabitEthernet0/0",
    #     "ip address 192.168.10.1 255.255.255.0",
    #     "no shutdown"
    # ]

    # # Usar session_state para llevar progreso
    # if "indice" not in st.session_state:
    #     st.session_state.indice = 0

    # if st.button("Enviar comando"):
    #     esperado = comandos_correctos[st.session_state.indice]
    #     if comando.strip().lower() == esperado.lower():
    #         st.success(f"✅ Correcto: {comando}")
    #         st.session_state.indice += 1
    #     else:
    #         st.error(f"❌ Incorrecto. Se esperaba algo como: '{esperado}'")

    # if st.session_state.indice == len(comandos_correctos):
    #     st.success("🎉 ¡Configuración completada correctamente!")
    # else:
    #     st.write(f"Progreso: {st.session_state.indice}/{len(comandos_correctos)}")
    
with st.container():            
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacio final
    st.caption("© 2025-2026 IEEE Computer Society.")
    st.caption("Aplicación construida usando Python y Streamlit.")
    