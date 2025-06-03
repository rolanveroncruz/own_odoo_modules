from odoo import models, fields, api
from datetime import timedelta

class WeeklySalesPlan(models.Model):
    _name = 'weekly.sales.plan'
    _description = 'Weekly Sales Plan'
    _order = 'start_date desc' # Good practice for list views

    name = fields.Char(string='Plan Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)

    # New computed field for the nearest Monday
    nearest_monday_date = fields.Date(
        string='Nearest Monday',
        compute='_compute_nearest_monday',
        store=True # Store the computed value for better performance and filtering
    )

    task_ids = fields.One2many(
        'weekly.sales.plan.task',  # 'comodel_name': The name of the related model (detail model)
        'weekly_plan_id',    # 'inverse_name': The name of the Many2one field in the detail model
        string='Tasks'
    )

    @api.depends('task_ids.start_datetime')
    def _compute_nearest_monday(self):
        for task in self.task_ids:
            if task.start_datetime:
                # weekday() returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
                day_of_week = task.start_datetime.weekday()

                if day_of_week <= 3: # Monday (0), Tuesday (1), Wednesday (2), Thursday (3)
                    # Go back to the Monday of the current week
                    self.nearest_monday_date = task.start_datetime - timedelta(days=day_of_week)
                else: # Friday (4), Saturday (5), Sunday (6)
                    # Go forward to the Monday of the next week
                    # (7 - day_of_week) calculates days remaining to reach next Monday (e.g., if Friday=4, 7-4=3 days to Monday)
                    days_to_add = (7 - day_of_week) % 7
                    self.nearest_monday_date = task.start_datetime+ timedelta(days=days_to_add)
            else:
                self.nearest_monday_date = False
