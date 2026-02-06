from google import genai
from google.genai import types

client = genai.Client(api_key="")


def gemini_ai(command_ask):
    print("Looking for Gemini AI response .....")
    model_id = "gemini-3-flash-preview"
    config_value = types.GenerateContentConfig(
        system_instruction="You are a concise assistant. Your responses must be exactly 5 sentences long. No more, no less.",
        max_output_tokens=300
    )
    response = client.models.generate_content(
        model=model_id,
        contents=command_ask,
        config=config_value
    )
    return str(response.text)
