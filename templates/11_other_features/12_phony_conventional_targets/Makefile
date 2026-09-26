# makeling exercise: 11_other_features/12_phony_conventional_targets
# title: all, clean and install are phony
# objective: Declare the conventional targets phony so a file named install and a directory named clean cannot shadow them.
# reference: .phony
# hint: One .PHONY line can list several targets: .PHONY: all clean install. A phony target is out of date whenever make looks at it, whatever files share its name.

all: app.txt

app.txt: notes.txt
	cp notes.txt app.txt

install:
	cp app.txt installed.txt

clean:
	rm -f app.txt installed.txt
