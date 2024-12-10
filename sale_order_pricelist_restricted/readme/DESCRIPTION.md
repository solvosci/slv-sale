Enables some restrictions about pricelist selection within a Sales Order.

With these restrictions, for a Pricelist now it's possible to configure the
following options:
- If a Pricelist is always selectable for a Sales Order.
- If a Pricelist is exclisive for certain customer.

Then, when selecting a Pricelist for a Sales Order, only certain pricelist
could be selected:
- Pricelist marked as default for the Sales Order partner, or
- those pricelist with "selectable" mark is set, or
- those marked as exclusive for Sales Order partner.

The other feature added by this addon adds general security access (e.g. Pricelist
menu) for pricelists depending on user Sales level access:
- For a "See own documents" Sales user, only "selectable" pricelists and
  those linked to customers whom user is their salesman, are available.
- For upper Sales security levels every pricelist is still available.
