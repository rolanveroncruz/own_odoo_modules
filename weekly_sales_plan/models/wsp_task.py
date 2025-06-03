from odoo import models, fields, api
from datetime import timedelta

class WeeklySalesPlanTask(models.Model):
    _name = 'weekly.sales.plan.task'
    _description = 'Weekly Sales Plan Task'
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
    estimated_expenses_desc = fields.Text(string='Description for Estimated Expense',
                                          help="The estimated total cost of the task.")

    weekly_plan_id = fields.Many2one(
        'weekly.sales.plan',  # 'comodel_name': The name of the related model (master model)
        string='Weekly Plan',
        ondelete='cascade',  # Optional: If the weekly plan is deleted, delete its tasks
        required=True # A task must belong to a weekly plan
    )


