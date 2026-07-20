import sys

import ollama
from StructuredOutput import SQLTranslatorResponse
from File import read_file

def translate_sql(user_query: str, database_schema: str):
    system_content = (
        "Here is the database schema to use for the query.\n\n"
        "### DATABASE SCHEMA ###\n"
        f"{database_schema}\n"
        "### END DATABASE SCHEMA ###"
    )
    response = ollama.chat(
        model="sql-translator:latest",
        messages=[
            {
                "role": "system",
                "content": system_content
            },
            {
                "role" : "user",
                "content": f"Query: {user_query}"
            }
        ],
        format=SQLTranslatorResponse.model_json_schema())
    sql_translator_response = SQLTranslatorResponse.model_validate_json(response.message.content)
    return "SQL Query: " + sql_translator_response.sql_query + "\nDescription: " + sql_translator_response.description

def main():
    try:
        database_schema = read_file('schema.sql')
        user_query = input("Enter what you wish to do with the database. I will translate your request into an SQL query.\n-> ")
        print(f"Translating your request into an SQL query...\n")
        result = translate_sql(user_query, database_schema)
        print(result)
    except Exception as e:
        print(f"Error translating your request: {e}")   

if __name__ == "__main__":
    main()