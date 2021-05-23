import numpy as np
import pandas as pd
import re

df = pd.read_excel('data.xlsx', header=0)
x = df.iloc[1]
pos = x['Position']
check = re.match(r"\bD.*\(R.*\)", pos)

gk = {}
dl = {}
dc = {}
dr = {}
dm = {}
mc = {}
ml = {}
mr = {}
aml = {}
amr = {}
amc = {}
fs = {}
ts = {}

for i in range(len(df)):
    player = df.iloc[i]
    pos = player['Position']
    dl_match = re.search(r"\bD.*\(.*L.*\)", pos)
    dr_match = re.search(r"\bD.*\(.*R.*\)", pos)
    dc_match = re.search(r"\bD[^M]*\(.*C.*\)", pos)
    dm_match = re.search(r"\bDM.*", pos)
    mc_match = re.search(r"\bM.*\(.*C.*\)", pos)
    ml_match = re.search(r"\bM.*\(.*L.*\)", pos)
    mr_match = re.search(r"\bM.*\(.*R.*\)", pos)
    aml_match = re.search(r"\bAM.*\(.*L.*\)", pos)
    amr_match = re.search(r"\bAM.*\(.*R.*\)", pos)
    amc_match = re.search(r"\bAM.*\(.*C.*\)", pos)
    st_match = re.search(r"\bST.*", pos)
    if pos == 'GK':
        weigths = [0.12, 0.12, 0.10, 0.09]
        attributes = [player['Han'], player['Ref'], player['Dec'], player['Agi']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        gk[player['Name']] = rating
    if dl_match or dr_match:
        weigths = [0.15, 0.14, 0.13, 0.11, 0.07, 0.07, 0.07]
        attributes = [player['Acc'], player['Pos'], player['Dec'], player['Pac'],
                      player['Tck'], player['Cnt'], player['Agi']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        if dl_match:
            dl[player['Name']] = rating
        if dr_match:
            dr[player['Name']] = rating
    if dc_match:
        weigths = [0.13, 0.10, 0.10, 0.09, 0.08, 0.08, 0.08]
        attributes = [player['Dec'], player['Pos'], player['Mar'], player['Acc'],
                      player['Jum'], player['Str'], player['Pac']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        dc[player['Name']] = rating
    if dm_match:
        weigths = [0.12, 0.11, 0.10, 0.08, 0.07, 0.07]
        attributes = [player['Acc'], player['Dec'], player['Tck'], player['Pac'],
                      player['Str'], player['Agi']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        dm[player['Name']] = rating
    if mc_match:
        weigths = [0.12, 0.11, 0.10, 0.10, 0.07, 0.07]
        attributes = [player['Acc'], player['Vis'], player['Pas'], player['Pac'],
                      player['Dec'], player['Agi']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        mc[player['Name']] = rating
    if ml_match or mr_match:
        weigths = [0.26, 0.20, 0.07]
        attributes = [player['Acc'], player['Pac'], player['Agi']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        if ml_match:
            ml[player['Name']] = rating
        if mr_match:
            mr[player['Name']] = rating
    if aml_match or amr_match:
        weigths = [0.28, 0.28, 0.07]
        attributes = [player['Acc'], player['Pac'], player['Dri']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        if aml_match:
            aml[player['Name']] = rating
        if amr_match:
            amr[player['Name']] = rating
    if amc_match:
        weigths = [0.23, 0.13, 0.09]
        attributes = [player['Acc'], player['Pac'], player['Vis']]
        rating = round(np.dot(weigths, attributes) * 1 / sum(weigths), 2)
        amc[player['Name']] = rating
    if st_match:
        weigths_fs = [0.24, 0.17, 0.08]
        weigths_ts = [0.17, 0.13, 0.12, 0.10]
        attributes_fs = [player['Acc'], player['Pac'], player['Fin']]
        attributes_ts = [player['Acc'], player['Hea'], player['Jum'], player['Pac']]

        rating_fs = round(np.dot(weigths_fs, attributes_fs) * 1 / sum(weigths_fs), 2)
        rating_ts = round(np.dot(weigths_ts, attributes_ts) * 1 / sum(weigths_ts), 2)

        fs[player['Name']] = rating_fs
        ts[player['Name']] = rating_ts

gk = dict(sorted(gk.items(), key=lambda item: item[1], reverse=True))  # sort the dictionary
dl = dict(sorted(dl.items(), key=lambda item: item[1], reverse=True))
dr = dict(sorted(dr.items(), key=lambda item: item[1], reverse=True))
dc = dict(sorted(dc.items(), key=lambda item: item[1], reverse=True))
dm = dict(sorted(dm.items(), key=lambda item: item[1], reverse=True))
mc = dict(sorted(mc.items(), key=lambda item: item[1], reverse=True))
ml = dict(sorted(ml.items(), key=lambda item: item[1], reverse=True))
mr = dict(sorted(mr.items(), key=lambda item: item[1], reverse=True))
aml = dict(sorted(aml.items(), key=lambda item: item[1], reverse=True))
amr = dict(sorted(amr.items(), key=lambda item: item[1], reverse=True))
amc = dict(sorted(amc.items(), key=lambda item: item[1], reverse=True))
fs = dict(sorted(fs.items(), key=lambda item: item[1], reverse=True))
ts = dict(sorted(ts.items(), key=lambda item: item[1], reverse=True))

print("Goalkeeper: ")
for name, value in gk.items():
    print(name, value)

print("\nDL: ")
for name, value in dl.items():
    print(name, value)

print("\nDR: ")
for name, value in dr.items():
    print(name, value)

print("\nDM: ")
for name, value in dm.items():
    print(name, value)

print("\nCM: ")
for name, value in mc.items():
    print(name, value)

print("\nML: ")
for name, value in ml.items():
    print(name, value)

print("\nMR: ")
for name, value in mr.items():
    print(name, value)

print("\nAML: ")
for name, value in aml.items():
    print(name, value)

print("\nAMR: ")
for name, value in amr.items():
    print(name, value)

print("\nAMC: ")
for name, value in amc.items():
    print(name, value)

print("\nST (fast): ")
for name, value in fs.items():
    print(name, value)

print("\nST (target): ")
for name, value in ts.items():
    print(name, value)

input()