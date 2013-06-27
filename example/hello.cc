#include <boost/python.hpp>
#include <ncurses.h>
#include <SDL/SDL.h>

using namespace boost::python;

void test_ncurses(object f) {
  initscr();
  object message = f();
  printw(extract<char*>(message));
  refresh();
  getch();
  endwin();
}

SDL_Surface* screen;
SDL_Event event;

void test_opengl() {
  // open a window
  SDL_Init(SDL_INIT_EVERYTHING);
  screen = SDL_SetVideoMode(640, 480, 16, SDL_SWSURFACE);

  bool done = false;
  while (!done) {
    // take user input
    while (SDL_PollEvent(&event)) {
      if (event.type == SDL_QUIT) {
        done = true;
      }
    }

    // black screen
    SDL_FillRect(screen, &screen->clip_rect, SDL_MapRGB(screen->format, 0, 0, 0));
    SDL_Flip(screen);
  }
  SDL_Quit();
}

BOOST_PYTHON_MODULE(hello) {
  def("test_ncurses", test_ncurses);
  def("test_opengl", test_opengl);
}
