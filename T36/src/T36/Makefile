DIROBJ := obj/
DIREXE := exec/
DIRHEA := include/
DIRSRC := src/

CFLAGS := -I$(DIRHEA) -c -Wall -ansi
LDFLAGS := -lglut -lGLU -lGL
CC := gcc

SRCFILES := $(patsubst $(DIRSRC)%.c,%,$(wildcard $(DIRSRC)*.c))

all: dirs compile

compile: $(SRCFILES)

dirs:
	mkdir -p $(DIROBJ) $(DIREXE)

$(SRCFILES): %: $(DIROBJ)%.o
	$(CC) -o $(DIREXE)$@ $^ $(LDFLAGS)

$(DIROBJ)%.o: $(DIRSRC)%.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -rf *~ core $(DIROBJ) $(DIREXE) $(DIRHEA)*~ $(DIRSRC)*~