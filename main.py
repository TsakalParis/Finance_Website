from flask import Flask, request, render_template
from get_stock_data import get_stock_data

app = Flask(__name__)

@app.route("/")
def base():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def base_post():
    if request.method == 'POST':
        # Get the form data
        form_data = request.form

        ticker_1 = form_data["input-ticker1"]
        ticker_2 = form_data["input-ticker2"]
        start_date = form_data["input-start-date"]
        end_date = form_data["input-end-date"]
        tickers = [ticker_1, ticker_2]

        # Process the form data 
        result = get_stock_data(tickers, start_date, end_date)

        if type(result) == str:
            condition = True
            return render_template("base.html", result=result)
        else:
            stock_a, stock_b = result
            condition = False
            return render_template("base.html", results=[stock_a.to_html(classes="stock_a"),
            stock_b.to_html(classes="stock_b")], titles = ['na', ticker_1, ticker_2])

if __name__ == '__main__':
    app.run(debug=True)