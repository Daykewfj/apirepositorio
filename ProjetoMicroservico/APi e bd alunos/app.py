from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Conexão com o banco de dados
def db_connection():
    return psycopg2.connect(
        host="db",  # Nome do serviço do container Docker
        database="escola",
        user="admin",
        password="admin"
    )

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alunos")
    alunos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (data['aluno_id'], data['nome'], data['endereco'], data['cidade'], data['estado'], data['cep'], data['pais'], data['telefone'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201

@app.route('/alunos/<aluno_id>', methods=['PUT'])
def alterar_aluno(aluno_id):
    data = request.json
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE alunos SET nome=%s, endereco=%s, cidade=%s, estado=%s, cep=%s, pais=%s, telefone=%s WHERE aluno_id=%s",
        (data['nome'], data['endereco'], data['cidade'], data['estado'], data['cep'], data['pais'], data['telefone'], aluno_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Aluno atualizado com sucesso!"})

@app.route('/alunos/<aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM alunos WHERE aluno_id=%s", (aluno_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Aluno excluído com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
