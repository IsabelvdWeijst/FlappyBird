import pickle

with open("best_bird_genome.pkl", "rb") as f:
    best_genome = pickle.load(f)

print(type(best_genome))
