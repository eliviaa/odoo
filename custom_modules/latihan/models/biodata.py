from odoo import models, fields, api
from datetime import date

class biodata(models.Model):
    _name = "latihan.biodata"
    _description = "Biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    birth_date = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(string="Umur", compute="_compute_age", store=True)
    sibling_position = fields.Integer(string="Anak ke Berapa")
    photo = fields.Binary(string="Foto")
    gender = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'),
    ], string='Jenis Kelamin')
    
    sd = fields.Boolean(string="SD")
    smp = fields.Boolean(string="SMP")
    sltp = fields.Boolean(string="SLTP")
    sma = fields.Boolean(string="SMA")
    smk = fields.Boolean(string="SMK")
    smu = fields.Boolean(string="SMU")
    slta = fields.Boolean(string="SLTA")
    kuliah = fields.Boolean(string="Kuliah")

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                    (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)
                )
            else:
                rec.age = 0