src := style_doc
test-src := tests
other-src := setup.py

check:
	style-doc --max_len 119 --check_only --py_only $(src) $(test-src) $(other-src)
	black $(src) $(test-src) $(other-src) --check --diff
	flake8 $(src) $(test-src) $(other-src)
	isort $(src) $(test-src) $(other-src) --check --diff
	mdformat --check *.md
	mypy --install-types --non-interactive $(src) $(test-src) $(other-src)
	pylint $(src)

format:
	style-doc --max_len 119 --py_only $(src) $(test-src) $(other-src)
	black $(src) $(test-src) $(other-src)
	isort $(src) $(test-src) $(other-src)
	mdformat *.md

test:
	pytest $(test-src)
