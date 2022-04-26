from flask import session
from sqlalchemy.orm import backref
from consultorio import db

class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    nome_consultorio = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.nome_usuario

class Acesso(db.Model):

    acesso_ID = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), unique=False, nullable=False)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref = db.backref('pessoas', lazy = True))

class Sexo(db.Model):

    sexo_ID = db.Column(db.Integer, primary_key=True)
    sexo_Nome = db.Column(db.String(15), primary_key=True)

class Pessoa(db.Model):

    pessoa_ID = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    data_de_nascimento = db.Column(db.Date)
    sexo_ID = db.Column(db.Integer, db.ForeignKey('sexo.sexo_ID'))
    sexo = db.relationship('Sexo', foreign_keys= sexo_ID)
    cpf = db.Column(db.String(11), unique = False, nullable=True)
    rg = db.Column(db.String(9), unique = False, nullable=True)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario')

class Psicopedagogo(db.Model):
    
    psicopedagogo_ID = db.Column(db.Integer, primary_key=True)
    pessoa_ID = db.Column(db.Integer, db.ForeignKey('pessoa.pessoa_ID'), nullable=False)
    pessoa = db.relationship('Pessoa', foreign_keys=pessoa_ID)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

class Tipo_contato(db.Model):

    tipo_ID = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer, nullable=False)

class Escola(db.Model):

    escola_ID = db.Column(db.Integer, primary_key=True)
    escola_nome = db.Column(db.String(30))
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

class Coordenador(db.Model):

    coordenador_ID = db.Column(db.Integer, primary_key=True)
    coordenador_nome = db.Column(db.String(30))
    escola_ID = db.Column(db.Integer, db.ForeignKey('escola.escola_ID'))
    escola = db.relationship('Escola', foreign_keys=escola_ID)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

class Contato(db.Model):

    contato_ID = db.Column(db.Integer, primary_key=True)
    pessoa_ID = db.Column(db.Integer, db.ForeignKey('pessoa.pessoa_ID'))
    pessoa = db.relationship('Pessoa', foreign_keys=pessoa_ID)
    escola_ID = db.Column(db.Integer, db.ForeignKey('escola.escola_ID'))
    escola = db.relationship('Escola', foreign_keys=escola_ID)
    coordenador_ID = db.Column(db.Integer, db.ForeignKey('coordenador.coordenador_ID'))
    coordenador = db.relationship('Coordenador', foreign_keys=coordenador_ID)
    tipo_ID = db.Column(db.Integer, db.ForeignKey('tipo_contato.tipo_ID'), nullable=False)
    tipo = db.relationship('Tipo_contato', foreign_keys=tipo_ID)
    contato = db.Column(db.String(50), nullable=False)


class Agenda_atendimento(db.Model):
        
    psicopedagogo_ID = db.Column(db.Integer, db.ForeignKey('psicopedagogo.psicopedagogo_ID'), primary_key=True)
    psicopedagogo = db.relationship('Psicopedagogo', backref = db.backref('psicopedagogos', lazy = True))
    dia = db.Column(db.Integer, nullable= False)
    hora = db.Column(db.Integer, nullable= False)


class Situacao(db.Model):
    
    situacao_ID = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable= False)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

class Paciente(db.Model):

    paciente_ID = db.Column(db.Integer, primary_key=True)
    pessoa_ID = db.Column(db.Integer, db.ForeignKey('pessoa.pessoa_ID'), nullable=False)
    pessoa = db.relationship('Pessoa',foreign_keys =pessoa_ID, backref = db.backref('pacientes', lazy = True))
    responsavel_ID = db.Column(db.Integer, db.ForeignKey('pessoa.pessoa_ID'))
    responsavel = db.relationship("Pessoa", foreign_keys= responsavel_ID)
    situacao_ID = db.Column(db.Integer, db.ForeignKey('situacao.situacao_ID'), nullable=False)
    situacao = db.relationship('Situacao', backref = db.backref('pacientes', lazy = True))
    psicopedagogo_ID = db.Column(db.Integer, db.ForeignKey('psicopedagogo.psicopedagogo_ID'))
    psicopedagogo = db.relationship('Psicopedagogo', foreign_keys= psicopedagogo_ID)
    escola_ID = db.Column(db.Integer, db.ForeignKey('escola.escola_ID'))
    escola = db.relationship('Escola', foreign_keys=escola_ID)
    coordenador_ID = db.Column(db.Integer, db.ForeignKey('coordenador.coordenador_ID'))
    coordenador = db.relationship('Coordenador', foreign_keys=coordenador_ID)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)
    obs = db.Column(db.String(500))

