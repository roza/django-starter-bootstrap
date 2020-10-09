FROM gitpod/workspace-full:latest

USER gitpod

RUN sudo apt-get update \
 && sudo apt-get install -y \
    chromium-chromedriver\
 && sudo rm -rf /var/lib/apt/lists/*