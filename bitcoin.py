from flask import Flask,render_template,request
import requests
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('SearchBitcoin.html')
@app.route('/data', methods=['POST'])
def coin():
    info = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json')
    r_json = info.json()
    time=r_json['time']['updated']
    #USD

    USD_code=r_json['bpi']['USD']['code']
    USD_symbol=str(r_json['bpi']['USD']['symbol'])
    USD_Desc=r_json['bpi']['USD']['description']
    USD_rate=r_json['bpi']['USD']['rate_float']
    # GBP

    GBP_code = r_json['bpi']['GBP']['code']
    GBP_symbol = r_json['bpi']['GBP']['symbol']
    GBP_Desc = r_json['bpi']['GBP']['description']
    GBP_rate = r_json['bpi']['GBP']['rate_float']
    # EUR

    EUR_code = r_json['bpi']['EUR']['code']
    EUR_symbol = r_json['bpi']['EUR']['symbol']
    EUR_Desc = r_json['bpi']['EUR']['description']
    EUR_rate = r_json['bpi']['EUR']['rate_float']
    return render_template("data.html",Time=time,Ucode=USD_code,Usymbol=USD_symbol,Udesc=USD_Desc,Urate=USD_rate
                           ,Gcode=GBP_code,Gsymbol=GBP_symbol,Gdesc=GBP_Desc,Grate=GBP_rate
                           ,Ecode=EUR_code,Esymbol=EUR_symbol,Edesc=EUR_Desc,Erate=EUR_rate)



if __name__=='__main__':
    app.run(debug=True)