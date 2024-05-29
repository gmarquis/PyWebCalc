provider "aws" {
  region = "eu-west-1"
}

# Create Lambda function
resource "aws_lambda_function" "cloudfront_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "your_lambda_function_name"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda_function.handler"
  runtime       = "python3.8"

  # If your Lambda function code is in a separate directory, you can use source_code_hash instead of filename
  # source_code_hash = filebase64sha256("path/to/lambda_function_payload.zip")
}

# IAM role for Lambda execution
resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_execution_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Attach policy to Lambda execution role
resource "aws_iam_role_policy_attachment" "lambda_exec_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Create CloudFront distribution with Lambda@Edge association
resource "aws_cloudfront_distribution" "my_distribution" {
  origin {
    domain_name = "your_s3_bucket_name.s3.amazonaws.com"
    origin_id   = "S3-Bucket-Origin"
  }

  enabled             = true
  default_root_object = "index.html"

  # Specify the Lambda@Edge function association
  default_cache_behavior {
    # Other cache behavior settings...

    lambda_function_association {
      event_type    = "viewer-request"
      lambda_arn    = aws_lambda_function.cloudfront_lambda.qualified_arn
      include_body  = false
    }
  }

  # Other CloudFront distribution settings...
}

