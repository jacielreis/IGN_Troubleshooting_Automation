# Solo una prueba #
problem_type = str(input('Tipo de problema: serv_degr or serv_out ')) #serv_degr or serv_out
dmark = str(input('¿equipo de demarcacion? true or false ')) #true or false
# Solo una prueba #

if problem_type == 'serv_degr':
    if dmark == 'true':
        problem_type = 'serv_degr'
        dmark = 'true'
        print('serv_degr_dmark')
    else:print('serv_degr')
    
else:
    if  dmark == 'true':
        problem_type = 'serv_out'
        dmark = 'true'
        print('serv_out_dmark')
    else:print('serv_out')
