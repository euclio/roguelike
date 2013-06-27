COMPILE_ARGS= -c -fpic
INCS= -I/usr/include/python2.7
LIBS= -lboost_python -lncurses -lSDL

hello.so : hello.o
	gcc -shared -Wl,-soname,"hello.so" -L/usr/local/lib hello.o ${LIBS} -o hello.so

hello.o : hello.cc
	g++ ${COMPILE_ARGS} ${INCS} hello.cc

.PHONY: clean
clean : 
	rm -f *.so *.o
