import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="RAG Document Assistant",
    layout="centered"
)


st.title(" RAG Document Assistant")

st.write(
    "Upload a PDF and ask questions about its content."
)


if "document_processed" not in st.session_state:
    st.session_state.document_processed = False


uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)


if uploaded_file is not None:

    if st.button("Process document"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        try:

            with st.spinner("Processing document..."):

                response = requests.post(
                    f"{API_URL}/documents",
                    files=files
                )

            if response.status_code == 200:

                st.session_state.document_processed = True

                st.success(
                    "Document processed successfully."
                )

            else:

                st.session_state.document_processed = False

                st.error(
                    f"Error processing document: "
                    f"{response.text}"
                )

        except requests.exceptions.RequestException:

            st.error(
                "Could not connect to the RAG API. "
                "Make sure FastAPI is running."
            )


st.divider()


st.subheader("Ask a question")


question = st.text_input(
    "Question",
    placeholder="What is this document about?"
)


if st.button("Ask"):

    if not st.session_state.document_processed:

        st.warning(
            "Please upload and process a document first."
        )

    elif not question:

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner("Generating answer..."):

                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question,
                        "top_k": 3
                    }
                )

            if response.status_code == 200:

                result = response.json()

                st.subheader("Answer")

                st.write(result["answer"])

                st.subheader("Sources")

                for source in result["sources"]:

                    st.write(
                        f" **{source['source']}** — "
                        f"Page {source['page']} — "
                        f"Relevance: {source['score']:.4f}"
                    )

            else:

                st.error(
                    f"Error generating answer: "
                    f"{response.text}"
                )

        except requests.exceptions.RequestException:

            st.error(
                "Could not connect to the RAG API. "
                "Make sure FastAPI is running."
            )