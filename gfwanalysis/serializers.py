"""Serializers"""
import logging


def serialize_umd(analysis, type):
    """."""
    return {
        'id': None,
        'type': type,
        'attributes': {
            'loss': analysis.get('loss', None),
            'gain': analysis.get('gain', None),
            'treeExtent': analysis.get('tree_extent', None),
            'areaHa': analysis.get('area_ha', None),
        }
    }


def serialize_histogram(analysis, type):
    """."""

    return {
        'id': None,
        'type': type,
        'attributes': {
            'histogram': analysis.get('result', None),
            'areaHa': analysis.get('area_ha', None),
        }
    }

def serialize_landcover(analysis, type):
    """."""

    return {
        'id': None,
        'type': type,
        'attributes': {
            'landcover': analysis.get('result', None),
            'areaHa': analysis.get('area_ha', None),
        }
    }


def serialize_forma(analysis, type):
    """Convert the output of the forma250 analysis to json"""
    return {
        'id': None,
        'type': type,
        'attributes': {
            'areaHa': analysis.get('area_ha', None),
            'areaHaLoss': analysis.get('area_ha_loss', None),
            'alertCounts': analysis.get('alert_counts', None)
        }
    }

def serialize_biomass(analysis, type):
    """Convert the output of the biomass_loss analysis to json"""
    return {
        'id': None,
        'type': type,
        'attributes': {
            'biomass': analysis.get('biomass', None),
            'biomassLoss': analysis.get('biomass_loss', None),
            'biomassLossByYear': analysis.get('biomass_loss_by_year', None),
            'cLossByYear': analysis.get('c_loss_by_year', None),
            'co2LossByYear': analysis.get('co2_loss_by_year', None),
            'treeLossByYear': analysis.get('tree_loss_by_year', None),
            'areaHa': analysis.get('area_ha', None)
        }
    }

def serialize_landsat_url(analysis, type):
    """Convert output of landsat_tiles to json"""
    return {
        'id': None,
        'type': type,
        'attributes':{
            "url": analysis.get('url', None)
            }
        }

def serialize_sentinel_url(analysis, type):
    """Convert output of landsat_tiles to json"""
    return {
        'id': None,
        'type': type,
        'attributes':{
            "url_image": analysis.get('image_tiles', None),
            "url_boundary": analysis.get('boundary_tiles', None),
            "date_time": analysis.get('metadata', None).get('date_time', None),
            "product_id": analysis.get('metadata', None).get('product_id', None),
            }
        }

##### CHECK THIS. For loop for element retrieval.
def serialize_highres_url(analysis, type):
    """Convert output of images to json"""
    output = []

    for e in range (0, len(analysis)):
        temp_output = {
            'id': None,
            'type': type,
            'attributes':{
                'source': analysis[e].get('metadata', None).get('source', None),
                'cloud_score': analysis[e].get('metadata', None).get('cloud_score', None),
                'date_time': analysis[e].get('metadata', None).get('date_time', None),
                'metadata': analysis[e].get('metadata', None),
                'tile_url': analysis[e].get('tile_url', None),
                'thumbnail_url': analysis[e].get('thumbnail_url', None),
                'boundary_tiles': analysis[e].get('boundary_tiles', None)
            }
        }
        output.append(temp_output)

    return output

def serialize_recent_url(analysis, type):
    logging.info("[SERIALISER] initiating...")
    """Convert output of images to json"""
    output = []

    for e in range (0, len(analysis)):
        temp_output = {
            'id': None,
            'type': type,
            'attributes':{
                'source': analysis[e].get('id', None),
                'cloud_score': analysis[e].get('cloud_score', None),
                'date_time': analysis[e].get('date', None),
                'tile_url': analysis[e].get('tile_url', None),
                'thumbnail_url': analysis[e].get('thumb_url', None),
                'boundary_tiles': analysis[e].get('boundary', None)
            }
        }
        output.append(temp_output)
    logging.info("[SERIALISER] Complete!")
    return output
