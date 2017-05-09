all: resume.1.pdf

resume.1.pdf: resume.1.html
	weasyprint resume.1.html resume.1.pdf

resume.1.html: resume.1.md
	ronn resume.1.md --date="2016-03-02" --manual "Dominic May" -5

clean:
	rm -f resume.1.pdf resume.1.html resume.1
