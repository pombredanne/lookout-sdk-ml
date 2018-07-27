from modelforge import Model


class Analyzer:
    def __init__(self, model: Model, url: str, config: dict):
        raise NotImplementedError

    def analyze(self, commit_from: str, commit_to: str):
        raise NotImplementedError

    @classmethod
    def train(cls, url: str, commit: str, config: str):
        raise NotImplementedError