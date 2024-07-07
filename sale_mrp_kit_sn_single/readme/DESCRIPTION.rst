For S/N tracked kit components, ensures that pickings moves created from a sale
kit product are created with 1.0 quantity each one. This will be useful if such
BoM component product will fire a MO, and we need 1 MO per unit (as we cannot
produce more than 1 unit in the same MO for an s/n product).

For example, if a product kit named PROD1, for every unit BoM lines indicate
that 1 unit of serial numbered COMP1 is needed, as well as 2 units of
non-tracked COMP2, when a SO is created for 3 units of PROD1, picking will be
created with these lines:

* 3 different line with COMP1 for 1 unit each one.
* 1 line with COMP2 for 6 units.

With standard behavior only 2 picking lines would be created, the first one
for 3 units of COMP1.
