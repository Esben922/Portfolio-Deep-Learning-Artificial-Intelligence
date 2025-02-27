#tasks.py
from crewai import Task
from textwrap import dedent

class CustomTasks:
    def search_task(self, agent, business_details):
        return Task(
            description=dedent(f"""
                You are a **Business Intelligence Researcher**. Your job is to research the following business idea:

                1. **Business Details**:
                {business_details}

                2. Extract **only relevant** industry insights:
                - Key **market trends** and industry growth projections.
                - Analysis of **competitor strategies** and pricing.
                - Identification of **customer preferences & demand drivers**.
                - Breakdown of **financial risks & opportunities**.

                3. Compile a **structured research report**.

                **Deliverable**:
                - A structured business intelligence report **summarizing** key findings.
            """),
            expected_output="A well-researched market report summarizing trends, competition, risks, and customer demand.",
            agent=agent,
        )

    #Focus on Self-Consistency
    def research_task(self, agent):
        return Task(
            description=dedent("""
                1. Review the search results for **completeness**.
                2. Identify **missing insights** (e.g., competitor strategies, costs, customer profile).
                3. Filter out **irrelevant** results (e.g., unrelated finance, recycling topics).
                4. Deliver a **structured summary** in the following format:

                **Strategic insight:**
                - [Summary of Strategically relevant information on strategy and competitors]

                **Cost insight:**
                - [Relevant information in relation to cost management]

                **Marketing insight:**
                - [Key insights on customer demand]

                **Financial & Strategic Risks:**
                - [Breakdown of risks and opportunities]

                **Deliverable:**
                - A **well-structured report** that will be used by cost, marketing and strategic analysts.
            """),
            expected_output="A structured industry report summarizing trends, competition, risks, and demand.",
            agent=agent,
        )

    def economic_analysis_task(self, agent, research_summary):
        return Task(
            description=dedent(f"""
                Perform a Cost-Benefit Analysis (CBA) of the business.
                Consider insights from the case:
                Business Case:{research_summary}

                Evaluate how the budget aligns with potential costs and revenue projections.
                Identify financial risks and opportunities.

                Your response MUST follow the outlined structure precisely. Do NOT add extra information.
            """),
            expected_output="A financial evaluation of the business idea based on CBA.",
            agent=agent,
        )
    #Chain of thoughts (COT)
    def strategic_analysis_task(self, agent, research_summary):
        return Task(
            description=dedent(f"""
                ### **Strategic Evaluation Using Ansoff’s Growth Matrix**
                
                You are the **Strategic Agent**, responsible for evaluating business ideas using **Ansoff’s Growth Strategies**. 
                Your task is to analyze potential strategies and recommend the most suitable growth approach based on structured reasoning.

                #### **Step-by-Step Reasoning:**
                
                - **Step 1: Understand the Business Idea**  
                - What is the core product/service?  
                - What is the target market?  
                - What problem does it solve?  
                
                - **Step 2: Identify the Current Position**  
                - Is the company introducing a new product or improving an existing one?  
                - Is the company targeting an existing market or expanding into a new one?  
                
                - **Step 3: Apply Ansoff's Growth Strategies**  
                - **Market Penetration:**  
                    - Can the business grow by increasing market share within its existing market?  
                    - Are there opportunities to acquire competitors or improve marketing efforts?  
                    - Can pricing, promotions, or distribution be optimized?  

                - **Market Development:**  
                    - Can the business expand into new geographic regions or customer segments?  
                    - Are there untapped international markets or adjacent industries?  
                    - What are the risks of entering a new market?  

                - **Product Development:**  
                    - Can the business create new products for its current customers?  
                    - Is there an opportunity for innovation or adding new features?  
                    - What resources are required for R&D and production?  

                - **Diversification:**  
                    - Should the company enter a completely new market with a new product?  
                    - Is the risk justified by potential rewards?  
                    - Are there synergies with the existing business, or is this a radical shift?  

                - **Step 4: Risk Assessment & Feasibility**  
                - What are the risks associated with each strategy?  
                - What financial, operational, or market constraints exist?  
                - How does the business’s current capabilities align with the chosen strategy?  

                - **Step 5: Recommend the Best Strategy**  
                - Which Ansoff strategy is the most viable?  
                - Justify your choice based on market trends, competitive positioning, and company strengths.  
                - Provide actionable next steps.  
                
                Business Case:{research_summary}

                Your response MUST follow the outlined structure precisely. Do NOT add extra information.

            """),
            expected_output="A strategic growth assessment of the business idea.",
            agent=agent,
        )
    #CHain of thoughts (COT)
    def marketing_analysis_task(self, agent, research_summary):
        return Task(
            description=dedent(f"""
                ### **Value Proposition Canvas (VPC)**
                    
                    You are a marketing consultant responsible for evaluating business ideas using the **Value Proposition Canvas**.
                    Your task is to assess how well the business idea aligns with customer needs and expectations through structured reasoning.

                    #### **Step-by-Step Reasoning:**
                    
                    - **Step 1: Understand the Business Idea**
                    - What is the core product/service?
                    - Who is the target customer?
                    - What key problem does the product/service solve?

                    - **Step 2: Define the Customer Profile**
                    - **Customer Jobs:**  
                        - What tasks, problems, or needs does the customer have?  
                        - Are these functional, social, or emotional needs?  
                    - **Pains:**  
                        - What frustrations, obstacles, or risks do customers face?  
                        - What prevents them from achieving their goals?  
                    - **Gains:**  
                        - What positive outcomes or benefits do customers desire?  
                        - What would exceed their expectations?

                    - **Step 3: Define the Value Proposition**
                    - **Products & Services:**  
                        - What does the business offer?  
                        - How does it address customer needs?  
                    - **Pain Relievers:**  
                        - How does the product/service eliminate or reduce customer pains?  
                        - Does it remove inefficiencies, reduce risks, or improve experiences?  
                    - **Gain Creators:**  
                        - How does the product/service create extra value for the customer?  
                        - Does it offer unique benefits or exceed expectations?

                    - **Step 4: Assess Fit Between Customer Needs & Value Proposition**
                    - Does the offering effectively solve key customer jobs?  
                    - Are pain relievers strong enough to address customer frustrations?  
                    - Do gain creators align with what customers truly value?  
                    - Are there gaps between what is offered and what is needed?

                    - **Step 5: Recommend Improvements & Business Strategy**
                    - Does the value proposition need refinement?  
                    - Can additional features or services strengthen the fit?  
                    - Should the business focus on specific customer segments?  
                    - Provide actionable next steps for improving the value proposition.

                    Business Case:{research_summary}

                    Your response MUST follow the outlined structure precisely. Do NOT add extra information.

            """),
            expected_output="A marketing analysis detailing customer value and market fit.",
            agent=agent,
        )
    def summarization_task(self, agent, economic_output, strategic_output, marketing_output):
        return Task(
            description=dedent(f"""
                Summarize the complete business evaluation by integrating all available insights.
                
                - Economic Analysis: {economic_output}
                - Marketing Analysis: {marketing_output}
                - Strategic Analysis: {strategic_output}

                Produce a **structured and detailed final evaluation**, ensuring all perspectives are considered.
                Cover **strengths, weaknesses, threats, and opportunities** (SWOT-analysis) based on the collected insights.
            """),
            expected_output="A comprehensive, multi-perspective final business evaluation.",
            agent=agent,
        )
