import os
from supabase import Client
from groq import Groq 
from typing import List, Dict

class ArticleHandler:
    def __init__(self, supabase: Client, groq_api_key: str):
        self.supabase = supabase
        self.groq_client = Groq(api_key=groq_api_key)
        self.model= "llama-3.3-70b-versatile"


        self.agents = [
            {
                "name": "Centrist Carl",
                "prompt": "You are a centrist political commentator. Provide a balanced take."
            },
            {
                "name": "Leftist Luna",
                "prompt": "You are a progressive commentator focused on social justice and equity."
            },
            {
                "name": "Rightwing Ron",
                "prompt": "You are a conservative thinker who values tradition and free markets."
            },
        ]

    
    def generate_take(self, agent_prompt: str, title: str, summary: str) -> str:
        full_prompt = f"""{agent_prompt}

        Headline: {title}
        Summary: {summary}

        What's your take?"""

        response = self.groq_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": full_prompt}],
        )

        return response.choices[0].message.content.strip()

    def handle_article(self, title: str, summary: str) -> List[Dict[str, str]]:
        print({
            "title": title,
            "summary": summary,
        })

        article_res = self.supabase.table("Articles").insert({
            "title": title,
            "summary": summary
        }).execute()
        print(article_res)
        article_id = article_res.data[0]["article_id"]

        takes = []
        for agent in self.agents:
            take = self.generate_take(agent["prompt"], title, summary)
            
            self.supabase.table("Takes").insert({
                "article_id": article_id,
                "agent_name": agent["name"],
                "take": take
            }).execute()

            takes.append({"agent": agent["name"], "take": take})

        return takes