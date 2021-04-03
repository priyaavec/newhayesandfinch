import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect, url_for, send_file,render_template
import datetime
from datetime import datetime
import json
import gspread
import numpy as np
from pandas import DataFrame
from oauth2client.service_account import ServiceAccountCredentials
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        description = request.form['description']
        container_type = request.form['container_type']
        product_code = request.form['product_code']
        fragnance_type = request.form['fragnance_type']
        customer = request.form['customer']
        wax_type = request.form['wax_type']
        production_quantity = request.form['production_quantity']
        sustainer_type = request.form['sustainer_type']

        time1 = request.form['time1']
        time2 = request.form['time2']
        time3 = request.form['time3']
        time4 = request.form['time4']
        time5 = request.form['time5']
        time6 = request.form['time6']
        time7 = request.form['time7']
        time8 = request.form['time8']
        time9 = request.form['time9']
        time10 = request.form['time10']
        time11 = request.form['time11']
        time12 = request.form['time12']

        flame1 = request.form['flame1']
        flame2 = request.form['flame2']
        flame3 = request.form['flame3']
        flame4 = request.form['flame4']
        flame5 = request.form['flame5']
        flame6 = request.form['flame6']
        flame7 = request.form['flame7']
        flame8 = request.form['flame8']
        flame9 = request.form['flame9']
        flame10 = request.form['flame10']
        flame11 = request.form['flame11']
        flame12 = request.form['flame12']

        tolerance1 = request.form['tolerance1']
        tolerance2 = request.form['tolerance2']
        tolerance3 = request.form['tolerance3']
        tolerance4 = request.form['tolerance4']
        tolerance5 = request.form['tolerance5']
        tolerance6 = request.form['tolerance6']
        tolerance7 = request.form['tolerance7']
        tolerance8 = request.form['tolerance8']
        tolerance9 = request.form['tolerance9']
        tolerance10 = request.form['tolerance10']
        tolerance11 = request.form['tolerance11']
        tolerance12 = request.form['tolerance12']

        accept1 = request.form['accept1']
        accept2 = request.form['accept2']
        accept3 = request.form['accept3']
        accept4 = request.form['accept4']
        accept5 = request.form['accept5']
        accept6 = request.form['accept6']
        accept7 = request.form['accept7']
        accept8 = request.form['accept8']
        accept9 = request.form['accept9']
        accept10 = request.form['accept10']
        accept11 = request.form['accept11']
        accept12 = request.form['accept12']

        above1 = request.form['above1']
        above2 = request.form['above2']
        above3 = request.form['above3']
        above4 = request.form['above4']
        above5 = request.form['above5']
        above6 = request.form['above6']
        above7 = request.form['above7']
        above8 = request.form['above8']
        above9 = request.form['above9']
        above10 = request.form['above10']
        above11 = request.form['above11']
        above12 = request.form['above12']

        trim1 = request.form['trim1']
        trim2 = request.form['trim2']
        trim3 = request.form['trim3']
        trim4 = request.form['trim4']
        trim5 = request.form['trim5']
        trim6 = request.form['trim6']
        trim7 = request.form['trim7']
        trim8 = request.form['trim8']
        trim9 = request.form['trim9']
        trim10 = request.form['trim10']
        trim11 = request.form['trim11']
        trim12 = request.form['trim12']

        evidence1 = request.form['evidence1']
        evidence2 = request.form['evidence2']
        evidence3 = request.form['evidence3']
        evidence4 = request.form['evidence4']
        evidence5 = request.form['evidence5']
        evidence6 = request.form['evidence6']
        evidence7 = request.form['evidence7']
        evidence8 = request.form['evidence8']
        evidence9 = request.form['evidence9']
        evidence10 = request.form['evidence10']
        evidence11 = request.form['evidence11']
        evidence12 = request.form['evidence12']

        evidence1 = request.form['evidence1']
        evidence2 = request.form['evidence2']
        evidence3 = request.form['evidence3']
        evidence4 = request.form['evidence4']
        evidence5 = request.form['evidence5']
        evidence6 = request.form['evidence6']
        evidence7 = request.form['evidence7']
        evidence8 = request.form['evidence8']
        evidence9 = request.form['evidence9']
        evidence10 = request.form['evidence10']
        evidence11 = request.form['evidence11']
        evidence12 = request.form['evidence12']

        tunnel1 = request.form['tunnel1']
        tunnel2 = request.form['tunnel2']
        tunnel3 = request.form['tunnel3']
        tunnel4 = request.form['tunnel4']
        tunnel5 = request.form['tunnel5']
        tunnel6 = request.form['tunnel6']
        tunnel7 = request.form['tunnel7']
        tunnel8 = request.form['tunnel8']
        tunnel9 = request.form['tunnel9']
        tunnel10 = request.form['tunnel10']
        tunnel11 = request.form['tunnel11']
        tunnel12 = request.form['tunnel12']

        club1 = request.form['club1']
        club2 = request.form['club2']
        club3 = request.form['club3']
        club4 = request.form['club4']
        club5 = request.form['club5']
        club6 = request.form['club6']
        club7 = request.form['club7']
        club8 = request.form['club8']
        club9 = request.form['club9']
        club10 = request.form['club10']
        club11 = request.form['club11']
        club12 = request.form['club12']

        melt1 = request.form['melt1']
        melt2 = request.form['melt2']
        melt3 = request.form['melt3']
        melt4 = request.form['melt4']
        melt5 = request.form['melt5']
        melt6 = request.form['melt6']
        melt7 = request.form['melt7']
        melt8 = request.form['melt8']
        melt9 = request.form['melt9']
        melt10 = request.form['melt10']
        melt11 = request.form['melt11']
        melt12 = request.form['melt12']#

        afterglow1 = request.form['afterglow1']
        afterglow2 = request.form['afterglow2']
        afterglow3 = request.form['afterglow3']
        afterglow4 = request.form['afterglow4']
        afterglow5 = request.form['afterglow5']
        afterglow6 = request.form['afterglow6']
        afterglow7 = request.form['afterglow7']
        afterglow8 = request.form['afterglow8']
        afterglow9 = request.form['afterglow9']
        afterglow10 = request.form['afterglow10']
        afterglow11 = request.form['afterglow11']
        afterglow12 = request.form['afterglow12']

        candle_weight1 = request.form['candle_weight1']
        candle_weight2 = request.form['candle_weight2']
        candle_weight3 = request.form['candle_weight3']
        candle_weight4 = request.form['candle_weight4']
        candle_weight5 = request.form['candle_weight5']
        candle_weight6 = request.form['candle_weight6']
        candle_weight7 = request.form['candle_weight7']
        candle_weight8 = request.form['candle_weight8']
        candle_weight9 = request.form['candle_weight9']
        candle_weight10 = request.form['candle_weight10']
        candle_weight11 = request.form['candle_weight11']
        candle_weight12 = request.form['candle_weight12']

        burn_rate1 = request.form['burn_rate1']
        burn_rate2 = request.form['burn_rate2']
        burn_rate3 = request.form['burn_rate3']
        burn_rate4 = request.form['burn_rate4']
        burn_rate5 = request.form['burn_rate5']
        burn_rate6 = request.form['burn_rate6']
        burn_rate7 = request.form['burn_rate7']
        burn_rate8 = request.form['burn_rate8']
        burn_rate9 = request.form['burn_rate9']
        burn_rate10 = request.form['burn_rate10']
        burn_rate11 = request.form['burn_rate11']
        burn_rate12 = request.form['burn_rate12']

        temp_start1 = request.form['temp_start1']
        temp_start2 = request.form['temp_start2']
        temp_start3 = request.form['temp_start3']
        temp_start4 = request.form['temp_start4']
        temp_start5 = request.form['temp_start5']
        temp_start6 = request.form['temp_start6']
        temp_start7 = request.form['temp_start7']
        temp_start8 = request.form['temp_start8']
        temp_start9 = request.form['temp_start9']
        temp_start10 = request.form['temp_start10']
        temp_start11 = request.form['temp_start11']
        temp_start12 = request.form['temp_start12']

        temp_end1 = request.form['temp_end1']
        temp_end2 = request.form['temp_end2']
        temp_end3 = request.form['temp_end3']
        temp_end4 = request.form['temp_end4']
        temp_end5 = request.form['temp_end5']
        temp_end6 = request.form['temp_end6']
        temp_end7 = request.form['temp_end7']
        temp_end8 = request.form['temp_end8']
        temp_end9 = request.form['temp_end9']
        temp_end10 = request.form['temp_end10']
        temp_end11 = request.form['temp_end11']
        temp_end12 = request.form['temp_end12']

        test_carried_by = request.form['test_carried_by']
        position = request.form['position']
        signature = request.form['signature']
        date = request.form['date']
        comment = request.form['comment']
        import time
        start_time = time.time()
        file_location = uploadfile()
        result = [description, container_type, product_code, fragnance_type, customer, wax_type, production_quantity, sustainer_type,
                  time1, time2, time3, time4, time5, time6, time7, time8, time9, time10, time11, time12,
                  flame1, flame2, flame3, flame4, flame5, flame6, flame7, flame8, flame9, flame10, flame11, flame12,
                  tolerance1, tolerance2, tolerance3, tolerance4, tolerance5, tolerance6, tolerance7, tolerance8, tolerance9, tolerance10, tolerance11, tolerance12,
                  accept1, accept2, accept3, accept4, accept5, accept6, accept7, accept8, accept9, accept10, accept11, accept12,
                  above1, above2, above3, above4, above5, above6, above7, above8, above9, above10, above11, above12,
                  trim1, trim2, trim3, trim4, trim5, trim6, trim7, trim8, trim9, trim10, trim11, trim12,
                  evidence1, evidence2, evidence3, evidence4, evidence5, evidence6, evidence7, evidence8, evidence9, evidence10, evidence11, evidence12,
                  tunnel1, tunnel2, tunnel3, tunnel4, tunnel5, tunnel6, tunnel7, tunnel8, tunnel9, tunnel10, tunnel1, tunnel2,
                  club1, club2, club3, club4, club5, club6, club7, club8, club9, club10, club11, club12,
                  melt1, melt2, melt3, melt4, melt5, melt6, melt7, melt8, melt9, melt10, melt11, melt12,
                  afterglow1, afterglow2, afterglow3, afterglow4, afterglow5, afterglow6, afterglow7, afterglow8, afterglow9, afterglow10, afterglow11, afterglow12,
                  candle_weight1, candle_weight2, candle_weight3, candle_weight4, candle_weight5, candle_weight6, candle_weight7, candle_weight8, candle_weight9, candle_weight10, candle_weight11, candle_weight12,
                  burn_rate1, burn_rate2, burn_rate3, burn_rate4, burn_rate5, burn_rate6, burn_rate7, burn_rate8, burn_rate9, burn_rate10, burn_rate11, burn_rate12,
                  temp_start1, temp_start2, temp_start3, temp_start4, temp_start5, temp_start6, temp_start7, temp_start8, temp_start9, temp_start10, temp_start11, temp_start12,
                  temp_end1, temp_end2, temp_end3, temp_end4, temp_end5, temp_end6, temp_end7, temp_end8, temp_end9, temp_end10, temp_end11, temp_end12,
                  test_carried_by, position, signature, date, comment, file_location]

        recordcount = insertdata(result)
        print("--- %s seconds ---" % (time.time() - start_time))
        return render_template('success.html', result=result, recordcount = recordcount, file_location = file_location)
    return render_template('form.html')


