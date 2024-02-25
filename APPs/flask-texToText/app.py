
from openai import OpenAI
from flask import Flask, render_template,request
import json


api_key2="sk-AJ7hKOzylbkFJTKHRWlQyl77x"
client=OpenAI(api_key=api_key2)

def get_suggestion(promt):
    message=[{"role":"system",
              "content":"You are an expert recruter, having 10+ years of experince in creating clear, precise and proper job description. You have knowledge of all technology and non tech roles in industry, you are well aware of skills and responsibilities for new jobs in market"},
             {"role":"user",
              "content":promt}]
    
    response=client.chat.completions.create(messages=message,model='gpt-3.5-turbo')
    
    
    return response.choices[0].message.content



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def fun():
    return render_template('index.html')


@app.route('/suggest',methods=['GET','POST'])

def fun2():
    data=dict(request.form)
    print(data['desg'])
    
    promt=f"provide detailed list of skill for the job role {data['desg']},onlyprovide comma seperated"
    
    skills=get_suggestion(promt)
    
    promt=f"provide a detailed job description with component such as job summary, qualification, Responsibility for job role {data['desg']}"
    
    jobdes=get_suggestion(promt)
    
    return render_template('index.html',job_desc=jobdes, skills=skills,desg=data['desg'])



@app.route("/summit",methods=['GET','POST'])

def fun3():
    data= dict(request.form)
    print(data)
    return "hello world from CHAT GPT"

app.run(port=5003)
    
