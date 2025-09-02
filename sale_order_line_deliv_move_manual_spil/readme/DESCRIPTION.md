Takes in account delivery quantity introduced by
sale_order_line_deliv_move_manual when link from stock moves to invoice lines
is generated.

A stock move is not linked to an invoice line if no destination quantity
is filled yet.
