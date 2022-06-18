

from xmlrpc.client import Boolean
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario
from flask_cors import CORS, cross_origin


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.integer(11))