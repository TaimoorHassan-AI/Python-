import numpy as np
rng=np.random.default_rng()
fruits=np.array(["apple","mango","aam","lassan"])
fruits=rng.choice(fruits,size=(3,3))
print(fruits)