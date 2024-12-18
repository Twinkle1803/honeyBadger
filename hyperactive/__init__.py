# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

__version__ = "0.4.1.6"
__license__ = "MIT"

from .optimizers.local import HillClimbingOptimizer
from .optimizers.local import StochasticHillClimbingOptimizer
from .optimizers.local import TabuOptimizer

from .optimizers.random import RandomSearchOptimizer
from .optimizers.random import RandomRestartHillClimbingOptimizer
from .optimizers.random import RandomAnnealingOptimizer

from .optimizers.monte_carlo import SimulatedAnnealingOptimizer
from .optimizers.monte_carlo import StochasticTunnelingOptimizer
from .optimizers.monte_carlo import ParallelTemperingOptimizer

from .optimizers.population import ParticleSwarmOptimizer
from .optimizers.population import EvolutionStrategyOptimizer
from .optimizers.population import HoneyBadgerAlgorithm
from .optimizers.population import MHoneyBadgerAlgorithm
from .optimizers.population import BareBonesHoneyBadgerAlgorithm

from .optimizers.sequence_model import BayesianOptimizer

from .sub_packages import Hydra
from .sub_packages import MetaLearn
from .sub_packages import Iota
from .sub_packages import Insight


__all__ = [
    "HillClimbingOptimizer",
    "StochasticHillClimbingOptimizer",
    "TabuOptimizer",
    "RandomSearchOptimizer",
    "RandomRestartHillClimbingOptimizer",
    "RandomAnnealingOptimizer",
    "SimulatedAnnealingOptimizer",
    "StochasticTunnelingOptimizer",
    "ParallelTemperingOptimizer",
    "ParticleSwarmOptimizer",
    "EvolutionStrategyOptimizer",
    "HoneyBadgerAlgorithm",
    "MHoneyBadgerAlgorithm",
    "BareBonesHoneyBadgerAlgorithm",
    "BayesianOptimizer",
    "Hydra",
    "MetaLearn",
    "Iota",
    "Insight",
]
