from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

###### dotenv を利用しない場合は消してください ######
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    import warnings
    warnings.warn("dotenv not found. Please make sure to set your environment variables manually.", ImportWarning)
################################################

# 画面
st.set_page_config(page_title="喋り相手", page_icon=":robot_face:")
st.header("喋り相手")

# セレクトボックス
character_name = st.selectbox('誰と喋りますか？', ('ゆうちゃみ', '高倉健', 'ボブ・ディラン','井上陽水'))
# 区切り線
st.divider()





# 質問
#user_input = "いい天気やん"

user_input = st.text_input("なんか喋って", value="こんにちは")   
if not user_input:
    st.stop()

#llm
#llm = ChatOpenAI()
#llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.2)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

#プロンプト
#prompt = ChatPromptTemplate.from_messages([
#    ("system","あなたは、ゆうちゃみです。ゆうちゃみ風にユーザーと会話してください。話す内容やキャラクターに応じて絵文字も使ってください。"),
#    ("user","{input}")
#])
prompt = ChatPromptTemplate.from_messages([
    ("system", f"あなたは、{character_name}です。{character_name}風にユーザーと会話してください。"),
    ("user", "{input}")
])

#出力
output_parser = StrOutputParser()

#LCEL
chain = prompt | llm | output_parser

#実行
response = chain.invoke({"input": user_input})

#表示
#print(response)

st.markdown(response)
