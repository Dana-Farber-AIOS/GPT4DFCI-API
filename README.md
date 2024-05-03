# GPT4DFCI API 🔌

**Welcome to the code repository for GPT4DFCI API, the API client of [GPT4DFCI](https://github.com/Dana-Farber-AIOS/GPT4DFCI), which a allows you to leverage GPT4DFCI programmatically in your application.**

*ℹ️ GPT4DFCI is a private and secure generative AI tool, based on GPT-4 and deployed for non-clinical use at Dana-Farber Cancer Institute. See all details about it in its [code repository](https://github.com/Dana-Farber-AIOS/GPT4DFCI).*

This repository is organized in the following sections:

* Prerequisites
* Run the GPT4DFCI API demo
* License
* Contact

## ⚙️  Prerequisites

[Poetry](https://python-poetry.org) is a tool for dependency management and packaging in Python used by a number of the demos.

If you are already familiar with Poetry, or are comfortable setting up your own environment with other tools, you can probably skip this.

### Installing Poetry
https://python-poetry.org/docs/#installation

#### For macOS this would be the suggested way:

- Install brew: 

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install poetry using: 
```
brew install poetry
```

### Installing GPT4DFCI API dependencies

After installing Poetry, navigate to the directory you are interested in and run:

```
poetry install --no-root
```

This should create a virtual environment with the dependencies specified in `pyproject.toml` installed.


To activate the virtual environment, run:

```
poetry shell
```

or, alternatively, if you don't want to use Poetry's [sub-shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment) pattern, you can run:
```
source .venv/bin/activate
```


## 🟢  Run the GPT4DFCI API demo

### Set up environment variables
In a file called `.env`, fill in the following values:

```
AZURE_OPENAI_ENDPOINT=https://...
AZURE_OPENAI_ENTRA_SCOPE=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

`AZURE_OPENAI_ENDPOINT` should be the GPT4DFCI API endpoint, without the `/openai` suffix.

`AZURE_OPENAI_ENTRA_SCOPE` should be the scope required for the bearer token, the UUID `client_id`.

### Authenticate via Azure CLI
Prerequisites: [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)

For macOS this would be

```
brew install azure-cli
```

Then, make sure you are logged in via the Azure CLI to an account that has been granted access to the GPT4DFCI API.

```
az login
```

Close the window after logging in and get back to the shell.


### VPN

```
Turn on the VPN or make sure you are running from an on-prem resource.
```

### Run the demo
```
export $(cat .env | xargs) && python demo.py
```

### Shutting down

When finished working, shut the current virtual environment with

```
deactivate
```

### Resuming work

When you are read to resume working on this, come back to this folder and resume working with

```
source .venv/bin/activate
export $(cat .env | xargs) && python demo.py
```

# 🎫 License

The GNU GPL v2 version of GPT4DFCI is made available via Open Source licensing. The user is free to use, modify, and distribute under the terms of the GNU General Public License version 2.

Commercial license options are available also, and include additional features.


# 📧 Contact

Questions? Comments? Suggestions? Get in touch!

aios@dfci.harvard.edu
