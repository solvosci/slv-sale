* This addon prevents timesheet editing when a project is linked to a locked
  sale order, but project is still selectable for timesheet entries.
  Exclude them from timesheet views should be useful.
* Lock revision is made for the whole project, but it could be optionally
  moved to task (when filled), becausa a task could be not linked to any order
  line, so timesheet editing shouldn't alter the linked order.
