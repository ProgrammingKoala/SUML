from package.path import *
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

main_dir = "optuna-pipeline"
path_to_parm = "data/06_models/rfr_params.csv"
path_to_data = "data/05_model_input/out.csv"
path_to_target = getPath(main_dir,path_to_parm)

target_column = "price"

def get_parm() -> tuple:
	df = pd.read_csv(path_to_target)
	n_estimators = df["values"][0],
	max_depth = df["values"][1],
	min_samples_split = df["values"][2],
	min_samples_leaf = df["values"][3]
	return (n_estimators[0],max_depth[0],min_samples_split[0],min_samples_leaf)

def get_dataframe() -> pd.DataFrame:
	return pd.read_csv(path_to_data)

def get_dataframeX() -> pd.DataFrame:
    return get_dataframe().drop([target_column],axis=1)
def get_dataframeY() -> pd.DataFrame:
    return get_dataframe()[target_column]

def get_model() -> RandomForestRegressor:
	parms = get_parm()
	return RandomForestRegressor(
        n_estimators = parms[0], 
        max_depth = parms[1], 
        min_samples_split = parms[2], 
        min_samples_leaf = parms[3]
		)

def get_fit_model() -> RandomForestRegressor:
	model = get_model()
	model.fit(get_dataframeX(),get_dataframeY())
	return model

def test():
	#input
	#wheelbase,carlength,carwidth,carheight,curbweight,enginesize,boreratio,stroke,compressionratio,horsepower,peakrpm,citympg,highwaympg,gas,hardtop,hatchback,sedan,wagon,fwd,rwd,five,four,six,three,twelve,two
	expected_pred = 13495.0
	x = [[88.6,168.8,64.1,48.8,2548,130,3.47,2.68,9.0,111,5000,21,27,1,0,0,0,0,0,1,0,1,0,0,0,0]]
	model = get_fit_model()
	y_pred = model.predict(x)
	print("Expected =",expected_pred)
	print("Prediction =",y_pred[0])


if __name__ == "__main__":
	test()