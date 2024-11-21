```markdown
# gptify

`gptify` is a command-line tool that converts a Git repository into a single text file suitable for Large Language Models (LLMs) like ChatGPT.  It preserves the file structure and content by prepending each file with a marker `----!@#$----` followed by the file path, and then the file contents. This format enables LLMs to understand the codebase's structure and process it for tasks such as code review, documentation generation, and answering questions about the code.  This project is a fork of [gptrepo](https://github.com/zackess/gptrepo) with added features.

## Relevance

This tool helps developers leverage the power of LLMs for various development tasks.  By converting a repository into an easily digestible format, `gptify` allows LLMs to understand the relationships between files and their contents within the project.  This is particularly useful for complex codebases where understanding the overall structure is crucial for effective analysis.

## Installation

`gptify` can be installed using `pip`:

```bash
pip install gptify
```

Alternatively, you can install it using `pipx`:

```bash
poetry build && pipx install dist/*.whl
```

Older versions can be uninstalled using the provided install script:

```bash
./install.sh
```

## Usage

Navigate to the root directory of your Git repository and run:

```bash
gptify
```

This command generates a file named `gptify_output.txt` in the current directory containing the formatted repository content. You can then copy and paste this file's contents into a ChatGPT session.

### Options

* `--output <filename>`: Specifies the output file name (default: `gptify_output.txt`).
* `--clipboard`: Copies the output directly to the clipboard, skipping file creation.
* `--openfile`: Opens the output file after creation using the default system application.
* `--preamble <filepath>`: Prepends a custom preamble to the output file. This is useful for providing context or instructions to the LLM.


## Example with custom output file and preamble:

```bash
gptify --output my_repo.txt --preamble preamble.txt
```

This will generate `my_repo.txt` with the processed repository data, prepended with the content of `preamble.txt`.

## Contributing

Contributions are welcome.  


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
