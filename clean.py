"""
Utils to clean old mlflow run
"""

import yaml
import os
import time
import shutil
import click

@click.command()
@click.option("--mlflowloc", default='./mlruns', help="Specify mlflow store location ")
@click.option("--old",default=200, help="Days. Delete all runs with start_time older than today minus old.")
def clean_old_run(mlflowloc: str, old: int):

    """

    Args:
        mlflowloc: path where mlflow store runs
        old: Integer. days. All runs with end_time older than
        today minus old will be deleted

    Returns:
        Nothing

    """

    del_time = (time.time() - (old * 24 * 60 * 60)) * 1000

    meta_yaml = [x[0] if _check_element(x[2]) else [] for x in os.walk(mlflowloc)]
    meta_yaml = [x for x in meta_yaml if x != []]

    for m in meta_yaml:
        with open(os.path.join(m,'meta.yaml')) as f:
            metainfo = yaml.safe_load(f)
            end_time = metainfo.get('start_time',None)

        if end_time:
            shutil.rmtree(m) if end_time < del_time else None


def _check_element(x):

    for l in x:
        if l.endswith('.yaml'):
            return True
        else:
            return False




if __name__=='__main__':

    clean_old_run()
