# NACCisTooBig
NACC is the data collected annually on 27,000 participants in a National Institute of Health study on Alzheimer's Disease. The file made available for my research project had about 9 years of data, 121,000 records, and was 289MB.

I was working on an AI modeling problem and sought to use the NACC data to train the model. Training took forever and I knew I had to shrink the data. This program was written to reduce the size of the data so the training time would come down but the performance of the trained model would not. 

I'm including a sanatized version of the data file for demonstration purposes. I was able to reduce the original size of the training data by 75% (289MB became 80MB). The file name is "shrunk nacc46 for use with ripper.xlsx".

The user still has to do some data preparation. Open the data file and reverse it's order.  Since it's a longitudinal study the records are added cronologically, oldest first.    

Steps:
1. Download the NACC spreadsheet and use it to create your local "NACCturnedUpsideDown.csv".
2. Run the program to create "NACCRippedToNew<N>.csv"
3. Check the resulting file before using it for training.4.  

This program returns only the most recent annual record for each participant of the study.   
