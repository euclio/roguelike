#include <boost/python.hpp>
#include <ncurses.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace boost::python;

char GetTileChar(object tile) {
  return '.';
}

void RenderRectangle(int x, int y, int width, int height,
                     const std::string &title) {
  for (int ix = x; ix < x + width; ix++) {
    for (int iy = y; iy < y + height; iy++) {
      mvaddch(iy, ix, ' ');
    }
  }
  for (int iy = y; iy < y + height; iy++) {
    mvaddch(iy, x, '*');
    mvaddch(iy, x + width, '*');
  }
  for (int ix = x; ix <= x + width; ix++) {
    mvaddch(y, ix, '=');
    mvaddch(y + height, ix, '=');
  }
  move(y, x+2);
  printw(title.c_str());
}

int ListMaxWidth(const std::vector<std::string> &lines) {
  int maxWidth = 0;
  for (int i=0; i<lines.size(); i++) {
    if (lines[i].size() > maxWidth) {
      maxWidth = lines[i].size();
    }
  }
  return maxWidth;
}

void RenderRectangleList(int x, int y, const std::string &title,
                         const std::vector<std::string> &lines) {
  int width = ListMaxWidth(lines) + 5;
  int height = lines.size() + 1;
  RenderRectangle(x, y, width, height, title);
  for (int i = 0; i < lines.size(); i++) {
    move(y + 1 + i, x + 2);
    printw(lines[i].c_str());
  }
}

void RenderInventory() {
  std::vector<std::string> lines;
  lines.push_back("item 1");
  lines.push_back("item 2 hahahhahahaha");
  lines.push_back("item 3");
  lines.push_back("item 4");

  for (int i=0; i<lines.size(); i++) {
    lines[i].insert(0, 4, ' ');
    lines[i][0] = '[';
    lines[i][1] = 'a' + i;
    lines[i][2] = ']';
  }

  RenderRectangleList(20, 5, "Inventory", lines);
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

  //RenderInventory();
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
