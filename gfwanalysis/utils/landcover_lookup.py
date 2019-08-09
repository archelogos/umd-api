import logging


def lookup(layer, result_dict, count_pixels):
    lkp = all_lulc_dict[layer]

    if count_pixels:
        area_type = 'pixelCount'
    else:
        area_type = 'areaHectares'

    output_list = []
    logging.info('adding landcover names')
    logging.info(result_dict)

    for key, val in result_dict.items():

        if key != 'null':
            landcover_name = lkp[key]

            result_dict = {'resultType': area_type,
                           'className': landcover_name,
                           'classVal': key}

            # unpack year dict into array of dicts
            if isinstance(val, dict):
                val = [{'year': year, 'result': result} for year, result in val.items()]

            result_dict['result'] = val

            output_list.append(result_dict)

    return output_list


def valid_lulc_codes(layer):
    return [int(x) for x in all_lulc_dict[layer].keys()]


def get_landcover_types():
    return list(all_lulc_dict.keys())


all_lulc_dict = {
    'nlcd_landcover': {
        '11':'Water Body',
        '12':'Perennial Ice/Snow',
        '21':'Developed, Open Space',  
        '22':'Developed, Low Intensity', 
        '23':'Developed, Medium Intensity',
        '24':'Developed, High Intensity',
        '31':'Barren Land',
        '41':'Deciduous Forest',
        '42':'Evergreen Forest',
        '43':'Mixed Forest',
        '51':'Dwarf Scrub', 
        '52':'Shrub/Scrub',
        '71':'Grassland/Herbaceous', 
        '72':'Sedge/Herbaceous',
        '73':'Lichens',
        '74':'Moss',
        '81':'Pasture/Hay', 
        '82':'Cultivated Crops',
        '90':'Woody Wetlands',
        '95':'Emergent Herbaceous Wetlands'

    },
    'globcover': {
        '11': 'Post-flooding or irrigated croplands',
        '14': 'Rainfed croplands',
        '20': 'Mosaic Cropland (50-70%) / Vegetation (grassland, shrubland, forest) (20-50%)',
        '30': 'Mosaic Vegetation (grassland, shrubland, forest) (50-70%) / Cropland (20-50%)',
        '40': 'Closed to open (>15%) broadleaved evergreen and/or semi-deciduous forest (>5m)',
        '50': 'Closed (>40%) broadleaved deciduous forest (>5m)',
        '60': 'Open (15-40%) broadleaved deciduous forest (>5m)',
        '70': 'Closed (>40%) needleleaved evergreen forest (>5m)',
        '90': 'Open (15-40%) needleleaved deciduous or evergreen forest (>5m)',
        '100': 'Closed to open (>15%) mixed broadleaved and needleleaved forest (>5m)',
        '110': 'Mosaic Forest/Shrubland (50-70%) / Grassland (20-50%)',
        '120': 'Mosaic Grassland (50-70%) / Forest/Shrubland (20-50%)',
        '130': 'Closed to open (>15%) shrubland (<5m)',
        '140': 'Closed to open (>15%) grassland',
        '150': 'Sparse (>15%) vegetation (woody vegetation, shrubs, grassland)',
        '160': 'Closed (>40%) broadleaved forest regularly flooded - Fresh water',
        '170': 'Closed (>40%) broadleaved semi-deciduous and/or evergreen forest regularly flooded - Saline water',
        '180': 'Closed to open (>15%) vegetation (grassland, shrubland, woody vegetation) on regularly flooded or waterlogged soil - Fresh, brackish or saline water',
        '190': 'Artificial surfaces and associated areas (urban areas >50%) GLOBCOVER 2009',
        '200': 'Bare areas',
        '210': 'Water bodies',
        '220': 'Permanent snow and ice',
        '230': 'Unclassified'
    },

    'foraf': {
        '1': 'Dense moist forest',
        '2': 'Submontane forest',
        '3': 'Mountain forest',
        '4': 'Edaphic forest',
        '5': 'Mangrove',
        '6': 'Forest-savanna mosaic',
        '7': 'Rural complex and young secondary forest',
        '8': 'Closed to open deciduous woodland',
        '9': 'Savanna woodland-Tree savanna',
        '10': 'Shrubland',
        '11': 'Grassland',
        '12': 'Aquatic grassland',
        '13': 'Swamp grassland',
        '14': 'Sparse vegetation',
        '15': 'Mosaic cultivated areas/vegeatation( herbaceous or shrub)',
        '16': 'Agriculture',
        '17': 'Irrigated agriculture',
        '18': 'Bare areas',
        '19': 'Artificial surfaces and associated areas',
        '20': 'Water Bodies'
    },

    'gfw-landcover-2000':  {
        '1': 'Agriculture',
        '2': 'Forest',
        '3': 'Grassland',
        '4': 'Wetland',
        '5': 'Settlement',
        '6': 'Shrubland',
        '7': 'Sparse vegetation',
        '8': 'Bare',
        '9': 'Water',
        '10': 'Permanent snow and ice'
        },

    'gfw-landcover-2015':  {
        '1': 'Agriculture',
        '2': 'Forest',
        '3': 'Grassland',
        '4': 'Wetland',
        '5': 'Settlement',
        '6': 'Shrubland',
        '7': 'Sparse vegetation',
        '8': 'Bare',
        '9': 'Water',
        '10': 'Permanent snow and ice'
    },

    'liberia': {
        '0': 'NoData',
        '1': 'Forest >80%',
        '2': 'Forest 30 - 80%',
        '3': 'Forest <30%',
        '4': 'Mangrove & Swamps',
        '5': 'Settlements',
        '7': 'Surface Water Bodies',
        '8': 'Grassland',
        '9': 'Shrub',
        '10': 'Bare soil',
        '11': 'Ecosystem complex (rock & sand)',
        '25': 'Clouds'
    },

    'ifl2000': {
        '1': 'Intact Forest Landscape 2000'
    },

    'primary-forest': {
        '0': 'Not Primary Forest',
        '1': 'Primary Forest'
    },

    'mangroves': {
        '1': 'Landsat Mangroves 2000'
    },

    'idn-landcover': {
        '0': 'Secondary forest',
        '1': 'Primary forest',
        '2': 'Timber plantation',
        '3': 'Agriculture',
        '4': 'Settlement',
        '5': 'Swamp',
        '6': 'Grassland/shrub',
        '7': 'Bare land',
        '8': 'Estate crop plantation',
        '9': 'Body of water',
        '10': 'Fish pond',
        '11': 'Mining'
    },

    'sea-landcover': {
        '0': 'Mining',
        '1': 'Mixed tree crops',
        '2': 'No data',
        '3': 'Oil palm plantation',
        '4': 'Settlements',
        '5': 'Swamp',
        '6': 'Timber plantation',
        '7': 'Primary forest',
        '8': 'Water bodies',
        '9': 'Bare land',
        '10': 'Coastal fish pond',
        '11': 'Rubber plantation',
        '12': 'Agriculture',
        '13': 'Secondary forest',
        '14': r'Grassland/shrub'
    }

}
