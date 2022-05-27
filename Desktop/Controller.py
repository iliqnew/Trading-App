
class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
    
    def start(self):
        while True:
            tickers = self.model.tickers
            self.view.update(tickers)