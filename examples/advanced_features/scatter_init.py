from sklearn.datasets import load_iris
from hyperactive import SimulatedAnnealingOptimizer

iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# this defines the model and hyperparameter search space
search_config = {
    "sklearn.ensemble.RandomForestClassifier": {
        "n_estimators": range(10, 200, 10),
        "max_depth": [3, 4, 5, 6],
        "criterion": ["gini", "entropy"],
    }
}

# Without scatter initialization
opt = SimulatedAnnealingOptimizer(
    search_config, n_iter=20, random_state=0, scatter_init=False
)
opt.fit(X, y)


# With scatter initialization
opt = SimulatedAnnealingOptimizer(
    search_config, n_iter=20, random_state=0, scatter_init=True
)
opt.fit(X, y)
