"""API ROUTER"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from flask import jsonify, request, Blueprint
from gfwanalysis.routes.api import error, set_params
from gfwanalysis.services.hansen_service import HansenService
from gfwanalysis.validators import validate_world, validate_use
from gfwanalysis.middleware import get_geo_by_hash, get_geo_by_use, get_geo_by_wdpa
from gfwanalysis.errors import HansenError
from gfwanalysis.serializers import serialize_umd

hansen_endpoints_v1 = Blueprint('hansen_endpoints_v1', __name__)


def get_hansen(geojson, area_ha):
    """get_hansen"""
    geojson = geojson or request.get_json().get('geojson', None)
    area_ha = area_ha or 0

    if not geojson:
        return error(status=400, detail='Geojson is required')

    threshold, begin, end = set_params(request)

    if request.args.get('aggregate_values', '').lower() == 'false':
        aggregate_values = False
    else:
        aggregate_values = True

    try:
        data = HansenService.hansen_all(
            geojson=geojson,
            threshold=threshold,
            begin=begin,
            end=end,
            aggregate_values=aggregate_values)
    except HansenError as e:
        logging.error('[ROUTER]: '+e.message)
        return error(status=500, detail=e.message)
    except Exception as e:
        logging.error('[ROUTER]: '+str(e))
        return error(status=500, detail='Generic Error')

    data['area_ha'] = area_ha
    return jsonify(data=serialize_umd(data, 'umd')), 200


@hansen_endpoints_v1.route('/', strict_slashes=False, methods=['GET', 'POST'])
@validate_world
@get_geo_by_hash
def get_world(geojson, area_ha):
    """World Endpoint"""
    logging.info('[ROUTER]: Getting world')
    return get_hansen(geojson, area_ha)


@hansen_endpoints_v1.route('/use/<name>/<id>', strict_slashes=False, methods=['GET'])
@validate_use
@get_geo_by_use
def get_use(name, id, geojson, area_ha):
    """Use Endpoint"""
    logging.info('[ROUTER]: Getting use')
    return get_hansen(geojson, area_ha)


@hansen_endpoints_v1.route('/wdpa/<id>', strict_slashes=False, methods=['GET'])
@get_geo_by_wdpa
def get_wdpa(id, geojson, area_ha):
    """Wdpa Endpoint"""
    logging.info('[ROUTER]: Getting wdpa')
    return get_hansen(geojson, area_ha)