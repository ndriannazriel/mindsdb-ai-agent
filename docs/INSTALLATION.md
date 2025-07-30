# Installation Guide

This document provides comprehensive instructions for setting up your MindsDB AI agent project.

## Prerequisites

* **Docker Desktop**: Ensure Docker Desktop is installed and running on your system.
    * [Download & Install Docker Desktop](https://www.docker.com/products/docker-desktop/)
* **Python 3.8+**:
    * [Download Python](https://www.python.org/downloads/)
* **`pip`**: Python package installer (usually comes with Python).
* **An OpenAI API Key**: Required to configure the AI model in MindsDB.
    * [Get an OpenAI API Key](https://platform.openai.com/account/api-keys)

## Step-by-Step Setup

### 1. Clone the Repository

First, clone this Git repository to your local machine:

bash
```
git clone [https://github.com/your-username/mindsdb-ai-agent.git](https://github.com/your-username/mindsdb-ai-agent.git)
cd mindsdb-ai-agent
```

### 2. Docker 
```
docker pull mindsdb/mindsdb
docker run -p 47334:47334 -p 47335:47335 mindsdb/mindsdb
```
### 3. Follow Reference1 and Reference2

#### Working with Unstructured Data
[Reference1](../Reference1.md) 
* Create a Database to crawl a webpage.
* Create a new View.
* Turn into a Knowledge Base(Vectorized data/database where it automatically chunks and embeds the different text content that comes from our data and something the AI agent can use) 
* Insert data into the Knowledge Base.
* Query the Knowledge Base.

#### Set up a structured database using a PostgreSQL connection and then combine into an AI agent for more accurate replies
[Reference2](../Reference2.md)
* Connect to sample datasource/dataset from Mindsdb
* For this example we'll be using the engineering dataset from MindsDB.
* Enrich the data before passing to the LLM.
* Get the LLM to generate new data based on the data to create new knowledge base.
* Generate an AI agent that connects to this data as well as the data that we pulled from the website(Reference1).
