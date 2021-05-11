# -*- coding: utf-8 -*-
from odoo import http


class Cityzenmag(http.Controller):
    @http.route('/cityzenmag/cityzenmag/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/cityzenmag/cityzenmag/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('cityzenmag.listing', {
            'root': '/cityzenmag/cityzenmag',
            'objects': http.request.env['cityzenmag.cityzenmag'].search([]),
        })

    @http.route('/cityzenmag/cityzenmag/objects/<model("cityzenmag.cityzenmag"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('cityzenmag.object', {
            'object': obj
        })
