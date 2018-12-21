#! /usr/bin/python
#--------------------------------------------------------------------
# PROGRAM    : alma2cmor.gswp3.py	
# CREATED BY : hjkim @IIS.2018-12-12 23:23:41.796067
# MODIFED BY :
#
# USAGE      : $ ./alma2cmor.gswp3.py
#
# DESCRIPTION:
#------------------------------------------------------cf0.2@20120401


class ALMAVars( object ):

    Tair    = { 'inputVarName'  : 'Tair',
                'cmorTable'     : 'A3hrPt',
                'outputVarName' : 'tas',
                'outputUnits'   : 'K',
                'positive'      : None,

                'heightEntry'   : 'height2m',
                'height'        : 2.,
            }


    Qair    = { 'inputVarName'  : 'Qair',
                'cmorTable'     : 'A3hrPt',
                'outputVarName' : 'huss',
                'outputUnits'   : '1.0',
                'positive'      : None,

                'heightEntry'   : 'height2m',
                'height'        : 2.,
            }

    PSurf   = { 'inputVarName'  : 'PSurf',
                'cmorTable'     : 'A3hrPt',
                'outputVarName' : 'psl',
                'outputUnits'   : 'Pa',
                'positive'      : None,
            }

    SWdown  = { 'inputVarName'  : 'SWdown',
                'cmorTable'     : 'A3hr',
                'outputVarName' : 'rsds',
                'outputUnits'   : 'W m-2',
                'positive'      : 'down',

            }

    LWdown  = { 'inputVarName'  : 'LWdown',
                'cmorTable'     : 'A3hr',
                'outputVarName' : 'rlds',
                'outputUnits'   : 'W m-2',
                'positive'      : 'down',

            }

    Rainf   = { 'inputVarName'  : 'Rainf',
                'cmorTable'     : 'A3hr',
                'outputVarName' : 'prra',
                'outputUnits'   : 'kg m-2 s-1',
                'positive'      : None,

            }

    Snowf   = { 'inputVarName'  : 'Snowf',
                'cmorTable'     : 'A3hr',
                'outputVarName' : 'prra',
                'outputUnits'   : 'kg m-2 s-1',
                'positive'      : None,

            }

    Wind    = { 'inputVarName'  : 'Wind',
                'cmorTable'     : 'A3hr',
                'outputVarName' : 'sfcWind',
                'outputUnits'   : 'm s-1',
                'positive'      : None,

                'heightEntry'   : 'height10m',
                'height'        : 10.,
            }


