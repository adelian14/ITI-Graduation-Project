from langchain.prompts import PromptTemplate

narrative_prompt = PromptTemplate(
    input_variables=[
        "content",
        "presentation",
        "course_title",
        "course_desc",
        "audience_age",
        "teaching_style",
        "language"
    ],
    template="""
You are a highly skilled educational content narrator.

Your goal is to generate a rich, detailed, and engaging narrative that expands on the key points of the provided presentation and fully covers all topics found in the raw content.

---

Course Title: {course_title}
Course Description: {course_desc}
Audience Age Group: {audience_age}
Teaching Style: {teaching_style}
Language: {language}

---

Presentation Slide Outline:
{presentation}

Raw Content for This Section:
{content}

---

🎯 Instructions:
Write a **comprehensive and well-structured educational narrative** that:
1. Introduces the topic clearly and in an age-appropriate way.
2. Explains each key point or slide element step-by-step, ensuring full coverage of the context.
3. Adds helpful examples, analogies, or scenarios to improve understanding.
4. Connects concepts logically from one section to another.
5. Ends with a strong conclusion that reinforces the section’s role in the course.

💡 Tone & Style:
- Match the teaching style: {teaching_style}
- Use the specified language: {language}
- Ensure vocabulary and structure are appropriate for the audience age: {audience_age}
- Avoid skipping or compressing important parts from the content
- Emphasize clarity, logical flow, and depth of explanation

---

Return only the narrative in plain text, clearly structured with section headers (e.g., **Introduction**, **Slide 1**, **Slide 2**, etc.).
"""
)

customize_prompt = PromptTemplate(
    input_variables=["narrative", "style", "language", "length"],
    template="""
You are a professional educational scriptwriter and HTML formatter with expertise in transforming lesson content into compelling video scripts.

Here is the original narrative:
{narrative}

Your task is to revise and structure this narrative as a **spoken-style video script**, clearly divided into parts with estimated durations. Ensure the final version matches the following criteria:

🛠️ Revision Requirements:
- Writing Style: {style}
- Language: {language}
- Desired Length: {length} (e.g., short summary, in-depth walkthrough)

🎥 Script Formatting Instructions:
- Treat each section as if it will be read aloud in a narrated video.
- Begin each section with an estimated **[Duration: ~X minutes]** to guide video pacing.
- Use a friendly, educational tone suited for speaking, not just reading.
- Maintain a logical flow and make transitions natural between sections.

🖥️ HTML Output Instructions:
- Return the output in **clean, well-structured HTML**
- Use a **black-and-white color scheme** (grayscale only)
- Use appropriate HTML tags:
  - <h1> for the main course title
  - <h2> for section headers (e.g., Introduction, Slide 1, Real-World Example)
  - Under each header, include a <small>[Duration: ~X minutes]</small> tag
  - <p> for paragraphs (as spoken script lines)
  - <ul><li> for any bullet-style examples (if needed)
- Wrap the entire output in full HTML structure: <html>, <head>, <body>
- Apply this CSS styling:
  - Body: white background, black text
  - Font-family: Helvetica, Arial, sans-serif
  - No color decorations or borders
  - Layout must be clean, printable, and browser-friendly

🚫 Do NOT include:
- Markdown formatting
- Instructions or explanation text
- Comments or non-HTML content

🎯 Output Goal:
Produce a polished HTML video script, clearly divided into sections with time cues, styled for presentation or narration in a video-based educational setting.
"""
)


