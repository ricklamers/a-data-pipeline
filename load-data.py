import orchest 
import pandas as pd

from sklearn import datasets

dataset_name = orchest.get_step_param("dataset")

loader = getattr(datasets, "load_" + dataset_name)

sk_dataset = loader()

orchest.output(sk_dataset, name="dataset")