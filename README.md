## ChatGPT for your own contents
this example is based on below tutorial:  
https://blog.langchain.dev/tutorial-chatgpt-over-your-data/

![flow](flow.png)
source: https://bdtechtalks.com/2023/05/01/customize-chatgpt-llm-embeddings/
## How to run
- install requirements.txt
- run command `shiny run app.py`
- open a browser and check http://localhost:8000

## Use Docker container
- docker run -e "OPENAI_API_KEY=XXX" -p 8000:8000 mewu/idmgpt:latest
- open a browser and check http://localhost:8000

## Note
Langchain is developing fast so please refer to their documentation site to check latest updates:
https://python.langchain.com/docs/use_cases/question_answering/
![example](example.png)
