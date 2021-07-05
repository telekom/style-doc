# Style-Doc

Style-Doc is Black for Python Docstrings and reStructuredText. It can be used to format
docstrings ([Google docstring format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings))
in Python files or [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).

This work is based on the
[`style_doc.py`](https://github.com/huggingface/transformers/blob/23ab0b6980e8af5e0b42905d8c09d388245a029d/utils/style_doc.py)
script from [The HuggingFace Inc. team](https://huggingface.co/).

## Installation

Style-Doc is available at [the Python Package Index (PyPI)](https://pypi.org/project/style-doc/).
It can be installed with _pip_:

```bash
$ pip install style-doc
```

## Usage

```bash
$ style-doc --help
usage: style-doc [-h] [--max_len MAX_LEN] [--check_only] [--py_only]
                 [--rst_only]
                 files [files ...]

positional arguments:
  files              The file(s) or folder(s) to restyle.

optional arguments:
  -h, --help         show this help message and exit
  --max_len MAX_LEN  The maximum length of lines.
  --check_only       Whether to only check and not fix styling issues.
  --py_only          Whether to only check py files.
  --rst_only         Whether to only check rst files.
```

## Licensing

Copyright (c) 2020 The HuggingFace Inc. team<br/>
Copyright (c) 2021 Philip May, Deutsche Telekom AG

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
