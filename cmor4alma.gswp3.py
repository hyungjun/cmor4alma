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


import  os, sys
from    optparse                import OptionParser

import  json
import  cmor
import  cdms2       as cdm
import  cdtime      as cdt
import  numpy       as np

from    cmoraxes                import CMORAxes
from    alma                    import ALMA


def main( args, opts ):
    print args
    print opts

    print 'python ./cmor4alma.gswp3.py ALAM_VarName'
    print '----------------------------------------'+'\n'

    almavn      = args[0]

    alma        = ALMA( almavn )

    # read json file &
    # Update frequency based on variable and write output to CMOR input file
    prjJson     = json.load( open( './gswp3-do-input.json' ) )
    prjJson[ 'frequency' ]  = alma.cmorjson( 'variable_entry' )[ 'frequency' ]

    json.dump( prjJson, 
               open('tmp.json','w'),
               ensure_ascii=True,
               encoding='utf-8',
               sort_keys=True
               )

    print '='*80
    print 'CMOR Table Path:', alma.tblpath

    for srcpath in alma.fileList:

        print srcpath
        f = cdm.open(srcpath)
        d = f( alma.varname ) ; # Or use temporal subset for testing below

        # Reset missing value
        d.setMissing(1e20) ; # This should also set fill_value, and suppress CMOR variable history being written

        # Get axes
        lat = d.getLatitude()
        lon = d.getLongitude()
        time = d.getTime() ; # Assumes variable is named 'time', for the demo file this is named 'months'

        #%% Initialize and run CMOR
        print 'Start CMORizing..'
        # For more information see https://cmor.llnl.gov/mydoc_cmor3_api/
        cmor.setup(inpath='./',netcdf_file_action=cmor.CMOR_REPLACE_4) #,logfile='cmorLog.txt')
        cmor.dataset_json('tmp.json')
        cmor.load_table( alma.tblpath )

        if hasattr( alma, 'heightEntry' ):
            axisIds = [ cmor.axis( **CMORAxes.get_timeAx( alma, time ) ),
                        cmor.axis( **CMORAxes.get_heightAx( alma, cdm ) ),
                        cmor.axis( **CMORAxes.get_latitudalAx( lat ) ),
                        cmor.axis( **CMORAxes.get_longitudalAx( lon ) ),
                        ]

        else:
            axisIds = [ cmor.axis( **CMORAxes.get_timeAx( alma, time ) ),
                        cmor.axis( **CMORAxes.get_latitudalAx( lat ) ),
                        cmor.axis( **CMORAxes.get_longitudalAx( lon ) ),
                        ]


        print axisIds

        # Setup units and create variable to write using cmor - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
        d.units = alma.outputUnits
        varid   = cmor.variable( alma.outputVarName,
                                 d.units,
                                 axisIds,
                                 missing_value = d.missing,
                                 positive = alma.positive )

        values  = np.array( d[:], np.float32 )

        cmor.set_deflate( varid, 1, 1, 1 ) ; # shuffle=1,deflate=1,deflate_level=1 - Deflate options compress file data
        # Write variable with time axis
        cmor.write( varid, values, time_vals=time, time_bnds=time.getBounds() ) 

        f.close()
        cmor.close()

    os.remove('tmp.json')

    return


if __name__=='__main__':
    usage   = 'usage: %prog [options] arg'
    version = '%prog 1.0'

    parser  = OptionParser(usage=usage,version=version)

#    parser.add_option('-r','--rescan',action='store_true',dest='rescan',
#                      help='rescan all directory to find missing file')

    (options,args)  = parser.parse_args()

#    if len(args) == 0:
#        parser.print_help()
#    else:
#        main(args,options)

#    LOG     = LOGGER()
    main(args,options)

    
