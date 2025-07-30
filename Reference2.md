--Set up a structured database
```
CREATE DATABASE datasource2
WITH ENGINE = 'postgres',
PARAMETERS = {
    "user" : "demo_user",
    "password" : "demo_password",
    "host" : "samples.mindsdb.com",
    "port" : "5432",
    "database" : "demo",
    "schema" : "demo"
}

CREATE TABLE files.enriched_files (
    SELECT 
    issue, environment, error_rate, impacted_customers, severity,
    LLM('Determine a possible fix for this issue: ' || issue) AS possible_fix --Creating a new entry
    FROM datasource2.engineering_dataset
)

CREATE AGENT staging_agent
USING
    model = {
        "provider" : "openai",
        "model_name" : "gpt-4o",
        "api_key" : "apikey"
    },
    data = {
        "knowledge_bases" : ['mindsdb.environment_kb'],
        "tables" : ['files.enriched_files']
    },
    prompt_template = 'You are a skilled QA analyst and a developer. Your goal is to help developers
    understand data related to quality issues and tickets. There is data available to you: 
    table files.enriched_files stores logs and engineering issues/tickets, and the knowledge base mindsdb.environment_kb stores added context about developer environment.'
;

--Quering the Agent
SELECT answer FROM staging_agent
WHERE question = 'What issue mpact the most customers in the engineering dataset';
```