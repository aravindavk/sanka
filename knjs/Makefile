gen:
	mkdir -p dist
	python3 src/datagen.py > dist/kn.js
	cat src/base.js >> dist/kn.js
	python3 src/testsgen.py > dist/tests_kn.js
	cat src/tests_manual.js >> dist/tests_kn.js

test: gen
	python -m SimpleHTTPServer

clean:
	rm -rf dist
