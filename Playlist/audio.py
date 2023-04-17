class Audio:

    def __init__(self, nome, duracao):
        self._nome = nome
        self._duracao = duracao
        self._likes = 0
        
    @property 
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1
    
class Podcast(Audio):

    def __init__(self, episodio, nome, duracao):
        super().__init__(nome, duracao)
        self._episodio = episodio
    
    def __str__(self):
        return F"Nome: {self._nome} - Episódio: {self._episodio} - Duração: {self._duracao}min - Likes: {self._likes}"
    
class Musica(Audio):

    def __init__(self, album, nome, duracao):
        super().__init__(nome, duracao)
        self._album = album
    
    def __str__(self):
        return F"Nome: {self._nome} - Album: {self._album} - Duração: {self._duracao}min - Likes: {self._likes}"

class Playlist:
    def __init__(self, nome, audio):
        self.nome = nome
        self.audio = audio

    def __getitem__(self, item):
        return self.audio[item]

musica1 = Musica("album1", "nome1", 10)
podcast1 = Podcast(1,"nomepodcast1", 70)

podcast1.dar_likes()
podcast1.dar_likes()
podcast1.dar_likes()
musica1.dar_likes()
musica1.dar_likes()

musicas = [musica1,podcast1]
minha_playlist = Playlist("minha_playlist", musicas)



for musicas in minha_playlist:
    print(musicas)
