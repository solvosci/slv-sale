# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade
import logging


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return
    logger = logging.getLogger(__name__)
    logger.info(
        "Creating columns: stock_move_line (fcd_document_line_id)."
    )
    openupgrade.logged_query(
        env.cr,
        """
            ALTER TABLE stock_move_line
            ADD COLUMN IF NOT EXISTS fcd_document_line_id INT
        """
    )
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE stock_move_line
            SET fcd_document_line_id = COALESCE(spl1.fcd_document_line_id, spl2.fcd_document_line_id)
            FROM stock_move_line sml
            LEFT JOIN stock_production_lot spl1 ON spl1.id = sml.lot_id
            LEFT JOIN stock_production_lot spl2 ON spl2.id = spl1.fcd_origin_lot_id
            WHERE stock_move_line.id = sml.id;
        """
    )
    logger.info("Successfully updated stock_move_line table")
