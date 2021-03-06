from openerp import models, fields, api
from openerp.exceptions import Warning
from odoo.exceptions import UserError
from openerp.exceptions import UserError


class EcubeRawAttendance(models.Model):
	_name = 'ecube.raw.attendance'

	_rec = 'GYM Attendance'
	name = fields.Char('ERP Name')
	# machine_name = fields.Char('Machine Name')
	machine_id = fields.Char(string='Member Ship No')
	date = fields.Date(string='Date')
	time = fields.Char(string='Attendance Time')
	employee_id = fields.Many2one('reg.form',string="Member Name")
	department = fields.Many2one('hr.department',string="Department")
	attendance_date = fields.Char('Attendance Date')