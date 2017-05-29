"""MIDDLEWARE"""

from functools import wraps
from flask import request

from gfwanalysis.routes.api import error
from gfwanalysis.services.geostore_service import GeostoreService
from gfwanalysis.errors import GeostoreNotFound


def get_geo_by_hash(func):
    """Get geodata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            geostore = request.args.get('geostore')
            if not geostore:
                return error(status=400, detail='Geostore is required')
            try:
                geojson, area_ha = GeostoreService.get(geostore)
            except GeostoreNotFound:
                return error(status=404, detail='Geostore not found')
            kwargs["geojson"] = geojson
            kwargs["area_ha"] = area_ha
        return func(*args, **kwargs)
    return wrapper


def get_geo_by_national(func):
    """Get geodata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            try:
                iso = request.view_args.get('iso')
                geojson, area_ha = GeostoreService.get_national(iso)
            except GeostoreNotFound:
                return error(status=404, detail='Geostore not found')
            kwargs["geojson"] = geojson
            kwargs["area_ha"] = area_ha
        return func(*args, **kwargs)
    return wrapper


def get_geo_by_subnational(func):
    """Get geodata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            try:
                iso = request.view_args.get('iso')
                id1 = request.view_args.get('id1')
                geojson, area_ha = GeostoreService.get_subnational(iso, id1)
            except GeostoreNotFound:
                return error(status=404, detail='Geostore not found')
            kwargs["geojson"] = geojson
            kwargs["area_ha"] = area_ha
        return func(*args, **kwargs)
    return wrapper


def get_geo_by_use(func):
    """Get geodata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            try:
                name = request.view_args.get('name')
                use_id = request.view_args.get('id')
                geojson, area_ha = GeostoreService.get_use(name, use_id)
            except GeostoreNotFound:
                return error(status=404, detail='Geostore not found')
            kwargs["geojson"] = geojson
            kwargs["area_ha"] = area_ha
        return func(*args, **kwargs)
    return wrapper


def get_geo_by_wdpa(func):
    """Get geodata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            try:
                wdpa_id = request.view_args.get('id')
                geojson, area_ha = GeostoreService.get_wdpa(wdpa_id)
            except GeostoreNotFound:
                return error(status=404, detail='Geostore not found')
            kwargs["geojson"] = geojson
            kwargs["area_ha"] = area_ha
        return func(*args, **kwargs)
    return wrapper