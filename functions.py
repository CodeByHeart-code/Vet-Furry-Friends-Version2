import logging
from classes import Owner, Pet, Consultation

# Configuración del logging
logging.basicConfig(
    filename='clinica_veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Comentario: El logging está configurado para registrar eventos de nivel INFO o superior,
# con formato que incluye fecha/hora, nivel y mensaje descriptivo.
# Todos los logs se almacenan en 'clinica_veterinaria.log'.

# Listas para almacenar objetos Owner y Pet
owners = []
pets = []

def is_valid_name(value):
    """Valida que el valor no sea solo numérico y tenga sentido como nombre."""
    return value and not value.isdigit() and any(char.isalpha() for char in value)

def is_valid_reason_or_diagnosis(value):
    """Valida que el motivo o diagnóstico no sea solo numérico, no esté vacío y tenga letras."""
    return value and not value.isdigit() and any(char.isalpha() for char in value)

def is_valid_date(value):
    """Valida que la fecha no esté vacía, no sea solo números y que tenga un formato básico."""
    # Opcional: se puede mejorar con expresiones regulares para formato dd/mm/aaaa
    return value and not value.isdigit() and any(char.isdigit() for char in value) and any(char.isalpha() for char in value) == False

def register_owner():
    """Registra un nuevo dueño y lo agrega a la lista de dueños. Maneja errores de entrada y los deja en el log."""
    print("=== Register Owner ===")
    try:
        name = input("Owner's name: ").strip()
        if not is_valid_name(name):
            logging.warning(f"Nombre de dueño inválido ingresado: '{name}'")
            raise ValueError("Owner's name must contain letters and cannot be only numbers.")

        phone = input("Phone: ").strip()
        if not phone or phone.isalpha():
            logging.warning(f"Teléfono inválido ingresado: '{phone}'")
            raise ValueError("Phone must be a non-empty number.")
        # Puedes agregar validaciones adicionales para formato de teléfono si lo deseas

        address = input("Address: ").strip()
        if not address:
            logging.warning("Dirección vacía ingresada.")
            raise ValueError("Address cannot be empty.")

        owner = Owner(name, phone, address)
        owners.append(owner)
        print("Owner successfully registered.")
        logging.info(f"Owner registered: {owner}")
        return owner
    except ValueError as ve:
        print(f"Input error: {ve}")
        logging.warning(f"Input error in register_owner: {ve}")
    except Exception as e:
        print(f"Error registering owner: {e}")
        logging.error(f"Exception in register_owner: {e}")


def find_owner_by_name(name):
    """Busca un dueño por nombre."""
    for o in owners:
        if o.name.lower() == name.lower():
            return o
    return None


def register_pet():
    """Registra una nueva mascota y la asigna a un dueño, validando entradas y logueando errores."""
    print("=== Register Pet ===")
    try:
        name = input("Pet's name: ").strip()
        if not is_valid_name(name):
            logging.warning(f"Nombre de mascota inválido ingresado: '{name}'")
            raise ValueError("Pet's name must contain letters and cannot be only numbers.")

        species = input("Species: ").strip()
        if not is_valid_name(species):
            logging.warning(f"Especie inválida ingresada: '{species}'")
            raise ValueError("Species must contain letters and cannot be only numbers.")

        breed = input("Breed: ").strip()
        if not is_valid_name(breed):
            logging.warning(f"Raza inválida ingresada: '{breed}'")
            raise ValueError("Breed must contain letters and cannot be only numbers.")

        age_input = input("Age: ").strip()
        if not age_input.isdigit() or int(age_input) < 0:
            logging.warning(f"Edad inválida ingresada: '{age_input}'")
            raise ValueError("Age must be a non-negative integer.")
        age = int(age_input)

        owner_name = input("Owner's name: ").strip()
        if not is_valid_name(owner_name):
            logging.warning(f"Nombre de dueño inválido ingresado: '{owner_name}'")
            raise ValueError("Owner's name must contain letters and cannot be only numbers.")

        owner = find_owner_by_name(owner_name)
        if not owner:
            print("Owner not found. Please register them first.")
            logging.warning(f"Attempted to register pet for non-existent owner: {owner_name}")
            owner = register_owner()
            if not owner:
                logging.error("Pet registration aborted due to failed owner registration.")
                return

        pet = Pet(name, species, breed, age, owner)
        pets.append(pet)
        print("Pet successfully registered.")
        logging.info(f"Pet registered: {pet}")
    except ValueError as ve:
        print(f"Input error: {ve}")
        logging.warning(f"Input error in register_pet: {ve}")
    except Exception as e:
        print(f"Error registering pet: {e}")
        logging.error(f"Exception in register_pet: {e}")


def find_pet_by_name(name):
    """Busca una mascota por nombre."""
    for p in pets:
        if p.name.lower() == name.lower():
            return p
    return None


def register_consultation():
    """Registra una consulta veterinaria para una mascota específica, validando entradas y logueando errores."""
    print("=== Register Consultation ===")
    try:
        pet_name = input("Pet's name: ").strip()
        if not is_valid_name(pet_name):
            logging.warning(f"Nombre de mascota inválido ingresado para consulta: '{pet_name}'")
            raise ValueError("Pet's name must contain letters and cannot be only numbers.")
        pet = find_pet_by_name(pet_name)
        if not pet:
            print("Pet not found, please register it first.")
            logging.warning(f"Attempted to register consultation for non-existent pet: {pet_name}")
            return
        date = input("Date of consultation: ").strip()
        if not is_valid_date(date):
            logging.warning(f"Fecha inválida ingresada: '{date}'")
            raise ValueError("Date must not be only numbers, cannot be empty and should contain digits and separators (e.g. 10/05/2024).")
        reason = input("Reason: ").strip()
        if not is_valid_reason_or_diagnosis(reason):
            logging.warning(f"Motivo inválido ingresado: '{reason}'")
            raise ValueError("Reason must contain letters and cannot be only numbers.")
        diagnosis = input("Diagnosis: ").strip()
        if not is_valid_reason_or_diagnosis(diagnosis):
            logging.warning(f"Diagnóstico inválido ingresado: '{diagnosis}'")
            raise ValueError("Diagnosis must contain letters and cannot be only numbers.")
        consultation = Consultation(date, reason, diagnosis, pet)
        pet.add_consultation(consultation)
        print("Consultation successfully registered.")
        logging.info(f"Consultation registered for pet {pet.name}: {consultation}")
    except ValueError as ve:
        print(f"Input error: {ve}")
        logging.warning(f"Input error in register_consultation: {ve}")
    except Exception as e:
        print(f"Error registering consultation: {e}")
        logging.error(f"Exception in register_consultation: {e}")


def list_pets():
    """Muestra todas las mascotas registradas y sus dueños."""
    print("=== List of Pets ===")
    if not pets:
        print("No pets registered.")
        logging.info("Attempted to list pets but none registered.")
    for p in pets:
        print(p)
        print("-" * 40)


def view_pet_history():
    """Muestra el historial de consultas de una mascota específica."""
    print("=== Consultation History ===")
    try:
        pet_name = input("Pet's name: ").strip()
        pet = find_pet_by_name(pet_name)
        if pet:
            print(pet.show_consultations())
            logging.info(f"Consultation history viewed for pet {pet_name}")
        else:
            print("Pet not found.")
            logging.warning(f"Consultation history requested for non-existent pet: {pet_name}")
    except Exception as e:
        print(f"Error viewing pet history: {e}")
        logging.error(f"Exception in view_pet_history: {e}")

# Nota: El uso de try-except asegura que el programa no se detenga ante entradas inválidas,
# proporcionando mensajes claros al usuario y registrando los eventos en el archivo de log.