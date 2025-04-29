import os
import random
import json
import re
from tqdm import tqdm


def clean_text(text):
    # Remove blank lines
    # text = re.sub(r'<0x[a-fA-F0-9]+>', '', text)
    text = " ".join(line for line in text.splitlines() if line.strip() != "")
    return text


def sample_txt_files(root_folder, sample_size, seed):
    random.seed(seed)
    all_files_by_year = {}

    # Collect all txt files under each year folder
    print("Collecting files...")
    for year_folder in os.listdir(root_folder):
        year_path = os.path.join(root_folder, year_folder)
        if os.path.isdir(year_path) and year_folder.isdigit():
            txt_files = [f for f in os.listdir(year_path) if f.endswith(".txt")]
            if txt_files:
                all_files_by_year[year_folder] = txt_files

    # Check there are enough files
    total_available = sum(len(files) for files in all_files_by_year.values())
    if sample_size > total_available:
        raise ValueError(f"Requested sample size exceeds total available files ({total_available}).")

    # Determine balanced sampling across years
    num_years = len(all_files_by_year)
    per_year = sample_size // num_years
    remainder = sample_size % num_years

    sampled_files = []
    for year, files in all_files_by_year.items():
        k = min(per_year + (1 if remainder > 0 else 0), len(files))
        sampled = random.sample(files, k)
        sampled_files.extend([(year, fname) for fname in sampled])
        if remainder > 0:
            remainder -= 1

    return sampled_files


def create_json(root_folder, sampled_files, head_only=False):
    output_data = []

    for year, fname in tqdm(sampled_files, desc="Processing files"):
        file_path = os.path.join(root_folder, year, fname)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            cleaned_content = clean_text(content)

            if head_only:
                tokens = cleaned_content.split()
                cleaned_content = " ".join(tokens[:512])

            entry = {"id": f"cuad{year}{os.path.splitext(fname)[0]}", "text": cleaned_content}
            output_data.append(entry)

    return output_data


root_folder = "./contracts"
output_file = "heads_1.json"
sample_size = 5000
seed = 2

sampled_files = sample_txt_files(root_folder, sample_size, seed)
output_data = create_json(root_folder, sampled_files, head_only=True)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"\n Output saved to {output_file}")
