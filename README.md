# mlflow-utils

Delete old run from mlflow storage location ( only local)

Mlflow won't allow ( for now ) a feature for permanently deleting https://github.com/mlflow/mlflow/issues/2152

Usage:

```bash
python clean.py --mlflowloc=./mlruns --old=100
```
