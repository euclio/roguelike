#include <boost/python.hpp>
#include <ncurses.h>

using namespace boost::python;

void Render(object world) {
  // just press
  object message = world.attr("message");
  printw(extract<char*>(message));
}

void GameInit(object world, object inputHandler) {
  initscr();
  while (1) {
    Render(world);
    refresh();
    char inputChar = getch();
    if (inputChar == 'q') {
      break;
    }
    inputHandler(inputChar);
  }
  endwin();
}

BOOST_PYTHON_MODULE(rgame) {
  def("GameInit", GameInit);
}
