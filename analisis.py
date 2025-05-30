import openai

def analizar_ventas(api_key, texto_ventas):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sos un analista de datos de ventas."},
            {"role": "user", "content": f"Analizá estas ventas: {texto_ventas}"}
        ]
    )
    return response.choices[0].message.content