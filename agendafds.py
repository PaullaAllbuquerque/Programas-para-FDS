from enum import Enum
class Playlist:
	def __init__(self, nome, atividades):
		self.nome = nome
		self._atividades = atividades

	def __getitem__(self, item):
		return self._atividades[item]

	def __len__(self):
		return len(self._atividades)


class Programa:
	def __init__(self, nome, duracao):
		self._nome = nome
		self.duracao = duracao

	@property
	def nome(self):
		return self._nome
	@nome.setter
	def nome(self, nome):
		self._nome = nome

	def __str__(self):
		return f"Programa: {self.nome}"

class Passeio(Programa):
	def __init__(self, nome, descricao, cidade, duracao):
		super().__init__(nome, duracao)
		self.descricao = descricao
		self.cidade = cidade

	def __str__(self):
		return f" {self.nome}: {self.descricao} - {self.cidade} - {self.duracao} horas"

class Pipoca(Programa):
	def __init__(self, nome, descricao, plataforma, duracao):
		super().__init__(nome, duracao)
		self.plataforma = plataforma
		opcoes = {1: "Filme", 2: "Série", 3: "Documentário"}
		if descricao in opcoes:
			self.descricao = opcoes[descricao]
		else:
			raise ValueError("O número da opção deve ser válido")

	def __str__(self):
		return f" {self.nome}: {self.descricao} - {self.plataforma} - {self.duracao} horas"

class Exercicio(Programa):
	def __init__(self, nome, descricao, duracao):
		super().__init__(nome, duracao)
		self.descricao = descricao

	def __str__(self):
		return f" {self.nome}: {self.descricao} - {self.duracao} horas"

class Leitura(Programa):
	def __init__(self, nome, descricao, autor, duracao):
		super().__init__(nome, duracao)
		self.autor = autor
		opcoes_validas = {1: "Livro", 2: "Revista", 3: "Quadrinhos"}
		if descricao in opcoes_validas:
			self.descricao = opcoes_validas[descricao]
		else:
			raise ValueError("A descrição deve ser uma opção válida.")

	def __str__(self):
		return f" {self.nome}: {self.descricao} - {self.autor} - {self.duracao} horas"


passeio1= Passeio("Cachoeira Alta", "Visita a cidade + cachoeira + Pôr do Sol", "Ipoema/MG", 16)
pipoca1 = Pipoca("Dark", 2, "Netflix", 5)
exercicio1 = Exercicio("Corrida", "Corrida na lagoa com a Gaia", 2)
livro1 = Leitura("Todos os Nomes", 1, "Saramago", 1)

playlist = [passeio1, pipoca1, exercicio1, livro1] #festa #arrumar_casa
playlist_fds = Playlist("Programas para FDS", playlist)

print(f"Foram programadas {len(playlist_fds)} atividades para esse FDS: ")
for objeto in playlist_fds:
	print(objeto)
