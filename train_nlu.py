import subprocess

subprocess.run(["rasa", "train", "nlu", "--config", "config.yml", "--data", "data/nlu.yml", "--out", "models/"])



# from rasa.cli.train import train_nlu

# train_nlu(config="config.yml", nlu_data="data/nlu.yml", output="models/")

