import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="demo_db"
)
my_cursor = my_db.cursor()


def add_client_to_db(*data):
    try:
        sql = "INSERT INTO clienti (cnp,nume,prenume,loc_de_munca,functie,studii) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (data[0], data[1], data[2], data[3], data[4], data[5])
        my_cursor.execute(sql, val)
        my_db.commit()
    except Exception as e:
        return e
    else:
        return "Ok"


@app.route("/")
def show_home():
    return render_template("home_page.html")


@app.route("/get_client", methods=["POST"])
def get_client():
    name = request.form.get("name")
    prenume = request.form.get("prenume")
    cnp = request.form.get("cnp")
    loc_de_munca = request.form.get("loc_de_munca")
    functie = request.form.get("functie")
    studii = request.form.get("studii")
    result = add_client_to_db(cnp, name, prenume, loc_de_munca, functie, studii)
    if result == "Ok":
        print("Succes on adding client")
        return redirect(
            url_for("show_result", ok=1, name=name, cnp=cnp, prenume=prenume, loc_de_munca=loc_de_munca,
                    functie=functie,
                    studii=studii))
    else:
        print(result)
        return redirect(url_for("show_result", ok=0, error=result))


@app.route("/show_result")
def show_result():
    if request.args.get("ok") == 1:
        status = "Client added"
        return render_template("show_result.html", status=status, nume=request.args.get("name"),
                               prenume=request.args.get("prenume"),
                               cnp=request.args.get("cnp"), loc_de_munca=request.args.get("loc_de_munca"),
                               functie=request.args.get("functie"), studii=request.args.get("studii"))
    else:
        return render_template("show_result.html", status=request.args.get("error"))


if __name__ == '__main__':
    app.run(debug=True)
