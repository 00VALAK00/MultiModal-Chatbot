import streamlit as st
from PIL import Image

from MultiModal import model
from utils.prompts import ocr_prompt, information_retrieval_prompt

st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")


def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]


with st.sidebar:
    st.title("Explore the tasks")
    vllm = model.VisionModel()

    task = st.selectbox("Tasks",
                        options=["Q&A", "Optical Character Recognition (OCR)", "Invoice information extraction"])

    st.text("This Application is powered by an open-source model called MiniCPM-V-2_6")
    st.header("What is interesting about this model?")
    st.markdown(
        "1. Surpasses **GPT-4o mini, GPT-4V, Gemini 1.5 Pro, and Claude 3.5 Sonnet** in single-image understanding.")
    st.markdown("2. **Strong OCR Capability**")
    st.markdown("3. **Superior Efficiency**: inference speed, memory usage")
    st.markdown("4. **Video understanding**")
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


def stream_completion(prompt, img=None):
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            completion = vllm.complete(prompt=prompt, image=img)
            placeholder = st.empty()
            full_text = ""
            for item in completion:
                full_text += item
                placeholder.markdown(full_text)
            placeholder.write(full_text)

    st.session_state.messages.append({"role": "assistant", "content": full_text})


def initial_message():
    if task == "Q&A":
        return "How may I assist you today?"
    elif task == "Invoice information extraction":
        return "What are the key features you want to extract? (e.g., Expiry date, recipient name)"
    elif task == "Optical Character Recognition (OCR)":
        return "Please upload an image to perform OCR."
    return "How may I assist you today?"


st.title(task)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": initial_message()}]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if task != "Q&A":
    if st.session_state.messages[-1]["role"] == "assistant" or len(st.session_state.messages) == 1:
        img = st.file_uploader("Drag and drop image here", type=["png", "jpg", "jpeg"])

        if img:
            st.image(img, use_column_width=True)
            img = Image.open(img).convert("RGB")

            if task == "Optical Character Recognition (OCR)":

                stream_completion(prompt=ocr_prompt, img=img)

            if task == "Invoice information extraction":
                if features := st.chat_input("Enter features to extract (e.g., expiry date, recipient name):"):
                    st.session_state.messages.append({"role": "user", "content": features})
                    with st.chat_message("user"):
                        st.write(features)
                    formatted_prompt = information_retrieval_prompt.format(features=features)
                    print(formatted_prompt)
                    stream_completion(formatted_prompt, img)

else:

    if prompt := st.chat_input("Ask me anything!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = vllm.complete(prompt=prompt)
                placeholder = st.empty()
                full_text = ""
                for item in result:
                    full_text += item
                    placeholder.markdown(full_text)
                placeholder.write(full_text)
                st.session_state.messages.append({"role": "assistant", "content": full_text})
