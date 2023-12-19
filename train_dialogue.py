import subprocess

subprocess.run(["rasa", "train", "--config", "config.yml", "--domain", "domain.yml", "--data", "data/", "--out", "models/"])


# from rasa.cli.train import train

# train(config="config.yml", domain="domain.yml", training_files="data/", output="models/")
