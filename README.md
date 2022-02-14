### A data pipeline in Orchest

The goal is to create a pipeline in Orchest and run it as a weekly cron job. The starting point is this repository of files.

The order of execution should be:

- load-data.py 
- data-viz.ipynb
- split-data.ipynb
- train-linear-model.ipynb
- eval-model.ipynb
- conditional-model-upload.ipynb

For data passing the following connections need to be created:

- load-data.py -> data-viz.ipynb
- load-data.py -> split-data.ipynb
- split-data.ipynb -> train-linear-model.ipynb
- split-data.ipynb -> eval-model.ipynb
- train-linear-model.ipynb -> eval-model.ipynb
- eval-model.ipynb -> conditional-model-upload.ipynb

The `load-data.py` step takes the following step parameters:

```json
{
  "dataset": "iris"
}
```
