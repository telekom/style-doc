# Style-Doc

[![Apache 2.0 License](https://img.shields.io/github/license/telekom/style-doc)](https://github.com/telekom/style-doc/blob/main/LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Code%20of%20Conduct-Contributor%20Covenant-ff69b4.svg)](https://github.com/telekom/style-doc/blob/main/CODE_OF_CONDUCT.md)
[![Python Version](https://img.shields.io/pypi/pyversions/style-doc)](https://www.python.org)
[![pypi](https://img.shields.io/pypi/v/style-doc.svg)](https://pypi.python.org/pypi/style-doc)
<br/>
[![pytest](https://github.com/telekom/style-doc/actions/workflows/pytest.yml/badge.svg)](https://github.com/telekom/style-doc/actions/workflows/pytest.yml)
[![Static Code Checks](https://github.com/telekom/style-doc/actions/workflows/static_checks.yml/badge.svg)](https://github.com/telekom/style-doc/actions/workflows/static_checks.yml)
[![GitHub issues](https://img.shields.io/github/issues-raw/telekom/style-doc)](https://github.com/telekom/style-doc/issues)

Style-Doc is Black for Python docstrings and reStructuredText (rst). It can be used to format
docstrings ([Google docstring format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings))
in Python files or [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).

Style-Doc can handle Linux, Windows and Mac style line endings. The output will nevertheless be convertet to `\n` Linux line endings.

## Table of Contents

- [Maintainers](#maintainers)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Support and Feedback](#support-and-feedback)
- [Reporting Security Vulnerabilities](#reporting-security-vulnerabilities)
- [Contribution](#contribution)
- [Code of Conduct](#code-of-conduct)
- [Licensing](#licensing)

## Maintainers

![One Conversation](https://raw.githubusercontent.com/telekom/style-doc/main/docs/source/imgs/1c-logo.png)
<br/>
This project is maintained by the [One Conversation](https://www.welove.ai/)
team of [Deutsche Telekom AG](https://www.telekom.com/).
It is based on the
[style_doc.py](https://github.com/huggingface/transformers/blob/23ab0b6980e8af5e0b42905d8c09d388245a029d/utils/style_doc.py)
script from the [HuggingFace](https://huggingface.co/) team.
Many thanks for [your consent](https://github.com/huggingface/transformers/issues/12473)
to publish it as a standalone package 🤗 ♥.

## Installation

Style-Doc is available at [the Python Package Index (PyPI)](https://pypi.org/project/style-doc/).
It can be installed with pip:

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
  files              file(s) or folder(s) to restyle

optional arguments:
  -h, --help         show this help message and exit
  --max_len MAX_LEN  maximum length of lines, default: 119
  --check_only       only check and not fix styling issues
  --py_only          only check py files
  --rst_only         only check rst files
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

## Support and Feedback

The following channels are available for discussions, feedback, and support requests:

- [open an issue in our GitHub repository](https://github.com/telekom/style-doc/issues/new/choose)
- [send an e-mail to our open source team](mailto:opensource@telekom.de)

## Reporting Security Vulnerabilities

This project is built with security and data privacy in mind to ensure your data is safe.
We are grateful for security researchers and users reporting a vulnerability to us, first.
To ensure that your request is handled in a timely manner and non-disclosure of vulnerabilities
can be assured, please follow the below guideline.

**Please do not report security vulnerabilities directly on GitHub.
GitHub Issues can be publicly seen and therefore would result in a direct disclosure.**

Please address questions about data privacy, security concepts,
and other media requests to the [opensource@telekom.de](mailto:opensource@telekom.de) mailbox.

## Contribution

Our commitment to open source means that we are enabling - in fact encouraging - all interested
parties to contribute and become part of our developer community.

Contribution and feedback is encouraged and always welcome. For more information about how to
contribute, as well as additional contribution information, see our
[Contribution Guidelines](https://github.com/telekom/style-doc/blob/main/CONTRIBUTING.md).

## Code of Conduct

This project has adopted the [Contributor Covenant](https://www.contributor-covenant.org/)
as our code of conduct. Please see the details in our
[Contributor Covenant Code of Conduct](https://github.com/telekom/style-doc/blob/main/CODE_OF_CONDUCT.md).
All contributors must abide by the code of conduct.

## Licensing

Copyright (c) 2020 The HuggingFace Inc. team<br/>
Copyright (c) 2021 Philip May, Deutsche Telekom AG

Licensed under the [Apache License, Version 2.0](https://github.com/telekom/style-doc/blob/main/LICENSE) (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
