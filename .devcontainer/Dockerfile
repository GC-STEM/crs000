# syntax=docker/dockerfile:1

# Course devcontainer: build the SOE from a pinned public source snapshot.
# The course CSO is resolved after the course checkout is mounted.
FROM ubuntu:24.04

ARG SOE_COMMIT=1b50676df8559fdd2a02ce36934430504604eebc

LABEL org.opencontainers.image.title="GC-STEM SOE + course CSO" \
      org.opencontainers.image.source="https://github.com/GC-STEM/SOE" \
      org.opencontainers.image.description="Ubuntu 24.04 / Python 3.12 course environment"

ENV LANG=C.UTF-8 TZ=Etc/UTC SOE_ROOT=/opt/gc-stem/soe \
    SOE_SCHEMA_PATH=/opt/gc-stem/schema/manifest.schema.json \
    PIP_DISABLE_PIP_VERSION_CHECK=1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates curl gpg git openssh-client python3 python3-venv \
        sudo tar gzip procps libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

# Fetch the canonical SOE manifest and automation from an immutable commit.
RUN mkdir -p "$SOE_ROOT" \
    && curl --fail --location --retry 3 --max-time 120 \
        "https://github.com/GC-STEM/SOE/archive/${SOE_COMMIT}.tar.gz" \
        | tar -xz --strip-components=1 -C "$SOE_ROOT"

# Vendor-signed GitHub CLI repository; package signatures are checked by APT.
RUN mkdir -p /etc/apt/keyrings \
    && curl --fail --location --retry 3 --max-time 60 \
        https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        --output /etc/apt/keyrings/githubcli.gpg \
    && chmod 644 /etc/apt/keyrings/githubcli.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/githubcli.gpg] https://cli.github.com/packages stable main" \
        > /etc/apt/sources.list.d/github-cli.list

RUN python3 -m venv /opt/gc-stem/runtime \
    && /opt/gc-stem/runtime/bin/python -m pip install --no-cache-dir \
        -r "$SOE_ROOT/.config/requirements-automation.txt"

# Fetch the one canonical schema, matching the SOE build process.
ADD --chmod=0444 https://raw.githubusercontent.com/GC-STEM/.github/refs/heads/main/schemas/manifest.schema.json /opt/gc-stem/schema/manifest.schema.json

RUN chmod 0755 /opt/gc-stem/schema \
    && /opt/gc-stem/runtime/bin/python "$SOE_ROOT/scripts/python/soe.py" \
        install-system --workspace "$SOE_ROOT" --mode soe \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && if getent group 1000 > /dev/null; then \
        groupmod --new-name vscode "$(getent group 1000 | cut -d: -f1)"; \
       else groupadd --gid 1000 vscode; fi \
    && if getent passwd 1000 > /dev/null; then \
        usermod --login vscode --gid 1000 --home /home/vscode \
            --move-home --shell /bin/bash \
            "$(getent passwd 1000 | cut -d: -f1)"; \
       else useradd --uid 1000 --gid 1000 --create-home \
            --shell /bin/bash vscode; fi \
    && echo 'vscode ALL=(root) NOPASSWD:ALL' > /etc/sudoers.d/vscode \
    && chmod 440 /etc/sudoers.d/vscode \
    && mkdir -p /workspaces /home/vscode/Repos \
    && chown vscode:vscode /workspaces /home/vscode/Repos

USER vscode
WORKDIR /workspaces
RUN /opt/gc-stem/runtime/bin/python "$SOE_ROOT/scripts/python/soe.py" \
    verify --workspace "$SOE_ROOT" --mode soe

# Codespaces mounts the course; postCreateCommand then provisions its CSO.
CMD ["sleep", "infinity"]
