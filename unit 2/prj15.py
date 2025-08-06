# write data.csv file in python using list
import csv
f1=open("unit 2/data.csv",'w')
w=csv.writer(f1)
l1=[[1,2,3],[4,5,6],[7,8,9]]
w.writerows(l1)    
