import requests
import streamlit as st 
st.title("AL QURAN ")
st.title("by Syed Ashir")


meriSurahList=requests.get("https://api.alquran.cloud/v1/surah")


surahs =meriSurahList.json()["data"]



options=[]
for s in surahs:
   options.append(f"{s["number"]} | {s["name"]}")




item =st.selectbox("choose the surah",options)
surah_num= int(item.split("|")[0])
st.write(surah_num)



meriAyahList=requests.get(f"https://api.alquran.cloud/v1/surah/{surah_num}/ar.abdurrahmaansudais")



ayahs =meriAyahList.json()["data"]["ayahs"]



for a in ayahs:
   st.success(a["numberInSurah"])
   st.warning(a["text"])
   st.audio(a["audio"])

