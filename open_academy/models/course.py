from odoo import api, fields, models,_


class AcademyCourse(models.Model):
    _name="academy.course"
    _description="Academy Course"

    name=fields.Char(string="Course Name",required=True)
    description=fields.Text(string="Course Description",required=True)
    responsible_id=fields.Many2one('res.users',string="Responsible",ondelete="set null")
    session_ids=fields.One2many('academy.session','course_id',string="Sessions")

    _sql_constraints = {
        ('name_description_check',
         'CHECK(name != description)',
         'The title of the course should not be the description'),
        ('name_unique',
         'UNIQUE(name)',
         'The course title must be unique')
    }