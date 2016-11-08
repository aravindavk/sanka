ELM=elm-make
CLOSURE=java -jar /home/aravinda/bin/compiler-latest/compiler.jar
CLOSURE_FLAGS=

ELM_SRC=src
STATIC_JS=static
KN_SRC=knjs

default: elm

elm: $(STATIC_JS)/app.min.js $(STATIC_JS)/kn.js

$(STATIC_JS)/app.min.js: $(ELM_SRC)/app.js
	$(CLOSURE) $(CLOSURE_FLAGS) --js $(ELM_SRC)/app.js --js_output_file $(STATIC_JS)/app.min.js

$(ELM_SRC)/app.js: $(ELM_SRC)/Main.elm
	cd $(ELM_SRC) && $(ELM) Main.elm --output app.js

$(STATIC_JS)/kn.js: $(KN_SRC)/src/datagen.py $(KN_SRC)/src/base.js $(KN_SRC)/src/testsgen.py $(KN_SRC)/src/tests_manual.js
	cd $(KN_SRC) && make gen
	cp $(KN_SRC)/dist/kn.js $(STATIC_JS)/kn.js
	cp $(KN_SRC)/dist/tests_kn.js $(STATIC_JS)/tests_kn.js

.PHONY: clean

clean:
	cd $(KN_SRC) && make clean
	rm -f $(ELM_SRC)/app.js
	rm -f $(STATIC_JS)/app.min.js
	rm -f $(STATIC_JS)/kn.js
	rm -f $(STATIC_JS)/tests_kn.js
