# Nautobot Azure VNet Automation

This repository provides automation for provisioning Azure Virtual Networks (VNets) based on data sourced from Nautobot.

It combines:
- **Nautobot API** as a Source of Truth
- **Python script** for data extraction
- **Terraform** for Azure resource provisioning
- **GitLab CI/CD pipeline** for automated execution and deployment

The workflow is fully automated through GitLab CI/CD, enabling consistent, repeatable, and secure infrastructure deployments across environments.

---

## Overview

## Workflow

The automation workflow consists of several steps that transform network data from Nautobot into deployed Azure infrastructure:

### 1. Data Source – Nautobot

Nautobot acts as the **Source of Truth** for network data.

- Prefixes are stored in Nautobot IPAM
- Only prefixes with the custom field `is_vnet = true` are considered
- Additional required custom and standard fields:
  - `vnet` → VNet name
  - `resource_group` → Azure Resource Group
  - `location` → Azure region

---

### 2. Data Extraction (Python Script)

The `cicd.py` script:

- Connects to Nautobot API using an API token
- Fetches:
  - Prefixes (`/api/ipam/prefixes/`)
  - Location assignments (`/api/ipam/prefix-location-assignments/`)
- Processes and maps data:
  - Matches prefix to Azure region
  - Extracts metadata from custom fields
- Create nautobot_vnets.json file which will be used by Terraform

---

### 3. Terraform Processing

Terraform reads `nautobot_vnets.json` and:

- Iterates over defined VNets
- Creates:
  - Azure Resource Groups
  - Azure Virtual Networks
- Uses locals and variables to dynamically map input data

---

### 4. Deployment (CI/CD Pipeline)

The process is automated via **GitLab CI/CD**:

Typical pipeline flow:

1. Export required environment variables (secrets)
2. Run Python script to generate JSON
3. Run:
   ```
   terraform init
   terraform plan
   terraform apply
   ```

---

### 5. Execution from Nautobot (Optional)

The entire workflow can also be triggered directly from Nautobot as a job.

- A dedicated Nautobot Job implementation is available in the `nautobot-jobs` repository
