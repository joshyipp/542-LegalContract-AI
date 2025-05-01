"""CUAD Sampler - A utility for sampling and processing contract documents from the CUAD dataset.

This module provides functions for:
- Cleaning contract text
- Sampling text files from different years
- Creating JSON output with processed contract text
"""

import json
import os
import random

from tqdm import tqdm


def clean_text(text):
    """Clean the provided text by removing blank lines and condensing to a single string.

    Parameters
    ----------
    text : str
        The raw text to be cleaned.

    Returns
    -------
    str
        The cleaned text with blank lines removed and content joined with spaces.
    """
    # Remove blank lines
    # text = re.sub(r'<0x[a-fA-F0-9]+>', '', text)
    return " ".join(line for line in text.splitlines() if line.strip() != "")


def sample_txt_files(root_folder, sample_size, seed):
    """Sample text files from different years in the given root folder.

    Parameters
    ----------
    root_folder : str
        Path to the root folder containing year-based subdirectories with txt files.
    sample_size : int
        Number of files to sample.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    list
        List of tuples containing (year, filename) for sampled files.

    Raises
    ------
    ValueError
        If requested sample size exceeds total available files.
    """
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
    """Create JSON output data from sampled contract files.

    Parameters
    ----------
    root_folder : str
        Path to the root folder containing year-based subdirectories with txt files.
    sampled_files : list
        List of tuples containing (year, filename) pairs to process.
    head_only : bool, optional
        If True, only include the first 512 tokens of each contract. Default is False.

    Returns
    -------
    list
        List of dictionaries containing contract data with 'id' and 'text' fields.
    """
    output_data = []

    for year, fname in tqdm(sampled_files, desc="Processing files"):
        file_path = os.path.join(root_folder, year, fname)
        with open(file_path, encoding="utf-8", errors="ignore") as f:
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
