import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PoliMarketplace.settings')
django.setup()

from signup.models import Sector

def populate_sectors():
    # Lista de sectores a agregar
    sectores = ['La Floresta', 'La Carolina', 'Iñaquito', 'Rumipamba']

    # Borrar el contenido de la tabla Sector
    Sector.objects.all().delete()

    # Agregar sectores a la base de datos
    for sector_name in sectores:
        sector, created = Sector.objects.get_or_create(name=sector_name)
        if created:
            print(f'Sector "{sector_name}" creado.')
        else:
            print(f'Sector "{sector_name}" ya existe.')

if __name__ == '__main__':
    populate_sectors()