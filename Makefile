src := style_doc setup.py
test-src := tests
other-src := setup.py

# check the code
check:
	style-doc --max_len 119 --check_only --py_only $(src) $(test-src) $(other-src)
	black $(src) $(test-src) $(other-src) --check --diff
	flake8 $(src) $(test-src) $(other-src)
	isort $(src) $(test-src) $(other-src) --check --diff
	mdformat --check *.md

# format the code
format:
	style-doc --max_len 119 --py_only $(src) $(other-src)
	black $(src) $(test-src) $(other-src)
	isort $(src) $(test-src) $(other-src)
	mdformat *.md

# execute tests
test:
	pytest $(test-src)
