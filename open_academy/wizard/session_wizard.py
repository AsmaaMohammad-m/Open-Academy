from odoo import api, fields, models,_



class SessionWizard(models.TransientModel):
    _name = "session.wizard"
    _description = "Session Wizard Quick Registration of Attendees to Sessions"

    def _default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))
    session_id=fields.Many2one('academy.session',string="Session",required=True,default=_default_session)
    attendee_ids=fields.Many2many('res.partner',string="Attendees")

    def subscribe(self):
        self.session_id.attendee_ids |=self.attendee_ids
        return {}