@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
    data_frame = showdata()
    #datatype = type(data)
    return render_template("show_data.html", tables=[data_frame.to_html(classes='data')], column_names=data_frame.columns.values, row_data=list(data_frame.values.tolist()), zip=zip)

def connecttoexcel():
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds1 = ServiceAccountCredentials.from_json_keyfile_name("hayesandfinch.json", scope)
    client = gspread.authorize(creds1)
    sheet = client.open("hayes1").sheet1
    return sheet

def insertdata(result):
    sheet = connecttoexcel()
    data = sheet.get_all_records()
    now = datetime.now()
    dateandtime = now.strftime("%d/%m/%Y, %H:%M:%S")
    print("date and time:", dateandtime)
    result.insert(0, dateandtime)
    sheet.insert_row(result, len(data)+2)
    return len(data)

def showdata():
    sheet = connecttoexcel()
    data = sheet.get_all_records()
    data_df = DataFrame(data,
                        columns=['DATE','DESCRIPTION', 'CONTAINER TYPE', 'PRODUCT CODE', 'FRAGRANCE TYPE + %', 'CUSTOMER',
                                 'WAX TYPE', 'PRODUCTION QTY', 'SUSTAINER TYPE',
                                 'start time', 'time after 4 HRS', 'time after 8 HRS', 'time after 12 HRS',
                                 'time after 16 HRS', 'time after 20 HRS', 'time after 24 HRS',
                                 'time after 28 HRS', 'time after 32 HRS', 'time after 36 HRS', 'time after 40 HRS',
                                 'time TBH',
                                 'Flame Height 0HR', 'Flame Height 4HR', 'Flame Height 8HR', 'Flame Height 12HR',
                                 'Flame Height 16HR', 'Flame Height 20HR', 'Flame Height 24HR', 'Flame Height 28HR',
                                 'Flame Height 32HR', 'Flame Height 36HR', 'Flame Height 40HR', 'Flame Height TBH',
                                 'Below Tolerance 0HR', 'Below Tolerance 4HR', 'Below Tolerance 8HR',
                                 'Below Tolerance 12HR', 'Below Tolerance 16HR', 'Below Tolerance 20HR',
                                 'Below Tolerance 24HR', 'Below Tolerance 28HR', 'Below Tolerance 32HR',
                                 'Below Tolerance 36HR', 'Below Tolerance 40HR', 'Below Tolerance TBH',
                                 'Acceptable: xxmm 0HR','Acceptable: xxmm 4HR', 'Acceptable: xxmm 8HR', 'Acceptable: xxmm 12HR',
                                 'Acceptable: xxmm 16HR','Acceptable: xxmm 20HR', 'Acceptable: xxmm 24HR',
                                 'Acceptable: xxmm 28HR','Acceptable: xxmm 32HR', 'Acceptable: xxmm 36HR',
                                 'Acceptable: xxmm 40HR','Acceptable: xxmm TBH',
                                 'Above Tolerance 0HR','Above Tolerance 4HR', 'Above Tolerance 8HR',
                                 'Above Tolerance 12HR', 'Above Tolerance 16HR', 'Above Tolerance 20HR',
                                 'Above Tolerance 24HR', 'Above Tolerance 28HR', 'Above Tolerance 32HR',
                                 'Above Tolerance 36HR', 'Above Tolerance 40HR', 'Above Tolerance TBH',
                                 'Wick Needs Trimming? 0HR', 'Wick Needs Trimming? 4HR', 'Wick Needs Trimming? 8HR',
                                 'Wick Needs Trimming? 12HR', 'Wick Needs Trimming? 16HR', 'Wick Needs Trimming? 20HR',
                                 'Wick Needs Trimming? 24HR', 'Wick Needs Trimming? 28HR', 'Wick Needs Trimming? 32HR',
                                 'Wick Needs Trimming? 36HR', 'Wick Needs Trimming? 40HR', 'Wick Needs Trimming? TBH',
                                 'Evidence of Sooting? 0HR', 'Evidence of Sooting? 4HR', 'Evidence of Sooting? 8HR',
                                 'Evidence of Sooting? 12HR', 'Evidence of Sooting? 16HR', 'Evidence of Sooting? 20HR',
                                 'Evidence of Sooting? 24HR', 'Evidence of Sooting? 28HR', 'Evidence of Sooting? 32HR',
                                 'Evidence of Sooting? 36HR', 'Evidence of Sooting? 40HR', 'Evidence of Sooting? TBH',
                                 'Candle Tunnel? Y / N 0HR', 'Candle Tunnel? Y / N 4HR', 'Candle Tunnel? Y / N 8HR',
                                 'Candle Tunnel? Y / N 12HR', 'Candle Tunnel? Y / N 16HR', 'Candle Tunnel? Y / N 20HR',
                                 'Candle Tunnel? Y / N 24HR', 'Candle Tunnel? Y / N 28HR', 'Candle Tunnel? Y / N 28HR',
                                 'Candle Tunnel? Y / N 32HR', 'Candle Tunnel? Y / N 36HR', 'Candle Tunnel? Y / N 40HR',
                                 'Candle Tunnel? Y / N TBH',
                                 'Clubbing MIN / MAX 0HR', 'Clubbing MIN / MAX 4HR', 'Clubbing MIN / MAX 8HR',
                                 'Clubbing MIN / MAX 12HR', 'Clubbing MIN / MAX 16HR', 'Clubbing MIN / MAX 20HR',
                                 'Clubbing MIN / MAX 24HR', 'Clubbing MIN / MAX 28HR', 'Clubbing MIN / MAX 32HR',
                                 'Clubbing MIN / MAX 36HR', 'Clubbing MIN / MAX 40HR', 'Clubbing MIN / MAX TBH',
                                 'Melt pool diameter 0HR', 'Melt pool diameter 4HR', 'Melt pool diameter 8HR',
                                 'Melt pool diameter 12HR', 'Melt pool diameter 16HR', 'Melt pool diameter 20HR',
                                 'Melt pool diameter 24HR', 'Melt pool diameter 28HR', 'Melt pool diameter 32HR',
                                 'Melt pool diameter 36HR', 'Melt pool diameter 40HR', 'Melt pool diameter TBH',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 0HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 4HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 8HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 12HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 16HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 20HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 24HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 28HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 32HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 36HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) 40HR',
                                 'Afterglow within Tolerance? (<20 secs after extinguishing) TBH',
                                 'Candle Weight (g) 0HR', 'Candle Weight (g) 4HR', 'Candle Weight (g) 8HR',
                                 'Candle Weight (g) 12HR', 'Candle Weight (g) 16HR', 'Candle Weight (g) 20HR',
                                 'Candle Weight (g) 24HR', 'Candle Weight (g) 28HR', 'Candle Weight (g) 32HR',
                                 'Candle Weight (g) 36HR', 'Candle Weight (g) 40HR', 'Candle Weight (g) TBH',
                                 'Burn Rate (g/hr) 0HR', 'Burn Rate (g/hr) 4HR', 'Burn Rate (g/hr) 8HR',
                                 'Burn Rate (g/hr) 12HR', 'Burn Rate (g/hr) 16HR', 'Burn Rate (g/hr) 20HR',
                                 'Burn Rate (g/hr) 24HR', 'Burn Rate (g/hr) 28HR', 'Burn Rate (g/hr) 32HR',
                                 'Burn Rate (g/hr) 36HR', 'Burn Rate (g/hr) 40HR', 'Burn Rate (g/hr) TBH',
                                 'Room Temp Start of test 0HR', 'Room Temp Start of test 4HR',
                                 'Room Temp Start of test 8HR', 'Room Temp Start of test 12HR',
                                 'Room Temp Start of test 16HR', 'Room Temp Start of test 20HR',
                                 'Room Temp Start of test 24HR', 'Room Temp Start of test 28HR',
                                 'Room Temp Start of test 32HR', 'Room Temp Start of test 36HR',
                                 'Room Temp Start of test 40HR', 'Room Temp Start of test TBH',
                                 'Room Temp End of test 0HR', 'Room Temp End of test 4HR', 'Room Temp End of test 8HR',
                                 'Room Temp End of test 12HR', 'Room Temp End of test 16HR',
                                 'Room Temp End of test 20HR', 'Room Temp End of test 24HR',
                                 'Room Temp End of test 28HR', 'Room Temp End of test 32HR',
                                 'Room Temp End of test 36HR', 'Room Temp End of test TBH',
                                 'Test Carried Out By', 'Position', 'Signature', 'Date', 'Comment', 'Candle Image'])
    data_df.fillna('-')
    data_df.replace(np.nan, '')
    return data_df

