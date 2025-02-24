# Projekt IoT: NodeMCU v3 z przekaźnikiem (LED) sterowanym przez Django REST API
Projekt demonstruje, jak kontrolować przekaźniki, diody LED lub inne urządzenia wymagające przełączania binarnego (True/False) za pomocą protokołu HTTP. Projekt integruje NodeMCU v3 z Django REST Framework API, umożliwiając zdalne sterowanie stanami urządzeń. Aplikacja Django może być hostowana na serwisach takich jak PythonAnywhere.
### Przegląd projektu
Celem tego projektu jest nauka sterowania urządzeniami IoT (np. przekaźnikami i diodami LED) za pomocą API opartego na HTTP. Dzięki Django REST Framework możemy łatwo obsługiwać żądania API i przełączać stany urządzeń przez internet. NodeMCU komunikuje się z backendem Django, wysyłając i odbierając dane do sterowania stanami urządzeń.
### Funkcje
- Sterowanie przekaźnikami lub diodami LED za pomocą żądań HTTP GET.
- Integracja z Django REST API.
- Proste wdrożenie na PythonAnywhere.
- Zrozumienie koncepcji sterowania urządzeniami IoT.
### Wada
Jedną z wad jest to, że czas pomiaru jest rejestrowany w GMT zamiast w lokalnej strefie czasowej.
_____________________________________________________________________________________________________________________________
# IoT Project: NodeMCU v3 with Relay (LED) Control via Django REST API

This project demonstrates how to control relays, LEDs, or other devices that require binary (True/False) state switching using the HTTP protocol. The project integrates a NodeMCU v3 with a Django REST Framework API, allowing state changes to be transmitted and controlled remotely. The Django application can be hosted on services like PythonAnywhere.

## Project Overview

The aim of this project is to learn how to control IoT devices (like relays and LEDs) using an HTTP-based API. By leveraging the Django REST Framework, we can easily handle API requests and toggle device states through the internet. The NodeMCU communicates with the Django backend, sending or receiving data to control device states.

## Features

1. Control relays or LEDs via HTTP GET requests.
2. Integration with Django REST API.
3. Easy deployment using PythonAnywhere.
4. Understanding the concept of IoT device control.

## Requirements

- **Django**: 5.0.7
- **Django REST Framework**: 3.15.2
- **django-filter**: 24.2
- **Markdown**: 3.6
- **Python**: 3.12.3 (You may use another version, but it is recommended to use Python 3.9 or newer.)

## Deploying the Django Project

You can learn how to deploy a Django project in this video: [How to Deploy a Django Project](https://www.youtube.com/watch?v=xtnUwvjOThg)

# Homepage of the website
![20240926_202427](https://github.com/user-attachments/assets/cca91c70-731e-47ed-9cd4-58fbee075326)

# Drawback
One disadvantage is that the measurement time is recorded in GMT instead of the time zone.
