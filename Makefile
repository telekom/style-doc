src := style_doc setup.py
test-src := tests

# check the code
check:
	style-doc --max_len 119 --check_only --py_only $(src) $(test-src)
	black $(src) $(test-src) --check --diff
	flake8 $(src) $(test-src)
	isort $(src) $(test-src) --check --diff
	mdformat --check *.md

# format the code
format:
	style-doc --max_len 119 --py_only $(src)
	black $(src) $(test-src)
	isort $(src) $(test-src)
	mdformat *.md

# execute tests
test:
	pytest $(test-src)
