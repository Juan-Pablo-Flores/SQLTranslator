# SQLTranslator
This is an exercise on AI Application development.
This project is under development. 
The project will be a command-line tool that translates natural language Queries into SQL queries
given a database schema. 
I will use Ollama to create a local API endpoint and a Python backend to interact with it and the command line.

## Installation & Setup

1. [Download](https://www.python.org/downloads/) & Install Python.
2. Install python dependencies
```commandline
pip install pydantic ollama
```
3. [Download](https://ollama.com/download) & install Ollama.

4. Download the model qwen2.5-coder:1.5b 
```commandline
ollama pull qwen2.5-coder:1.5b
```

5. Create a model from Modelfile
```commandline
ollama create sql-translator -f .\Modelfile
```

6. Run SQLTranslator.py
  - Windows
```commandline
py SQLTranslator.py
```
  - MacOs/Linux
```commandline
python SQLTranslator.py
```
