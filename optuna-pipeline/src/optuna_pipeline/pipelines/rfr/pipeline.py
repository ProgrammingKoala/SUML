"""
This is a boilerplate pipeline 'rfr'
generated using Kedro 0.19.1
"""
from kedro.pipeline import Pipeline, pipeline

from kedro.pipeline.node import node

from .nodes import get_dataframeX, get_dataframeY, optuna_run

import optuna

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=get_dataframeX, inputs=["model_input","params:target_column"], outputs="dataframeX"),
        node(func=get_dataframeY, inputs=["model_input","params:target_column"], outputs="dataframeY"),
        node(func=optuna_run, inputs=["dataframeX","dataframeY","params:n_trials"], outputs="rfr_params"),
    ])
