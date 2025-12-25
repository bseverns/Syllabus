.PHONY: pdf clean

DOCS := $(shell find courses -name '*.md' -not -path '*/sessions/*')
OUT  := docs

pdf:
	@mkdir -p $(OUT)
	@for f in $(DOCS); do \	  name=$$(basename $${f%.md}).pdf; \	  dir=$$(echo $$f | sed 's#courses/##' | xargs dirname | tr '/' '-'); \	  out="$(OUT)/$${dir}-$${name}"; \	  echo "pandoc $$f -> $$out"; \	  pandoc "$$f" -o "$$out"; \	done

clean:
	rm -rf $(OUT)/*.pdf
