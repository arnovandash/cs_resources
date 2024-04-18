variable "vpc" {}
variable "subnetid" {}
variable "keyname" {}

resource "aws_security_group" "ssh" {
  vpc_id = var.vpc

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_iam_role" "ringier_example_role" {
  name = "ringier_example_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_instance_profile" "ringier_example_profile" {
  name = "ringier_example_profile"
  role = aws_iam_role.ringier_example_role.name
}

resource "aws_instance" "ringier_ubuntu_graviton" {
  ami           = "ami-0ccedbebe3a0f5ecc"
  instance_type = "t4g.nano"
  key_name      = var.keyname
  subnet_id     = var.subnetid
  vpc_security_group_ids = [aws_security_group.ssh.id]

  iam_instance_profile = aws_iam_instance_profile.ringier_example_profile.name

  tags = {
    Name = "RingierBastionGravitonInstance"
  }
}
