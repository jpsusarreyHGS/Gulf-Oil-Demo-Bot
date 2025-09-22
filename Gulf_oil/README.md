# ⛽ Gulf Oil Assistant: Intelligent Lubricant Recommender

An AI-powered web application that provides intelligent lubricant recommendations based on vehicle images and specifications. This demo showcases how Gulf Oil's products can be matched to specific vehicle requirements using **computer vision** and **natural language processing**.

!

---

## ✨ Features

* **Vehicle Image Analysis**: Upload images of vehicles to automatically identify type, brand, and model.
* **Intelligent Recommendations**: Get tailored Gulf Oil product suggestions based on vehicle specifications.
* **Interactive Chat Interface**: Natural conversation with the AI assistant.
* **Markdown Support**: Formatted responses with product details and specifications.
* **Responsive Design**: Works seamlessly on desktop and mobile devices.

---

## 💡 Demo Highlights

This demonstration showcases:

* **Computer Vision Integration**: The system can analyze vehicle images to extract make, model, and specifications.
* **Product Matching Engine**: An intelligent algorithm that matches Gulf Oil products to vehicle requirements.
* **Natural Language Interface**: A conversational AI that understands user queries about oil products.
* **Technical Specification Compliance**: Recommendations include viscosity grades, compliance standards, and application-specific benefits.

---

## 🛠️ Technical Stack

* **Backend**: FastAPI with Python
* **AI Model**: Azure OpenAI GPT-4o-mini with vision capabilities
* **Frontend**: HTML, CSS, JavaScript with responsive design
* **Templating**: Jinja2 templates
* **Deployment**: Vercel-ready configuration

---

## 🚀 Setup Instructions

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up environment variables**:
    Create a `.env` file or set the following variables in your environment:
    ```bash
    AZURE_OPENAI_ENDPOINT=your_azure_endpoint
    AZURE_OPENAI_API_KEY=your_azure_api_key
    ```

3.  **Run the application**:
    ```bash
    uvicorn backend:app --reload
    ```

4.  **Open your browser**:
    Navigate to `http://localhost:8000` to access the application.

---

## 📝 Usage

1.  Upload an image of a vehicle (motorcycle, car, truck, etc.).
2.  The AI will analyze the image and confirm vehicle details.
3.  Receive a tailored Gulf Oil product recommendation.
4.  Ask follow-up questions about products, specifications, or applications.

---

## 📂 Project Structure

```text
├── backend.py          # FastAPI server with AI integration
├── chat.html          # Frontend chat interface
├── prompt.py          # System prompts for the AI assistant
├── requirements.txt   # Python dependencies
├── vercel.json        # Deployment configuration
└── static/
    └── templates/
        ├── chat.html  # HTML template
        └── Logo.png   # Gulf Oil branding
```

Note: This is a demonstration application showcasing AI capabilities for product recommendation in the petroleum industry. Recommendations are based on simulated data and should not be considered professional advice for actual vehicle maintenance.
