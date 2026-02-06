import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass      #helps you to define variables insdie the class wihtout writing __init__

#class is wirtten for taking the inputs of the files and data, and storing them at some location
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts',"train.csv")                            #these 3 lines are for the same purpose (creating a folder artifacts and storing them in their files )
    test_data_path:str = os.path.join('artifacts',"test.csv")
    raw_data_path:str = os.path.join('artifacts',"data.csv")



#if we are jsut using a class to define variables we may use @dataclass, if not avoid using it
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()    #ingetsion_config is the class variable and as soon as the class is called the 3 variables from above class will be stored here, ingestion_config is the object of class dataingetsionconfig 
    
    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion component ")
        try:
            df=pd.read_csv('notebook\data\stud.csv')        #just reading the data from the file
            logging.info("read the dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)        #to make the folder named artifacts, we have to give the path, the name & path is taken from the any one of the variable from the upper class

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header = True)            
            #we have toconvert each file in csv, so we just converted the raw data file in csv as it doesnt require any action, later rest 2 fiels are also converted in csv
            #index+false jsut means that when creating the file dont give each row a index, it is of no use 
            #header=true is very importatnt as it means the new file created sould also have column names , if the column names are not written we woint be able to undestand the data

            logging.info("train test split initiated")

            #just splitting the data in train and test 
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False, header=True)

            logging.info("ingestion of data is completed ")


        except(Exception) as e:
            
            raise CustomException (e,sys)


if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()