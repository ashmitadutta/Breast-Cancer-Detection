from wtforms import FloatField, Form, validators

class InputForm(Form):
    A = FloatField(
        label='Clump Thickness',
        validators=[validators.InputRequired()])
    B = FloatField(
        label='Uniformity of Cell Size',
        validators=[validators.InputRequired()])
    C = FloatField(
        label='Uniformity of Cell Shape',
        validators=[validators.InputRequired()])
    D = FloatField(
        label='Marginal Adhesion',
        validators=[validators.InputRequired()])
    E = FloatField(
        label='Single Epithelial Cell Size',
        validators=[validators.InputRequired()])
    F = FloatField(
        label='Bare Nuclei',
        validators=[validators.InputRequired()])
    G = FloatField(
        label='Bland Chromatin',
        validators=[validators.InputRequired()])
    H = FloatField(
        label='Normal Nucleoli',
        validators=[validators.InputRequired()])
    I = FloatField(
        label='Mitoses',
        validators=[validators.InputRequired()])