# Configure the AWS Provider
provider "aws" {
	access_key = var.access
	secret_key = var.secret
  region = var.region
}

# Create Instans
resource "aws_instance" "jenkins-master" {
  ami                    = "ami-0ea18256de20ecdfc"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.jenkins-master-SG.id]
  user_data              = file("./user_data.sh")

  tags = {
    Name = "jenkins-master"
  }
}

## Create Security Group
resource "aws_security_group" "jenkins-master-SG" {
  name        = "jenkins-master-SG"
    
  ingress {
    description          = "ssh"
    from_port            = 22
    to_port              = 22
    protocol             = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  
  ingress {
    description          = "http"
    from_port            = 8080
    to_port              = 8080
    protocol             = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}
