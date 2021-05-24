import numpy as np
import pandas as pd
import re
import tkinter as tk

df = pd.read_html('data.html', header=0)[0]
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
    dl_match = re.search(r"\bD[/\w]*\s?\(.{0,3}L.*\)", pos)
    dr_match = re.search(r"\bD[/\w]*\s?\(.{0,3}R.*\)", pos)
    dc_match = re.search(r"\bD\s?\(.{0,3}C.*\)", pos)
    dm_match = re.search(r"\bDM.*", pos)
    mc_match = re.search(r"\bM[/\w]*\s?\(.{0,3}C.*\)", pos)
    ml_match = re.search(r"\bM[/\w]*\s?\(.{0,3}L.*\)", pos)
    mr_match = re.search(r"\bM[/\w]*\s?\(.{0,3}R.*\)", pos)
    aml_match = re.search(r"\bAM\s?\(.{0,3}L.*\)", pos)
    amr_match = re.search(r"\bAM\s?\(.{0,3}R.*\)", pos)
    amc_match = re.search(r"\bAM\s?\(.{0,3}C.*\)", pos)
    st_match = re.search(r"\bST.*", pos)
    if pos == 'GK':
        weights = [0.12, 0.12, 0.10, 0.09]
        attributes = [player['Han'], player['Ref'], player['Dec'], player['Agi']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        gk[player['Name']] = rating
    if dl_match or dr_match:
        weights = [0.15, 0.14, 0.13, 0.11, 0.07, 0.07, 0.07]
        attributes = [player['Acc'], player['Pos'], player['Dec'], player['Pac'],
                      player['Tck'], player['Cnt'], player['Agi']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        if dl_match:
            dl[player['Name']] = rating
        if dr_match:
            dr[player['Name']] = rating
    if dc_match:
        weights = [0.13, 0.10, 0.10, 0.09, 0.08, 0.08, 0.08]
        attributes = [player['Dec'], player['Pos'], player['Mar'], player['Acc'],
                      player['Jum'], player['Str'], player['Pac']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        dc[player['Name']] = rating
    if dm_match:
        weights = [0.12, 0.11, 0.10, 0.08, 0.07, 0.07]
        attributes = [player['Acc'], player['Dec'], player['Tck'], player['Pac'],
                      player['Str'], player['Agi']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        dm[player['Name']] = rating
    if mc_match:
        weights = [0.12, 0.11, 0.10, 0.10, 0.07, 0.07]
        attributes = [player['Acc'], player['Vis'], player['Pas'], player['Pac'],
                      player['Dec'], player['Agi']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        mc[player['Name']] = rating
    if ml_match or mr_match:
        weights = [0.26, 0.20, 0.07]
        attributes = [player['Acc'], player['Pac'], player['Agi']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        if ml_match:
            ml[player['Name']] = rating
        if mr_match:
            mr[player['Name']] = rating
    if aml_match or amr_match:
        weights = [0.28, 0.28, 0.07]
        attributes = [player['Acc'], player['Pac'], player['Dri']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
        if aml_match:
            aml[player['Name']] = rating
        if amr_match:
            amr[player['Name']] = rating
    if amc_match:
        weights = [0.23, 0.13, 0.09]
        attributes = [player['Acc'], player['Pac'], player['Vis']]
        rating = round(np.dot(weights, attributes) * 1 / sum(weights), 2)
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


def on_selection(event):
    position = None
    choice = list_box.curselection()[0]
    if choice == 0:
        position = gk.items()
    elif choice == 1:
        position = dc.items()
    elif choice == 2:
        position = dl.items()
    elif choice == 3:
        position = dr.items()
    elif choice == 4:
        position = dm.items()
    elif choice == 5:
        position = mc.items()
    elif choice == 6:
        position = ml.items()
    elif choice == 7:
        position = mr.items()
    elif choice == 8:
        position = aml.items()
    elif choice == 9:
        position = amr.items()
    elif choice == 10:
        position = amc.items()
    elif choice == 11:
        position = fs.items()
    elif choice == 12:
        position = ts.items()
    string = ""

    for name, value in position:
        string += name + " " + str(value)
        string += "\n"

    text_box.delete('1.0', 'end')
    text_box.insert('1.0', string)


root = tk.Tk()
root.title("Player ratings")
text_box = tk.Text(height=15)
text_box.grid(row=0, column=0)
list_box = tk.Listbox(height=15)
list_box.insert(1, "GK")
list_box.insert(2, "DC")
list_box.insert(3, "DL")
list_box.insert(4, "DR")
list_box.insert(5, "DM")
list_box.insert(6, "MC")
list_box.insert(7, "ML")
list_box.insert(8, "MR")
list_box.insert(9, "AML")
list_box.insert(10, "AMR")
list_box.insert(11, "AMC")
list_box.insert(12, "FS")
list_box.insert(13, "TS")

list_box.bind('<<ListboxSelect>>', on_selection)
list_box.grid(row=0, column=1)

root.mainloop()
