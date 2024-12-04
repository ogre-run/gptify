# gptify

`gptify` is a command-line tool that transforms a Git repository into a single text file or multiple text chunks suitable for use with Large Language Models (LLMs) like ChatGPT. It preserves the file structure and content, enabling LLMs to understand and process the codebase for tasks such as code review, documentation generation, and answering questions about the code. This project is a fork of [gptrepo](https://github.com/zackess/gptrepo) with added features.

## Relevance

This tool addresses the challenge of effectively using LLMs with codebases. By converting a repository into a digestible format, `gptify` allows developers to leverage the power of LLMs for various development tasks.  It simplifies the process of feeding code context into LLMs, avoiding size limitations and formatting issues.

## Installation

The easiest way to install `gptify` is using `pip`:

```bash
pip install gptify
```

Alternatively, you can install it using `pipx`:

```bash
poetry build && pipx install dist/*.whl
```

You can also uninstall older versions using the provided install script:

```bash
./install.sh
```

## Usage

1. **Navigate to the root directory** of your Git repository.
2. **Run the `gptify` command**:

```bash
gptify
```

This will generate a file named `gptify_output.txt` in the current directory containing the formatted repository content.  You can then copy and paste the contents of this file into a ChatGPT session.


### Options

* `--output <filename>`: Specifies the name of the output file (default: `gptify_output.txt`).
* `--clipboard`: Copies the output directly to the clipboard instead of creating an output file.
* `--openfile`: Opens the output file after creation using the default system application.
* `--preamble <filepath>`: Prepends a custom preamble to the output file.  This is useful for providing instructions or context to the LLM.
* `--chunk`: Enables chunking of the output into smaller files, useful for handling large repositories that exceed LLM context limits. Used with `--max_tokens` and `--overlap`.
* `--max_tokens`:  Sets the maximum number of tokens per chunk when using the `--chunk` option (default: 900000).  Requires the `tiktoken` library.
* `--overlap`: Sets the number of overlapping tokens between chunks when using the `--chunk` option (default: 400). Helps maintain context across chunks. Requires the `tiktoken` library.
* `--output_dir`: Specifies the output directory for chunks when using `--chunk` (default: `gptify_output_chunks`).


## Example with custom output file and preamble:

```bash
gptify --output my_repo.txt --preamble instructions.txt
```

This command will generate `my_repo.txt` with the processed repository data, prepended with the content of `instructions.txt`.

## Example with chunking:

```bash
gptify --chunk --max_tokens 4000 --overlap 200
```
This will create multiple files in the `gptify_output_chunks` directory, each containing a chunk of the repository data, with a maximum of 4000 tokens and an overlap of 200 tokens.

## Contributing

Contributions are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
