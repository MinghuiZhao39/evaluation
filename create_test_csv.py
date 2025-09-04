import os
import pandas as pd

folder_path = "mos/gradtts-10-published-ckp"
link_prefix = "https://github.com/MinghuiZhao39/evaluation/raw/main/mos/gradtts-10-published-ckp/"
audio_links = []

# Gather audio links
for f in os.listdir(folder_path):
    if f.endswith(".wav"):
        audio_links.append(link_prefix + f)
        print(link_prefix + f)

# Build rows for the DataFrame
rows = []
num_assignments = len(audio_links) // 5
for i in range(2):
    rows.append({
        "assignmentId": f"A{i+1}",
        "audio_url_1": audio_links[i*5],
        "audio_url_2": audio_links[i*5 + 1],
        "audio_url_3": audio_links[i*5 + 2],
        "audio_url_4": audio_links[i*5 + 3],
        "audio_url_5": audio_links[i*5 + 4],
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(rows)
df.to_csv("test_assignment.csv", index=False)