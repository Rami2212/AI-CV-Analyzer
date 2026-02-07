# AI CV Analyzer

A Streamlit-based web application that analyzes CVs using AI to provide actionable insights and recommendations for job applications.

## Features

- **Multi-format Support**: Upload CVs in PDF or TXT format
- **Role-specific Analysis**: Get tailored feedback for specific job roles
- **Comprehensive Evaluation**: Analyzes content clarity, skills presentation, experience description, and more
- **Fast Processing**: Quick AI-powered analysis with clear, actionable feedback

## Prerequisites

- Python 3.8 or higher
- OpenAI API credentials (or compatible API)

## Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd ai-cv-analyzer
```

2. **Install required packages**
```bash
pip install streamlit openai PyPDF2 python-dotenv
```

3. **Set up environment variables**

Create a `.env` file in the project root directory:
```env
AICC_API_KEY=your_api_key_here
AICC_BASE_URL=your_api_base_url_here
```

## Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Access the web interface**
   - The application will open in your default browser
   - Default URL: `http://localhost:8501`

3. **Analyze your CV**
   - Upload your CV (PDF or TXT format)
   - Optionally enter the job role you're applying for
   - Click "Analyze CV" to get insights

## Analysis Features

The AI analyzer evaluates your CV across four key dimensions:

1. **Content Clarity and Aspects**: Overall structure and readability
2. **Skills Presentation**: How effectively your skills are showcased
3. **Experience Description**: Quality and impact of work experience descriptions
4. **Role-specific Improvements**: Tailored recommendations for your target role

## Project Structure
```
ai-cv-analyzer/
├── app.py              
├── .env                
└── README.md          
```