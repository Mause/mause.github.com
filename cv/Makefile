.PHONY: all clean view

all: resume.1.pdf index.html resume.1

resume.1.pdf: resume.1.html
	cat resume.1.html
	weasyprint resume.1.html resume.1.pdf

FLAGS=bundle exec ronn resume.1.md --date=`date --iso` --manual "Elliana May"

resume.1.html: resume.1.md
	$(FLAGS) --html

resume.1: resume.1.md
	$(FLAGS) --roff

view: resume.1.md
	$(FLAGS) --man

index.html: resume.1.html
	cp resume.1.html index.html

clean:
	rm -f resume.1.pdf resume.1.html resume.1 index.html
