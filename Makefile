SRC_DIR = src/
LIB_DIR = lib/
JAR_NAME = hiccupy.jar

all:
	cd $(SRC_DIR); $(MAKE) $(MFLAGS)

clean: 
	$(RM) $(SRC_DIR)*.class
	$(RM) $(LIB_DIR)*.class
	$(RM) $(LIB_DIR)plugins/*.class
	$(RM) $(LIB_DIR)plugins/plugins-enabled/*.class
	$(RM) $(SRC_DIR)burp/*.class
	$(RM) $(JAR_NAME)
