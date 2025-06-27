import os
import re
from typing import List, Dict
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = Groq(api_key=GROQ_API_KEY)

class UserInput(BaseModel):
    message: str
    role: str = "user"
    conversation_id: str

class Conversation:
    def __init__(self):
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": (
                "You are a helpful assistant that answers electric vehicle questions in a concise, plain-text format. "
                "Avoid markdown formatting like **bold** or lists with numbers and asterisks. "
                "Use clean plain-text bullet points (e.g., starting with •) to list items. Avoid dashes (-), numbers, or markdown formatting like **bold**. Each bullet point should be in a new line. "

            )}
        ]
        self.active: bool = True

conversations: Dict[str, Conversation] = {}

# Function to clean markdown and improve formatting
def clean_response(text: str) -> str:
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold
    text = re.sub(r'\s*\d+\.\s*', '• ', text)     # Replace numbered lists with bullet points
    #text = re.sub(r'\n{2,}', '\n', text)          # Collapse multiple newlines
    return text.strip()

def query_groq_api(conversation: Conversation) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation.messages,
            temperature=0.3,
            max_tokens=512,
            top_p=1,
            stream=True,
            stop=None,
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error with Groq API: {str(e)}")


def get_or_create_conversation(conversation_id: str) -> Conversation:
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]

@app.post("/chat/")
async def chat(input: UserInput):
    conversation = get_or_create_conversation(input.conversation_id)

    if not conversation.active:
        raise HTTPException(
            status_code=400, 
            detail="The chat session has ended. Please start a new session."
        )

    try:
        # Append the user's message to the conversation
        conversation.messages.append({
            "role": input.role,
            "content": input.message
        })

        response = query_groq_api(conversation)
        cleaned_response = clean_response(response)

        conversation.messages.append({
            "role": "assistant",
            "content": cleaned_response
        })

        return {
            "response": cleaned_response,
            "conversation_id": input.conversation_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
