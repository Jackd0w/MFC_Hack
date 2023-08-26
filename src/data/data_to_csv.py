import pandas as pd
  
# Read and store content
# of an excel file 
read_file = pd.read_excel ("src/data/train_dataset.xlsx")
  
# Write the dataframe object
# into csv file
read_file.to_csv ("Train_dataset.csv", 
                  index = None,
                  header=True)
    
# read csv file and convert 
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Train_dataset.csv"))
  
# show the dataframe
df