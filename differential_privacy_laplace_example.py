import numpy as np
import pandas as pd

def laplace_mechanism(data, sensitivity, epsilon):
    """
    Aplica el mecanismo de Laplace para garantizar privacidad diferencial.

    Parameters:
    - data: array-like, los datos de entrada.
    - sensitivity: float, sensibilidad de la consulta.
    - epsilon: float, parámetro de privacidad.

    Returns:
    - resultado privatizado.
    """
    # Calcular el resultado de la consulta
    query_result = np.mean(data)

    # Generar ruido Laplace
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)

    # Agregar ruido al resultado
    privatized_result = query_result + noise
    return privatized_result

def add_noise_to_data(data, sensitivity, epsilon):
    """
    Agrega ruido Laplace a cada elemento de los datos.

    Parameters:
    - data: array-like, los datos de entrada.
    - sensitivity: float, sensibilidad de cada elemento.
    - epsilon: float, parámetro de privacidad.

    Returns:
    - Lista de datos con ruido agregado.
    """
    scale = sensitivity / epsilon
    noisy_data = data + np.random.laplace(0, scale, size=len(data))
    noisy_data = np.round(noisy_data, 2)  # Redondear a 2 decimales
    return noisy_data

# Simulación de datos inventados
np.random.seed(42)  # Semilla para reproducibilidad
data = np.random.randint(18, 80, size=50)  # Edades simuladas de 50 personas

# Parámetros de privacidad y sensibilidad
epsilon = 0.5  # Nivel de privacidad
sensitivity = 1  # Sensibilidad para cada elemento

# Agregar ruido a cada edad y calcular la media privatizada
noisy_data = add_noise_to_data(data, sensitivity, epsilon)
noisy_mean = np.mean(noisy_data)

# Mostrar resultados originales y privatizados
print(f"Edades originales: {data}")
print(f"Edades privatizadas: {noisy_data}")
print(f"Promedio real de edades: {np.mean(data):.2f}")
print(f"Promedio privatizado con edades ruidosas: {noisy_mean:.2f}")
