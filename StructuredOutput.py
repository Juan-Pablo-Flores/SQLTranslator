from pydantic import BaseModel, Field

class SQLTranslatorResponse(BaseModel):
    sql_query: str = Field(description="The translated SQL query")