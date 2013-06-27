COMPILE_ARGS= -c -fpic
INCS= -I/usr/include/python2.7
LIBS= -lboost_python -lncurses -lSDL

rgame.so : rgame.o
	gcc -shared -Wl,-soname,"rgame.so" -L/usr/local/lib rgame.o ${LIBS} -o rgame.so

rgame.o : rgame.cc
	g++ ${COMPILE_ARGS} ${INCS} rgame.cc

.PHONY: clean
clean : 
	rm -f *.so *.o
