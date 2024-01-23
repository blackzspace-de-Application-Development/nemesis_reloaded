import logging, coloredlogs



def logger(self):
    logg=logging
    loggy = logg.getLogger(__name__)

    fieldstyle = {'asctime': {'color': 'green'},
                'levelname': {'bold': True, 'color': 'black'},
                'filename':{'color':'cyan'},
                'funcName':{'color':'blue'}}
                                   
    levelstyles = {'critical': {'bold': True, 'color': 'red'},
                'debug': {'color': 'green'}, 
                'error': {'color': 'red'}, 
                'info': {'color':'blue'},
               'warning': {'color': 'yellow'}}

    coloredlogs.install(level=logg.INFO,
                        logger=loggy,
                        fmt='%(asctime)s [%(levelname)s] - %(message)s',
                        datefmt='%H:%M:%S',
                        field_styles=fieldstyle,
                        level_styles=levelstyles)  