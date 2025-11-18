FROM ubuntu:20.10

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

# Instalar el cliente OpenSSH
RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Comando por defecto al iniciar el contenedor (mantiene vivo el contenedor)
CMD ["tail", "-f", "/dev/null"]
