resource "aws_vpc" "vpc1"{
  cidr_block = "${var.cidrvpc}"

tags = {
    Name = "vpcCovid19"
  }
}


resource "aws_subnet" "lab1" {
  vpc_id     = aws_vpc.vpc1.id
  cidr_block = "${var.subnetcidr}"
  availability_zone = "${var.region}" 

  tags = {
    Name = "LabCovid19"
  }
}

resource "aws_security_group" "securityAllTraffic" {
  name        = "all traffic allow"
  description = "Allow all inbound traffic"
  vpc_id      = aws_vpc.vpc1.id

  ingress = [
    {
      description      = "TLS from VPC"
      from_port        = 0
      to_port          = 0
      protocol         = -1
      cidr_blocks      = ["0.0.0.0/0"]
      
    }
  ]

  egress = [
    {
      description      = "TLS from VPC"
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
      
    }
  ]

  tags = {
    Name = "SecutityAllowAllCovid"
  }
}

resource "aws_internet_gateway" "igateway" {
  vpc_id = aws_vpc.vpc1.id

  tags = {
    Name = "iggatewayCovid19"
  }
}

resource "aws_route_table" "routetablecovid19" {
  vpc_id = aws_vpc.vpc1.id

  route = [
    {
      cidr_block = "${var.routetablecidr}"
      gateway_id = aws_internet_gateway.igateway.id
    }
  ]

  tags = {
    Name = "routetablecovid19"
  }
}

resource "aws_route_table_association" "association" {
  subnet_id      = aws_subnet.lab1.id
  route_table_id = aws_route_table.routetablecovid19.id
}






resource "aws_instance" "Master" {
  ami           = "${var.ami}"
  instance_type =  "${var.instance_type}"
  subnet_id = aws_subnet.lab1.id
  security_groups = ["aws_security_group.securityAllTraffic"]
  key_name = "${var.key}"

  tags = {
    Name = "K8sMaster"
  }
}

resource "aws_instance" "Slave" {
  count = 2
  ami           = "${var.ami}"
  instance_type =  "${var.instance_type}"
  subnet_id = aws_subnet.lab1.id
  security_groups = ["aws_security_group.securityAllTraffic"]
  key_name = "${var.key}"

  tags = {
    Name = "K8sSlave-${count.index}"
  }
}

