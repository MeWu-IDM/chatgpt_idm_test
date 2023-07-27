import os
import pickle
from shiny import App, ui, render, reactive
from query import ask_db
from pathlib import Path

# Part 1: ui ----
app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", href="styles.css")
    ),
    ui.panel_title(title=ui.div(ui.img(src="logo_IDM.jpg", width="20%"), ui.h2("ChatGPT For IDM"))),
    ui.layout_sidebar(
        ui.panel_sidebar(
            # ui.img(src="logo_IDM.jpg", width="30%"),
            ui.input_text_area("question", "What do you want to ask?"),
            ui.input_slider("temperature", "Temperature", min=0, max=1, step=0.1, value=0.5),
            ui.input_password("openai_api_key", "OPENAI API KEY"),
            ui.input_action_button("submit", "Submit"),
        ),
        ui.panel_main(
            ui.output_text_verbatim("answer", placeholder=True)
        ),
    ),

)


# Part 2: server ----
def server(input, output, session):
    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    result = reactive.Value({"answer": "", "sources": ""})

    @reactive.Effect
    @reactive.event(input.submit)
    def ask():
        print("asking...")
        question = input.question()
        temperature = input.temperature()
        print(question)
        if question != "":
            if 'OPENAI_API_KEY' not in os.environ:
                if input.openai_api_key() == "":
                    result.set({"answer": "Please enter your OpenAI API key", "sources": ""})
                    return
                os.environ['OPENAI_API_KEY'] = input.openai_api_key()
            result.set(ask_db(store, question, temperature))

    @output
    @render.text
    def answer():
        answers = result()['result'].replace('. ', '.\n').replace(', ', '.\n').replace('!', '!\n')
        sources = "\n".join([r.metadata['source'] for r in result()['source_documents']])
        return f"Answers:\n {answers} \n\nSources:\n {sources}"


# Combine into a shiny app.
# Note that the variable must be "app".
www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
