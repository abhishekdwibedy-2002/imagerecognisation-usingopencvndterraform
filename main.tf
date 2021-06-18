
provider "aws" {
    region = "ap-south-1" #region id which u want to selecdt
    access_key = "#access key of your IAM USER AWS Account"
    secret_key = "#Secret key of your IAM USER AWS Account"
}

resource "aws_instance" "web" {
    ami = "ami-06a0b4e3b7eb7a300"
    instance_type = "t2.micro"

    tags = {
        Name = "task-6"
    }
}

resource "aws_ebs_volume" "example" {
  availability_zone = aws_instance.web.availability_zone
  size              = 5

  tags = {
    Name = "EBS Volume through face Recognition"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.example.id
  instance_id = aws_instance.web.id
}
