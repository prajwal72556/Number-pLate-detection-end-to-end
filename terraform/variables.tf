variable "region" {
    type = string
    default = "ap-south-1"

}

variable "cidrvpc"{
  type = string
  default = "192.168.0.0/16"
}

variable "subnetcidr"{
  type = string
  default = "192.168.1.0/24"
}

variable "routetablecidr"{
  type = string
  default = "0.0.0.0/0"
}

variable "ami"{
    type = string
    default = "ami-010aff33ed5991201"
}

variable "instance_type"{
    type = string 
    default = "t2.micro"
}



variable "key"{
    type = string
    default = "hadoopKey"
}