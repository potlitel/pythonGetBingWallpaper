import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

BASE_URL = 'https://bingwallpaper.anerg.com/'
SAVE_DIR = 'C:/Users/potli/Videos/'

def is_connected(test_url='https://www.google.com', timeout=3):
    """Verifica si hay conexión a Internet intentando acceder a una web confiable."""
    try:
        requests.get(test_url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    
def get_soup(url: str):
    """Obtiene e interpreta el contenido HTML de una URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error accediendo a la URL {url}: {e}")
        return None

def find_today_wallpaper(soup: BeautifulSoup):
    """Busca el contenedor del wallpaper actual."""
    return soup.find('div', string="Today's Wallpaper")

def get_image_page_url(today_wallpaper: str):
    """Obtiene la URL de la página de la imagen a partir del contenedor del wallpaper actual."""
    link_tag = today_wallpaper.find_next('a') if today_wallpaper else None
    return BASE_URL + link_tag['href'] if link_tag else None

def get_download_url(image_page_url: str):
    """Obtiene la URL de descarga de la imagen 4K."""
    soup = get_soup(image_page_url)
    if soup:
        button = soup.find('a', class_='btn d-block btn-warning')
        return button['href'] if button else None
    return None

def download_image(download_url: str, save_path: str):
    """Descarga y guarda la imagen en disco."""
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f'Imagen 4K descargada y guardada en {save_path} ✔️')
    except requests.RequestException as e:
        print(f"Error descargando la imagen: {e}")
        
def download_image_with_progress(download_url: str, save_path: str):
    """Descarga una imagen mostrando una barra de progreso visual."""
    response = requests.get(download_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    if response.status_code != 200:
        print(f"Error al descargar la imagen: status code {response.status_code}")
        return
    block_size = 1024  # Puedes ajustar el tamaño del bloque
    with open(save_path, 'wb') as file, tqdm(total=total_size, unit='B', unit_scale=True, desc=save_path) as progress_bar:
        for data in response.iter_content(block_size):
            file.write(data)
            progress_bar.update(len(data))
    print(f'Imagen 4K descargada y guardada en {save_path} ✔️')

def main():
    if not is_connected():
        print("No hay conexión a Internet. Por favor verifique su red y vuelva a intentarlo.")
        exit(1)
    # Si hay conexión, continúa normalmente
    soup = get_soup(BASE_URL)
    if not soup:
        return

    today_wallpaper = find_today_wallpaper(soup)
    if not today_wallpaper:
        print("No se encontró el label 'Today's Wallpaper'.")
        return

    image_page_url = get_image_page_url(today_wallpaper)
    if not image_page_url:
        print("No se encontró el enlace para 'Today's Wallpaper'.")
        return

    print(f"Image page url: {image_page_url} ✔️")
    download_url = get_download_url(image_page_url)
    if not download_url:
        print("No se encontró el botón 'Download 4K'.")
        return

    image_name = os.path.basename(image_page_url)
    file_extension = os.path.splitext(download_url)[1]
    save_path = os.path.join(SAVE_DIR, f"{image_name}{file_extension}")
    download_image_with_progress(download_url, save_path)

if __name__ == "__main__":
    main()
