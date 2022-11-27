# File-Search

A mostly rudimentary implementation of grep (and other search
tools).

### Usage
`python file-search.py {PATH_TO_DIR} {SEARCH_TERM}`

### TODOS
- One of the main things that makes grep quick is it's use
  of Boyer-Moore (amongst many other optimizations). A small
  test on the `test-files` directory shows this file search
  program takes roughly 46 times longer than `grep` (about 0.186s).
  See if this speeds it up (and if not, speed it up anyways).

- grep has support for a variety of args (show line numbers
  buffered output, etc). Build that in.

- Get some automated testing (pytest, etc).