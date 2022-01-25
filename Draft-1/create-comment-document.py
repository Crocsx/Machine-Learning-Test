import subprocess
import pandas
import argparse
import csv

parser = argparse.ArgumentParser(description='Retrive Comment List from dataset')
parser.add_argument('--appId', metavar='ID', nargs='?',
                    help='App Id Comment to Retrive', default='sixpack.sixpackabs.absworkout')
parser.add_argument('--commentRow', metavar='row', nargs='?',
                    help='The row containing the comment', default='content')
args = parser.parse_args()


cmd = "python ./select-app-id-comments.py --appId="+args.appId
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate() 

file = open("./dataset/"+args.appId+".csv",encoding='utf-8')
df = pandas.read_csv(file)

result = open("./dataset/"+args.appId+".txt","w+",encoding='utf-8')

for comment in df[args.commentRow]:
    result.write(f"{comment}\n")
