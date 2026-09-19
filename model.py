from groq import Groq

client = Groq()

def general_response(message):
  completion = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[
        {
          "role": "system",
          "content": """You are a helpful chtbot for matric leaners
            whom want want apply in Unizulu or uiversity of Zululand 
            You isizulu when asked in isizulu and you speak english when asked in english"""
        },
      
        {
          "role": "user",
          "content": f"{message}"
        }
      ],
      temperature=1,
      max_completion_tokens=2048,
      top_p=1,
      reasoning_effort="medium",
      stream=True,
      stop=None
  )

  answer = ""


  for chunk in completion:
      answer+=chunk.choices[0].delta.content or ""

  return answer