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


import  os
import  json

from    almavars        import ALMAVars


class ALMA( ALMAVars ):

    def __init__( self, vname ):

        self.alma       = getattr( self, vname )

        self.years      = range( 1901, 1903 )
        #self.years      = range( 1901, 2015 )
        self.varname    = vname
        self.basedir    = '/work/hk01/gswp3/in.exp1/tags/v1.09/{vn}/'
        self.srcfile    = 'GSWP3.BC.{vn}.3hrMap.{yr}.nc'

        self.tbldir     = './Tables'
        self.tblpath    = os.path.join( self.tbldir, 
                                        'input4MIPs_{}.json'.format( self.cmorTable ) 
                                        )
        self.cmorJson   = json.load( open( self.tblpath.format( self.cmorTable ) ) ) 


    def __getattr__( self, k ):

        if k in self.alma.keys():
            return self.alma[ k ]

        else:
            return getattr( self, k )


    @property
    def fileList( self ):
        return self.get_srcpaths( self.varname )


    def cmorjson( self, k ):
        return self.cmorJson[ k ][ self.outputVarName ]


    def get_srcpaths( self, vn ):

        srcpath     = os.path.join( self.basedir, self.srcfile )
    
        return [ srcpath.format( vn=vn, yr=yr ) for yr in self.years ]


