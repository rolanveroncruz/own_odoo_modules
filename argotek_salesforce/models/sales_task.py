from odoo import models, fields, api
from datetime import timedelta

class FieldSalesTask(models.Model):
    _name = 'field.sales.task'
    _description = 'Field Sales Task'
    _order = 'start_datetime desc' # Good practice for list views

    name = fields.Char(string='Task Name', required=True, help="A brief name for the task.")
    description = fields.Text(string='Details', help="Detailed description of the task.")
    start_datetime = fields.Datetime(string='Scheduled Start', required=True, default=fields.Datetime.now,
                                     help="The planned start date and time for the task.")
    end_datetime = fields.Datetime(string='Scheduled End',
                                   help="The planned end date and time for the task. If empty, considered instantaneous or open-ended.")
    assigned_to_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user,
                                     help="The salesperson or user assigned to this task.")
    customer_id = fields.Many2one('res.partner', string='Customer',
                                  help="The client for whom this service task is performed.")
    estimated_expenses = fields.Float(string='Estimated Expense', help="The estimated total cost of the task.")
    estimated_expenses_desc = fields.Text(string='Description for Estimated Expense', help="The estimated total cost of the task.")


    @api.onchange('start_datetime')
    def _onchange_start_datetime(self):
        # If end_datetime is not set or is before start_datetime, set it to start_datetime + 1 hour
        if not self.end_datetime or self.end_datetime < self.start_datetime:
            self.end_datetime = self.start_datetime + timedelta(hours=2)