# Assistente Conversacional PandasAI

## Sobre o Projeto.

Este projeto tem o objetivo de recriar um assistente conversacional que analisa planilhas e possui a capacidade de responder questões especificas sobre os dados e gerar gráficos.

![Aplicação](https://github.com/MoisesArruda/PandasAI/blob/main/images/aplica%C3%A7%C3%A3o.png)

![Gráfico](https://github.com/MoisesArruda/PandasAI/blob/main/images/Gr%C3%A1fico.png)

# Instalação

1. Clone o repositório:

```bash
git clone https://github.com/MoisesArruda/PandasAI
```

2. Mude para o diretório do projeto:
 ```bash
cd PandasAI
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

4. Obtenha sua Azure OpenAI API key.

5. Crie um arquivo .env, copie e altere as seguintes chaves no seu arquivo:
```bash
OPENAI_API_KEY= "YOUR_OPENAI_API_KEY"
OPENAI_API_BASE= "YOUR_OPENAI_API_BASE"
OPENAI_API_TYPE= "azure"
OPENAI_API_VERSION= "YOUR_OPENAI_API_TYPE"
DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
EMBEDDING_DEPLOYMENT_NAME="YOUR_EMBEDDING_DEPLOYMENT_NAME"
```

6. Rode sua aplicação Streamlit:
```bash
 streamlit run app/frontEnd.py
```

7. Abra seu navegador de preferência e vá até http://localhost:8501 para acessar a aplicação.


# Como utilizar

1. A planilha será carregada.
3. Faça uma pergunta sobre a planilha na caixa de texto.
4. O agente conversacional de IA irá gerar uma resposta ccom base na pergunta e na imagem.
5. A resposta irá aparecer.

# Tecnologias

Este projeto utiliza o OpenAI GPT-3.5 Turbo model. Visite [OpenAI](https://openai.com/) para mais informações.

A interface interativa é desenvolvida com a biblioteca Streamlit. Consulte a [documentação do Streamlit](https://docs.streamlit.io/) para mais detalhes.

O agente de IA conversacional e as ferramentas são gerenciados pela biblioteca LangChain. Confira o [repositório do LangChain no Github](https://github.com/langchain-ai/langchain) para obter mais informações.

A biblioteca PandasAI é empregada para inferir recursos de IA. Visite [PandasAI](https://docs.pandas-ai.com/en/latest/) para obter descrições detalhadas.

