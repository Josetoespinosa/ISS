import requests
from bs4 import BeautifulSoup

# URL del sitio web que deseas hacer scraping
url = "https://www.falabella.com/falabella-cl/collection/boho?mkid=LA_B1_VER_4418&f.product.brandName=basement"

# Realizar la solicitud HTTP
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Crear el objeto BeautifulSoup con el contenido HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontrar los elementos que deseas extraer (por ejemplo, nombres de productos)
    # Aquí podrías inspeccionar la página y buscar clases o tags específicos
    productos_html = soup.find_all('div', class_='jsx-1068418086')
    productos = {}
    productos_id = 0
    
    
    
    # Extraer los textos o atributos que desees
    for producto in productos_html:
        precio_actual = producto.find('li', class_='prices-0').find('span').get_text(strip=True)
        if producto.find('li', class_='prices-1') is not None:
            precio_anterior = producto.find('li', class_='prices-1').find('span').get_text(strip=True)
            
        else:
            precio_anterior = None
        if producto.find('img') is not None:
            url_imagen = producto.find('img').get('src')
        else:
            url_imagen = None
        if producto.find('b', class_='title1'):
            marca = producto.find('b', class_='title1').get_text(strip=True)
        else:
            marca = None

        if producto.find('b', class_="pod-subTitle"):
            descripcion = producto.find('b', class_="pod-subTitle").get_text(strip=True)

        else:
            descripcion = None

        vendedor = producto.find('b', class_='seller-text-rebrand').get_text(strip=True)
        productos[productos_id] = {
            "Descripción": descripcion,
            "Precio actual": precio_actual,
            "Precio anterior": precio_anterior,
            "Imagen": url_imagen,
            "Marca": marca,
            "Vendedor": vendedor
        }
        productos_id += 1


        
else:
    print(f"Error al acceder a la página: {response.status_code}")

print(productos)
