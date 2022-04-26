from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.datetime import DateField, DateTimeField, TimeField
from wtforms.fields.simple import TextAreaField

class Formulario_de_registro(Form):
    nome = StringField('Nome', [validators.Length(min=4, max=25)])
    nome_consultorio = StringField('Nome do Consultório', [validators.Length(min=4, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senhas precisam ser iguais')
    ])
    confirm = PasswordField('Confirmação de senha')

class Formulario_login(Form):

    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('Senha', [validators.DataRequired()])

class Formulario_cadastro_sala(Form):

    nome = StringField('Nome da Sala', [validators.Length(min=4, max=25)])

class Formulario_registro_psicopedagogo(Form):

    nome = StringField('Nome', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    cpf = StringField('CPF', [validators.Length(min=11, max=11)])
    rg = StringField('RG', [validators.Length(min=8, max=9)])
    telefone = StringField('Telefone', [validators.Length(min=6, max=35)])

class Formulario_registro_paciente(Form):

    nome = StringField('Nome', [validators.Length(min=4, max=25)])
    cpf = StringField('CPF')
    data_de_nascimento = DateField('Data de nascimento')
    rg = StringField('RG')
    tel = StringField('Telefone')
    email = StringField('Email')
    nome_r = StringField('Nome do Responsável', [validators.Length(min=4, max=25)])
    cpf_r = StringField('CPF do Responsável', [validators.Length(min=11, max=11)])
    rg_r = StringField('RG do Responsável')
    tel_r = StringField('Telefone do Responsável')
    email_r = StringField('Email do Responsável')
    serie_atual = StringField("Série Atual")

    obs = TextAreaField("Observações")


class Formulario_resgistro_agendamento(Form):

    hora = TimeField("Hora")
    obs = TextAreaField("Observações")

class Formulario_registro_escola(Form):

    nome = StringField("Nome", [validators.Length(min=4, max=25)])
    endereco = StringField("Endereço", [validators.Length(min=4, max=50)])
    telefone = StringField("Telefone", [validators.Length(min=9, max=15)])

class Formulario_registro_coordenador(Form):

    nome = StringField("Nome", [validators.Length(min=4, max=25)])
    telefone = StringField("Telefone", [validators.Length(min=9, max=15)])

class Formulario_cadastro_situacao(Form):

    nome = StringField('Situação', [validators.Length(min=4, max=25)])
