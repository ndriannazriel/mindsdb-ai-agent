import mindsdb_sdk
import os

# Get host and port from environment variables, defaulting to local MindsDB URL
mindsdb_host = os.getenv('MINDSDB_HOST', '127.0.0.1')
mindsdb_port = os.getenv('MINDSDB_PORT', '47334')

# THIS IS THE CRUCIAL LINE: Construct the full URL and pass it as a single argument
mindsdb_url = f"http://{mindsdb_host}:{mindsdb_port}"

try:
    # Connect to MindsDB using the full URL
    server = mindsdb_sdk.connect(mindsdb_url)
    print(f"Successfully connected to MindsDB at {mindsdb_url}")
except Exception as e:
    print(f"Error connecting to MindsDB at {mindsdb_url}: {e}")
    print("Please ensure MindsDB is running and accessible at the specified URL.")
    exit()

# Get the 'mindsdb' project (this is the default project where agents are created)
project = server.get_project('mindsdb')

# Define the function to create the query string
# IMPORTANT: Replace 'my_ai_agent' with the actual name of your agent if it's different
# I'm using 'my_ai_agent' as per our earlier discussion, but if you named it 'staging_agent', change this line.
agent_name = 'staging_agent' # Or 'staging_agent' if that's what you used
make_query_str = lambda question: f"SELECT response FROM {agent_name} WHERE question = '{question}';"


print("\nAI Agent Chat (type 'exit' to quit)")
while True:
    question = input("Ask me anything: ")
    if question.lower() == "exit":
        break

    new_query_str = make_query_str(question)
    print(f"Sending query: {new_query_str}") # Debugging: show the query being sent

    try:
        query = project.query(new_query_str)
        result = query.fetch()

        # Check if the result DataFrame is not empty and contains the 'response' column
        # MindsDB agents typically return the predicted text in a column named 'response'
        if not result.empty and 'response' in result.columns:
            first_row_answer = result.iloc[0]['response']
            print(f"Agent: {first_row_answer}")
        else:
            print("Agent: No valid response received or 'response' column not found.")
            if not result.empty:
                print(f"Agent raw result (for debugging): {result.to_dict()}")
            else:
                print("Agent raw result: Empty DataFrame.")

    except Exception as e:
        print(f"An error occurred while querying the agent: {e}")
        print("Please check MindsDB logs for more details or verify your agent configuration.")
