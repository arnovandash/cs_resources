
## Challenges

### 1. **REST API Code Challenge**

Develop a REST web API that includes:
- An endpoint with a GET method that returns: The average server load and the available disk space on the current file system.
- An endpoint with a GET method that retrieves the value of the key "return_value" from a provided JSON file (`tech_assess.json`).
- **Bonus**: An endpoint with a POST method that allows overwriting the "return_value" key in the `tech_assess.json` file.

**Requirements**:
- Use any programming language.
- The API should both return and accept data in JSON format.

### 2. **Terraform Infrastructure Challenge**

Create a bastion host within AWS using Terraform:
- EC2 instance with a security group.
- Open ports: Inbound 22, Outbound all traffic.
- Any Linux AMI, instance type t3.nano.
- IAM role attached to the EC2 (no specific policies required).
- Variables: VPC ID (`var.vpc`), Subnet (`var.subnetid`), SSH Key (`var.keyname`).

**Bonus**: Version with an AWS Graviton instance type.

### 3. **Docker Container Challenge**

Containerize and run a NodeJS application, exposing it on port 8080:
- Provide a Dockerfile that contains and runs the application.
- Start the application with: `node main.js`.

**Bonus**: Include a Docker build script that utilizes buildkit and caching logic.

