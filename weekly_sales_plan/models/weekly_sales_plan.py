from odoo import models, fields, api
from datetime import timedelta, datetime


class WeeklySalesPlan(models.Model):
    _name = 'weekly.sales.plan'
    _description = 'Weekly Sales Plan'
    _order = 'start_date desc' # Good practice for list views

    name = fields.Char(string='Plan Name', required=True)
    start_date = fields.Date(string='Start Date (computed)', compute='_compute_start_date', store=True)
    end_date = fields.Date(string='End Date (computed)', compute='_compute_end_date', store=True)
    total_estimated_expenses = fields.Float(string='Total Estimated Expenses', compute='_compute_estimated_expenses', store=True)


    task_ids = fields.One2many(
        'weekly.sales.plan.task',  # 'comodel_name': The name of the related model (detail model)
        'weekly_plan_id',    # 'inverse_name': The name of the Many2one field in the detail model
        string='Tasks'
    )


    @api.depends('task_ids.end_datetime')
    def _compute_end_date(self):
        for record in self:
            temp_end_date = datetime.min
            for task in record.task_ids:
                if task.end_datetime is not None:
                    if task.end_datetime and task.end_datetime >temp_end_date:
                        temp_end_date = task.end_datetime
                record.end_date = temp_end_date

    @api.depends('task_ids.start_datetime')
    def _compute_start_date(self):
        for record in self:
            temp_start_date = datetime.max
            for task in record.task_ids:
                if task.start_datetime < temp_start_date:
                    temp_start_date = task.start_datetime
            record.start_date = temp_start_date

    @api.depends('task_ids.fuel_expenses', 'task_ids.food_expenses')
    def _compute_estimated_expenses(self):
        for record in self:
            total_expenses = 0
            for task in record.task_ids:
                total_expenses += task.fuel_expenses + task.food_expenses
            record.total_estimated_expenses = total_expenses


