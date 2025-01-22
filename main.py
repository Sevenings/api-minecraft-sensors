
# Carregar as variáveis de ambiente do python-dotenv
# from dotenv import load_dotenv
# load_dotenv()

# Imports
import os
from app import create_app #, db
# from app.models import Andamento
# from flask_migrate import Migrate, init, migrate, upgrade





# Cria o app pelo padrão app factory
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# m = Migrate(app, db)


# Realiza a iniciação do banco de dados e do script de migração, caso não exista
# with app.app_context():
#     from pathlib import Path
#     if not Path('migrations').exists():
#         init(directory='migrations', multidb=False)
#         migrate(directory='migrations', message=None, 
#                 sql=False, head='head', splice=False, 
#                 branch_label=None, version_path=None, rev_id=None)
#         upgrade(directory='migrations', revision='head', sql=False, tag=None)
#

# Adiciona import automatico de db e Processo ao flask shell
# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, Andamento=Andamento)


# Cria e executa a thread de monitoramento
# if app.config['SCAN_ENABLED'] == 1:
#     from threading import Thread
#     from app.monitoramento import monitorar
#     def monitorar_com_contexto():
#         with app.app_context():
#             tempo_entre_scan = app.config['TIME_BETWEEN_SCAN']
#             monitorar(tempo_entre_scan=tempo_entre_scan)
#
#     t_monitoramento = Thread(target=monitorar_com_contexto, name='t_monitoramento')
#     t_monitoramento.start()


# No modo produção inicia o servidor WSGI
# if app.config['PRODUCTION']:
#     addr = app.config['ADDRESS']
#     port = app.config['PORT']
#
#     print(f"Iniciando WSGI no endereço: {addr}:{port}")
#
#     from waitress import serve
#     serve(app, listen=f'{addr}:{port}')


