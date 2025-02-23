# Stock Analysis and Investment Insights Using AI

This application is an AI-powered financial assistant that provides **real-time stock data**, **sentiment analysis of news articles**, and **investment insights**. Leveraging **LangChain** and **Google’s Gemini 2.0 model**, the system fetches stock market data via **Yahoo Finance**, analyzes financial news using **SerpAPI**, and evaluates sentiment with **TextBlob**.

The AI agent delivers **up-to-date market trends**, helping users make informed investment decisions by summarizing news, assessing stock movements, and offering strategic insights.

## Technology Stack

This project integrates multiple tools to provide a structured AI-powered pipeline for real-time stock analysis, sentiment assessment, and investment recommendations:

- **LangChain** – AI-powered automation  
- **Google Gemini AI** – Large language model for analysis  
- **Yahoo Finance API (yfinance)** – Real-time stock market data  
- **SerpAPI** – Web search for financial news  
- **TextBlob** – Sentiment analysis  

---

## Team Members

This project was developed collaboratively by Esben Münster Graahede, Frederik Emil Lauritzen & Mathias Salomonsen Juul, with each member contributing to coding, testing, and documentation. The work was conducted as a joint effort, with no specific sections being solely attributed to one person.

---

## Notebook Structure

The notebook is divided into six key sections:

1. **Installing Dependencies**  
2. **Importing Required Libraries**  
3. **Setting Up API Keys**  
4. **Defining AI-powered Analysis Tools**  
5. **Building the LangChain Agent**  
6. **Executing the Analysis and Presenting Insights**

---

## 1. Installing Dependencies

To ensure smooth execution, we install essential libraries such as:

- `yfinance` for stock market data  
- `textblob` for sentiment analysis  
- `langchain` for AI-powered automation  
- `google-generativeai` for using Google's Gemini AI Model  
- `SerpAPI` for Google News Search  

---

## 2. Importing Required Libraries

The project requires:

- `yfinance` to retrieve real-time stock prices  
- `LangChain` components for AI integration  
- `TextBlob` for sentiment analysis  
- `SerpAPIWrapper` to fetch financial news  

---

## 3. Setting Up API Keys

The system retrieves API keys securely using Colab secrets, ensuring safe authentication for:

- **Google Gemini AI**  
- **SerpAPI for web search**  

---

## 4. Defining AI-powered Analysis Tools

The project defines multiple AI-powered tools to analyze stock performance:

- **News Retrieval Tool**  
  - Fetches the latest financial news about a stock using Google Search API.  

- **Stock Data Fetcher**  
  - Retrieves real-time stock market data (e.g., price, market cap, highs/lows) using `yfinance`.  

- **Sentiment Analysis Tool**  
  - Uses `TextBlob` to determine whether news sentiment is **Positive**, **Negative**, or **Neutral** based on textual analysis.  

- **Investment Advice Tool**  
  - Provides basic investment insights based on stock performance trends.  

---

## 5. Building the LangChain AI Agent

The AI agent is initialized with four analytical tools, allowing it to:

- Fetch stock news  
- Analyze stock performance  
- Determine sentiment trends  
- Provide investment insights  

The agent operates in a **zero-shot reasoning mode**, meaning it dynamically decides which tool to use based on the user's request.

---

## 6. Running the AI Agent

Finally, we invoke the agent with the prompt:

"Summarize today's latest news on Apple stock and analyze sentiment. Provide investment insights."


The agent:

- Fetches real-time news on **Apple Inc.**  
- Analyzes sentiment to determine market mood  
- Provides stock trend analysis  
- Generates investment insights  

---

## Conclusion

This project successfully integrates **AI-driven financial analysis**, providing a fully automated stock intelligence system. While the current implementation offers valuable insights, future improvements could include:

- **Advanced deep learning for trend forecasting**  
- **Integration of more financial indicators**  
- **User-customizable investment strategies**  

This project highlights the **power of AI in financial decision-making**, automating real-time analysis for smarter investments.

