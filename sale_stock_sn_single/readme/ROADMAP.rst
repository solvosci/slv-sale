* This new functionality only works for new confirmed SO lines. When a SO line
  quantity is updated, it doesn't work as expected behavior adding pending new
  stock picking lines.
* Single quantity stock moves for the same product merge process is prevented
  changing ``description_picking`` field, that could be changed by user. With such
  technique there's no need of other differences (like e.g. a manufacture rule
  that generates a different ``created_production_id`` field) to ensure one move per
  quantity. Using a properly managed custom new field for this (like a "single quantity
  move sequence for this S/N product") could be a better solution.
