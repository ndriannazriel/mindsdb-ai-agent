#### `docs/USAGE.md`

This file would contain detailed examples of how to interact with the agent, including various types of queries and expected outputs.

# Agent Usage Guide

This document provides examples and best practices for interacting with your MindsDB AI agent.

## Querying the Agent

You can query the `my_ai_agent` using the MindsDB GUI, SQL editor, or programmatically via the Python SDK.

### 1. Via MindsDB SQL Editor

Open the MindsDB GUI (`http://localhost:47334`) and use the SQL editor to send queries.

**Basic Query:**

```
SELECT response FROM mindsdb.my_ai_agent WHERE question = 'What is MindsDB?';
```

Querying Web Knowledge Base:

The agent will automatically route questions related to the web-crawled content to the web_knowledge_base tool.
```
SELECT response FROM mindsdb.my_ai_agent WHERE question = 'How does MindsDB help build AI agents?';
```
Querying Structured Data:

Questions related to your structured database (e.g., PostgreSQL issues table) will be routed to the my_structured_data_view tool.
```
SELECT response FROM mindsdb.my_ai_agent WHERE question = 'What are the most common issues reported in our database?';
```
Querying Enriched Data:

If you configured data enrichment (e.g., suggested_fix column), you can ask questions that leverage these insights.
```
SELECT response FROM mindsdb.my_ai_agent WHERE question = 'Can you suggest a solution for issue ID 123?';
```
Combined Queries:

The agent can combine information from multiple tools to answer complex questions.
```
SELECT response FROM mindsdb.my_ai_agent WHERE question = 'Tell me about MindsDB and also what is the status of issue ID 456 from our database?';
```

### Tips for Effective Querying

--Be Specific: The more specific your question, the better the agent can utilize its tools to find relevant information.
--Context is Key: If your question relates to structured data, mentioning relevant IDs or keywords from that data source can help.
--Experiment: Try different phrasings and combinations of questions to understand how your agent processes information.
--Check MindsDB Logs: If you're not getting expected results, check the MindsDB logs for insights into how the agent is interpreting your query and which tools it's attempting to use.

