/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";
import { sprintf } from "@web/core/utils/strings";


patch(Order.prototype, {

    async pay() {
        for(var i = 0, lines = this.get_orderlines().length; i < lines; ++i){
            const pricelist = await this.loadPricelist(i)
            const lastInvoicePrice = await this.loadInvoices(i)
            const netPrice = this.get_orderlines()[i].get_base_price() / this.get_orderlines()[i].quantity

            if(lastInvoicePrice.length > 0 && (netPrice < lastInvoicePrice[0].price_subtotal)){
                this.env.services.popup.add(ErrorPopup, {
                    title: _t("Unable complete the pay"),
                    body: sprintf(
                        _t(
                            "Net price of %s, %s must be higher that the last purchase invoice price %s"
                        ),
                        lastInvoicePrice[0].product_id[1],
                        netPrice.toFixed(2),
                        lastInvoicePrice[0].price_subtotal.toFixed(2)
                    )
                });
                return;
            }
            if(pricelist != false){
                const line = this.get_orderlines()[i];

                const pricelist_value = await this.env.services.orm.call(
                    "sale.order.line",
                    "get_price_from_lowest_pricelist_id",
                    [],
                    {
                        product_id: this.get_orderlines()[i].product.id,
                        quantity: line.quantity,
                        pricelist_id: pricelist,
                        partner_id: this.get_partner() ? this.get_partner().id : false,
                    }
                );
                if(netPrice < pricelist_value[0]){
                    this.env.services.popup.add(ErrorPopup, {
                    title: _t("Unable complete the pay"),
                    body: sprintf(
                        _t(
                            "Net price of %s, %s must be higher that the lowest pricelist %s"
                        ),
                        lastInvoicePrice[0].product_id[1],
                        netPrice.toFixed(2),
                        pricelist_value[0].toFixed(2)
                    )
                });
                return;
                }

            }
        }
        return super.pay();
    },

    async loadInvoices(i) {
        const productId = this.get_orderlines()[i]?.product?.id;
        const invoice = await this.env.services.orm.call(
            "sale.order.line",
            'get_last_purchase_invoice_line',
            [[],productId]
        );
        const price = await this.env.services.orm.searchRead(
            "account.move.line", [["id", "=", invoice["move_line_id"]]],
            ["product_id", "price_subtotal"]
        );
        return price;
    },

    async loadPricelist(i){
        const lineId = this.get_orderlines()[i].id;
        const pricelist = await this.env.services.orm.call(
            "sale.order.line",
            'get_control_pricelist',
            [[lineId]]
        );

        return pricelist;
    }
});
