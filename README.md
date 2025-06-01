# maru-ai
# ROMBOOOOTLOS


##How to run the app 
1. Activate the virtual environment
2. pip install -r requirements.txt
3. python -m uvicorn main:app --reload
4. Check the hello world
curl http://localhost:8000

5. To test completion API please set the prompt value:

curl -i -H "Content-Type: application/json" -X POST  http://localhost:8000/math -d '{ "a" : 5, "b" : 10 }'

curl -i -H "Content-Type: application/json" -X GET  http://localhost:8000/math/4/1000

curl -i -H "Content-Type: application/json" -X GET  "http://localhost:8000/math_query?a=3&b=117"

6. to be able to run completion endpoint you need to export before running the app in step 3:
export OPENAI_API_KEY=your_api_key
Then set your prompt with :

curl -i -H "Content-Type: application/json" -X POST  http://localhost:8000/completion -d '{ "prompt" : "Who is the president of Mexico today? " }'

