from .mostrar_ubicacion_actual import *
from .mostrar_comisarias import *
from .mostrar_ultimos_reportes import *
from .delimitar_distritos import *
from .mostrar_mapa_de_calor import *
from .efectuar_denuncia import *
from .funcionalidades import *

def ubicacion_crimenes():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes.html")
    return mapaCuidao

def ubicacion_comisarias():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_comisarias.html")
    return mapaCuidao

def ubicacion_distritos():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_distritos.html")
    return mapaCuidao

def ubicacion_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_calor.html")
    return mapaCuidao

def crimenes_comisarias():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_comisarias.html")
    return mapaCuidao

def crimenes_distritos():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_distritos.html")
    return mapaCuidao

def crimenes_calor():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_calor.html")
    return mapaCuidao

def comisarias_distritos():
    mapaCuidao = mostrar_comisarias()
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/comisarias_distritos.html")
    return mapaCuidao

def comisarias_calor():
    mapaCuidao = mostrar_comisarias()
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/comisarias_calor.html")
    return mapaCuidao

def distritos_calor():
    mapaCuidao = delimitar_distritos()
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/distritos_calor.html")
    return mapaCuidao

def ubicacion_crimenes_comisarias():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_comisarias.html")
    return mapaCuidao

def ubicacion_crimenes_distritos():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_distritos.html")
    return mapaCuidao

def ubicacion_crimenes_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_calor.html")
    return mapaCuidao

def ubicacion_comisarias_distritos():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_comisarias_distritos.html")
    return mapaCuidao

def ubicacion_comisarias_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_comisarias_calor.html")
    return mapaCuidao

def ubicacion_distritos_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_distritos_calor.html")
    return mapaCuidao

def crimenes_comisarias_distritos():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_comisarias_distritos.html")
    return mapaCuidao

def crimenes_comisarias_calor():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_comisarias_calor.html")
    return mapaCuidao

def crimenes_distritos_calor():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_distritos_calor.html")
    return mapaCuidao

def comisarias_distritos_calor():
    mapaCuidao = mostrar_comisarias()
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/comisarias_distritos_calor.html")
    return mapaCuidao

def ubicacion_crimenes_comisarias_distritos():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_comisarias_distritos.html")
    return mapaCuidao

def ubicacion_crimenes_comisarias_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_comisarias_calor.html")
    return mapaCuidao

def ubicacion_crimenes_distritos_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_distritos_calor.html")
    return mapaCuidao

def ubicacion_comisarias_distritos_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_comisarias_distritos_calor.html")
    return mapaCuidao

def crimenes_comisarias_distritos_calor():
    mapaCuidao = mostrar_ultimos_reportes()
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/crimenes_comisarias_distritos_calor.html")
    return mapaCuidao

def ubicacion_crimenes_comisarias_distritos_calor():
    mapaCuidao = mostrar_ubicacion_actual()
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)
    mapaCuidao.save("app/templates/ubicacion_crimenes_comisarias_distritos_calor.html")
    return mapaCuidao

