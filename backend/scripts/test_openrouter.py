import truststore

truststore.inject_into_ssl()

import httpx
from app.core.config import settings


def main():
    if not settings.LLM_API_KEY:
        raise RuntimeError("LLM_API_KEY não configurada no .env")

    url = f"{settings.LLM_BASE_URL.rstrip('/')}/chat/completions"

    payload = {
        "model": settings.LLM_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um assistente educacional que "
                    "explica conceitos em português brasileiro."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Explique em uma frase simples para que "
                    "serve a Constituição Federal brasileira."
                ),
            },
        ],
        "max_tokens": 150,
        "temperature": 0.2,
    }

    headers = {
        "Authorization": f"Bearer {settings.LLM_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                url,
                headers=headers,
                json=payload,
            )

            response.raise_for_status()
            data = response.json()

        print("Conexão com OpenRouter realizada!")
        print("Modelo:", data.get("model", "não informado"))
        print("Resposta:")
        print(data["choices"][0]["message"]["content"])

    except httpx.HTTPStatusError as exc:
        print("Erro HTTP:", exc.response.status_code)
        print("Detalhes:", exc.response.text[:500])

    except (httpx.RequestError, KeyError, IndexError) as exc:
        print("Falha na requisição ou resposta:", exc)


if __name__ == "__main__":
    main()
