import streamlit as st 
import math as mt 

st.set_page_config(
    page_title="CalculateMe",
    layout="centered"
)

st.title("calcolatore aree provini")
st.caption("calcola facilmente le aree dei tuoi provini")

with st.sidebar:
    st.header("impostazioni")
    forma = st.selectbox("scegli forma del provino",
                     ["tondo","quadro","tubo"])

    st.info("tutte le dimensioni vanno espresse in mm")



if forma == "tondo":
    st.subheader("provino tondo")
    with st.expander("come viene calcolata l'area?"):
        st.write("l'area viene calcolata secondo la seguente formula:")
        st.latex(r"A= \frac{\pi}{4} \times D^2")
    diametro = st.number_input("inserisci il diametro:", min_value=0.0)
    if st.button("calcola"):
        if diametro == 0:
            st.warning("il diametro deve essere maggiore di zero")
        else:
            area = diametro**2 * mt.pi / 4
            area_visulaizzata = mt.trunc(area*100)/100
            st.metric("area della sezione",f"{area_visulaizzata:.2f}mm²")


if forma == "quadro":
    st.subheader("provino quadro")  
    with st.expander("come viene calcolata l'area?"):
        st.text("l'area viene calcolata secondo la seguente formula:")
        st.latex(r"A= spessore \times larghezza" )
    colonna_1 , colonna_2 = st.columns(2)
    with colonna_1:
        spessore = st.number_input("inserire lo spessore:",min_value=0.0)
    with colonna_2:
        larghezza = st.number_input("inserire la larghezza:",min_value=0.0)
    if st.button("calcola"):
        if larghezza == 0 or spessore == 0:
            st.warning("spessore e/o larghezza devono essere maggiori di zero")
        else:
            area = larghezza * spessore
            area_visulaizzata = mt.trunc(area*100)/100
            st.metric("area della sezione",f"{area_visulaizzata:.2f}mm²")


if forma == "tubo":
    st.subheader("provino tubolare")
    with st.expander("come viene calcoalta l'area?"):
        st.write("per primo viene calcolato il diametro interno mediante seguente formula:")
        st.latex(r"Di = De - (spessore \times 2)")
        st.write("infine si calcola l'area utilizzando la formula della corona circolare:")
        st.latex(r"A = \frac{\pi}{4}(De^2 - Di^2)")
    colonna_1, colonna_2 = st.columns(2)
    with colonna_1:
        diametro_esterno = st.number_input("inserire il diametro esterno:",min_value=0.0)
    with colonna_2:
        spessore = st.number_input("inserire lo spessore:",min_value=0.0)
    if st.button("calcola"):
        if diametro_esterno == 0 or spessore == 0:
            st.warning("il diametro esterno e/o lo spessore devono essere maggiori di zero")
        else:
            diametro_interno = diametro_esterno - 2* spessore
            area = (mt.pi/4) * (diametro_esterno**2 - diametro_interno**2)
            area_visulaizzata = mt.trunc(area*100)/100
            st.metric("area della sezione",f"{area_visulaizzata:.2f}mm²")

    



   