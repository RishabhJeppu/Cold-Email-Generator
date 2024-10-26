import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-70b-versatile",
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE
            {page_data}
            ### INSTRUCTION:
            The scraped text if from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing
            folowing keys: role, experience, skills and description
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        # Creating a pipe
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
        ### JOB DESCRIPTION:
        {job_description}
    
        ### INSTRUCTION:
        You are Arjun, a business development executive at CognixAI. CognixAI is an AI & Data Analytics company focused on leveraging 
        cutting-edge AI solutions to drive business transformation. 
        Our expertise lies in creating custom AI models, automating data workflows, and providing actionable insights to help companies 
        improve decision-making, increase efficiency, and scale seamlessly.
        Your job is to write a cold email to the client regarding the job mentioned above, describing CognixAI's capability 
        in fulfilling their needs.
        Also, add the most relevant ones from the following links to showcase CognixAI's portfolio: {link_list}
        Remember you are Arjun, BDE at CognixAI. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
    
        """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content
