- Historically this period was obtained from partner_invoice_id to
support setups where the billing contact defined the period.

- It would be valuable to introduce a configurable mode allowing users
to choose the source (main partner vs billing address) to support
legacy workflows.

- There is a known issue: if the invoice_period field is deleted in res.partner, no validation is currently enforced.
This will be addressed in the next [FIX] commit.
