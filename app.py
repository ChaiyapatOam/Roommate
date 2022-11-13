from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from roommate import Bill, RoomMate

app = Flask("Home")

class Home(MethodView):
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform = bill_form)

class ResultPage(MethodView):
    def post(self):
        form = BillForm(request.form)

        bill = Bill(float(form.amount.data), form.period.data)
        roommate1 = RoomMate(form.roommate1.data, float(form.days1.data))
        roommate2 = RoomMate(form.roommate2.data, float(form.days2.data))
        return f"{roommate1.name} pays {roommate1.pay(bill, roommate2)} <br/> {roommate2.name} pays {roommate2.pay(bill, roommate1)}"

class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    roommate1 = StringField("Name: ")
    days1 = StringField("How many days?: ")
    roommate2 = StringField("Name: ")
    days2 = StringField("How many days?: ")

    button = SubmitField("Calculate")


# app.add_url_rule('/', view_func=Home.as_view('home_page'))
app.add_url_rule('/', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))


app.run(debug = True)