#include <boost/python.hpp>
#include <ncurses.h>

using namespace boost::python;

char GetTileChar(object tile) {
  return '.';
}

void Render(object gamestate) {
  erase();

  // render map
  object map = gamestate.attr("tile_map");
  int width = extract<int>(map.attr("get_grid_size")()[0]);
  int height = extract<int>(map.attr("get_grid_size")()[1]);
  for (int y=0; y<height; y++) {
    for (int x=0; x<width; x++) {
      object tile = map.attr("get_tile_at")(x, y);
      mvaddch(y, x, GetTileChar(tile));
    }
  }

  // render pointer
  object player = gamestate.attr("player");
  mvaddch(extract<int>(player.attr("location")[0]),
          extract<int>(player.attr("location")[1]), '@');
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
