from sklearn.ensemble import RandomForestClassifier

class SignalModel:

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=200, max_depth=5)

    def train(self, X, y):
        split = int(len(X) * 0.7)
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]

        self.model.fit(X_train, y_train)

        acc = self.model.score(X_test, y_test)
        print(f"Validation Accuracy: {acc:.3f}")

    def predict(self, X):
        preds = self.model.predict(X)
        return preds
