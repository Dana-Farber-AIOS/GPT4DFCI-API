import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

# Pick a model from this list: https://wiki.dfci.harvard.edu:8443/aodssud/gpt4dfci-api-437749411.html

# Completion example, pick a model
# model = "gpt-4-turbo-0125-api" # this is GPT-4 Turbo 0125-preview
# model = "gpt-4o-mini-2024-07-18-api" # this is GPT-4o mini v0718
# model = "gpt-4o-2024-05-13-api" # this is GPT-4o v2024-05-13
# model = "o1-mini-2024-09-12-api" # This is o1-mini v2024-09-12 
model = "o1-preview-2024-09-12-api" # This is o1-preview v2024-09-12
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


