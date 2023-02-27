def fnct(df):
    import pandas as pd
    import numpy as np
	#df=pd.read_csv('temperature.csv')
    df_copy=df
    df_copy.dropna(inplace=True)
    df_copy['AverageTemperatureUncertaintyCels']=(df_copy.AverageTemperatureUncertaintyFahr-32)/1.8
    df_copy['AverageTemperatureCels']=(df_copy.AverageTemperatureFahr-32)/1.8
    df_copy.drop(columns=['AverageTemperatureFahr','AverageTemperatureUncertaintyFahr'],inplace=True)
    df_copy.to_csv('temperature_clean.csv',index=False)
    dfnew=pd.read_csv('temperature_clean.csv')
    dfnew_copy=dfnew
    return dfnew_copy











