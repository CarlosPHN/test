DIROBJ := obj/
DIREXE := exec/
DIRHEA := include/
DIRSRC := src/

CFLAGS := -I $(DIRHEA)
CC := g++

SRCFILES := $(patsubst $(DIRSRC)%.c,%,$(wildcard $(DIRSRC)*.c))

all: dirs compile

compile: $(SRCFILES)

dirs:
	mkdir -p $(DIROBJ) $(DIREXE)

$(SRCFILES): %: $(DIROBJ)%.o
	$(CC) -o $(DIREXE)$@ $^

$(DIROBJ)%.o: $(DIRSRC)%.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm -rf *~ core $(DIROBJ) $(DIREXE) $(DIRHEA)*~ $(DIRSRC)*~