# coding=utf-8
# Copyright (c) 2021 Philip May, Deutsche Telekom AG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os


def test_linux_line_separators(tmpdir):
    tmp_file_name = os.path.join(tmpdir, "file.rst")
    with open(tmp_file_name, "w") as f:
        f.write("Main\n====\n")

    os.system(f"style-doc --max_len 99 {tmpdir}")

    with open(tmp_file_name, "r") as f:
        content = f.readlines()

    assert content[0] == "Main\n"
    assert content[1] == "=" * 99 + "\n"


def test_windows_line_separators(tmpdir):
    tmp_file_name = os.path.join(tmpdir, "file.rst")
    with open(tmp_file_name, "w") as f:
        f.write("Main\r\n====\r\n")

    os.system(f"style-doc --max_len 99 {tmpdir}")

    with open(tmp_file_name, "r") as f:
        content = f.readlines()

    assert content[0] == "Main\n"
    assert content[1] == "=" * 99 + "\n"


def test_mac_line_separators(tmpdir):
    tmp_file_name = os.path.join(tmpdir, "file.rst")
    with open(tmp_file_name, "w") as f:
        f.write("Main\r====\r")

    os.system(f"style-doc --max_len 99 {tmpdir}")

    with open(tmp_file_name, "r") as f:
        content = f.readlines()

    assert content[0] == "Main\n"
    assert content[1] == "=" * 99 + "\n"
