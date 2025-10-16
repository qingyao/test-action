import os
import pandas as pd
model_dir = './best_model'
metrics = pd.read_csv(os.path.join(model_dir, 'metrics.tsv'), sep='\t')
print(metrics.columns)
print(metrics)
threshold = metrics['threshold'][0]

with open('output/out.txt', 'w') as wf:
    print(threshold, file =wf)