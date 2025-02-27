#agents.py
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from crewai_tools import SerperDevTool




class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

        self.search_tool = SerperDevTool(n_results=3)

    def search_agent(self):
        return Agent(
            role="Business Intelligence Researcher",
            backstory="An expert in analyzing market trends and business insights using Google Search.",
            goal="Gather high-quality business intelligence from Google search results.",
            tools=[self.search_tool],
            llm=self.OpenAIGPT35,
            verbose=True,
        )

    def research_agent(self):
        return Agent(
            role="Business Analyst",
            backstory="Analyzes gathered market and industry information to form a comprehensive business overview.",
            goal="Process the search results and synthesize insights about the industry landscape.",
            llm=self.OpenAIGPT35,
        )

    # Crew 2: Evaluation Crew
    #N-shot prompt engineering
    def economic_agent(self):
        return Agent(
            role="Financial Economist",
            backstory="Specialist in Cost-Benefit Analysis (CBA) to assess the financial viability of business ideas. This is the only concept you know of.",
            goal="Evaluate the financial risks and benefits of the proposed business.",
            llm=self.OpenAIGPT35,
            examples=[
                {
                    "input": "Business Idea: A subscription-based AI legal assistant. Company Vision: To democratize legal assistance by making AI-driven legal guidance accessible to startups. Budget: $200,000",
                    "output": "Costs: Manufacturing Costs – Using sustainable materials (e.g., biodegradable plastics, recycled materials) increases production costs, potentially impacting profit margins. Estimated initial setup and material sourcing could take a significant portion of the $10M budget. Research & Development (R&D) – Designing durable, eco-friendly blocks that maintain quality and safety standards requires investment in material testing and innovation. Marketing & Consumer Education – Raising awareness about the benefits of eco-friendly toys will require targeted marketing efforts, increasing branding and outreach expenses. Supply Chain & Logistics – Sourcing sustainable materials and ensuring eco-friendly packaging could result in higher operational costs. Benefits: Market Demand & Growth Potential – The growing eco-conscious consumer base provides a strong opportunity for high sales and brand loyalty. Competitive Advantage – Entering the market early with a high-quality sustainable toy can differentiate the brand and establish credibility. Long-Term Cost Savings - As sustainable materials become more widely available, production costs may decrease, improving profitability. Brand Loyalty & Positive Reputation – Aligning with environmental values enhances brand image, increasing customer retention and trust. Conclusion: Despite higher initial costs, the market's shift toward eco-friendly toys offers strong revenue potential and brand-building opportunities. If executed strategically—balancing sustainability with affordability—the company can secure a solid position in this growing market while fostering creativity in children."
                }
        ]
        )

    def strategic_agent(self):
        return Agent(
            role="Strategy Consultant",
            backstory="Expert in Ansoff’s Growth Strategies, focusing on market and product expansion potential. This is the only concept you know of.",
            goal="Assess potential growth opportunities and risks of the business idea.",
            llm=self.OpenAIGPT35,
        )

    def marketing_agent(self):
        return Agent(
            role="Marketing Strategist",
            backstory="Expert in Value Proposition Canvas (VPC), evaluating customer needs and market fit. This is the only concept you know of.",
            goal="Analyze the business idea from a customer value perspective.",
            llm=self.OpenAIGPT35,
        )
    
    def summarization_agent(self):
        return Agent(
            role="Business Evaluation Summarizer",
            backstory="An expert business analyst responsible for consolidating financial, strategic, and marketing evaluations into a detailed final report.",
            goal="Summarize all findings into a long, structured response, considering economic, strategic, and marketing perspectives.",
            llm=self.OpenAIGPT35,
        )

