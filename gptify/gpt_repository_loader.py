#!/usr/bin/env python3

import argparse
import fnmatch
import os
import sys
import pyperclip
import tiktoken

HERE = os.path.dirname(os.path.abspath(__file__))

# Utility functions
def get_ignore_list(ignore_file_path):
    ignore_list = []
    with open(ignore_file_path, "r") as ignore_file:
        for line in ignore_file:
            if sys.platform == "win32":
                line = line.replace("/", "\\")
            ignore_list.append(line.strip())
    return ignore_list

def should_ignore(file_path, ignore_list):
    for pattern in ignore_list:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False

def process_repository(repo_path, ignore_list, output_file):
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, repo_path)
            if not should_ignore(relative_file_path, ignore_list):
                with open(file_path, "r", errors="ignore") as file:
                    contents = file.read()
                output_file.write("----!@#$----\n")
                output_file.write(f"{relative_file_path}\n")
                output_file.write(f"{contents}\n")

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def tokenize_text(text, tokenizer):
    return tokenizer.encode(text, disallowed_special=())

def chunk_text(tokens, max_tokens, overlap=0):
    chunks = []
    start = 0
    while start < len(tokens):
        end = start + max_tokens
        chunks.append(tokens[start:end])
        start += max_tokens - overlap
    return chunks

def decode_chunks(chunks, tokenizer):
    return [tokenizer.decode(chunk) for chunk in chunks]

def save_chunks(chunks, output_dir):
    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(output_dir, f"chunk_{i + 1}.txt")
        with open(chunk_path, "w", encoding="utf-8") as file:
            file.write(chunk)

# Main functionality
def process_git_repository(
    repo_path,
    output_path,
    ignore_file_path=os.path.join(HERE, ".gptignore"),
    preamble_file=None,
    chunk_output=False,
    max_tokens=900000,
    overlap=400,
    output_dir=None
):
    if not ignore_file_path:
        ignore_file_path = os.path.join(repo_path, ".gptignore")
    if sys.platform == "win32":
        ignore_file_path = ignore_file_path.replace("/", "\\")

    if not os.path.exists(ignore_file_path):
        ignore_file_path = os.path.join(HERE, ".gptignore")
        assert os.path.exists(ignore_file_path)
    ignore_list = get_ignore_list(ignore_file_path) if os.path.exists(ignore_file_path) else []

    with open(output_path, "w") as output_file:
        if preamble_file:
            with open(preamble_file, "r") as pf:
                preamble_text = pf.read()
                output_file.write(f"{preamble_text}\n")
        else:
            output_file.write(
                "The following text is a Git repository with code. The structure of the text are sections that begin with ----!@#$----, followed by a single line containing the file path and file name, followed by a variable amount of lines containing the file contents. The text ends with --END--.\n"
            )
        process_repository(repo_path, ignore_list, output_file)
        output_file.write("--END--")

    if chunk_output:
        text = load_text(output_path)
        tokenizer = tiktoken.get_encoding("cl100k_base")
        tokens = tokenize_text(text, tokenizer)
        token_chunks = chunk_text(tokens, max_tokens, overlap)
        text_chunks = decode_chunks(token_chunks, tokenizer)
        os.makedirs(output_dir, exist_ok=True)
        save_chunks(text_chunks, output_dir)

# CLI
def main():
    parser = argparse.ArgumentParser(
        description="Process a git repository into a single file for chat gpt."
    )
    parser.add_argument("repo_path", help="Path to the git repository", type=str, nargs="?")
    parser.add_argument("-p", "--preamble", help="Path to the preamble file", type=str)
    parser.add_argument("--clipboard", help="Copy the output to the clipboard", action="store_true")
    parser.add_argument("--openfile", help="Open the output file after creation", action="store_true")
    parser.add_argument("--output", help="Path to save the output file", type=str, default="gptify_output.txt")
    parser.add_argument("--output_dir", help="Directory for chunked output", type=str, default="gptify_output_chunks")
    parser.add_argument("--chunk", help="Chunk the output file for NLP pipelines", action="store_true")
    parser.add_argument("--max_tokens", help="Maximum tokens per chunk", type=int, default=900000)
    parser.add_argument("--overlap", help="Overlap tokens between chunks", type=int, default=400)
    args = parser.parse_args()

    repo_path = args.repo_path or os.getcwd()
    output_file = os.path.abspath(args.output)
    output_dir = os.path.abspath(args.output_dir)

    process_git_repository(
        repo_path,
        output_file,
        preamble_file=args.preamble,
        chunk_output=args.chunk,
        max_tokens=args.max_tokens,
        overlap=args.overlap,
        output_dir=output_dir,
    )

    if args.clipboard:
        contents = load_text(output_file)
        pyperclip.copy(contents)
        os.remove(output_file)
        print("Copied to clipboard")
    else:
        print(f"Repository contents written to {output_file}")
        if args.openfile:
            if sys.platform == "win32":
                os.startfile(output_file)
            elif sys.platform == "darwin":
                os.system(f"open {output_file}")
            else:
                os.system(f"xdg-open {output_file}")

if __name__ == "__main__":
    main()
