"""Exercises for the tutorial's "Functions" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.

Most of these exercises are observed through ``$(info ...)``: the text functions
run while make parses the file, so their results appear before any rule does.
"""

from spec import ex, mk

TOPIC = "10_functions"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_subst",
        title="Replace text with $(subst)",
        objective=(
            "Use $(subst from,to,text) to turn the sentence "
            '"I am not superman" into \'"I am "totally" superman"\'.'
        ),
        reference="First Functions",
        hint=(
            "$(subst from,to,text) replaces every occurrence of the literal "
            "string from with to. The quotes in the example are ordinary "
            "characters: they are part of the third argument, not syntax."
        ),
        makefile="""
# $(subst from,to,text) replaces every occurrence of "from" in "text".
bar := $(subst not,"totally", "I am not superman")
plain := $(subst world,there,hello world)

$(info bar=[$(bar)])
$(info plain=[$(plain)])

all:
\t@echo $(plain)
""",
        steps=[
            mk(
                stdout="bar=[ \"I am \"totally\" superman\"]",
                stdout_mode="contains",
                description="every 'not' is replaced, quotes and all",
            ),
            mk(
                stdout="plain=[hello there]",
                stdout_mode="contains",
                description="a plainer substitution at the top level",
            ),
            mk(
                stdout="hello there",
                description="the recipe prints the substituted sentence",
            ),
        ],
        breaks=[
            (
                '$(subst not,"totally", "I am not superman")',
                '$(subst "totally",not, "I am not superman")',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="02_subst_spaces_and_commas",
        title="Replacing spaces and commas",
        objective=(
            "Turn the list a b c into the single word a,b,c by replacing every "
            "space with a comma."
        ),
        reference="First Functions",
        hint=(
            "Neither a comma nor a space is easy to write as an argument, so "
            "build them first: comma := , and space := $(empty) $(empty). "
            "Adding extra spaces around an argument makes them part of the "
            "string that is searched for or inserted."
        ),
        makefile="""
# A comma and a space are awkward to type literally; build them from variables.
comma := ,
empty :=
space := $(empty) $(empty)

foo := a b c
joined := $(subst $(space),$(comma),$(foo))
# Watch out: the spaces around the arguments below end up in the result.
spaced := $(subst $(space), $(comma) ,$(foo))

$(info joined=[$(joined)])
$(info spaced=[$(spaced)])

all:
\t@echo $(joined)
""",
        steps=[
            mk(
                stdout="joined=[a,b,c]",
                stdout_mode="contains",
                description="the list is joined with commas",
            ),
            mk(
                stdout="spaced=[a , b , c]",
                stdout_mode="contains",
                description="extra spaces around the arguments are inserted too",
            ),
            mk(
                stdout="a,b,c",
                description="the recipe prints the joined list",
            ),
        ],
        breaks=[("space := $(empty) $(empty)", "space := $(empty)$(empty)")],
    ),
    ex(
        topic=TOPIC,
        slug="03_strip",
        title="Cleaning up whitespace with $(strip)",
        objective=(
            "Normalise the messy variable into a b c: no leading, trailing or "
            "repeated whitespace left."
        ),
        reference="First Functions",
        hint=(
            "$(strip text) removes leading and trailing whitespace and reduces "
            "every run of spaces inside the text to a single space. "
            "Whitespace-only text strips down to the empty string."
        ),
        makefile="""
empty :=
raw := a   b $(empty)  c
clean := $(strip $(raw))
blank := $(strip $(empty)   )

$(info clean=[$(clean)])
$(info blank=[$(blank)])
$(info words=[$(words $(clean))])

all:
\t@echo $(clean)
""",
        steps=[
            mk(
                stdout="clean=[a b c]",
                stdout_mode="contains",
                description="the runs of spaces are collapsed",
            ),
            mk(
                stdout="blank=[]",
                stdout_mode="contains",
                description="a whitespace-only value strips to nothing",
            ),
            mk(
                stdout="words=[3]",
                stdout_mode="contains",
                description="the cleaned value is a three word list",
            ),
        ],
        breaks=[("clean := $(strip $(raw))", "clean := $(raw)")],
    ),
    ex(
        topic=TOPIC,
        slug="04_findstring",
        title="Looking for a substring with $(findstring)",
        objective=(
            "Ask whether the haystack contains the word quick, and whether it "
            "contains the word slow."
        ),
        reference="First Functions",
        hint=(
            "$(findstring find,in) searches in for the text find and returns "
            "find itself when it is there, or the empty string when it is not. "
            "The arguments are (needle, haystack)."
        ),
        makefile="""
haystack := the quick brown fox

$(info found=[$(findstring quick,$(haystack))])
$(info single=[$(findstring o,$(haystack))])
$(info missing=[$(findstring slow,$(haystack))])

all:
\t@echo searched for quick and slow
""",
        steps=[
            mk(
                stdout="found=[quick]",
                stdout_mode="contains",
                description="the needle is echoed back when it is present",
            ),
            mk(
                stdout="single=[o]",
                stdout_mode="contains",
                description="a single character works as well",
            ),
            mk(
                stdout="missing=[]",
                stdout_mode="contains",
                description="an absent needle returns nothing",
            ),
        ],
        breaks=[
            ("$(findstring quick,$(haystack))", "$(findstring $(haystack),quick)")
        ],
    ),
    ex(
        topic=TOPIC,
        slug="05_patsubst",
        title="Rewriting words with $(patsubst)",
        objective=(
            "Turn a.o b.o l.a c.o into a.c b.c l.a c.c, and turn the two src/ "
            "paths into build/ paths, with %.o and %.c patterns."
        ),
        reference="String Substitution",
        hint=(
            "$(patsubst pattern,replacement,text) rewrites every word that "
            "matches pattern; the % stands for any characters, and the % in the "
            "replacement is filled in with whatever it matched. A word that "
            "does not match is left alone."
        ),
        makefile="""
foo := a.o b.o l.a c.o

obj := $(patsubst %.o,%.c,$(foo))
moved := $(patsubst src/%.c,build/%.o,src/a.c src/b.c)

$(info obj=[$(obj)])
$(info moved=[$(moved)])

all:
\t@echo $(obj)
""",
        steps=[
            mk(
                stdout="obj=[a.c b.c l.a c.c]",
                stdout_mode="contains",
                description="only the words ending in .o are rewritten",
            ),
            mk(
                stdout="moved=[build/a.o build/b.o]",
                stdout_mode="contains",
                description="the % carries the file name across",
            ),
            mk(
                stdout="a.c b.c l.a c.c",
                description="the recipe prints the rewritten list",
            ),
        ],
        breaks=[("$(patsubst %.o,%.c,$(foo))", "$(patsubst .o,.c,$(foo))")],
    ),
    ex(
        topic=TOPIC,
        slug="06_substitution_reference",
        title="The $(text:pattern=replacement) shorthand",
        objective=(
            "Express the same rewrite twice: once with the % shorthand and once "
            "with the suffix-only shorthand."
        ),
        reference="String Substitution",
        hint=(
            "$(foo:%.o=%.c) is shorthand for $(patsubst %.o,%.c,$(foo)), and "
            "$(foo:.o=.c) is the suffix-only form of the same thing. Do not "
            "pad the shorthand with spaces; they would become part of the "
            "search or the replacement."
        ),
        makefile="""
foo := a.o b.o l.a c.o

# $(foo:pattern=replacement) is a shorthand for $(patsubst pattern,replacement,$(foo)).
one := $(foo:%.o=%.c)
# Dropping the % makes it a plain suffix substitution.
two := $(foo:.o=.c)

$(info one=[$(one)])
$(info two=[$(two)])

all:
\t@echo $(one)
""",
        steps=[
            mk(
                stdout="one=[a.c b.c l.a c.c]",
                stdout_mode="contains",
                description="the % shorthand rewrites every match",
            ),
            mk(
                stdout="two=[a.c b.c l.a c.c]",
                stdout_mode="contains",
                description="the suffix shorthand gives the same answer",
            ),
            mk(
                stdout="a.c b.c l.a c.c",
                description="the recipe prints the rewritten list",
            ),
        ],
        breaks=[("two := $(foo:.o=.c)", "two := $(foo:.c=.o)")],
    ),
    ex(
        topic=TOPIC,
        slug="07_word_functions",
        title="Counting and picking words",
        objective=(
            "Report how many words names holds, then pick out its first, last, "
            "second and middle words."
        ),
        reference="First Functions",
        hint=(
            "$(words list) counts the words, $(firstword list) and "
            "$(lastword list) take the ends, $(word n,list) takes the nth, and "
            "$(wordlist start,end,list) takes a range. Asking for a word that "
            "is past the end returns nothing."
        ),
        makefile="""
names := ada grace edsger barbara

$(info count=[$(words $(names))])
$(info first=[$(firstword $(names))])
$(info last=[$(lastword $(names))])
$(info second=[$(word 2,$(names))])
$(info middle=[$(wordlist 2,3,$(names))])
$(info past=[$(word 9,$(names))])

all:
\t@echo $(firstword $(names)) and $(lastword $(names))
""",
        steps=[
            mk(
                stdout="count=[4]",
                stdout_mode="contains",
                description="the list has four words",
            ),
            mk(
                stdout="first=[ada]\nlast=[barbara]",
                description="the ends of the list",
            ),
            mk(
                stdout="second=[grace]",
                stdout_mode="contains",
                description="n is one-based",
            ),
            mk(
                stdout="middle=[grace edsger]",
                stdout_mode="contains",
                description="wordlist takes an inclusive range",
            ),
            mk(
                stdout="past=[]",
                stdout_mode="contains",
                description="there is no ninth word",
            ),
        ],
        breaks=[("$(words $(names))", "$(words names)")],
    ),
    ex(
        topic=TOPIC,
        slug="08_sort",
        title="$(sort) sorts and removes duplicates",
        objective=(
            "Merge the two lists of sources into one alphabetical list without "
            "repeating a.c, and count the result."
        ),
        reference="First Functions",
        hint=(
            "$(sort list) returns the words sorted, and drops every duplicate. "
            "It is the shortest way to merge two lists into a set."
        ),
        makefile="""
src := b.c a.c
gen := c.c a.c

combined := $(sort $(src) $(gen))

$(info combined=[$(combined)])
$(info count=[$(words $(combined))])

all:
\t@echo $(combined)
""",
        steps=[
            mk(
                stdout="combined=[a.c b.c c.c]",
                stdout_mode="contains",
                description="sorted, and the duplicate a.c is gone",
            ),
            mk(
                stdout="count=[3]",
                stdout_mode="contains",
                description="four words in, three distinct words out",
            ),
            mk(
                stdout="a.c b.c c.c",
                description="the recipe prints the merged list",
            ),
        ],
        breaks=[("combined := $(sort $(src) $(gen))", "combined := $(src) $(gen)")],
    ),
    ex(
        topic=TOPIC,
        slug="09_filename_functions",
        title="Splitting file names apart",
        objective=(
            "Take src/a.c src/b.h apart into directories, file names, suffixes "
            "and stems."
        ),
        reference="First Functions",
        hint=(
            "$(dir) keeps everything up to and including the last slash, "
            "$(notdir) drops it, $(suffix) and $(basename) split at the last "
            "dot. $(basename) keeps the directory part of the path."
        ),
        makefile="""
files := src/a.c src/b.h

$(info dirs=[$(dir $(files))])
$(info names=[$(notdir $(files))])
$(info suffixes=[$(suffix $(files))])
$(info stems=[$(basename $(files))])
$(info bare=[$(basename noext)][$(suffix noext)])

all:
\t@echo $(notdir $(files))
""",
        steps=[
            mk(
                stdout="dirs=[src/ src/]",
                stdout_mode="contains",
                description="the directory keeps its trailing slash",
            ),
            mk(
                stdout="names=[a.c b.h]",
                stdout_mode="contains",
                description="notdir drops the directory",
            ),
            mk(
                stdout="suffixes=[.c .h]",
                stdout_mode="contains",
                description="the suffix includes the dot",
            ),
            mk(
                stdout="stems=[src/a src/b]",
                stdout_mode="contains",
                description="basename keeps the directory, drops the suffix",
            ),
            mk(
                stdout="bare=[noext][]",
                stdout_mode="contains",
                description="a name without a dot has no suffix",
            ),
        ],
        breaks=[
            (
                "$(info stems=[$(basename $(files))])",
                "$(info stems=[$(basename $(notdir $(files)))])",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="10_addprefix_addsuffix_join",
        title="Building new names with $(addprefix), $(addsuffix) and $(join)",
        objective=(
            "Turn the two names main util into object files, then put them "
            "under src/, and pair the prefixes src/ and build/ with two files."
        ),
        reference="First Functions",
        hint=(
            "$(addsuffix x,list) appends to every word, $(addprefix x,list) "
            "prepends to every word, and you can nest them. "
            "$(join list1,list2) glues the words together pairwise."
        ),
        makefile="""
names := main util

$(info objects=[$(addsuffix .o,$(names))])
$(info paths=[$(addprefix src/,$(addsuffix .o,$(names)))])
$(info joined=[$(join src/ build/,a.c b.c)])
$(info short=[$(join a b c,1 2)])

all:
\t@echo $(paths)
""",
        steps=[
            mk(
                stdout="objects=[main.o util.o]",
                stdout_mode="contains",
                description="a suffix on every word",
            ),
            mk(
                stdout="paths=[src/main.o src/util.o]",
                stdout_mode="contains",
                description="a prefix wrapped around the suffixed words",
            ),
            mk(
                stdout="joined=[src/a.c build/b.c]",
                stdout_mode="contains",
                description="join pairs the words off one by one",
            ),
            mk(
                stdout="short=[a1 b2 c]",
                stdout_mode="contains",
                description="a longer list simply keeps its extra words",
            ),
        ],
        breaks=[
            (
                "$(addprefix src/,$(addsuffix .o,$(names)))",
                "$(addsuffix src/,$(addsuffix .o,$(names)))",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="11_wildcard",
        title="Finding files with $(wildcard)",
        objective=(
            "Collect the C sources in the current directory and in the sub/ "
            "directory, and confirm that a pattern with no matches gives an "
            "empty list."
        ),
        reference="First Functions",
        hint=(
            "$(wildcard pattern) expands to the sorted list of files matching "
            "the glob, and to nothing at all when nothing matches. "
            "Unlike the * in a rule, it runs as soon as the variable is "
            "expanded."
        ),
        makefile="""
sources := $(wildcard *.c)

$(info sources=[$(sources)])
$(info count=[$(words $(sources))])
$(info none=[$(wildcard *.zzz)])
$(info nested=[$(wildcard sub/*.c)])

all:
\t@echo sources: $(sources)
""",
        steps=[
            mk(
                stdout="sources=[a.c b.c]",
                stdout_mode="contains",
                description="both C files are found, sorted",
            ),
            mk(
                stdout="count=[2]",
                stdout_mode="contains",
                description="the header is not a .c file",
            ),
            mk(
                stdout="none=[]",
                stdout_mode="contains",
                description="a pattern that matches nothing yields no words",
            ),
            mk(
                stdout="nested=[sub/e.c]",
                stdout_mode="contains",
                description="the glob can look into a subdirectory",
            ),
        ],
        breaks=[("$(wildcard *.c)", "$(wildcard *.h)")],
        files={
            "a.c": "/* a.c */\n",
            "b.c": "/* b.c */\n",
            "d.h": "/* d.h */\n",
            "sub/e.c": "/* sub/e.c */\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="12_realpath_and_abspath",
        title="$(realpath) needs the file, $(abspath) does not",
        objective=(
            "Show that realpath resolves a name that exists on disk while "
            "abspath gives an absolute path for any name at all."
        ),
        reference="First Functions",
        hint=(
            "$(realpath names) resolves names that exist, following symlinks, "
            "and returns nothing for a name that is not there. "
            "$(abspath names) turns any name into an absolute path, whether or "
            "not the file exists."
        ),
        makefile="""
# present.txt exists; nosuch.txt does not.
$(info real_missing=[$(if $(realpath nosuch.txt),found,missing)])
$(info abs_missing=[$(if $(abspath nosuch.txt),found,missing)])
$(info real_here=[$(if $(realpath present.txt),found,missing)])
$(info abs_here=[$(if $(abspath present.txt),found,missing)])

all:
\t@echo checked
""",
        steps=[
            mk(
                stdout="real_missing=[missing]",
                stdout_mode="contains",
                description="realpath returns nothing for a name that is not there",
            ),
            mk(
                stdout="abs_missing=[found]",
                stdout_mode="contains",
                description="abspath resolves a name that does not exist",
            ),
            mk(
                stdout="real_here=[found]",
                stdout_mode="contains",
                description="realpath resolves the file that does exist",
            ),
        ],
        breaks=[("$(realpath nosuch.txt)", "$(abspath nosuch.txt)")],
        files={"present.txt": "here\n"},
    ),
    ex(
        topic=TOPIC,
        slug="13_foreach",
        title="Looping with $(foreach)",
        objective=(
            "Append an exclamation mark to each word of who are you, producing "
            "who! are! you!"
        ),
        reference="The foreach function",
        hint=(
            "$(foreach var,list,text) sets var to each word of list in turn and "
            "expands text for each of them. The results are joined with single "
            "spaces. Inside text you must use the loop variable, not the whole "
            "list."
        ),
        makefile="""
foo := who are you
# For each "word" in foo, output that same word with an exclamation after it.
bar := $(foreach wrd,$(foo),$(wrd)!)

$(info bar=[$(bar)])

all:
\t@echo $(bar)
""",
        steps=[
            mk(
                stdout="bar=[who! are! you!]",
                stdout_mode="contains",
                description="the loop variable is expanded once per word",
            ),
            mk(
                stdout="who! are! you!",
                description="the recipe prints the transformed list",
            ),
        ],
        breaks=[
            ("$(foreach wrd,$(foo),$(wrd)!)", "$(foreach wrd,$(foo),$(foo)!)")
        ],
    ),
    ex(
        topic=TOPIC,
        slug="14_foreach_paths",
        title="Building a list of paths with $(foreach)",
        objective=(
            "Map the module names auth cart order to build/auth.o build/cart.o "
            "build/order.o using a single foreach."
        ),
        reference="The foreach function",
        hint=(
            "Write the path around the loop variable: "
            "$(foreach m,$(modules),build/$(m).o). The text is re-expanded for "
            "every word, so $(m) takes a different value each time."
        ),
        makefile="""
modules := auth cart order
objects := $(foreach m,$(modules),build/$(m).o)

$(info objects=[$(objects)])

all:
\t@echo $(objects)
""",
        steps=[
            mk(
                stdout="objects=[build/auth.o build/cart.o build/order.o]",
                stdout_mode="contains",
                description="one path per module, directory included",
            ),
            mk(
                stdout="build/auth.o build/cart.o build/order.o",
                description="the recipe prints the generated paths",
            ),
        ],
        breaks=[("$(foreach m,$(modules),build/$(m).o)", "$(foreach m,$(modules),$(m).o)")],
    ),
    ex(
        topic=TOPIC,
        slug="15_if",
        title="Choosing with $(if)",
        objective=(
            "Produce then! for a condition that expands to something, else! for "
            "one that expands to nothing, and use the two-argument form too."
        ),
        reference="The if function",
        hint=(
            "$(if condition,then-part,else-part) tests whether the condition "
            "expands to a non-empty string. The else-part is optional, and an "
            "empty condition makes the whole $(if) expand to nothing when it is "
            "left out."
        ),
        makefile="""
empty :=
foo := some-text

$(info one=[$(if this-is-not-empty,then!,else!)])
$(info two=[$(if $(empty),then!,else!)])
$(info three=[$(if $(empty),then!)])
$(info four=[$(if $(foo),yes)])
$(info five=[$(if $(empty),yes)])

all:
\t@echo done
""",
        steps=[
            mk(
                stdout="one=[then!]",
                stdout_mode="contains",
                description="a literal word is non-empty, so the then-part runs",
            ),
            mk(
                stdout="two=[else!]",
                stdout_mode="contains",
                description="an empty variable takes the else branch",
            ),
            mk(
                stdout="three=[]",
                stdout_mode="contains",
                description="with no else-part the result is empty",
            ),
            mk(
                stdout="four=[yes]",
                stdout_mode="contains",
                description="a non-empty variable is true",
            ),
            mk(
                stdout="five=[]",
                stdout_mode="contains",
                description="an empty variable is false",
            ),
        ],
        breaks=[
            ("$(if $(empty),then!,else!)", "$(if empty,then!,else!)"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="16_call_basics",
        title="Writing a function with $(call)",
        objective=(
            "Report the name of the called variable and its parameters with "
            "$(0), $(1) and $(2), and make a template that repeats its first "
            "parameter three times."
        ),
        reference="The call function",
        hint=(
            "A variable holding $(1), $(2), ... is a function you invoke with "
            "$(call variable,param1,param2). $(0) is the name of the variable "
            "being called, and parameters you do not pass are empty."
        ),
        makefile="""
sweet_new_fn = Variable Name: $(0) First: $(1) Second: $(2) Empty Variable: $(3)
triple = $(1) $(1) $(1)

$(info call=[$(call sweet_new_fn, go, tigers)])
$(info triple=[$(call triple,ha)])

all:
\t@echo $(call triple,ha)
""",
        steps=[
            mk(
                stdout="call=[Variable Name: sweet_new_fn First:  go Second:  tigers Empty Variable: ]",
                stdout_mode="contains",
                description="$(0) is the variable name, $(3) was never passed",
            ),
            mk(
                stdout="triple=[ha ha ha]",
                stdout_mode="contains",
                description="the first parameter can be used more than once",
            ),
            mk(
                stdout="ha ha ha",
                description="the recipe calls the same template",
            ),
        ],
        breaks=[("triple = $(1) $(1) $(1)", "triple = $(0) $(0) $(0)")],
    ),
    ex(
        topic=TOPIC,
        slug="17_call_template",
        title="A template that builds a list",
        objective=(
            "Use $(call) to turn the names main util into the object files "
            "src/main.o src/util.o, and let a pattern rule build them."
        ),
        reference="The call function",
        hint=(
            "Define the template with = first, then expand it with "
            "$(call objects_for,src,$(names)): $(1) becomes src and $(2) the "
            "list. Inside the template a $(foreach) visits every word of $(2)."
        ),
        makefile="""
# A template: $(1) is the directory, $(2) the list of names.
objects_for = $(foreach name,$(2),$(1)/$(name).o)

names := main util
objects := $(call objects_for,src,$(names))

$(info objects=[$(objects)])

app: $(objects)
\t@echo linking $^

src/%.o: src/%.c
\t@echo compile $< -o $@
""",
        steps=[
            mk(
                stdout="objects=[src/main.o src/util.o]",
                stdout_mode="contains",
                description="the template produced one object file per name",
            ),
            mk(
                stdout="compile src/main.c -o src/main.o",
                stdout_mode="contains",
                description="make builds the first object through the pattern rule",
            ),
            mk(
                stdout="linking src/main.o src/util.o",
                stdout_mode="contains",
                description="both objects are prerequisites of app",
            ),
        ],
        breaks=[
            (
                "$(call objects_for,src,$(names))",
                "$(call objects_for,$(names),src)",
            )
        ],
        files={
            "src/main.c": "int main(void) { return 0; }\n",
            "src/util.c": "int util(void) { return 1; }\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="18_shell",
        title="$(shell) runs at expansion time",
        objective=(
            "Make snapshot capture the value of who as it is when the variable "
            "is defined, so it stays first even though who becomes second "
            "afterwards."
        ),
        reference="The shell function",
        hint=(
            "$(shell command) runs the command while make expands the text and "
            "returns its output with every newline turned into a space. "
            "A recursive variable (=) re-runs the shell on every expansion; "
            "a simply expanded variable (:=) runs it once, at that line."
        ),
        makefile="""
who = first
snapshot := $(shell echo $(who))
who = second
live = $(shell echo $(who))

$(info snapshot=[$(snapshot)])
$(info live=[$(live)])
$(info two_lines=[$(shell echo alpha; echo beta)])

all:
\t@echo in recipe: $(live)
""",
        steps=[
            mk(
                stdout="snapshot=[first]",
                stdout_mode="contains",
                description="the shell ran while who still held first",
            ),
            mk(
                stdout="live=[second]",
                stdout_mode="contains",
                description="the recursive variable runs the shell again, later",
            ),
            mk(
                stdout="two_lines=[alpha beta]",
                stdout_mode="contains",
                description="two lines of output arrive as two words",
            ),
            mk(
                stdout="in recipe: second",
                stdout_mode="contains",
                description="the shell runs once more when the recipe is expanded",
            ),
        ],
        breaks=[
            ("snapshot := $(shell echo $(who))", "snapshot = $(shell echo $(who))")
        ],
    ),
    ex(
        topic=TOPIC,
        slug="19_filter",
        title="Selecting words with $(filter)",
        objective=(
            "Keep only the .o files from obj_files, then keep the .o and "
            ".result files, then keep every C source and header."
        ),
        reference="The filter function",
        hint=(
            "$(filter pattern,list) returns the words of list that match the "
            "pattern, in their original order, and drops the rest. Write as "
            "many patterns as you like, separated by spaces, and remember the "
            "% in front of the suffix."
        ),
        makefile="""
sources := a.c b.h c.c d.h
obj_files := foo.result bar.o lose.o

filtered := $(filter %.o,$(obj_files))

$(info filtered=[$(filtered)])
$(info both=[$(filter %.o %.result,$(obj_files))])
$(info keep=[$(filter %.c %.h,$(sources))])

all:
\t@echo $(filtered)
""",
        steps=[
            mk(
                stdout="filtered=[bar.o lose.o]",
                stdout_mode="contains",
                description="only the object files survive",
            ),
            mk(
                stdout="both=[foo.result bar.o lose.o]",
                stdout_mode="contains",
                description="several patterns can be given at once",
            ),
            mk(
                stdout="keep=[a.c b.h c.c d.h]",
                stdout_mode="contains",
                description="the original order is kept",
            ),
            mk(
                stdout="bar.o lose.o",
                description="the recipe prints the filtered list",
            ),
        ],
        breaks=[("$(filter %.o,$(obj_files))", "$(filter .o,$(obj_files))")],
    ),
    ex(
        topic=TOPIC,
        slug="20_filter_out",
        title="Removing words with $(filter-out)",
        objective=(
            "Drop the headers from files, drop everything starting with test "
            "from objects, and nest the two ideas to keep only the objects that "
            "are left."
        ),
        reference="The filter function",
        hint=(
            "$(filter-out pattern,list) is $(filter) with the sense reversed: "
            "it keeps the words that do not match. Filters can be nested, so "
            "$(filter %.o,$(filter-out test%,$(objects))) removes the test "
            "objects first and then keeps the .o ones."
        ),
        makefile="""
files := a.c b.h c.c d.h
objects := test_a.o a.o test_b.o b.o notes.txt

kept := $(filter %.o,$(filter-out test%,$(objects)))

$(info without_headers=[$(filter-out %.h,$(files))])
$(info candidates=[$(filter-out test%,$(objects))])
$(info kept=[$(kept)])

all:
\t@echo final: $(kept)
""",
        steps=[
            mk(
                stdout="without_headers=[a.c c.c]",
                stdout_mode="contains",
                description="everything that is not a header is kept",
            ),
            mk(
                stdout="candidates=[a.o b.o notes.txt]",
                stdout_mode="contains",
                description="the test% pattern removes two objects",
            ),
            mk(
                stdout="kept=[a.o b.o]",
                stdout_mode="contains",
                description="the nested filter drops the notes file too",
            ),
            mk(
                stdout="final: a.o b.o",
                stdout_mode="contains",
                description="the recipe prints the doubly filtered list",
            ),
        ],
        breaks=[("$(filter-out %.h,$(files))", "$(filter %.h,$(files))")],
    ),
]
