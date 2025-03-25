import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestAlunosAPI(unittest.TestCase):

    def setUp(self):
        # Configura o cliente de teste do Flask
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.db_connection')
    def test_listar_alunos(self, mock_db_connection):
        # Simula o retorno da consulta ao banco
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, 'João Silva', 'Rua A', 'São Paulo', 'SP', '12345-678', 'Brasil', '123456789')
        ]

        # Realiza a requisição GET
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIn( response.data)

    @patch('app.db_connection')
    def test_cadastrar_aluno(self, mock_db_connection):
        # Simula a execução do banco de dados
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Dados para a criação do aluno
        payload = {
            "aluno_id": 1,
            "nome": "Maria Oliveira",
            "endereco": "Rua B",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "98765-432",
            "pais": "Brasil",
            "telefone": "987654321"
        }

        # Realiza a requisição POST
        response = self.app.post(
            '/alunos',
            json=payload
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Aluno cadastrado com sucesso!', response.data)

    @patch('app.db_connection')
    def test_alterar_aluno(self, mock_db_connection):
        # Simula a execução do banco de dados
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Dados para atualizar o aluno
        payload = {
            "nome": "Carlos Souza",
            "endereco": "Rua 3",
            "cidade": "Belo Horizonte",
            "estado": "MG",
            "cep": "30000-000",
            "pais": "Brasil",
            "telefone": "31999999999"
        }

        # Realiza a requisição PUT
        response = self.app.put(
            '/alunos/1',
            json=payload
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Aluno atualizado com sucesso!', response.data)

    @patch('app.db_connection')
    def test_excluir_aluno(self, mock_db_connection):
        # Simula a execução do banco de dados
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Realiza a requisição DELETE
        response = self.app.delete('/alunos/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn( response.data)

if __name__ == '__main__':
    unittest.main()