from flask import Flask, render_template
import pandas as pd

# Local
import business as bus

app  = Flask(__name__)

district_codes = bus.read_district_json()
@app.route("/")
def home():

    mler_list = bus.get_data()

    return render_template(
        "index.html",
        top_list = mler_list
    )

@app.route("/leaderboard")
def get_leaderboard():

    u_districts = bus.get_unique_districts()
    
    return render_template(
        "leaderboard.html",
        unique_districts = u_districts,
        d_names = district_codes
    )


@app.route("/leaderboard/<district>")
def abc(district: str):

    district_code = bus.get_key_by_value(
        district_codes,
        district
    )  
    dist_top_list = bus.get_matched_rows_by_district_code(district_code)


    return render_template(
        "leaderboaed-district.html",
        district_top_list = dist_top_list
    )







if __name__ == '__main__':
    app.run(
        debug = True
    )