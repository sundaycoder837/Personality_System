from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [{
  
  "id": 1 ,
  "title": "CyeberSecurity" ,
  "location":"Suza,Zanzibar",
  "position":"2"
  
  
  },
  {
  "id": 2,
  "title": "DataScience" ,
  "location":"Suza,Zanzibar",
  "position":'4'
  
  },
  {
  "id": 3 ,
  "title": "Programmer(python)" ,
  "location":"Suza,Zanzibar",
  "position": '4'
  },
  {
  "id": 4,
  "title": "Software Engineer" ,
  "location":"Suza,Zanzibar",
  "position": "3"
  },

]


@app.route("/")
def hello_word():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name ='Personality')

@app.route("/api /jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
