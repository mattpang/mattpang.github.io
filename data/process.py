import pandas as pd

df = pd.read_csv('./data/wearables.tsv',sep='\t')
df.set_index('Year',inplace=True)

tmp = df.to_dict('list')

out = []
for k,v in tmp.items():
    out.append({'name':k,'data':v})

output = dict()
output['series'] = out
output['cat'] = df.index.tolist()

print(output)
import json 

json.dump(output, open('./data/wearables.json','w'))

# format required 
# elsewhere: 
# cat: [list of categories]
# series:[{
# name: 'field',
# data: [series data]
# },
# { name:'field2
#  data: [series2 data]
# }]