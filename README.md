# Style-Doc

[![Apache 2.0 License](https://img.shields.io/github/license/telekom/style-doc)](https://github.com/telekom/style-doc/blob/main/LICENSE)
[![Contributor Covenant v2.0](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](https://github.com/telekom/style-doc/blob/main/CODE_OF_CONDUCT.md)
[![Python Version](https://img.shields.io/pypi/pyversions/style-doc)](https://www.python.org)
[![pypi](https://img.shields.io/pypi/v/style-doc.svg)](https://pypi.python.org/pypi/style-doc)
<br/>
[![Static Code Checks](https://github.com/telekom/style-doc/actions/workflows/static_checks.yml/badge.svg)](https://github.com/telekom/style-doc/actions/workflows/static_checks.yml)
[![GitHub issues](https://img.shields.io/github/issues-raw/telekom/style-doc)](https://github.com/telekom/style-doc/issues)

Style-Doc is Black for Python docstrings and reStructuredText (rst). It can be used to format
docstrings ([Google docstring format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings))
in Python files or [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).

![One Conversation](https://raw.githubusercontent.com/telekom/style-doc/main/docs/source/imgs/1c-logo.png)
<br/>
This project is maintained by the [One Conversation](https://www.welove.ai/)
team of [Deutsche Telekom AG](https://www.telekom.com/). It is based on the
[style_doc.py](https://github.com/huggingface/transformers/blob/23ab0b6980e8af5e0b42905d8c09d388245a029d/utils/style_doc.py)
script from the [HuggingFace Inc.](https://huggingface.co/) team.

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

### Examples

- format all docstrings (.py files) and rst files in the `src` and `docs` folder with line length of 99:<br/>
  `style-doc --max_len 99 src docs`
- check all docstrings (.py files) and rst files in the `src` and `docs` folder with line length of 99:<br/>
  `style-doc --max_len 99 --check_only src docs`
- format all docstrings (.py files only) in the `src` folder with line length of 99:<br/>
  `style-doc --max_len 99 --py_only src`
- check all docstrings (.py files only) in the `src` folder with line length of 99:<br/>
  `style-doc --max_len 99 --check_only --py_only src`
- format all rst files only in the `docs` folder with line length of 99:<br/>
  `style-doc --max_len 99 --rst_only docs`
- check all rst files only in the `docs` folder with line length of 99:<br/>
  `style-doc --max_len 99 --check_only --rst_only docs`

To integrate Style-Doc (and more checks) into your [GitHub Actions](https://docs.github.com/en/actions) see our
[static_checks.yml](https://github.com/telekom/style-doc/blob/main/.github/workflows/static_checks.yml)
example and our configuration in [setup.py](https://github.com/telekom/style-doc/blob/main/setup.py).

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
