Adds analytic tags to sale lines depending on warehouse move lines, 
this new definition has a higher priority than "Analytic Defaults Rules".

For warehouse determination from a certain product move, this is the priority:
* If move source location is default stock location for a warehouse => first
occurrence is selected.
* If not, warehouse move is selected instead.