class Sala(db.Model):

    sala_ID = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable = False)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

class Atendimento(db.Model):

    atendimento_ID = db.Column(db.Integer, primary_key=True)
    psicopedagogo_ID = db.Column(db.Integer, db.ForeignKey('psicopedagogo.psicopedagogo_ID'))
    psicopedagogo = db.relationship('Psicopedagogo')
    data_hora = db.Column(db.DateTime, nullable = False)
    paciente_ID = db.Column(db.Integer, db.ForeignKey('paciente.paciente_ID'))
    paciente = db.relationship('Paciente', backref = db.backref('pacientes', lazy = True))

    sala_ID = db.Column(db.Integer, db.ForeignKey('sala.sala_ID'))
    sala = db.relationship('Sala', backref = db.backref('salas', lazy = True))

    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

    obs = db.Column(db.String(500))

class Tipo_endereco(db.Model):

    __tablename__ = 'tipo_endereco'
        
    tipo_ID = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20))

class Endereco(db.Model):
        
    endereco_ID = db.Column(db.Integer, primary_key=True)
    tipo_ID = db.Column(db.Integer, db.ForeignKey('tipo_endereco.tipo_ID'))
    tipo = db.relationship('Tipo_endereco')
    pessoa_ID = db.Column(db.Integer, db.ForeignKey('pessoa.pessoa_ID'))
    pessoa = db.relationship('Pessoa', foreign_keys=pessoa_ID)
    escola_ID = db.Column(db.Integer, db.ForeignKey('escola.escola_ID'))
    escola = db.relationship('Escola', foreign_keys=escola_ID)
    coordenador_ID = db.Column(db.Integer, db.ForeignKey('coordenador.coordenador_ID'))
    coordenador = db.relationship('Coordenador', foreign_keys=coordenador_ID)
    endereco = db.Column(db.String(50), nullable = False)

class Teste(db.Model):

    teste_ID = db.Column(db.Integer, primary_key=True)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    usuario = db.relationship('Usuario', foreign_keys= usuario_ID)

    nome = db.Column(db.String(50))

class Tipo_resposta(db.Model):

    tipo_resposta_ID = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), primary_key=True)

class Pergunta(db.Model):

    pergunta_ID = db.Column(db.Integer, primary_key=True)
    teste_ID = db.Column(db.Integer, db.ForeignKey('teste.teste_ID'))
    teste = db.relationship('Teste', backref = db.backref('perguntas', lazy = True))
    pergunta = nome = db.Column(db.String(150), nullable = False)
    tipo_resposta_ID = db.Column(db.Integer, db.ForeignKey('tipo_resposta.tipo_resposta_ID'))
    tipo_resposta = db.relationship('Tipo_resposta')

class Sugestao_de_resposta(db.Model):

    sugestao_ID = db.Column(db.Integer, primary_key=True)
    pergunta_ID = db.Column(db.Integer, db.ForeignKey('pergunta.pergunta_ID'))
    sugestao = db.Column(db.String(50), nullable = False)

class Resultado(db.Model):

    resultado_ID = db.Column(db.Integer, primary_key=True)
    teste_ID = db.Column(db.Integer, db.ForeignKey('teste.teste_ID'))
    paciente_ID = db.Column(db.Integer, db.ForeignKey('paciente.paciente_ID'))
    resultado = db.Column(db.String(100))


db.create_all()