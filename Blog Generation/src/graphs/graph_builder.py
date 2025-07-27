from langgraph.graph import StateGraph, START, END 
from src.llms.groqllm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.node import BlogNode

class GraphBuiler:
    def __init__(self, llm):
        self.llm = llm 
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blog on the basis of topic
        """
        self.blog_node_obj = BlogNode(self.llm)
        ## Nodes 
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        # Edges 
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_topic_graph()
        return self.graph.compile()
    
## Below code is for langsmith langgraph studio
llm = GroqLLM().get_llm()

graph_builder = GraphBuiler(llm)
graph = graph_builder.build_topic_graph().compile()