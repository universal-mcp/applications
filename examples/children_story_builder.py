import asyncio

from langgraph.checkpoint.memory import MemorySaver

from universal_mcp.agentr.registry import AgentrRegistry
from universal_mcp.agents import ReactAgent

SYSTEM_PROMPT = """
You are an world renowned storyteller. You write stories for children. You will be given a task to write a story and its anciallary functions. You will need to follow the steps below to complete the task.
Always use easy to understand language and simple words. The stories are meant for children. 

IMPORTANT:
- Do not ask for user confirmation in between, in case of confusion make assumptions and move one.
- For file paths, use the /tmp directory.

"""


async def main():
    registry = AgentrRegistry()
    tools = {
        # "reddit": ["r_subreddit_top", "get_subreddit_posts"],
        "google_gemini": ["generate_image", "generate_audio"],
        "file_system": ["write_file"],
    }
    checkpointer = MemorySaver()
    agent = ReactAgent(
        name="My Agent",
        instructions=SYSTEM_PROMPT,
        registry=registry,
        tools=tools,
        model="azure/gpt-5-chat",
        memory=checkpointer,
    )
    tasks = [
        """Task 1: Story Creation
        Write a captivating children's fairy tale story about a brave princess who rescues a prince from a dragon. 
        
        Requirements:
        - Target audience: Children aged 4-8 years
        - Use simple, age-appropriate vocabulary and sentence structure
        - Create 6-8 distinct scenes that flow logically from beginning to end
        - Include classic fairy tale elements: setting, characters, conflict, and resolution
        - Make the princess the hero of the story, showcasing courage and problem-solving
        - Ensure the story has a positive, uplifting message
        - Each scene should be 2-3 sentences long for easy comprehension
        - Include dialogue to make the story engaging
        
        Structure each scene with:
        - Scene number and descriptive title
        - Brief narrative text
        - Clear progression toward the rescue and happy ending""",
        """Task 2: Image Generation
        Generate high-quality images for each scene of the fairy tale story you just created.
        
        Requirements:
        - Create one image per scene (6-8 images total)
        - Style: Animated webtoon comic style with bright, cheerful colors
        - Include all main characters: princess, prince, and dragon in relevant scenes
        - Ensure visual consistency across all images (same character designs, art style)
        - Make images child-friendly and non-frightening
        - Include relevant background settings for each scene
        - Each image should clearly represent the key moment or action of its corresponding scene
        
        For each image prompt, include:
        - Scene description and key visual elements
        - Character descriptions and positions
        - Setting and background details
        - Mood and atmosphere
        - Specific mention of "webtoon comic style, animated, colorful, child-friendly"

        To ensure consisteny pass the previous image path as reference to next image generation.
        Generate all the scenes one by one.
        Verify that all scenes have corresponding images before proceeding.""",
        """Task 3: Story Narration Writing
        Transform the fairy tale story into an engaging audio narration script suitable for children.
        
        Requirements:
        - Write in a warm, friendly storytelling voice
        - Use varied sentence rhythms and pacing for audio delivery
        - Include natural pauses and emphasis points
        - Add descriptive language that paints vivid mental pictures
        - Use sound words and onomatopoeia where appropriate (whoosh, roar, etc.)
        - Create emotional engagement through tone and word choice
        - Ensure smooth transitions between scenes
        - Keep language simple but expressive
        - Add narrative cues that work well when spoken aloud
        - Total narration should be 3-5 minutes when read aloud
        
        Format the narration with:
        - Clear scene breaks
        - Emphasis markers for important moments
        - Natural breathing points
        - Engaging opening and satisfying conclusion""",
        """Task 4: Audio Generation
        Generate high-quality audio narration of the complete fairy tale story.
        
        Requirements:
        - Use the narration script from Task 3
        - Select a warm, friendly voice suitable for children's stories
        - Ensure clear pronunciation and appropriate pacing
        - Use natural storytelling rhythm with appropriate pauses
        - Maintain consistent volume and tone throughout
        - Generate as a single audio file containing the complete story
        - Save the audio in a web-compatible format (WAV or MP3)
        - Ensure the audio duration matches the 3-5 minute target length
        
        Voice characteristics:
        - Gender-neutral or female voice preferred
        - Warm, nurturing tone
        - Clear articulation
        - Moderate speaking pace suitable for children
        - Expressive delivery that brings the story to life""",
        """Task 5: Markdown Story Compilation
        Create a comprehensive markdown file that combines all story elements into a beautiful, complete presentation.
        
        Requirements:
        - Create a well-structured markdown document with proper formatting
        - Include an engaging title for the fairy tale
        - Organize content with clear headings and sections
        - Embed all generated images in their corresponding scenes
        - Include the audio narration file with proper markdown audio player syntax
        - Use proper markdown syntax for images: ![Alt text](image_path)
        - Use proper markdown syntax for audio: 🎧 [Listen to the Story](audio_path)
        - Add scene dividers and visual breaks for readability
        - Include a table of contents if helpful
        - Ensure all file paths are correct and accessible
        - Add any necessary alt text for accessibility
        
        Structure:
        - Title and introduction
        - Scene-by-scene presentation with embedded images
        - Audio narration section
        - Optional: Character descriptions or story themes
        
        Save the final markdown file with an appropriate filename like '/tmp/fairy_tale_story.md'
        Verify all embedded media files are properly linked and accessible.""",
    ]

    for task in tasks:
        result = await agent.invoke(task)
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
