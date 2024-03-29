===================
Sale Timesheet Lock
===================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-solvosci%2Fslv--sale-lightgray.png?logo=github
    :target: https://github.com/solvosci/slv-sale/tree/14.0/sale_timesheet_lock
    :alt: solvosci/slv-sale

|badge1| |badge2| |badge3| 

Adds restriction when trying to create or edit a timesheet that is linked to
a locked sales order.

**Table of contents**

.. contents::
   :local:

Known issues / Roadmap
======================

* This addon prevents timesheet editing when a project is linked to a locked
  sale order, but project is still selectable for timesheet entries.
  Exclude them from timesheet views should be useful.
* Lock revision is made for the whole project, but it could be optionally
  moved to task (when filled), becausa a task could be not linked to any order
  line, so timesheet editing shouldn't alter the linked order.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/solvosci/slv-sale/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/solvosci/slv-sale/issues/new?body=module:%20sale_timesheet_lock%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Solvos

Contributors
~~~~~~~~~~~~

* Christian Santamaría <christian.santamaria@solvos.es>
* David Alonso <david.alonso@solvos.es>

Maintainers
~~~~~~~~~~~

This module is part of the `solvosci/slv-sale <https://github.com/solvosci/slv-sale/tree/14.0/sale_timesheet_lock>`_ project on GitHub.

You are welcome to contribute.
