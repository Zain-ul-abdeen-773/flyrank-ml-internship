import json

with open("work/notebooks/w03_data_contract.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = cell["source"]
        for i, line in enumerate(source):
            if "fact_content_daily_performance/**/*.parquet" in line:
                source[i] = line.replace("fact_content_daily_performance/**/*.parquet", "fact_content_daily_performance/month=2026-03/*.parquet")
                
with open("work/notebooks/w03_data_contract.ipynb", "w", encoding="utf-8", newline="\n") as f:
    json.dump(nb, f, indent=1, ensure_ascii=True)
    f.write("\n")
