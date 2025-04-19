import traceback
import streamlit as st
from scripts.search import search
import json

with open("data/documents/docs.json") as f:
    docs = json.load(f)

# Just print UNC Chapel Hill's text for inspection
for doc in docs:
    if "unc" in doc["id"]:
        print(doc["text"][:2000])  # preview first 2000 characters
        break


st.set_page_config(page_title="MSCS Deadline Search", page_icon="🎓")
st.title("🎓 MSCS Deadline Search")
st.markdown("""
Type a query like:
- "MIT CS deadline Fall 2025"
- "Ivy League MS application dates"
- "Deadlines after December 2024"
""")

query = st.text_input("🔍 Enter your query:")

if query:
    with st.spinner("Searching..."):
        try:
            results = search(query)
            for res in results:
                st.subheader(res['title'])
                st.write(res['summary'])
                st.caption(f"Relevance Score: {res['score']:.3f}")
        except Exception as e:
            #st.error(f"❌ Error: {e}")
                # get the full traceback as a string
            tb = traceback.format_exc()
            # display it in Streamlit
            st.error(f"❌ An exception occurred:\n```\n{tb}\n```")