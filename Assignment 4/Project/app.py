#app.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from decouple import config
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = config("SERPER_API_KEY")

class BusinessIdeaRequest(BaseModel):
    business_idea: str
    company_vision: str
    budget: float

app = FastAPI(
    title="Business Idea Evaluation API",
    description="An agentic system for evaluating business ideas using Serper (Google Search API) and CrewAI.",
    version="1.1.0",
)

class BusinessEvaluationCrew:
    def __init__(self, business_idea, company_vision, budget):
        self.business_details = (
            f"Business Idea: {business_idea}\n"
            f"Company Vision: {company_vision}\n"
            f"Budget: ${budget:,.2f}"
        )

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        search_agent = agents.search_agent()
        search_task = tasks.search_task(search_agent, self.business_details)

        research_crew = Crew(
            agents=[search_agent],
            tasks=[search_task],
            verbose=True,
        )
        research_results = research_crew.kickoff()
        research_summary = str(research_results) 

        economic_agent = agents.economic_agent()
        strategic_agent = agents.strategic_agent()
        marketing_agent = agents.marketing_agent()

        economic_task = tasks.economic_analysis_task(economic_agent, research_summary)
        strategic_task = tasks.strategic_analysis_task(strategic_agent, research_summary)
        marketing_task = tasks.marketing_analysis_task(marketing_agent, research_summary)

        evaluation_crew = Crew(
            agents=[economic_agent, strategic_agent, marketing_agent],
            tasks=[economic_task, strategic_task, marketing_task],
            verbose=True,
        )

        evaluation_results = evaluation_crew.kickoff()

        economic_output = str(economic_task.output)
        strategic_output = str(strategic_task.output)
        marketing_output = str(marketing_task.output)

        summarization_agent = agents.summarization_agent()
        summarization_task = tasks.summarization_task(
            summarization_agent, economic_output, strategic_output, marketing_output
        )

        summarization_crew = Crew(
            agents=[summarization_agent],
            tasks=[summarization_task],
            verbose=True,
        )

        final_summary = summarization_crew.kickoff()

        return {
            "Research Results": research_summary, 
            "Economic Analysis": economic_output,
            "Strategic Analysis": strategic_output,
            "Marketing Analysis": marketing_output,
            "Final Evaluation": str(final_summary),
        }

@app.post("/evaluate_business")
async def evaluate_business(idea_request: BusinessIdeaRequest):
    try:
        evaluator = BusinessEvaluationCrew(
            idea_request.business_idea,
            idea_request.company_vision,
            idea_request.budget
        )
        result = evaluator.run()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
