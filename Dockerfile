FROM kalilinux/kali-rolling


RUN apt-get update --fix-missing
RUN apt-get install -y neovim
