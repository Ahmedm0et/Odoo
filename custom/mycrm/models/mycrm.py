from odoo import models, fields, api
from openerp.tools.translate import _



class ModifiedCRM(models.Model):
    # _name = "res.partner"  #create the same table structure with different name
    _inherit = "res.partner"
    related_patient_id= fields.Many2one("hms.patient")

    # @api.multi
    def unlink(self):
        for customer in self:
            if self.related_patient_id == None :
                super().unlink()
            else:
                return {
                    "warning": {
                        "title": "notice",
                        "message": "you cannnot delet this customer"
                    }
                }