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



class CMORAxes( object ):

    @staticmethod
    def get_timeAx( alma, time ):
    
        table_entry = 'time1' if alma.cmorTable == 'A3hrPt' else    \
                      'time'
    
        return { 'table_entry'   : table_entry,
                 'units'         : time.units,
                }
    
    
    @staticmethod
    def get_heightAx( alma, cdm ):
    
        coord_vals  = cdm.createAxis( [ alma.height ], id='height' )
    
        return { 'table_entry'  : alma.heightEntry,
                 'units'        : 'm',
                 'coord_vals'   : coord_vals,
                }

    @staticmethod
    def get_latitudalAx( lat ):

        return { 'table_entry'  : 'latitude',
                 'units'        : 'degrees_north',
                 'coord_vals'   : lat[:],
                 'cell_bounds'  : lat.getBounds(),
                }

    @staticmethod
    def get_longitudalAx( lon ):

        return { 'table_entry'  : 'longitude',
                 'units'        : 'degrees_east',
                 'coord_vals'   : lon[:],
                 'cell_bounds'  : lon.getBounds(),
                }

