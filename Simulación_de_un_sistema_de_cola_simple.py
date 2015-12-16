
# coding: utf-8

# # Simulación de un sistema  de cola simple - Taller 5

# 
# El presente informe presenta la simulación de un sistema simple de colas con una entrada y un servidor, las llegadas es la cantidad de clientes en una unidad de tiempo con distribución de Poisson con parámetro lambda y numero de clientes atendidos por unidad de tiempo del servidor con distribución normal con parámetros mu, sigma. Se calcula tiempos promedios de los clientes en la cola, en el servidor y en el sistema.
# 

# ## Script: 

# In[6]:



def cola_Simple(lam, mu, sigma):
    """Distribuciones de tasas de llegada del sistema Poisson(lam) tasa de servicios Normal(mu,sigma).
    """    
    
   
    #Se valida que la Tasa promedio de Servicios sea mayor que la Tasa promedio de Llegadas.
    if mu>lam:
        #Probabilidad de hallar el sistema ocupado (p).
        p = float(lam)/float(mu)
        #Número promedio de clientes en la cola (lq).
        lq = ((float(lam)*float(sigma))**2 + p**2) / (2*(1-p))
        #Tiempo promedio de espera de un cliente en la cola (wq).
        wq = lq/float(lam)
        #Tiempo promedio de espera de un cliente en el sistema(w).
        w = wq + (1/float(mu))
        print '\nEl Tiempo promedio de espera de un cliente en cola  es = ' + str(wq) 
        print 'unidades de tiempo.'
        print '\nEl Tiempo de servicio de un cliente  = ' + str(1/float(mu)) 
        print 'unidades de tiempo.'
        print '\nEl Tiempo promedio de espera de un cliente en el sistema = ' + str(w)
        print 'unidades de tiempo.'
    else:
        print 'Escoja un valor de mu mayor que lambda'
         
        


# Simulación de una cola simple con Distribución de Servicios Normal(4,2) y Distribución de Llegadas Poisson(2):

# In[7]:

cola_Simple(2,4,2);


# Simulación de una cola simple con Distribución de Servicios Normal(7,1) y Distribución de Llegadas Poisson(5):

# In[8]:

cola_Simple(5,7,1);


# In[ ]:



