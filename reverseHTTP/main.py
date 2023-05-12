from datetime import datetime
from flask import Flask, request, redirect, send_file, send_from_directory, url_for 
from datetime import datetime
app = Flask(__name__)


@app.route('/file/<name>', methods=['POST'])
def add_file(name):
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/'+name)
        return 'file uploaded successfully'

@app.route('/file/<name>', methods=['GET'])
def serve_file(name):
    return send_from_directory('uploads', name)

@app.route('/log/<name>', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTION'])
def index(name):
    # write everything here in file
    # name is the name of the file
    #
    #
    file = open(name, 'a')
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    file.write('\n')
    file.write('####################\n')
    file.write('# header\n')
    file.write('####################\n')
    file.write('\n')
    file.write(str(request.headers))


    file.write('####################\n')
    file.write('# Cookies\n')
    file.write('####################\n')
    for key, value in request.cookies.items():
        file.write(str(key) + ' : ' + str(value) + '\n')
    file.write('\n')

    file.write('####################\n')
    file.write('# Url\n')
    file.write('####################\n')
    file.write(request.url + '\n')
    file.write('\n')


    file.write('####################\n')
    file.write('# Data\n')
    file.write('####################\n')
    file.write(str(request.data)+ '\n')
    file.write(str(request.form)+ '\n')
    file.write(str(request.args)+ '\n')
    file.write(str(request.get_data())+ '\n')
    file.write('\n')


   
    file.close()
    return ''

@app.route('/gl/<name>')
def get_file(name):
    file = open(name, 'r')
    return file.read()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
