import streamlit as st
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_agenticai.LLMs.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """

    ## load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI")
        return 
    
    user_message = st.chat_input("Enter your messge: ")

    if user_message:
        try:
            ## Configure the llm's
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return 
            
            ## Initialize and set up the graph based on the use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No usecase selected")
                return 
            
            ## Graph Builder 
            graph_builder = GraphBuilder(model=model)
            try: 
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return 
        except Exception as e:
            st.error(f"Error: Process failed - {e}")
            return 