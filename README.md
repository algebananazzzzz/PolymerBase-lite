# PolymerBaseLite

PolymerBaseLite is a Framework dedicated to empower Backend development for Full-Stack Applications. It simplifies the provisioning of backend Serverless AWS resources using Terraform with CI/CD pipelines. It implements a unified source of truth within YAML configuration files for provisioning infrastructure and application configuration.


## Table of Contents

- [About](#about)
- [Configuration](#configuration)
- [Resources](#resources)
- [Installation](#installation)
- [Deployment](#deployment)
- [License](#license)
- [Contact](#contact)

## About

PolymerBaseLite is a member of the Polymer framework family, designed to empower developers in building sophisticated applications. This framework utilizes Terraform for provisioning Serverless resources within the AWS Cloud Infrastructure, while also facilitating the establishment of streamlined CI/CD pipelines through GitHub Actions. For more information about the Polymer framework, please visit the [PolymerBase repository](https://github.com/algebananazzzzz/PolymerBase).


This lite version of PolymerBase is designed for developing simple APIs by e.g. Flask, excluding Apollo Graphql and Webpack integrations.

## Configuration

Please refer to the example lambda configuration file for additional information:
[Example Configuration File](.polymer/lambda_config/main/dev.env.json)


Configuration within PolymerBase consists of three key aspects:

1. Resource Configuration: This involves the setup and customization of the resources that the Backend Stack deploys, e.g. API Gateway, Lambda.

2. Lambda Configuration: Configuration for Lambda. Consists of parameters such as VPC Configuration, environment variables, IAM.

Configuration is stored in YAML files, specific to CI/CD staging environments. Lambda configuration files should follow the format {stage}.env.json (e.g., dev.env.json for development).


## Resources

Here are the resources that PolymerBase will deploy if specified, along with instructions on how to configure them:

1. **S3 Data Bucket** to store Application Content

Under s3, you can choose the name for S3 bucket to be provisioned
```yaml
s3:
  data_bucket:
    name: polymerbase-data
```

2. **Lambda functions** for executing compute operations. Polymer will automatically provision CodeDeploy resources for All-At-Once deployment.

Under lambda, you can specify multiple functions, and where to source its production files from
```yaml
lambda:
  polymerbase:
    function_name: PolymerBase-%s-function # %s will be replaced by stage e.g. dev
    basedir: app/dist
    envfile_basedir: .polymer/lambda_config 
  polymerhandler:
    function_name: PolymerHandler-%s-function # %s will be replaced by stage e.g. dev
    basedir: app/handler
    envfile_basedir: .polymer/lambda_config 
```

3. **API Gateway Integration** for exposing API endpoints.

Under api_lambda_integration, you can which lambda functions require API Gateway Integrations
```yaml
api_lambda_integration:
  polymerbase:
    cors_configuration: 
      allow_origins: 
        - "*"
      allow_methods: 
        - OPTIONS
        - GET
        - POST
      allow_headers: 
        - "*"
      expose_headers: 
        - "*"
      max_age: 300
    cors_handler_name: cors-preflight-handler
```

4. **DynamoDB Tables**.

Under dynamodb, you can specify multiple tables. The **attributes** attribute is used to specify non-key attributes e.g. name, required in `gen.py` to generate application configuration and schema definition.
```yaml
dynamodb:
  users:
    table_name: users-PolymerBase
    key_attributes:
      id: S
      userId: S
    attributes:
      key: S
      name: S
      description: S
    hash_key: userId
    range_key: id
    read_capacity: 2
    write_capacity: 2
    child: posts # used for defining GraphQL models i.e. field of [Posts] within type Users
  posts:
    table_name: posts-ProjectBalls
    key_attributes:
      id: S
      postId: S
      userId: S
    attributes:
      labels: NS
      likes: N
      name: S
      text: S
    hash_key: userId
    range_key: id
    global_secondary_index:
      postId-id:
        hash_key: postId
        range_key: id
        write_capacity: 2
        read_capacity: 2
        projection_type: "ALL"
    read_capacity: 2
    write_capacity: 2
```

5. **EventBridge Groups**.

Used to create multiple Eventbridge Groups
```yaml
eventbridge_schedule_group:
  - AnelaBotScheduler
```


## Installation

1. Clone the PolymerBaseLite Framework
```shell
git clone https://github.com/algebananazzzzz/PolymerBase-lite
```

## Deployment


1. **Create a GitHub Repository:**
Start by creating a GitHub repository. After that, follow these steps to initialize Git and switch to the `dev` branch:
```
git init
git add -A
git commit
git checkout -b dev
git remote set-url origin https://github.com/{your_repository_name}.git
```

2. **Configure Secrets and Variables:**

For secure and streamline access to AWS and Terraform Cloud, follow these steps to configure secrets and variables within your GitHub repository:

- Click on the `Settings` tab within your repository.
- Navigate to `Secrets` (or `Environments` > `Secrets` depending on your GitHub version).
- Click on `New repository secret` to add secrets or `New repository variable` to add variables.

**Required Secrets:**

1. `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
2. `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
3. `TF_API_TOKEN`: Obtain this token by going to your [Terraform Cloud tokens page](https://app.terraform.io/app/settings/tokens).

**Required Variables:**

1. `APPLICATION_NAME`: Set your application's name.
2. `AWS_REGION`: Define the AWS region you're working with.
3. `TF_ORGANISATION`: If not already created, create a Terraform Cloud organization for use.

3. **Push to GitHub**
```shell
git push --set-upstream origin dev
```

With GitHub Actions in place, this push will automatically trigger Terraform Cloud to provision the necessary resources.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
[Provide a way for users to contact you, whether it's an email address, a link to your website, or social media profiles.]


## Contact

For inquiries and further information, feel free to reach out to me through my [portfolio page](https://www.algebananazzzzz.com).
