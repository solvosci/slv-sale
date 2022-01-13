* Go to `Products` and set "Stock Moves - Destination Quantity" for
  `Sales > Invoicing Policy`.
* Delivering a sale order, when the picking is in a "Done" state, unlock it 
  and set the proper "Dest." quantity for this product.
* When "Create Invoice" is clicked for this order, quantity to invoice will be
  calculated depending on "Dest." accumulated quantity for the related sale 
  line, instead of "Delivered" one.
* The sale order will become `Fully Invoiced` when all "Dest." quantities for
  these kind of products were satisfied, not "Received" ones.
