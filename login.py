from flask import Flask, request, jsonify, render_template
import os
import crypt
DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form['name']
        password = request.form['password']
        np = crypt.crypt(password, 'ww')
        cmd = 'useradd -d /home/%s -m -p %s %s' % (name, np, name)
        print cmd
        os.system(cmd)

        return render_template('index.html', suc=True, name=name, password=password)


if __name__ == '__main__':
    app.run(port=9090, host='0.0.0.0')
