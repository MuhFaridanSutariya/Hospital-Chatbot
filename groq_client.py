from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

def call_groq_llm(prompt, model="llama3-8b-8192"):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model
    )
    return chat_completion.choices[0].message.content
