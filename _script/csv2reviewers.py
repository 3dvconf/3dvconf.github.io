#%%
import pandas as pd
import os 
os.chdir('../')
print(os.getcwd())
# %%
df_ac = pd.read_csv("_temp\\3DV 2026 Area Chairs Status.csv")
df_rv = pd.read_csv("_temp\\3DV 2026 Reviewers Status.csv")
# %%
name_func = lambda x: ' '.join([nm.capitalize() for nm in x.split(' ')])
ac_names = df_ac['name'].apply(name_func)
rv_names = df_rv['name'].apply(name_func)
# capitalize the first letter of each name
# ac_names = [n.capitalize() for n in ac_names]
# rv_names = [n.capitalize() for n in rv_names]

ac_names = ac_names.str.title()
rv_names = rv_names.str.title()
print(ac_names)
# %%
ac_set = set(ac_names)
rv_set = set(rv_names)
reviewers_only = sorted(rv_set - ac_set)
acs_sorted = sorted(ac_set)


#%%
YEAR = 2026
# Build markdown:
lines = [f"{YEAR}:"]
# ACs first with ac: true
lines += [f"- name: {n}\n  ac: true" for n in acs_sorted]
# Then reviewers (non-ACs) without an ac flag
lines += [f"- name: {n}" for n in reviewers_only]

markdown_text = "\n".join(lines)
print(markdown_text)

# %%
