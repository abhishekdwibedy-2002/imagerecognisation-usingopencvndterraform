
provider "aws" {
    region = "ap-south-1"
    access_key = "AKIAX4DPQGU3FFF6DRBU"
    secret_key = "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"
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
