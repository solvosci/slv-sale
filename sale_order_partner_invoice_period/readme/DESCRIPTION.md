Adds a selector field to set the invoice period on partners.
This field is used when creating sale orders for that partner, to set the invoice period on the sale order.
It also adds a default invoice period field on company settings, to set a default invoice period for new partners.
- If no invoice period is set on the partner, the default invoice period from the company settings will be used.
- If no invoice period is set on the partner and no default invoice period is set on the company, a validation error will be raised when creating a new partner.
