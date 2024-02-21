import os
from dotenv import load_dotenv
from pandasai.llm.azure_openai import AzureOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import AzureChatOpenAI


load_dotenv()

class GPTConfig:

    """
    Classe para configurar os objetos do AzureChatOpenAI e OpenAIEmbeddings para serem utilizados.
    
    Attributes:
        openai_api_base (str): A URL base da API do OpenAI.
        openai_api_version (str): A versão da API do OpenAI.
        openai_api_key (str): A chave da API do OpenAI.
        openai_api_type (str): O tipo da API do OpenAI.
        deployment_name (str): O nome do deployment da API do OpenAI.
        temperature (float): O valor da temperatura para determinar o comportamento da resposta, por padrão é 0.0.
        chunk_size (int): O tamanho do chunk para o OpenAIEmbeddings.
    """
    def __init__(self):
        self.azure_endpoint = os.getenv("OPENAI_API_BASE")
        self.api_version = os.getenv("OPENAI_API_VERSION")
        self.api_token = os.getenv("OPENAI_API_KEY")
        self.openai_api_type = os.getenv("OPENAI_API_TYPE")
        self.deployment_name = os.getenv("DEPLOYMENT_NAME")
        self.temperature = 0.3

    def create_chat(self):
        """
        Configura os objetos do AzureChatOpenAI para serem utilizados.

        Returns:
            AzureChatOpenAI: O objeto de AzureChatOpenAi configurado.
        """
        return AzureOpenAI(
            azure_endpoint=self.azure_endpoint,
            api_version=self.api_version,
            api_token=self.api_token,
            openai_api_type=self.openai_api_type,
            deployment_name=self.deployment_name,
            temperature=self.temperature,
        )
    
    def create_embeddings(self,chunk_size=1):
        """
        Configura os objetos do OpenAIEmbeddings para serem utilizados.

        Returns:
            OpenAIEmbeddings: O objeto de OpenAIEmbeddings configurado.
        """
        return OpenAIEmbeddings(
            deployment=self.deployment,
            chunk_size=chunk_size
            )