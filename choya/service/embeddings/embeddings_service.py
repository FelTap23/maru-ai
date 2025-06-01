from abc import ABC, abstractmethod

class EmbeddingsService(ABC):

    @abstractmethod
    def make_embeddings(self):
        pass
