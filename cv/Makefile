all: resume.1.pdf index.html

resume.1.pdf: resume.1.html
	cat resume.1.html
	weasyprint resume.1.html resume.1.pdf

resume.1.html: resume.1.md
	bundle exec ronn resume.1.md --date="2024-01-16" --manual "Elliana May" -5

index.html: resume.1.html
	cp resume.1.html index.html

clean:
	rm -f resume.1.pdf resume.1.html resume.1 index.html
