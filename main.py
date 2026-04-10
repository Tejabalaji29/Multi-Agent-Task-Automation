#!/usr/bin/env python3
"""
Multi-Agent Task Automation - Main Entry Point
Orchestrates multiple agents to complete tasks autonomously.
"""

import os
import sys
from dotenv import load_dotenv
from agents import TaskAgent, AnalysisAgent, ExecutionAgent
from memory import Memory
from tools import register_tools

# Load environment variables
load_dotenv()

def main():
    """Main entry point for the multi-agent system."""

    # Initialize memory
    memory = Memory()

    # Register available tools
    tools = register_tools()

    # Initialize agents
    task_agent = TaskAgent(memory=memory, tools=tools)
    analysis_agent = AnalysisAgent(memory=memory, tools=tools)
    execution_agent = ExecutionAgent(memory=memory, tools=tools)

    # Example: Define and execute a task
    task = "Analyze the codebase and identify optimization opportunities"

    print(f"Starting task: {task}")
    print("=" * 60)

    # Task planning phase
    plan = task_agent.plan_task(task)
    print(f"\nPlan: {plan}")

    # Analysis phase
    analysis = analysis_agent.analyze(plan)
    print(f"\nAnalysis: {analysis}")

    # Execution phase
    result = execution_agent.execute(analysis)
    print(f"\nResult: {result}")

    print("=" * 60)
    print("Task completed.")

if __name__ == "__main__":
    main()
