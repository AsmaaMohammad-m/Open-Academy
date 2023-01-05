from odoo import api, fields, models,_
from  odoo.addons.partner_autocomplete.models.res_partner import ResPartner


class ResPartner(models.Model):
    _inherit="res.partner"
    instructor=fields.Boolean("Instructor",default=False)
    session_ids=fields.Many2many('academy.session',string="Attended Sessions",readonly=True)