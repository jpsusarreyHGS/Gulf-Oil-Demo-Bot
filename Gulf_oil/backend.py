import os
from fastapi import FastAPI, File, Form, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import base64
from prompt import SYSTEM_PROMPT

load_dotenv()
app = FastAPI()

# Mount static files directory (for CSS, JS, images if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="static/templates")

azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
api_key = os.environ["AZURE_OPENAI_API_KEY"]
api_version = "2024-08-01-preview"
deployment_name = "gpt-4o-mini" 

# Initialize LLM
llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version,
    azure_deployment=deployment_name,
    temperature=0.3,
    max_tokens=1024,
)

# Memory setup
memory = ConversationBufferMemory(return_messages=True)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serve the chat interface HTML page
    """
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat")
async def chat(
    text: str = Form(...),
    image: UploadFile = File(None)
):
    """
    Chat endpoint that accepts text + optional image and generates a response using Azure OpenAI
    with memory support.
    """
    try:
        # Start with system prompt
        messages = [SystemMessage(content=SYSTEM_PROMPT)]

        # Add previous conversation history
        messages.extend(memory.chat_memory.messages)

        # Prepare new user input
        message_content = [{"type": "text", "text": text}]
        if image:
            image_bytes = await image.read()
            image_b64 = base64.b64encode(image_bytes).decode("utf-8")
            message_content.append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{image.filename.split('.')[-1]};base64,{image_b64}"
                    }
                }
            )

        # Append new message
        human_message = HumanMessage(content=message_content)
        messages.append(human_message)

        # Get response
        response = await llm.ainvoke(messages)

        # Save to memory
        memory.chat_memory.add_message(human_message)
        memory.chat_memory.add_message(response)

        return JSONResponse(content={"response": response.content})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