def uploadfile():
    if 'file' not in request.files:
        print('no file')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        print('no filename')
        return redirect(request.url)
    else:
        fileupload = resize(file)
        filename = secure_filename(file.filename)
        fileupload.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        print("saved file successfully")
        file_location = uploadtodrive(file.filename)
    return file_location

import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']

def get_gdrive_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # return Google Drive API service
    return build('drive', 'v3', credentials=creds)


def uploadtodrive(filename):
    # import json
    # import requests
    # headers = {
    #     "Authorization": "Bearer ya29.a0AfH6SMB6XBKvN5U5Gtx5167K3GNWnyvDyAWLsguOFvB5rYgIKwysm9NwGLoAwarhNmOpMwftuBiti89UHIi6lFQDI3lRoE3L5u2O12-l-CdTrV-5lPl8eGKL56bh0EZOr41g-ogGLxRC4lllV7hEHvMbe9ln"}
    # para = {
    #     "name": filename,
    #     "parents": ["1sz_WI0MNEaHn5GPJxpg3rvyIrd6ujowE"]
    # }
    # files = {
    #     'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    #     'file': open("./uploads/"+filename, "rb")
    # }
    # r = requests.post(
    #     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    #     headers=headers,
    #     files=files
    # )
    # y = json.loads(r.text)
    # file_location = "https://drive.google.com/file/d/" + y['id'] + "/view"
    #get_gdrive_service()
    from pygdrive3 import service

    drive_service = service.DriveService('./client_secrets.json')
    drive_service.auth()
    file = drive_service.upload_file(filename, './uploads/'+filename, "1sz_WI0MNEaHn5GPJxpg3rvyIrd6ujowE",mime_type="image/*")
    file_location = "https://drive.google.com/file/d/" + file + "/view"
    print(file_location)
    return file_location

def resize(file):
    import PIL
    from PIL import Image
    image = Image.open(file)
    width, height = image.size
    image = image.resize((width // 2, height // 2))
    #image.save('./uploads/'+file)
    return image

if __name__ == "__main__":
    app.run(port=8080, debug=True)
