#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from num2words import num2words

class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.bill_of_exchange.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('bill_of_exchange.module_report')
        records = self.env['account.invoice'].browse(docids)

        
        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': records
            }

        return report_obj.render('bill_of_exchange.module_report', docargs)



##################### to install num2words ################################
##################### pip install num2words ################################

class Num2Words(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def convert_amount(self):
        word = num2words(self.amount_total)
        word = word.title() + " " + "Only"
        return word