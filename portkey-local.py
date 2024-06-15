from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
  api_key="<api key of open ai > ",
  # base_url="http://localhost:8787/v1",
  base_url=PORTKEY_GATEWAY_URL,
  default_headers=createHeaders(

    provider="openai",
    api_key="<api key of portkey>"
  )
)

chat_complete = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "What's a Fractal?"}],
)

print(chat_complete.choices[0].message.content)
