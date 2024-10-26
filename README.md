# Cold Email Generator

## Project Overview
The Cold Email Generator is a tool designed to streamline the process of creating personalized cold emails for job applications. A cold email is an unsolicited email sent to a potential employer or contact, often used to introduce oneself, express interest in a job, or inquire about opportunities. This project leverages state-of-the-art language models and a robust database of portfolio information to generate tailored emails, effectively matching job descriptions with relevant candidate skills and experience.

## Tech Stack
- **LLM Model**: `llama-3.1-70b-versatile` (Accessed via `groq_api`)
- **Vector Database**: `ChromaDB`

## How It Works

1. **Extracting Job Information**:
   - A URL pointing to a job posting is provided to the model.
   - Using the `WebBaseLoader` method from the `langchain_community` module, the tool retrieves and loads relevant text from the web page.

2. **Processing Job Description**:
   - The extracted job text, along with any additional user query, is fed into the LLM model (`llama-3.1-70b-versatile`).
   - The model generates a JSON object containing the parsed job requirements, which includes:
     - **Skills** required for the position
     - **Job Description**
     - **Experience** needed for the role

3. **Matching with Candidate Profiles**:
   - The generated JSON object is then used to match candidate portfolios stored in `ChromaDB`, a vector database containing relevant experiences with various technologies.

4. **Generating the Cold Email**:
   - Using the extracted job requirements and the data stored in `ChromaDB`, the model constructs a personalized cold email.
   - The final email includes links to relevant portfolios, helping recruiters see each candidate's qualifications directly aligned with the job description.

## Features
- **Automated Job Posting Analysis**: Extracts and interprets key requirements directly from job postings.
- **Personalized Cold Email Generation**: Matches job requirements with candidate skills to create a targeted, professional email.
- **Efficient Portfolio Linking**: Directs potential employers to relevant work samples, increasing engagement and visibility for candidates.

## Installation and Usage
To run this project, ensure you have the following prerequisites installed:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd cold-email-generator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your API keys (Groq API for LLM access and database configurations for ChromaDB).

4. Run the main script:
    ```bash
    streamlit run main.py
    ```

## Contributing
Contributions to improve this project are welcome! Please fork the repository and make a pull request with your suggested improvements.



