from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blogDescomplicandoDados.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Digite um nome de usuário válido")])
    email = StringField('E-mail', validators=[DataRequired(), Email(message = "Digite um endereço de e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20,message = "Digite um valor para a senha de 6 a 20 caracteres")])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(message="Senha diferente da preenchida anteriormente"), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado. Cadastre-se com um novo e-mail ou faça o login para continuar')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message = "Digite um endereço de e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20,message = "Digite um valor para a senha de 6 a 20 caracteres")])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Digite um nome de usuário válido")])
    email = StringField('E-mail', validators=[DataRequired(), Email(message = "Digite um endereço de e-mail válido")])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'ERRO')])
    stack_pandas = BooleanField("Pandas")
    stack_data_visualization = BooleanField("Data Visualization")
    stack_machine_learning = BooleanField("Machine Learning")
    stack_python = BooleanField("Python")
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField("Titulo do Post", validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField("Escreva o seu post aqui", validators=[DataRequired()])
    botao_submit_criarpost =SubmitField("Criar Post")
