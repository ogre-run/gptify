# gptify

`gptify` is a command-line tool that transforms a Git repository into a single text file suitable for use with Large Language Models (LLMs) like ChatGPT.  It preserves the file structure and content, enabling LLMs to understand and process the codebase for tasks such as code review, documentation generation, and answering questions about the code.  This project is a fork of [gptrepo](https://github.com/zackess/gptrepo) with added features specifically designed for the [miniogre devtool](https://github.com/ogre-run/miniogre).

## Relevance

This tool addresses the challenge of effectively using LLMs with codebases.  By converting a repository into a digestible format, `gptify` allows developers to leverage the power of LLMs for various development tasks.  Within the miniogre project, it plays a crucial role in facilitating AI-driven code understanding and interaction.

## Installation

The easiest way
`pip install gptify`.

`gptify` can also be installed using `pipx`:

```bash
poetry build && pipx install dist/*.whl
```
You can also uninstall older versions using the provided install script: `./install.sh`.

## Usage

After installation, navigate to the root directory of your Git repository and run:

```bash
gptify
```

This command will generate a file named `gptify_output.txt` in the current directory containing the formatted repository content.  You can then copy and paste the contents of this file into a ChatGPT session to interact with your codebase.

### Options

* `--output <filename>`: Specifies the name of the output file (default: `gptify_output.txt`).
* `--clipboard`: Copies the output directly to the clipboard, omitting the output file creation.
* `--openfile`: Opens the output file after creation using the default system application.
* `--preamble <filepath>`: Prepends a custom preamble to the output file.

## Example with custom output file:

```bash
gptify --output my_repo.txt
```

This will generate `my_repo.txt` with the processed repository data.

## Contributing

While contributions are welcome, the focus of this fork is on specific features for miniogre, and responses to pull requests might be delayed.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
