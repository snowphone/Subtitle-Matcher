DESTDIR=$$HOME/.local/bin

TARGET=$(DESTDIR)/match_subtitles

install: 
	mkdir -p $(DESTDIR)
	cp ./subtitle_matcher.py $(TARGET)
	chmod +x $(TARGET)

test:
	pytest --verbose .

coverage:
	pytest --cov .

uninstall:
	$(RM) $(TARGET)
