from odoo import api, fields, models,_,exceptions
from odoo.exceptions import ValidationError

# Import date class from datetime module
from datetime import timedelta

class AcademySession(models.Model):
    _name="academy.session"
    _description="Academy Session"

    name=fields.Char(string="Session Name",required=True)
    #start_date=fields.Date(string="Start Date",default=date.today())
    start_date=fields.Date(string="Start Date",default=fields.Date.today)
    duration = fields.Float('Duration in hours' ,required=True)
    number_of_seats = fields.Integer('Number Of Seats' ,required=True)
    instructor_id=fields.Many2one('res.partner',string="Instructor",ondelete="set null",domain="[('instructor','=',True)]")
    course_id=fields.Many2one('academy.course',string="Course",ondelete="cascade",required=True)
    attendee_ids=fields.Many2many('res.partner',string="Attendees")
    active=fields.Boolean(string="Active",default=True)
    attendees_count=fields.Integer(string="Attendees_count" ,store=True,compute='_get_attendees_count',required=True)

    percentage = fields.Float(string="Percentage",compute='_compute_percentage')
    end_date= fields.Date(string="End Date",store=True,
                          compute='_get_end_date',inverse='_set_end_date')
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for record in self:
            record.attendees_count=len(record.attendee_ids)
    @api.depends('attendee_ids','number_of_seats')
    def _compute_percentage(self):
        for record in self:
            if not  record.number_of_seats :
                record.percentage=0.0
            else:
                record.percentage  =100* len(record.attendee_ids)/record.number_of_seats

    @api.onchange('attendee_ids', 'number_of_seats')
    def _onchange_price(self):
        # set auto-changing field
        if(self.number_of_seats<0 or len(self.attendee_ids)>self. number_of_seats):
            return {
                'warning': {
                    'title': _("Something bad happened"),
                    'message': _("It was very bad indeed"),
                }
               }

    @api.constrains('attendee_ids','instructor_id')
    def _check_attendee(self):
        for record in self:
            if record.instructor_id and  record.instructor_id in record.attendee_ids:
                raise ValidationError("Your record is too old:can not be an instructor")
# all records passed the test, don't return anything
    @api.depends('start_date','duration')
    def _get_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date=record.start_date
                continue
            duration=timedelta(days=record.duration,seconds=-1)
            record.end_date=record.start_date+duration
    def _set_end_date(self):
        for record in self:
            if not (record.start_date and record.end_date):

                continue
            record.duration=(record.end_date-record.start_date).days+1
