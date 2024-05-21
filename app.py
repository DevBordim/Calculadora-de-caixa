from flask import Flask, render_template, request

# Configure Flask para procurar templates na pasta raiz
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('templates/index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        din = float(request.form['din'].replace(',', '.')) if request.form['din'] else 0
        cre = float(request.form['cre'].replace(',', '.')) if request.form['cre'] else 0
        deb = float(request.form['deb'].replace(',', '.')) if request.form['deb'] else 0
        prazo = float(request.form['prazo'].replace(',', '.')) if request.form['prazo'] else 0
        pix = float(request.form['pix'].replace(',', '.')) if request.form['pix'] else 0
        chp = float(request.form['chp'].replace(',', '.')) if request.form['chp'] else 0
        cha = float(request.form['cha'].replace(',', '.')) if request.form['cha'] else 0
        rets = float(request.form['rets'].replace(',', '.')) if request.form['rets'] else 0
        encer = float(request.form['encer'].replace(',', '.')) if request.form['encer'] else 0
        crediario = float(request.form['crediario'].replace(',', '.')) if request.form['crediario'] else 0

        cards = cre + deb
        total = din + cre + deb + prazo + pix + chp + cha + rets + crediario
        resul = total - encer
        totaldin = din + rets

        if total < encer:
            status = f"O caixa está faltando: R$ {resul:.2f}"
        else:
            status = f"O caixa está sobrando: R$ {resul:.2f}"

        return render_template('templates/resultado.html', cards=f"Total cartões: R$ {cards:.2f}", total=f"O valor total é: R$ {total:.2f}", status=status, totaldin=f"Total dinheiro é: R$ {totaldin:.2f}")
    except ValueError:
        return "Erro de entrada: Por favor, insira apenas números válidos."

if __name__ == '__main__':
    app.run(debug=True)
