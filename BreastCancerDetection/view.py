from model import InputForm
from flask import Flask, render_template, request
from keras.models import  load_model
import numpy as np

app = Flask(__name__)

@app.route('/view', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        model = load_model('breast_cancer_model.h5')
        arr = np.array([[form.A.data,form.B.data,form.C.data,form.D.data,form.E.data,form.F.data,form.G.data,form.H.data,form.I.data]],dtype=np.float32)
        result = model.predict(arr)
        if result >= 0.5:
            result = 'Malignant'
        else:
            result = 'Benign'

    else:
        result = None

    return render_template('webpage.html',form=form, result=result)

if __name__ == '__main__':
    app.run(debug=False,threaded=False) #fast tenserflow loadinf
