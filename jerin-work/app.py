from flask import Flask, render_template, request, redirect, url_for, session, flash
import pandas as pd
import const
import business
import json

app = Flask(__name__)
app.secret_key = 'abc-secretkey'

def get_dataframe():
    df = pd.read_excel(
        const.filename,
        sheet_name=const.sheetname,
        engine='openpyxl'
    )
    if 'Label' not in df.columns:
        df['Label'] = None
    return df

def load_admin_credentials():
    with open('admin.json', 'r') as file:
        return json.load(file)['admins']

def get_admin_id(username):
    admin_data = load_admin_credentials()
    print(f'admin data : {admin_data}')
    for admin in admin_data:
        if admin['username'] == username:
            return admin['admin_id']
    return None

@app.route("/admin", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin_data = load_admin_credentials()
        username = request.form['username']
        password = request.form['password']

        for admin in admin_data:
            if username == admin['username'] and password == admin['password']:
                session['logged_in'] = True
                session['username'] = username
                session['admin_id'] = get_admin_id(username)
                return redirect(url_for('dashboard'))

        flash('Invalid credentials, please try again.', 'error')
        return redirect(url_for('admin_login'))

    return render_template('admin_login.html')


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))

    df = get_dataframe()

    if request.method == 'POST':
        index = int(request.form['index'])
        
        if 'update' in request.form:
            new_label = request.form['Label']
            if not new_label.strip():
                new_label = "value not added"
            df.at[index, 'Label'] = new_label

            # Update the score in the dataframe
            admin_id = session.get('admin_id')
            df.at[index, admin_id] = new_label

        elif 'delete' in request.form:
            df = df.drop(index).reset_index(drop=True)
            index = max(index - 1, 0)

        business.save_df_to_excel(df, const.filename, const.sheetname)
        return redirect(url_for('dashboard', index=index))

    index = request.args.get('index', 0, type=int)
    print(f"1st index:{index}")
    if index < 0:
        index = 0
    elif index >= len(df):
        index = len(df) - 1

    row_exists = not df.empty
    row = df.iloc[index].to_dict() if row_exists else None
    print(f"row:{row}")

    return render_template(
        'index.html',
        row=row,
        index=index,
        total_rows=len(df),
        row_exists=row_exists,
        username=session.get('username')
    )

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for('dashboard'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('admin_login'))

if __name__ == "__main__":
    app.run(
        port=2878,
        debug=True
    )