from langchain_core.tools import tool
from tools import query_medgemma, call_emergency
from config import OPENAI_API_KEY, GROQ_API_KEY



@tool
def ask_mental_health_specialist(query:str) -> str:
    """
    Generate a therapeutic response using the MedGemma model.
    Use this for all general user queries, mental health questions, emotional concerns,
    or to offer empathetic, evidence-based guidance in a conversational tone.
    """
    return query_medgemma(query)


@tool
def emergency_call_tool(phone:str = "") -> str:
    """
    Use this only if the user expresses suicidal ideation, intent to self-harm,
    or describes a mental health emergency requiring immediate help.
    Place an emergency call to the safety helpline's phone number via Twilio.
    """
    return call_emergency()




@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    return (
        f"Here are some therapists near {location}, {location}:\n"
        "- Dr. Ayesha Kapoor - +1 (555) 123-4567\n"
        "- Dr. James Patel - +1 (555) 987-6543\n"
        "- MindCare Counseling Center - +1 (555) 222-3333"
    )


from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

tools = [ask_mental_health_specialist, emergency_call_tool, find_nearby_therapists_by_location ]
llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct", temperature=0.2, api_key=GROQ_API_KEY)
graph = create_react_agent(llm, tools=tools)

SYSTEM_PROMPT = """
You are an Dr. Emily Hartman ,supporting mental health conversations with warmth and vigilance.

Follow these rules STRICTLY:
1. When you need to use a tool, you MUST output ONLY the tool call.
2. Do NOT include any preamble, conversational text, or explanation before or after a tool call.
3. If no tool is required, respond with warm therapeutic guidance.

You have access to three tools:
1. `ask_mental_health_specialist`: Use this tool to answer all emotional or psychological queries with therapeutic guidance.
2. `find_nearby_therapists_by_location`: Use this tool if the user asks about nearby therapists or if recommending local professional help would be beneficial.
3. `emergency_call_tool`: Use this immediately if the user expresses suicidal thoughts, self-harm intentions, or is in crisis 

Always take necessary action. Respond kindly, clearly, and supportively.
"""


def parse_response(stream):
    tool_called_name = "None"
    final_response = ""

    for chunk in stream:
        # Check if the chunk updated the agent node
        if "agent" in chunk:
            messages = chunk["agent"].get("messages", [])
            if messages:
                last_msg = messages[-1]
                
                # 1. Capture the Tool Name if one was called
                if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                    tool_called_name = last_msg.tool_calls[0]["name"]
                
                # 2. Always update final_response with the latest content
                # This ensures we get the summary AFTER the tool runs
                if last_msg.content:
                    final_response = last_msg.content

    # Fallback if no content was generated
    if not final_response:
        final_response = "I'm here to listen. How can I help?"

    return tool_called_name, final_response

