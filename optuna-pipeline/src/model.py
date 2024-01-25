from package.path import *
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

main_dir = "optuna-pipeline"
path_to_data = "data/05_model_input/out.csv"
path_to_parm = "data/06_models/rfr_params.csv"
path_to_model = "data/07_model_output/rfr_model.pickle"
pathDir_to_parm = getPath(main_dir,path_to_parm)
pathDir_to_model = getPath(main_dir,path_to_model)


target_column = "price"

def get_parm() -> tuple:
	df = pd.read_csv(pathDir_to_parm)
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

def save_fit_model() -> RandomForestRegressor:
	model = get_model()
	model.fit(get_dataframeX().values,get_dataframeY().values)
	pickle.dump(model, open(pathDir_to_model,"wb"))
	return model

def get_trained_model() -> RandomForestRegressor:
	return pickle.load(open(pathDir_to_model,"rb"))

def test():
	#input parms
	#wheelbase,carlength,carwidth,carheight,curbweight,enginesize,boreratio,stroke,compressionratio,horsepower,peakrpm,citympg,highwaympg,gas,hardtop,hatchback,sedan,wagon,fwd,rwd,five,four,six,three,twelve,two
	
	#to build new model
	#save_fit_model()

	expected_pred = 13495.0
	x = [[88.6,168.8,64.1,48.8,2548,130,3.47,2.68,9.0,111,5000,21,27,1,0,0,0,0,0,1,0,1,0,0,0,0]]
	model = get_trained_model()
	y_pred = model.predict(x)
	print("Expected =",expected_pred)
	print("Prediction =",y_pred[0])

if __name__ == "__main__":
	test()