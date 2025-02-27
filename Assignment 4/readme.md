# AI Business Consultant

We want to create an agentic system which provides management with an objective evaluation of a potential business idea. The model will be based on the premise of it being either an existing company, or at the very least a company with a thought-out business plan. This application will add value in the evaluation of potential business ideas by gathering external information in the realm of the proposed business idea. The Agentic system is based on OpenAI’s Large Language Models, particularly their 3.5 Turbo model.

The product is also based on the functions of CrewAI and their approach to multi-agent systems. The overall setup consists of **two crews**:

## Crew 1: Research Crew

- **Search Agent**: Uses a search tool (DuckDuckGo) to gather relevant information.
- **Research Agent**: Uses its own knowledge and the information gathered by the Search Agent to collect as much relevant information as possible based on the user’s provided business idea.

## Crew 2: Evaluation Crew

This crew discusses the viability of the potential business idea based on the user-provided strategy. The discussion is framed using specific fields and highlighted theories:

### Roles in Crew 2:

- **Economical Agent**  
  - Based on **Cost-Benefit Analysis (CBA)**.  
  - Evaluates potential gains and losses and values them relative to each other.

- **Strategic Agent**  
  - Based on **Ansoff's Growth Strategies**.  
  - Analyzes potential growth opportunities by evaluating **market penetration, product development, market development, and diversification**.

- **Marketing Agent**  
  - Uses the **Value Proposition Canvas (VPC)**.  
  - Analyzes customer needs by examining **pains, jobs, and gains**, ensuring customer alignment.

---

## Finetuning Implementation

- **RAG (Retrieval-Augmented Generation)**:  
  Enhances AI responses by fetching relevant external information before generating answers. Implemented by **Agent 1 in Crew 1**.

- **Self-Consistency**:  
  Improves reasoning by generating multiple independent solutions to the same problem and selecting the most common answer. Used in **Task 2 of Crew 1**.

- **N-Shot Prompting**:  
  Provides multiple examples of the desired input-output format before asking the AI to solve a new problem. Implemented by **Agent 1 in Crew 2**.

- **Chain of Thought (C2-Task 2 & C2-Task 3)**:  
  Encourages AI to break down complex reasoning into explicit intermediate steps, improving accuracy in multi-step logic tasks.

---

## Deployment

The repository includes a **prototype deployment** linking backend and frontend through **FastAPI**. The prototype is launched in **Streamlit**, which consists of:

- A **user input terminal**
- The **output from the agentic system**

---

## How to Use the Artificial Business Consultant Agent

To run the application, ensure you have:

- **An OpenAI API key**
- **A Serper API key** (stored in your environment variables)

> **Note:** Running the code **will incur costs** due to OpenAI API usage, but these costs are minimal.

---

## Business Strategy Frameworks Used

This advisor utilizes **Cost-Benefit Analysis (CBA)**, **Ansoff’s Matrix**, and the **Value Proposition Canvas (VPC)** to ensure strategic alignment.

- **CBA** evaluates financial feasibility.
- **Ansoff’s Matrix** identifies growth opportunities.
- **VPC** ensures customer-centric value creation.

These tools support **informed decision-making** and **risk management**, balancing growth and sustainability.

---

## Frameworks Explained

### Cost-Benefit Analysis (CBA)
CBA evaluates the financial feasibility of a project or strategy by identifying and quantifying all costs and benefits. 

- **Costs**: Direct expenses, opportunity costs, and potential risks.  
- **Benefits**: Increased revenue, cost savings, or intangible gains like customer satisfaction.  

Each cost and benefit is assigned a monetary value where possible. If **benefits outweigh costs**, the decision is considered viable.  
CBA supports **data-driven decision-making** and **resource allocation**.

---

### Ansoff’s Matrix
A strategic tool that identifies growth opportunities through **four strategies**:

1. **Market Penetration**: Increasing sales of existing products in existing markets.
2. **Market Development**: Expanding into new markets with existing products.
3. **Product Development**: Creating new products for existing markets.
4. **Diversification**: Introducing new products into new markets (**highest risk**).

This framework helps assess **risk levels** and select the best approach for business expansion.

---

### Value Proposition Canvas (VPC)
A strategy tool aligning **products or services** with **customer needs**.

- **Customer Profile**:
  - **Jobs** (tasks customers need to accomplish)
  - **Pains** (challenges customers face)
  - **Gains** (desired benefits)

- **Value Map**:
  - **Pain Relievers** (solutions to challenges)
  - **Gain Creators** (added benefits)

Matching the **Value Map** to the **Customer Profile** ensures the product delivers **real value**.  
VPC is widely used for **product development, marketing, and business strategy**.

---

By combining **CBA, Ansoff’s Matrix, and VPC**, businesses can create a well-balanced, sustainable, and customer-centric strategy.
