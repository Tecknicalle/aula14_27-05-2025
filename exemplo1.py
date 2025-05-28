pip install sqlalchemy pymysql
from sqlalchemy import create_engine, text

# variaveis de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'bd_analise'

# função para realizar a conexão com o banco 
def conecta_banco():
    try:
        # URL de conexão com o banco 
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        with engine.connect() as conexao:
            query = 'SELECT * FROM vendas2' # consulta SQL 

            resultado = conexao.execute(text(query))
            
            print(resultado)

            if resultado.rowcount > 0:
                for item in resultado:
                    print(item)
                    print(item[0], item[1], item[2])

    except Exception as e:
        print(f'Algo deu errado: {e}')   


conecta_banco()