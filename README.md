# Multi-Agent Task Automation System

An intelligent multi-agent AI system that automates complex user tasks by decomposing them into smaller executable steps. The platform uses a Planner-Executor architecture where specialized agents collaborate to solve user requests efficiently while handling failures, retries and external API interactions.

---

## Overview

This project demonstrates how autonomous AI agents can work together to complete real-world tasks instead of relying on a single LLM response.

A Planner Agent understands the user's objective, breaks it into multiple subtasks and delegates them to specialized Executor Agents. Each agent performs its assigned task, retrieves external information if required and returns structured outputs. The planner combines these responses into a final answer.

---

## Features

- Multi-Agent Architecture
- Planner-Executor Workflow
- Task Decomposition
- External API Integration
- Retry Mechanism
- Error Handling
- Structured Outputs
- Modular Agent Design
- REST API Support
- Easily Extensible

---

## Architecture

```
                User Request
                      │
                      ▼
             Planner Agent
                      │
     ┌────────────────┼─────────────────┐
     │                │                 │
     ▼                ▼                 ▼
Weather Agent    Search Agent     Budget Agent
     │                │                 │
     └────────────────┼─────────────────┘
                      ▼
              Planner Aggregates
                      ▼
               Final Response
```

---

## Tech Stack

### Backend

- Python
- FastAPI

### AI Framework

- LangChain
- LangGraph

### LLM

- OpenAI GPT Models

### APIs

- Weather API
- Search APIs
- REST APIs

### Utilities

- Requests
- Pydantic
- Uvicorn

---

## Project Structure

```
multi-agent-task-automation/
│
├── agents/
│   ├── planner.py
│   ├── weather_agent.py
│   ├── search_agent.py
│   ├── budget_agent.py
│
├── tools/
│   ├── weather_tool.py
│   ├── search_tool.py
│
├── workflows/
│   ├── graph.py
│
├── api/
│   ├── routes.py
│
├── utils/
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

## Workflow

1. User submits a request.
2. Planner Agent analyzes the objective.
3. Planner creates multiple subtasks.
4. Executor Agents process their assigned tasks.
5. APIs are called when external information is required.
6. Failed tasks are retried automatically.
7. Planner combines all outputs.
8. Final response is returned.

---

## Example

### User Input

```
Plan a one-day trip to Hyderabad under ₹5000 and tell me the weather.
```

### Planner Tasks

- Get weather forecast
- Estimate travel cost
- Recommend places
- Calculate total budget

### Final Output

```
Weather: Sunny

Places:
- Charminar
- Golconda Fort
- Hussain Sagar

Estimated Budget:
₹4300

Suggested Itinerary:
9:00 AM - Charminar
12:00 PM - Lunch
2:00 PM - Golconda Fort
6:00 PM - Hussain Sagar
```

---

## Error Handling

The system supports:

- Automatic retries
- Timeout handling
- API failure recovery
- Invalid input validation
- Graceful fallbacks

---

## Future Improvements

- Memory-enabled agents
- Vector Database Integration
- RAG Support
- Human-in-the-loop Approval
- Multi-modal Agents
- Agent Observability
- Token Usage Dashboard
- Evaluation Pipelines
- Multi-LLM Support
- Docker Deployment

---

## Learning Outcomes

This project demonstrates practical knowledge of:

- Multi-Agent AI Systems
- Agent Orchestration
- LangGraph Workflows
- Prompt Engineering
- Function Calling
- Tool Integration
- API Orchestration
- Workflow Automation
- Error Recovery
- Modular System Design

---

## Author

**Teja Balaji Chejarla**

GitHub: https://github.com/Tejabalaji29

LinkedIn: https://www.linkedin.com/in/tejabalaji-chejarla-16501628b/

---

## License

This project is developed for educational and portfolio purposes.
