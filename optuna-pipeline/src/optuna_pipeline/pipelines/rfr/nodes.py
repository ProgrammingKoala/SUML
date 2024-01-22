"""
This is a boilerplate pipeline 'rfr'
generated using Kedro 0.19.1
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import optuna
import sys

def get_dataframeX(
        dataframe: pd.DataFrame,
        target_column: str,
        ) -> pd.DataFrame:
    return dataframe.drop([target_column],axis=1)

def get_dataframeY(
        dataframe: pd.DataFrame,
        target_column: str,
        ) -> pd.DataFrame:
    return dataframe[target_column]

def create_model(
        n_estimators: int, 
        max_depth: int, 
        min_samples_split: int, 
        min_samples_leaf: int
        ) -> float:
    return RandomForestRegressor(
        n_estimators = n_estimators, 
        max_depth = max_depth, 
        min_samples_split = min_samples_split, 
        min_samples_leaf = min_samples_leaf)

def objective(
        trial: optuna.Trial,
        dataframeX: pd.DataFrame,
        dataframeY: pd.DataFrame,
        ) -> float:
    n_estimators = trial.suggest_int(name="n_estimators", low = 50, high = 300)
    max_depth = trial.suggest_int(name="max_depth", low = 10, high = 50)
    min_samples_split = trial.suggest_int(name="min_samples_split", low = 2, high = 32)
    min_samples_leaf = trial.suggest_int(name="min_samples_leaf", low = 1, high = 32)
    model = create_model(n_estimators, max_depth, min_samples_split, min_samples_leaf)
    return cross_val_score(model, dataframeX, dataframeY, cv=5).mean()

def create_study(
        ):
    study = optuna.create_study(
        storage="sqlite:///data/06_models/rfr.db",
        load_if_exists=True,
        sampler=optuna.samplers.NSGAIISampler(),
        pruner=optuna.pruners.SuccessiveHalvingPruner(),
        study_name="rfr",
        direction=optuna.study.StudyDirection.MAXIMIZE
    )
    return study

def optuna_run(
        dataframeX: pd.DataFrame,
        dataframeY: pd.DataFrame,
        n_trials: int
        ):
    print("Starting...")
    if n_trials == 0:
        n_trials = None
    study = create_study()
    study.optimize(
        lambda trial: objective(trial, dataframeX, dataframeY),
        n_trials=n_trials,
        n_jobs=1,
    )
    print("Finished...")
    print("Best parameters:",study.best_params)
    return pd.DataFrame(list(study.best_params.items()), columns=["parameter","values"])