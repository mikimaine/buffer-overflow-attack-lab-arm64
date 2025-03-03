# SeedLab-2 ARM Version Solution

This repository contains the solution for the SeedLab-2 ARM version. This project is for educational purposes only.

## Prerequisites

- any ARM VM
- Docker
- Docker Compose

## Setup and Running the Solution

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/SeedLab-2-ARM.git
    cd SeedLab-2-ARM
    ```

2. **Build and run the containers:**

    ```sh
    docker-compose up --build
    ```

    This will build and start the containers for each buffer overflow server level (L1, L2, L3, L4).

3. **Access the running containers:**

    Each container runs a server that you can interact with. The IP addresses for the containers are as follows:
    - Level 1: `10.9.0.5`
    - Level 2: `10.9.0.6`
    - Level 3: `10.9.0.7`
    - Level 4: `10.9.0.8`

    You can access these servers using their respective IP addresses.

## Details

For more detailed information on the buffer overflow attacks and the solution, please refer to the [Buffer Overflow Attack Report ARM.pdf](./Buffer%20Overflow%20Attack%20Report%20ARM.pdf) file in the main directory.

## Disclaimer

This project is for educational purposes only. Do not use the code or techniques demonstrated here for malicious purposes.


