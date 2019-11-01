ELM=elm
CLOSURE=java -jar /home/aravinda/Downloads/closure-compiler-v20191027.jar
CLOSURE_FLAGS=

ELM_SRC=src
STATIC_JS=static
KN_SRC=knjs
# Set default Value only if not available
SITE?=site

default: elm

elm: $(STATIC_JS)/app.min.js $(STATIC_JS)/kn.js

$(STATIC_JS)/app.min.js: $(ELM_SRC)/app.js
	$(CLOSURE) $(CLOSURE_FLAGS) --js $(ELM_SRC)/app.js --js_output_file $(STATIC_JS)/app.min.js

$(ELM_SRC)/app.js: $(ELM_SRC)/Main.elm
	cd $(ELM_SRC) && $(ELM) make Main.elm --optimize --output app.js

$(STATIC_JS)/kn.js: $(KN_SRC)/src/datagen.py $(KN_SRC)/src/base.js $(KN_SRC)/src/testsgen.py $(KN_SRC)/src/tests_manual.js
	cd $(KN_SRC) && make gen
	cp $(KN_SRC)/dist/kn.js $(STATIC_JS)/kn.js
	cp $(KN_SRC)/dist/tests_kn.js $(STATIC_JS)/tests_kn.js

.PHONY: clean

publish: elm
	rm -rf $(SITE)
	cd $(STATIC_JS) && bower install
	mkdir -p $(SITE)/
	mkdir -p $(SITE)/$(STATIC_JS)/bower_components/qunit/qunit
	cp -r $(STATIC_JS)/bower_components/qunit/qunit/{qunit.js,qunit.css} $(SITE)/$(STATIC_JS)/bower_components/qunit/qunit/
	cp -r $(STATIC_JS)/*.js $(SITE)/$(STATIC_JS)/
	cp -r $(STATIC_JS)/*.css $(SITE)/$(STATIC_JS)/
	cp -r $(STATIC_JS)/*.png $(SITE)/$(STATIC_JS)/
	cp index.html $(SITE)/
	cp tests.html $(SITE)/

clean:
	cd $(KN_SRC) && make clean
	rm -f $(ELM_SRC)/app.js
	rm -f $(STATIC_JS)/app.min.js
	rm -f $(STATIC_JS)/kn.js
	rm -f $(STATIC_JS)/tests_kn.js
	rm -rf $(SITE)
