import pandas as pd
d = [{"1": [{"680.2 MB": "https://s316d2.akwam.link/download/1638536975/61a8c58f562f2/The.Billion.Dollar.Code.S01E01.720p.WEB-DL.akwam.io.mp4"}]}, {"2": [{"615.6 MB": "https://s303d2.akwam.link/download/1638536980/61a8c594ae4d3/The.Billion.Dollar.Code.S01E02.720p.WEB-DL.akwam.io.mp4"}]},
     {"3": [{"582.0 MB": "https://s305d2.akwam.link/download/1638536988/61a8c59c971c6/The.Billion.Dollar.Code.S01E03.720p.WEB-DL.akwam.io.mp4"}]}, {"4": [{"783.2 MB": "https://s310d1.akwam.link/download/1638536996/61a8c5a48f3e8/The.Billion.Dollar.Code.S01E04.720p.WEB-DL.akwam.io.mp4"}]}]
df = pd.DataFrame(d)

d2 = df.to_dict()
print(d2)