import os, pickle


DATA_PATH = './data'
with open(os.path.join(DATA_PATH, 'train_coo.pkl'), 'rb') as f:
    train_coo = pickle.load(f)
with open(os.path.join(DATA_PATH, 'test_coo.pkl'), 'rb') as f:
    test_coo = pickle.load(f)

# ecfp = np.load(
#     os.path.join(DATA_PATH, "total_ecfp.npy"), allow_pickle=True)

print(type(train_coo))