
# Technical Assessment Terraform Challenge

## Overview
These Terraform scripts are designed to provision Bastion Hosts on AWS, including setup of AWS EC2 instances and security groups.

## Files
- `bastion.tf`: Sets up a standard AWS EC2 instance as a Bastion Host.
- `bastion_gravitron.tf`: Sets up an AWS Graviton-based EC2 instance.

## Key Components
- **EC2 Instances**: Provision standard (t3.nano) and Graviton (t4g.nano) instances.
- **Security Group**: Configures to allow SSH access.
- **IAM Role and Instance Profile**: Created for EC2 instances.

## Usage
1. **Initialization**:
   ```bash
   terraform init
   ```
2. **Variables**:
   Provide values for `vpc`, `subnetid`, `keyname`.
3. **Planning and Apply**:
   ```bash
   terraform plan
   terraform apply
   ```
4. **Access**:
   Access the EC2 instance via SSH using the provided key pair.
5. **Clean-up**:
   ```bash
   terraform destroy
   ```
