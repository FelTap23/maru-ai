# maru-ai
# ROMBOOOOTLOS


##How to run the app 
1. Activate the virtual environment
2. pip install -r requirements.txt
3. python -m uvicorn main:app --reload
4. Check the hello world
curl http://localhost:8000

5. To test completion API please set the prompt value
curl -i -H "Content-Type: application/json" -X POST  http://localhost:8000/completion -d '{ "prompt" : "How is the president of Mexico" }'

curl -i -H "Content-Type: application/json" -X POST  http://localhost:8000/math -d '{ "a" : 5, "b" : 10 }'

curl -i -H "Content-Type: application/json" -X GET  http://localhost:8000/math/4/1000

curl -i -H "Content-Type: application/json" -X GET  "http://localhost:8000/math_query?a=3&b=117"