.PHONY: style

src := style_doc setup.py

# format the code
format:
	black $(src)
	isort $(src)
	mdformat *.md

# check the code
check:
	black $(src) --check --diff
	flake8 $(src)
	isort $(src) --check --diff	
	mdformat --check *.md
