# Troubleshooting Guide

This document provides solutions to common issues you might encounter while setting up or running the AI agent.

## General Issues

### MindsDB Docker Container Not Starting

* **Issue**: The `docker run` command fails, or MindsDB is not accessible at `http://localhost:47334`.
* **Solution**:
    * Ensure Docker Desktop is running and fully initialized.
    * Check for port conflicts: Another application might be using ports `47334` or `47335`. You can change the mapped ports in the `docker run` command (e.g., `-p 8080:47334`).
    * Check Docker logs: Run `docker logs <container_id_or_name>` to see if MindsDB is reporting any errors during startup.

### `mindsdb_client` Connection Issues in Python

* **Issue**: Your Python script fails to connect to MindsDB, or you get `Connection refused` errors.
* **Solution**:
    * Verify MindsDB is running: Ensure the Docker container is active and accessible at the specified `MINDSDB_HOST` and `MINDSDB_PORT` (default: `http://127.0.0.1:47334`).
    * Firewall: Check if your firewall is blocking connections to MindsDB's ports.
    * Correct Host/Port: Ensure the `host` and `port` in your `interact_with_agent.py` script (or environment variables) match your MindsDB instance.

## MindsDB Specific Issues

### AI Model (OpenAI) Configuration Errors

* **Issue**: `CREATE ML_ENGINE` or `CREATE MODEL` statements fail, often with authentication errors or model not found.
* **Solution**:
    * **API Key**: Double-check that your `OPENAI_API_KEY` in the `.env` file (or directly in the SQL) is correct, has no typos, and is active.
    * **API Key Quotas**: Ensure you haven't exceeded your OpenAI API usage limits or that your billing is set up correctly.
    * **Model Name**: Verify the `model_name` (e.g., `gpt-4`, `gpt-3.5-turbo`) is correct and supported by your OpenAI account.
    * **MindsDB Version**: Ensure your MindsDB version supports the specific LLM integration you are trying to use.

### Web Crawler Not Fetching Data

* **Issue**: The `web_data` database or `web_knowledge_view` is empty or incomplete after running `web_crawler_integration.sql`.
* **Solution**:
    * **`start_url`**: Verify the `start_url` is correct and publicly accessible.
    * **`depth`**: Increase the `depth` parameter if the content you need is on pages linked several levels deep from the `start_url`. Be mindful that increasing depth can significantly increase crawling time.
    * **Website Restrictions**: Some websites might have `robots.txt` rules or rate limiting that prevent extensive crawling.
    * **MindsDB Logs**: Check MindsDB's internal logs for any errors related to the web crawler.

### Structured Data (PostgreSQL) Connection Errors

* **Issue**: `CREATE DATABASE` for PostgreSQL fails, or queries to `my_pg_db` do not work.
* **Solution**:
    * **Connection Parameters**: Carefully verify `host`, `port`, `user`, `password`, and `database` in `structured_data_integration.sql`. Even a small typo can cause connection failures.
    * **Network Accessibility**: Ensure the MindsDB Docker container can reach your PostgreSQL database. If PostgreSQL is on another machine or a private network, you might need to configure network access or firewalls.
    * **PostgreSQL Status**: Confirm your PostgreSQL server is running and accepting connections.
    * **Database/Table Exists**: Ensure the specified `database` and `table` (e.g., `issues`) actually exist in your PostgreSQL instance.

### AI Agent Not Responding or Giving Irrelevant Answers

* **Issue**: Queries to `my_ai_agent` return empty responses, generic answers, or irrelevant information.
* **Solution**:
    * **Model Configuration**: Ensure `mindsdb.my_gpt_model` was created successfully and is functional. Test it directly with a simple `SELECT my_gpt_model.predict('Hello') AS response;` query.
    * **Tool Configuration**: Verify that the `tools` array in `agent_creation.sql` correctly lists your `web_knowledge_base` and `my_structured_data_view`.
    * **Data Availability**: Confirm that the `web_knowledge_base` and `my_structured_data_view` contain the data you expect. Query them directly (e.g., `SELECT * FROM web_knowledge_base LIMIT 5;`).
    * **Prompt Engineering**: The quality of the agent's response depends on the clarity of your questions. Try rephrasing your queries to be more specific or provide more context.
    * **LLM Behavior**: Sometimes, LLMs can "hallucinate" or provide less relevant answers. This is part of working with generative AI. Refine your questions or consider adding more specific data.
    * **MindsDB Agent Logs**: MindsDB often provides detailed logs for agent interactions, showing which tools were invoked and what data was passed. Check these logs for debugging.

## Getting Further Help

If you've tried the above solutions and are still facing issues, please:

* **Check MindsDB Documentation**: The official MindsDB documentation is an excellent resource.
* **Open a GitHub Issue**: If you believe it's a bug with this project or need specific help, open an issue on the GitHub repository, providing detailed steps to reproduce the problem and any error messages.