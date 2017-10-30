## Import the necessary packages
import pandas as pd
import numpy as np
# ## Load Data
full=pd.read_csv('../input/itcont.txt',sep="|", header=None)
train=full[[0,10,13,14,15]]
Input=train.rename(columns={0:'CMTE_ID', 10:'ZIP_CODE',13:'TRANSACTION_DT',14:'TRANSACTION_AMT',15:'OTHER_ID'})
Input.drop(0,axis=0,inplace=True)

# group data by ID and Zip
Input.ZIP_CODE=Input.ZIP_CODE.astype(str).apply(lambda x: x[:5])
# calculation and merge
GROUPZIP=Input.groupby(['CMTE_ID','ZIP_CODE'])
data_GROUPZIP=GROUPZIP.size().reset_index(name='Count_zip')
data_GROUPZIP[['mean_zip','sum_zip']]=GROUPZIP['TRANSACTION_AMT'].agg([np.mean,np.sum]).apply(np.rint).reset_index()[['mean','sum']]
Input = pd.merge(Input, data_GROUPZIP, how='left', on=['CMTE_ID','ZIP_CODE'])

# group data by ID and Date
GROUPDATE=Input.groupby(['CMTE_ID','TRANSACTION_DT'])
# calculation and merge
data_GROUPDATE=GROUPDATE.size().reset_index(name='Count_date')
data_GROUPDATE[['mean_date','sum_date']]=GROUPDATE['TRANSACTION_AMT'].agg([np.mean,np.sum]).apply(np.rint).reset_index()[['mean','sum']]
Input = pd.merge(Input, data_GROUPDATE, how='left', on=['CMTE_ID','TRANSACTION_DT'])


# export data
Medianvals_zip=['CMTE_ID','ZIP_CODE','mean_zip','Count_zip','sum_zip']
Medianvals_date=['CMTE_ID','ZIP_CODE','mean_date','Count_date','sum_date']
Input[Medianvals_zip].to_csv('../output/medianvals_by_zip.txt', header=True, index=False, sep='|')
Input[Medianvals_date].to_csv('../output/medianvals_by_zip.txt', header=True, index=False, sep='|')



