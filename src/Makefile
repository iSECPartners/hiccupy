FLAGS = -g -cp
JYTHON_PATH = /usr/local/Cellar/jython/2.5.2/libexec/jython.jar:.
JC = javac
JAR_NAME = ../hiccupy.jar

.SUFFIXES: .java .class

.java.class:
	$(JC) $(FLAGS) $(JYTHON_PATH) $*.java

CLASSES = BurpExtender.java

default: classes jar

classes: $(CLASSES:.java=.class)

jar: classes
	jar cvf $(JAR_NAME) $(SRC_DIR)*

