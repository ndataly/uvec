# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cityzenmag(models.Model):
    _name = 'cityzenmag.unite_valeur'
    _description = 'cityzenmag.cityzenmag'

    name = fields.Char()
    association_count = fields.Integer()


class membre(models.Model):
    _name = "membre"
    _description = "membre d'uee association"
    name = fields.Char(string='Nom')
    sexe = fields.Selection([('masculin', 'Masculin'), ('feminin', 'Feminin')])
    telephone = fields.Char('Telephone')
    adresse = fields.Char('Adresse')
    association = fields.Many2many('association', string='Membre dans')
    propriete = fields.Boolean("Es tu propriété d'une entreprise ?")
    biens = fields.Many2many('entreprise', string='Vos entreprises')


class association(models.Model):
    _name = 'association'
    _description = 'association'

    bureau = fields.Many2one('bureau', string='Bureau')
    name = fields.Char(string="Nom de l'association")
    unite_valeur = fields.Many2one(
        'cityzenmag.unite_valeur', 'Unité de valeur')


class bureau(models.Model):
    _name = "bureau"
    _description = "les membres du bureau"

    duree = fields.Integer('Durée du bureau (ans)')
    membre_bureau = fields.Many2many('poste', string="Membre du bureau")
    valide = fields.Boolean(default=True)


class poste(models.Model):
    _name = "poste"
    _description = " poste occupé par le membre du bureau"

    occupant = fields.Many2one('res.users', string="Poste pour")
    nom_poste = fields.Selection([('president', 'Président'), ('vise_president', 'Vise président'), (
        'secretaire', 'Secretaire'), ('tresorier', 'Trésorier'), ('communcateur', 'Charger de la communication')], 'Poste')

    valide = fields.Boolean(default=True)
    position = fields.Selection(
        [('1er', '1er'), ('2nd', '2nd'), ('3em', '3em')])


class entreprise(models.Model):
    _name = 'entreprise'
    _description = "une entreprise appartenant a un membre d'une association"

    name = fields.Char("Nom de l'entrepise")
    adresse = fields.Char("Adresse de l'entreprise")
    email = fields.Char("Email de l'entreprise")
