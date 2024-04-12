# gptify

This is a fork of [gptrepo](https://github.com/zackess/gptrepo) by zackees. This repo
implements features that are specific to its utilization inside the [miniogre devtool](https://github.com/ogre-run/miniogre).

Usage
```python
pip install gptify
gptify  # now output_gptify.txt should appear in the current directory
```

This tool concatenates through all the files in the repo and adds ai prompts which can be used for chat gpt conversations.

Simply open up the file, copy and paste it into the chat gpt window and then ask your question about the code.

`gptify` is a command-line tool that converts the contents of a Git repository into a text format, preserving the structure of the files and file contents. The generated output can be interpreted by AI language models, allowing them to process the repository's contents for various tasks, such as code review or documentation generation.

## Contributing

As of writing, development in the original repo seems to have been paused. This fork
implements very specific for use with miniogre.

Feel free to submit contributions, however, we might be slow to answer to PRs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
