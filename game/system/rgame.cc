#include <boost/python.hpp>
#include <ncurses.h>

using namespace boost::python;

char GetTileChar(object tile) {
  return '.';
}

void Render(object world) {
  erase();

  // render map
  object map = world.attr("map");
  int width = extract<int>(map.attr("get_grid_size")()[0]);
  int height = extract<int>(map.attr("get_grid_size")()[1]);
  for (int y=0; y<height; y++) {
    for (int x=0; x<width; x++) {
      object tile = map.attr("get_tile_at")(x, y);
      mvaddch(y, x, GetTileChar(tile));
    }
  }

  // render pointer
  object pointer = world.attr("pointer");
  mvaddch(extract<int>(pointer[0]),
          extract<int>(pointer[1]), '@');
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
