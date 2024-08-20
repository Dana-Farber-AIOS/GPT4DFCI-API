import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

# Completion example, pick a model
# model = "gpt-4-turbo-0125-api" # this is GPT-4 Turbo 0125-preview
# model = "gpt-4o-mini-2024-07-18-api" # this is GPT-4o mini
model = "gpt-4o-2024-05-13-api" # this is GPT-4o 2024-05-13
api_version = "2023-05-15"

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
entra_scope = os.getenv("AZURE_OPENAI_ENTRA_SCOPE")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), 
    entra_scope
)

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role":"system","content":"You are an AI with super-human data extraction and summarization abilities."},
        {"role":"user","content":"Hello! Who are you and what can you do for me?"}
    ]
)

print(response)

# Embedding example, pick a model
# emodel = "text-embedding-3-small-1-api" # this is Azure OpenAI embedding small v1
embedding_model = "text-embedding-3-large-1-api" # this is the Azure OpenAI flagship embedding (large) v1 
api_version = "2023-05-15"

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
entra_scope = os.getenv("AZURE_OPENAI_ENTRA_SCOPE")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), 
    entra_scope
)

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
)

response = client.embeddings.create(
    model=embedding_model,
    input = "Hello, world!"
)

print(response.model_dump_json(indent=2))


