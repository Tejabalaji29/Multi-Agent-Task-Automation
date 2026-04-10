"""
Streamlit Interface for Multi-Agent Task Automation
Interactive web interface for task orchestration and agent execution.
"""

import streamlit as st
from datetime import datetime
from agents import TaskAgent, AnalysisAgent, ExecutionAgent
from memory import Memory
from tools import register_tools

# Page configuration
st.set_page_config(
    page_title="Multi-Agent Task Automation",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "memory" not in st.session_state:
    st.session_state.memory = Memory()

if "execution_history" not in st.session_state:
    st.session_state.execution_history = []

# Header
st.title("🤖 Multi-Agent Task Automation")
st.markdown("Orchestrate multiple AI agents to complete complex tasks autonomously.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")

    # Agent selection
    st.subheader("Active Agents")
    use_task_agent = st.checkbox("Task Planning Agent", value=True)
    use_analysis_agent = st.checkbox("Analysis Agent", value=True)
    use_execution_agent = st.checkbox("Execution Agent", value=True)

    # Memory management
    st.subheader("Memory")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 View Memory"):
            st.session_state.show_memory = True
    with col2:
        if st.button("🗑️ Clear Memory"):
            st.session_state.memory.clear()
            st.success("Memory cleared!")

    st.divider()

    # Execution history
    st.subheader("Execution History")
    st.write(f"Total executions: {len(st.session_state.execution_history)}")

    if st.session_state.execution_history:
        for i, execution in enumerate(st.session_state.execution_history[-5:], 1):
            st.caption(f"{i}. {execution['task'][:40]}...")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📋 Task Input")

    task_input = st.text_area(
        "Enter your task:",
        placeholder="e.g., Analyze the codebase and identify optimization opportunities",
        height=100,
        key="task_input"
    )

    task_type = st.selectbox(
        "Task Type",
        ["Analysis", "Planning", "Execution", "Custom"]
    )

    col_submit, col_clear = st.columns(2)
    with col_submit:
        submit_button = st.button("▶️ Execute Task", type="primary", use_container_width=True)
    with col_clear:
        if st.button("🔄 Clear Input", use_container_width=True):
            st.rerun()

with col2:
    st.header("📈 Status")
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric("Tasks Completed", len(st.session_state.execution_history))
    with metric_col2:
        st.metric("Memory Entries", len(st.session_state.memory.entries))

# Execute task
if submit_button and task_input:
    with st.spinner("🔄 Executing task..."):
        try:
            # Initialize agents
            tools = register_tools()

            task_agent = TaskAgent(memory=st.session_state.memory, tools=tools) if use_task_agent else None
            analysis_agent = AnalysisAgent(memory=st.session_state.memory, tools=tools) if use_analysis_agent else None
            execution_agent = ExecutionAgent(memory=st.session_state.memory, tools=tools) if use_execution_agent else None

            # Progress tracking
            progress_placeholder = st.empty()
            results = {}

            # Task planning phase
            if task_agent:
                progress_placeholder.info("📍 Phase 1/3: Planning task...")
                plan = task_agent.plan_task(task_input)
                results["plan"] = plan

            # Analysis phase
            if analysis_agent:
                progress_placeholder.info("📍 Phase 2/3: Analyzing...")
                analysis = analysis_agent.analyze(task_input)
                results["analysis"] = analysis

            # Execution phase
            if execution_agent:
                progress_placeholder.info("📍 Phase 3/3: Executing...")
                execution = execution_agent.execute(task_input)
                results["execution"] = execution

            progress_placeholder.empty()

            # Store in history
            st.session_state.execution_history.append({
                "task": task_input,
                "timestamp": datetime.now().isoformat(),
                "task_type": task_type,
                "status": "completed"
            })

            # Display results
            st.success("✅ Task completed successfully!")

            # Results tabs
            if results:
                result_tabs = st.tabs(list(results.keys()) + ["Memory Log"])

                for i, (phase, content) in enumerate(results.items()):
                    with result_tabs[i]:
                        st.markdown(content)

                # Memory log tab
                with result_tabs[-1]:
                    memory_entries = st.session_state.memory.get_entries()
                    if memory_entries:
                        for entry in memory_entries[-10:]:  # Show last 10 entries
                            st.write(f"**{entry['source']}** ({entry['type']})")
                            st.caption(entry['timestamp'])
                            st.write(entry['content'][:200] + "..." if len(entry['content']) > 200 else entry['content'])
                            st.divider()
                    else:
                        st.info("No memory entries recorded.")

        except Exception as e:
            st.error(f"❌ Error executing task: {str(e)}")

# Memory viewer (in expandable section)
if st.checkbox("🧠 View Full Memory"):
    st.subheader("Memory Contents")

    col1, col2 = st.columns(2)

    with col1:
        filter_source = st.multiselect(
            "Filter by source:",
            options=[e["source"] for e in st.session_state.memory.entries] or ["No entries"],
            key="filter_source"
        )

    with col2:
        filter_type = st.multiselect(
            "Filter by type:",
            options=[e["type"] for e in st.session_state.memory.entries] or ["No entries"],
            key="filter_type"
        )

    # Display filtered entries
    filtered_entries = st.session_state.memory.get_entries()
    if filter_source:
        filtered_entries = [e for e in filtered_entries if e["source"] in filter_source]
    if filter_type:
        filtered_entries = [e for e in filtered_entries if e["type"] in filter_type]

    if filtered_entries:
        for entry in filtered_entries:
            with st.expander(f"📌 {entry['source']} - {entry['type']} ({entry['timestamp']})"):
                st.write(entry['content'])
    else:
        st.info("No memory entries match the selected filters.")

# Footer
st.divider()
st.markdown("""
    <div style="text-align: center; color: gray; font-size: 0.8rem;">
        Multi-Agent Task Automation System | Powered by Streamlit
    </div>
""", unsafe_allow_html=True)
