from crewai import Crew, Process
from pipeline.Narrative_generation_crew.agents import NarrativeGenerationAgents
from pipeline.Narrative_generation_crew.tasks import NarrativeGenerationTasks


class NarrativeGenerationCrew:
    def __init__(self):
        self.agents = NarrativeGenerationAgents()
        self.tasks = NarrativeGenerationTasks()

    
    def create_crew(self, lesson, learner):
        # Initialize all agents
        content_analyzer_agent = self.agents.content_analyzer_agent
        personalization_agent = self.agents.personalization_agent
        script_producer_agent = self.agents.script_producer_agent
        markdown_formatter_agent = self.agents.markdown_formatter_agent

        # Create tasks with dependencies
        analyze_and_structure_task = self.tasks.create_analyze_and_structure_task(
            lesson_content_string=lesson,
            learner = learner,
            agent=content_analyzer_agent
        )
        personalize_content_task = self.tasks.create_personalize_content_task(
            learner= learner,
            agent=personalization_agent,
            dependency_task=analyze_and_structure_task
        )
        produce_video_script_task = self.tasks.create_produce_video_script_task(
            learner=learner,
            agent=script_producer_agent,
            dependency_task=personalize_content_task
        )
        format_markdown_task = self.tasks.create_format_markdown_task(
            learner= learner,
            agent=markdown_formatter_agent,
            dependency_task=produce_video_script_task
        )


        # Create and return crew
        return Crew(
            agents=[content_analyzer_agent, personalization_agent, script_producer_agent, markdown_formatter_agent],
            tasks=[analyze_and_structure_task, personalize_content_task, produce_video_script_task, format_markdown_task],
            verbose=True,
            process="sequential"  # Explicitly set process type
        )
    
    def run(self, lesson ,learner):
        # Dictionary to store individual agent outputs
        agent_outputs = {}
        # Create crew with learner profile
        crew = self.create_crew(lesson, learner)

        try:
            # Execute crew and get final result
            result = crew.kickoff()
            
            # Access individual task outputs
            if hasattr(crew, 'tasks'):
                for i, task in enumerate(crew.tasks):
                    if hasattr(task, 'output'):
                        agent_name = task.agent.role
                        agent_outputs[agent_name] = task.output
                        print(f"\n📋 {agent_name} Output Captured")

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print("Please check your API key and input files.")

        # Return the final result and individual agent outputs
        return agent_outputs
    
    # Function to get specific agent output
    def get_agent_output(self, agent_name, agent_outputs):
        """Get output from a specific agent"""
        if agent_name in agent_outputs:
            return agent_outputs[agent_name].raw
        else:
            print(f" Agent '{agent_name}' not found. Available agents:")
            for name in agent_outputs.keys():
                print(f"   - {name}")
            return None

