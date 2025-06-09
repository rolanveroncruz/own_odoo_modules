from odoo import models, fields, api
from datetime import timedelta

class WeeklySalesPlanTask(models.Model):
    _name = 'weekly.sales.plan.task'
    _description = 'Weekly Sales Plan Task'
    _order = 'start_datetime desc' # Good practice for list views

    task_name = fields.Many2one('crm.stage', "Task Name", required=True, ondelete='cascade')
    # task_name = fields.Char(string='Task Name', compute='_compute_task_name', store=True)
    description = fields.Text(string='Details', help="Detailed description of the task.")
    start_datetime = fields.Datetime(string='Planned Start', required=True, default=fields.Datetime.now,
                                     help="The planned start date and time for the task.")

    end_datetime = fields.Datetime(string='Planned End',
                                   help="The planned end date and time for the task. If empty, considered instantaneous or open-ended.")
    assigned_to_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user,
                                     help="The salesperson or user assigned to this task.")
    customer_id = fields.Many2one('res.partner', string='Customer',
                                  help="The client for whom this service task is performed.")
    fuel_expenses = fields.Float(string='Fuel ', help="Fuel expenses.")
    food_expenses = fields.Float(string='Personal Food ', help="Personal Food expenses.")
    representation_expenses = fields.Float(string='Representation ', help="Representation expenses.")
    toll_expenses = fields.Float(string='Toll ', help="Toll expenses.")
    rental_expenses = fields.Float(string='Car Rental ', help="Car rental expenses.")
    lodging_expenses = fields.Float(string='Lodging ', help="Lodging expenses.")
    other_expenses = fields.Float(string='Other ', help="Other expenses.")

    weekly_plan_id = fields.Many2one(
        'weekly.sales.plan',  # 'comodel_name': The name of the related model (master model)
        string='Weekly Plan',
        ondelete='cascade',  # Optional: If the weekly plan is deleted, delete its tasks
        required=True # A task must belong to a weekly plan
    )


