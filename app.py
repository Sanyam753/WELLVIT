from flask import Flask,render_template,request,session,redirect,url_for,flash

from werkzeug.security import generate_password_hash,check_password_hash

from datetime import datetime

from flask import Flask, request, jsonify, render_template
import pandas as pd
import json
from model.inference import final_inference



# MY db connection
local_server= True
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSVs
try:
    gl_df = pd.read_csv('gl_df.csv')
    ex_df = pd.read_csv('exercise_data.csv')
    fd_df = pd.read_csv('food_intake.csv')
    med_df = pd.read_csv('medication_data.csv')
except Exception as e:
    print("Error loading CSV files:", e)

# Ensure required columns exist
required_columns = ["User_ID", "Date", "Blood_Glucose_Level"]
for col in required_columns:
    if col not in gl_df.columns:
        print(f"Missing column: {col} in glucose dataset")

def test_success(user_id, date_of_interest):
    if "Date" not in gl_df.columns:
        return {"error": "Column 'Date' is missing in the dataset"}

    # Filter data
    user_data = gl_df[(gl_df['User_ID'] == user_id) & (gl_df['Date'] == date_of_interest)].copy()
    
    if user_data.empty:
        return {"error": f"No data found for User_ID {user_id} on {date_of_interest}."}

    total_readings = len(user_data)
    
    # Count glucose level categories
    count_TIR = ((user_data['Blood_Glucose_Level'] >= 70) & (user_data['Blood_Glucose_Level'] <= 180)).sum()
    count_TBR = (user_data['Blood_Glucose_Level'] < 70).sum()
    count_TAR = (user_data['Blood_Glucose_Level'] > 180).sum()
    count_severe = (user_data['Blood_Glucose_Level'] < 54).sum()
    
    # Calculate percentages
    TIR_pct = (count_TIR / total_readings) * 100 if total_readings > 0 else 0
    TBR_pct = (count_TBR / total_readings) * 100 if total_readings > 0 else 0
    TAR_pct = (count_TAR / total_readings) * 100 if total_readings > 0 else 0
    severe_pct = (count_severe / total_readings) * 100 if total_readings > 0 else 0

    # Determine success
    success = (TIR_pct >= 70) and (TBR_pct <= 4) and (TAR_pct <= 25) and (severe_pct <= 1)
    success_status = "Successful Day" if success else "Unsuccessful Day"

    # Failure reasons
    reasons = []
    if TIR_pct < 70:
        reasons.append(f"TIR ({TIR_pct:.1f}%) is below 70%")
    if TBR_pct > 4:
        reasons.append(f"TBR ({TBR_pct:.1f}%) is above 4%")
    if TAR_pct > 25:
        reasons.append(f"TAR ({TAR_pct:.1f}%) is above 25%")
    if severe_pct > 1:
        reasons.append(f"Severe hypoglycemia ({severe_pct:.1f}%) is above 1%")

    user_id_unbalanced = user_id
    start_date_balanced = '2023-07-22'
    end_date_balanced = '2023-07-29'
    user_id_balanced = 3
    

    inference_txt= final_inference(start_date_balanced,end_date_balanced,user_id_balanced,user_id_unbalanced)
    inference_txt = str(inference_txt)
    return {
        "TIR_pct": round(TIR_pct, 2),
        "TBR_pct": round(TBR_pct, 2),
        "TAR_pct": round(TAR_pct, 2),
        "severe_pct": round(severe_pct, 2),
        "success_status": success_status,
        "failure_reasons": reasons,
        "inference":inference_txt

    }

@app.route('/san')
def home():
    return render_template('san.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json() or request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        user_id = int(data.get('user_id', -1))
        date_of_interest = data.get('date')

        if user_id == -1 or not date_of_interest:
            return jsonify({"error": "Missing user_id or date"}), 400

        result = test_success(user_id, date_of_interest)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500





@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/about')
def about(): 
    return render_template('about.html')


@app.route('/animetion')
def animation(): 
    return render_template('animation.html')


@app.route('/index3')
def index3(): 
    return render_template('index3.html')

@app.route('/blog')
def blog(): 
    return render_template('blog.html')


@app.route('/blog-details')
def blogd(): 
    return render_template('blog-details.html')


@app.route('/team')
def team(): 
    return render_template('team.html')

@app.route('/portfolio')
def portfolio(): 
    return render_template('portfolio.html')

@app.route('/portfolio-details')
def portfoliod(): 
    return render_template('portfolio-details.html')

@app.route('/services')
def services(): 
    return render_template('services.html')
@app.route('/service-details')
def servicesd(): 
    return render_template('service-details.html')



@app.route('/charts-apexcharts')

def chartsapexcharts(): 
    return render_template('charts-apexcharts.html')


@app.route('/charts-chartjs')

def chartschartjs(): 
    return render_template('charts-chartjs.html')


@app.route('/charts-echarts')

def chartsecharts(): 
    return render_template('charts-echarts.html')


@app.route('/components-accordion')

def componentsaccordion(): 
    return render_template('components-accordion.html')


@app.route('/components-alerts')

def componentsalerts(): 
    return render_template('components-alerts.html')


@app.route('/components-badges')

def componentsbadges(): 
    return render_template('components-badges.html')



@app.route('/components-breadcrumbs')

def ccomponentsbreadcrumbs(): 
    return render_template('components-breadcrumbs.html')

@app.route('/components-buttons')
def componentsbuttons(): 
    return render_template('components-buttons.html')

@app.route('/components-cards')
def componentscards(): 
    return render_template('components-cards.html')


@app.route('/components-carousel')
def componentscarousel(): 
    return render_template('components-carousel.html')


@app.route('/components-list-group')
def componentslistgroup(): 
    return render_template('components-list-group.html')


@app.route('/components-modal')
def componentsmodal(): 
    return render_template('components-modal.html')


@app.route('/components-pagination')
def ccomponentspagination(): 
    return render_template('components-pagination.html')

@app.route('/components-progress')
def componentsprogress(): 
    return render_template('components-progress.html')



@app.route('/components-spinners')
def componentsspinners(): 
    return render_template('components-spinners.html')


@app.route('/components-tabs')
def componentstabs(): 
    return render_template('components-tabs.html')


@app.route('/components-tooltips')
def componentstooltips(): 
    return render_template('components-tooltips.html')

@app.route('/san')
def san(): 
    return render_template('san.html')



@app.route('/users-profile')
def usersprofile(): 
    return render_template('users-profile.html')


@app.route('/pages-login')
def pageslogin(): 
    return render_template('pages-login.html')


@app.route('/pages-contact')
def pagescontact(): 
    return render_template('pages-contact.html')


@app.route('/forms-editors')
def formseditors(): 
    return render_template('forms-editors.html')


@app.route('/pages-faq')
def pagesfaq(): 
    return render_template('pages-faq.html')





# @app.route('/contact',methods=['POST','GET'])
# def contact():
#     query=Feedback.query.all()
#     if request.method=="POST":
#         name=request.form.get('name')
#         email=request.form.get('email')
#         subject=request.form.get('subject')
#         message=request.form.get('message')
#         feed=Feedback(name=name,email=email,subject=subject,message=message)
#         db.session.add(feed)
#         db.session.commit()
#         flash("feedback sent")
#         return redirect(url_for('signup'))

        
    # return render_template('contact.html',query=query)


if __name__== "__main__":
    app.run(debug=True)