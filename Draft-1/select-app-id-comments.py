import pandas
import argparse
import csv

parser = argparse.ArgumentParser(description='Filter a review list to match a single application')
parser.add_argument('--appId', metavar='ID', nargs='?',
                    help='App Id Comment to Retrive', default='sixpack.sixpackabs.absworkout')
args = parser.parse_args()

file = open("./dataset/Reviews.csv", encoding='utf-8')
df = pandas.read_csv(file)
df =  df[df.app_Id == args.appId] 

df.to_csv("./dataset/"+args.appId+".csv", index=False)