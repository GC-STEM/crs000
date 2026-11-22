# Course Reference Environment

The **Course Reference Environment (CRE)** is the official, tested computing environment used to run and evaluate coursework.

Each course uses the STEM **Standard Operating Environment (SOE)** and, when needed, a **Course-Specific Overlay (CSO)**.

Students may use other development environments if they are **functionally equivalent for coursework**. Submitted work must run correctly and meet assignment requirements in the designated CRE.

## Table of Contents <!-- omit from toc -->

1. [Getting Started (Students)](#getting-started-students)
2. [GitHub Codespaces (Optional Backup)](#github-codespaces-optional-backup)
3. [Advanced Development Options](#advanced-development-options)
4. [Environment Configuration and Maintenance](#environment-configuration-and-maintenance)

## Getting Started (Students)

Most students do not need to install or configure virtualization software.

Follow your course's [Module 1 Setup Tasks](../README.md#module-1-setup-tasks) to configure your development environment.

Depending on the course, your primary environment could be one of the following:

- **Local computer:** Install and configure the required development tools on your Windows, macOS, or Linux computer.
- **Codio Virtual Desktop:** Use the provided cloud development environment when available and designated by your course.

> [!NOTE]
> When a Codio Virtual Desktop (CVD) is available, it is designated as the CRE—the authoritative environment for evaluating coursework.

## GitHub Codespaces (Optional Backup)

GitHub Codespaces provides a cloud-based development environment accessible through a web browser.

Use Codespaces when temporarily working from another computer or when your normal development environment is unavailable.

To open your course repository in Codespaces:

1. Open your personal course repository on GitHub.
2. Select **Code > Codespaces > Create codespace**.
3. Allow the development environment to initialize.

Codespaces uses the repository's `.devcontainer/devcontainer.json` configuration to build and configure the course environment.

> [!NOTE]
> Codespaces usage is subject to [GitHub's account limits and billing policies](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces). It is intended as a backup unless your course specifies otherwise. Currently, GitHub provides 60 hours of Codespaces usage per month for free to all account holders and an additional 30 hours for students with a verified GitHub Education account.

---

STOP HERE WARNING: The following sections are intended for advanced users and are not necessary for most students.

---

## Advanced Development Options

The following options are primarily intended for advanced students, faculty, and STEM administrators who need to build, test, or verify course environments.

### Containers: Docker

Docker provides isolated Linux development environments that can run on Windows, macOS, and Linux.

The course's `.devcontainer/Dockerfile` builds an Ubuntu environment using the SOE and applies the course's CSO during container setup.

#### Local Docker Container

Install Docker with the Docker Compose plugin.

From the course repository root (e.g., `$HOME/Repos/crs000`), run:

```bash
cd "$HOME/Repos/crs000"
docker compose -f .devcontainer/compose.local.yaml run --build --rm soe
```

This command:

- Builds the course development image.
- Mounts the course repository inside the container.
- Applies the course-specific requirements.
- Opens a Bash terminal.

Changes made to files in the mounted course repository are saved on the host computer.

The local Docker container does not include a Linux graphical desktop or automatically install the VS Code extensions configured for Codespaces.

#### Verify the Environment

From inside the local Docker container, run:

```bash
/opt/gc-stem/runtime/bin/python \
  /opt/gc-stem/soe/scripts/python/soe.py verify \
  --workspace /workspaces/course
```

This checks the configured course development environment against the SOE and CSO requirements.

Codespaces runs environment verification automatically during startup and checks configured editor extensions when VS Code attaches.

### Virtual Machines and Other Platforms

Virtual machines provide complete guest operating systems when containers or native installations are insufficient.

| Platform | Host OS | Intended Use |
| --- | --- | --- |
| Docker | Windows, macOS, Linux | Primary container platform |
| VirtualBox | Windows, macOS, Linux* | Preferred full-VM platform when supported |
| WSL2 | Windows | Persistent Ubuntu development environment |
| WSLc | Windows | Alternative OCI container runtime |
| Hyper-V | Windows | Optional Windows-hosted virtualization |
| Multipass | Windows, macOS, Linux | Ubuntu VM deployment and testing |
| Windows Sandbox | Windows | Disposable Windows test environment |

*VirtualBox support depends on the host architecture, guest operating system, and software version.*

Not all platforms have fully implemented or qualified course configurations.

#### Windows: WSL2 and WSLc

**Windows Subsystem for Linux 2 (WSL2)** provides a Linux environment on Windows.

The SOE repository provides setup scripts for installing and configuring Ubuntu under WSL2. The course CSO supplies additional requirements when applicable.

**WSL containers (`wslc`)** provide another way to build and run OCI containers on Windows.

WSLc does not currently support Docker Compose, which the existing local Docker workflow requires. It is therefore an optional alternative pending validation of a complete course workflow.

#### VirtualBox, Hyper-V, and Vagrant

VirtualBox and Hyper-V may be used for courses or testing scenarios that require a complete virtual machine.

The repository includes a `Vagrantfile` placeholder for future automated VM provisioning.

**Vagrant support is not yet implemented.** The current `Vagrantfile` does not define a working course VM, and `vagrant up` is not a supported setup command.

#### Multipass

Multipass provides Ubuntu virtual machines for development and testing.

Use the shared provisioning scripts in [GC-STEM/soe](https://github.com/GC-STEM/soe/tree/main/scripts) to configure supported environments.

#### Windows Sandbox

`Sandboxfile.wsb` launches a temporary Windows environment using the shared [SOE Windows Sandbox setup script](https://github.com/GC-STEM/soe/blob/main/scripts/powershell/setup_windows_sandbox.ps1).

This option is intended for testing, not persistent student coursework.

Changes inside Windows Sandbox are lost when the Sandbox closes. Course-specific Windows capabilities require validation; some CSO settings are not yet supported.

## Environment Configuration and Maintenance

The course environment is defined by the following components:

| Component | Purpose |
| --- | --- |
| [GC-STEM/soe](https://github.com/GC-STEM/soe) | Canonical SOE manifests, tools, and provisioning scripts |
| [SOE manifest](https://github.com/GC-STEM/soe/blob/main/.config/soe_manifest.json) | Shared environment requirements |
| [CSO manifest](../.config/cso_manifest.json) | Course-specific requirements |
| `Dockerfile` | Container build instructions |
| `devcontainer.json` | VS Code and Codespaces configuration |
| `compose.local.yaml` | Local Docker deployment |
| `Sandboxfile.wsb` | Windows Sandbox deployment |
| `Vagrantfile` | Placeholder for future VM deployment |

The current course container targets:

- Ubuntu 24.04 LTS
- CPython 3.12
- AMD64 architecture

The Dockerfile's `SOE_COMMIT` argument selects the SOE source revision used to build the container.

### Published Container Images

The intended distribution model is to publish validated SOE and course-specific container images through the **GitHub Container Registry (GHCR)**.

This will allow Codespaces and local Dev Containers to use the same prebuilt, tested images rather than independently building the environment.

**Current implementation:** The repository's `devcontainer.json` and local Docker Compose configuration build from the Dockerfile. They do not yet reference published GHCR images.

### Maintenance Guidelines

1. Maintain shared dependencies and provisioning scripts in `GC-STEM/soe`.
2. Define course-specific requirements in `.config/cso_manifest.json`.
3. Test environment updates before deploying them to students.
4. Rebuild and verify containers after changing their SOE source revision or dependencies.
5. Keep the course's designated CRE consistent with its published setup instructions.

Courses requiring specific hardware, GPU capabilities, or other specialized computing resources may designate Codio or another managed environment as their CRE.

The goal is **functional equivalence for coursework**, not identical host hardware or operating systems.
