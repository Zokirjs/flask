


from flask import Flask, render_template, request, url_for

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
creds = ServiceAccountCredentials.from_json_keyfile_name("malumot.json", scope)




# (A2) FLASK SETTINGS + INIT


app = Flask(__name__)
# app.debug = True

# (B) DEMO - READ EXCEL & GENERATE HTML TABLE
@app.route("/")
def index():
   return render_template('homepage.html')

@app.route("/home")
def home():
  return render_template("index.html")

@app.route('/login' , methods=["POST"])
def receive_data():
  # do somsing
  name1 = request.form["ismi"]
  uqish = request.form['oqish_joyi']
  numer=request.form['phone']
  tet = request.form['textarea']
  yonalish = request.form['yonalish']
  viloyat = request.form['viloyat']
  tugulgan_yil = request.form['yil']
  
  

  client = gspread.authorize(creds)
  excel=client.open("DG registration").worksheet("Лист1")
  request_data = excel.get_all_records()
  values_list = excel.col_values(1)
  v = len(values_list)
  # print(request_data)

  excel.update_cell(1,1,"Eamil/User")
  excel.update_cell(1,2,"Yo'nalish")
  excel.update_cell(1,3,"Viloyat")
  excel.update_cell(1,4,"Nima uchun tanlashimiz ")
  excel.update_cell(1,5,"Tel nomer")
  excel.update_cell(1,6,"Tug'ulgan Yil")
  excel.update_cell(1,7,"O'qish joyi")




  excel.update_cell(v+1,1,f"{name1}")
  excel.update_cell(v+1,2,f"{yonalish}")
  excel.update_cell(v+1,3,f"{viloyat}")
  excel.update_cell(v+1,4,f"{tet}")
  excel.update_cell(v+1,5,f"{numer}")
  excel.update_cell(v+1,6,f"{tugulgan_yil}")
  excel.update_cell(v+1,7,f"{uqish}")



  return render_template('homepage.html')






if __name__ == "__main__":
  app.run(debug=True)





