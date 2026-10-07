from g4f.client import Client

# Display model name -> g4f model id.
# The provider is selected automatically by g4f (AnyProvider) for every model,
# so no provider mapping is needed anymore.
display_model_mapping = {
    'GPT-4o mini': 'gpt-4o-mini',
    'GPT-4o': 'gpt-4o',
    'Llama 3.3 70B': 'llama-3.3-70b',
    'Mixtral 8x7B': 'mixtral-8x7b',
    'Gemini 2.5 Flash': 'gemini-2.5-flash',
    'DeepSeek V3': 'deepseek-v3',
    'DeepSeek R1': 'deepseek-r1',
}


def get_model(display_model: str) -> str:
    """Get internal model name based on the display model name."""
    return display_model_mapping.get(display_model, '')


def get_provider(model: str):
    """Provider is chosen automatically by g4f for every model."""
    return None


def get_bot_response(prompt, internal_model, provider_name):
    client = Client()
    response = client.chat.completions.create(
        model=internal_model,
        messages=[{"role": "user", "content": prompt}],
        provider=provider_name,
    )
    return response.choices[0].message.content
