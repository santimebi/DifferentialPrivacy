import numpy as np

def gaussian_mechanism(data, sensitivity, epsilon, delta):
    """
    Aplica el mecanismo de Gauss para garantizar privacidad diferencial.

    Parameters:
    - data: array-like, los datos de entrada.
    - sensitivity: float, sensibilidad de la consulta.
    - epsilon: float, parámetro de privacidad.
    - delta: float, probabilidad de relajación en la privacidad.

    Returns:
    - resultado privatizado.
    """
    # Calcular el resultado de la consulta
    query_result = np.mean(data)

    # Calcular la desviación estándar del ruido gaussiano
    sigma = np.sqrt(2 * np.log(1.25 / delta)) * (sensitivity / epsilon)

    # Generar ruido gaussiano
    noise = np.random.normal(0, sigma)

    # Agregar ruido al resultado
    privatized_result = query_result + noise
    return privatized_result

def add_gaussian_noise_to_data(data, sensitivity, epsilon, delta):
    """
    Agrega ruido Gaussiano a cada elemento de los datos.

    Parameters:
    - data: array-like, los datos de entrada.
    - sensitivity: float, sensibilidad de cada elemento.
    - epsilon: float, parámetro de privacidad.
    - delta: float, probabilidad de relajación en la privacidad.

    Returns:
    - Lista de datos con ruido agregado.
    """
    sigma = np.sqrt(2 * np.log(1.25 / delta)) * (sensitivity / epsilon)
    noisy_data = data + np.random.normal(0, sigma, size=len(data))
    noisy_data = np.round(noisy_data, 2)  # Redondear a 2 decimales
    return noisy_data

# Ejemplo de datos
np.random.seed(42)  # Semilla para reproducibilidad
data = np.random.randint(0, 100, size=100)  # Datos sensibles (edades, por ejemplo)

# Parámetros de privacidad y sensibilidad
epsilon = 1.0
delta = 1e-5
sensitivity = 1  # Sensibilidad para cada elemento

# Agregar ruido Gaussiano a cada edad
noisy_data = add_gaussian_noise_to_data(data, sensitivity, epsilon, delta)
noisy_mean = np.mean(noisy_data)

# Calcular el resultado original y privatizado con el promedio
original_mean = np.mean(data)

print(f"Edades originales: {data}")
print(f"Edades privatizadas: {[f'{age:.2f}' for age in noisy_data]}")
print(f"Promedio real de edades: {original_mean:.2f}")
print(f"Promedio privatizado con edades ruidosas: {noisy_mean:.2f}")
