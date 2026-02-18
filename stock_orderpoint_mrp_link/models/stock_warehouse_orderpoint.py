# Copyright 2016-17 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    def action_view_mrp_productions(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "mrp.mrp_production_action"
        )
        production_ids = self.env["mrp.production"].search(
            [("orderpoint_id", "in", self.ids)]
        )
        action["domain"] = [("id", "in", production_ids.ids)]
        if len(production_ids) == 1:
            form_view = self.env.ref("mrp.mrp_production_form_view")
            action.update(
                {
                    "views": [(form_view.id, "form")],
                    "res_id": production_ids.id,
                }
            )
        return action
