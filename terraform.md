`terraform version` OR `terraform --version` ⌘ Check the installed version of terraform, including providers version after initialization

`aws --version` ⌘ Check the installed aws CLI version

`tarrform init` ⌘ Prepare your working directory for other commands, `-upgrade` for to upgrade providers (optional)

`terraform validate` ⌘ Check whether the configuration is valid

`terraform plan` ⌘ Show changes required by the current configuration

`terraform apply --auto-approve` ⌘ Create or update infrastructure, auto approval is optional

`terraform destory --auto-approve` ⌘ Destroy previously-created infrastructure, auto approval is optional

`terraform destory --target <resource-identifier>` ⌘ Destroy specific resource

All other commands:
  console       Try Terraform expressions at an interactive command prompt

`terraform fmt` ⌘ Reformat your configuration in the standard style

  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote Terraform modules
  graph         Generate a Graphviz graph of the steps in an operation

`terraform import <resource-dentifier>` ⌘ Associate existing infrastructure with a Terraform resource, must add configuration first before importing

`terraform login` ⌘ Obtain and save credentials for a remote host
`terraform logout` ⌘ Remove locally-stored credentials for a remote host
  metadata      Metadata related commands
  modules       Show all declared modules in a working directory
`tteraform output` ⌘ Show output values from your root module
  providers     Show the providers required for this configuration
  query         Search and list remote infrastructure with Terraform
`terraform refresh` ⌘ Update the state to match remote systems, Terraform automatically performs refresh while plan and apply
`terraform show` ⌘ Show the current state or a saved plan
  stacks        Manage HCP Terraform stack operations

`terraform state` ⌘ Advanced state management

`terraform state identities` ⌘List the identities of resources in the state

`terraform state list` ⌘ List resources in the state

`terraform state mv` ⌘ Move an item in the state

`terraform state pull` ⌘ Pull current state and output to stdout

`terraform state push` ⌘ Update remote state from a local state file

`terraform state replace-provider` ⌘ Replace provider in the state

`terraform state rm` ⌘ Remove instances from the state

`terraform state show` ⌘ Show a resource in the state

  taint         Mark a resource instance as not fully functional
untaint       Remove the 'tainted' state from a resource instance 

test          Execute integration tests for Terraform modules

`terraform workspace` ⌘ Workspace management, `default` is the `default` workspace

`terraform workspace list` ⌘ List workspaces

`terraform workspace show` ⌘ Show the name of current workspace

`terraform workspace new <workspace-name>` ⌘ Create a new workspace and switch to newly created workspace

`terraform workspace delete <workspace-name>` ⌘ Delete an existing workspace

`terraform workspace select <workspace-name>` ⌘ Change to another existing workspace

Code in terraform language is stored in plain text file with .tf extension. There is also a JSON-based variant of language that is need with .tf.json file extension. These files are called as configuration files or manifest files.

### Arguments
Arguments configure a particular resource which can be required or optional. Terraform will give an error and not apply the configuration at all if a required argument is missing. (Provider Specific)

### Attributes
Attributes are values exposed by a particular resource. Format - `resource_type.resource_name.attribute_name` (Provider Specific)

### Meta Arguments
Meta arguments change a resource type's behaviour and are not resource specific. Ex - `count`, `for_each` (Terraform Specific)

### Terraform Top Level Block
1. Terraform Settings Block
2. Provider Block
3. Resource Block
4. Input Variables Block
5. Output Variables Block
6. Local Values Block
7. Data Sources Block
8. Modules Block

- Fundamental Blocks - Terraform, Provider, Resources
- Variable Blocks - Input values, Output values, Local values
- Calling / Referencing Blocks - Data Sources, Modules

# Precedence of Environment Variables
- Environment Variables
- The terraform.tfvars file, if present
- The terraform.tfvars.json file, if present
- Any *.auto.tfvars or *.auto.tfvars.json files, processed in lexical order of their filenames
- Any -var and -var-file options on the command line, in the order they are provided

### Terraform Introduction
Traditional Infrastructure Setup: Before IaC, engineers manually configured servers, networks, and storage. This was error-prone, slow, and hard to replicate.

Why IaC?
- Automates infrastructure provisioning. 
- Ensures consistency across environments (dev, test, prod). 
- Makes infrastructure version-controlled, just like code.

Terraform’s Role: Terraform is one of the most popular IaC tools, enabling declarative infrastructure management across multiple cloud providers.

### Benefits of Infrastructure as a Code
1. Speed:
- The first significant benefit IaC provides is speed.
- Infrastructure as code enables you quickly set up your complete infrastructure by running a script.
- You can do that for every environment, from development to production, passing through staging, QA, and more.
- IaC can make the entire software development lifecycle more efficient.
2. Consistency:
- Manual processes result in mistakes.
- Humans are fallible. IaC solves that problem by having config files themselves be the single source of truth.
- That way, you guarantee the same configurations will be deployed over and over without discrepancies.
3. Accountability:
- This one is quick and easy. Since you can version IaC configuration files like any source code file, you have full traceability of the changes each configuration suffered.
- No more guessing games about who did what and when.


### Terraform Cloud

1. Working with Terraform involves managing collections of infrastructure resources and most organizations manage many different collections.
2. When run locally, terraform manages each collection of infrastructure with a persistent working directory, which contains a configuration, state data and variable.
3. Since terraform CLI uses content from directory it runs in, you can organize infrastructure resources into meaningful groups by keeping their configurations in separate directories.
4. Terraform cloud manages infrastructure collections with workspace instead of directories.
5. A workspace contains everything Terraform needs to manage a given collection of infrastructure and separate workspaces function like separate working directories.
6. Terraform cloud workspace and local working directories serve the same purpose, but they store the data differently.

| Component               | Local Terraform                                              | Terraform Cloud                                                     |
|-------------------------|--------------------------------------------------------------|---------------------------------------------------------------------|
| Terraform Cong Files    | On Disk                                                      | In linked version control repo or periodically uploaded via API/CLI |
| Variable values         | As ".tfvars" files, as CLI arguments or in shell environment | In workspace                                                        |
| State Files             | On Disk or separate backend                                  | In Workspace                                                        |
| Credentials and Secrets | In shell environment or entered at prompts           | In workspace, stored as sensitive variables                         |

7. In addition to the basic terraform content, terraform cloud keeps some additional data for each workspace

* State Versions:
- Each workspace retains backups of its previous state files
- Although only the current state is necessary for managing resources, the state history can be helpful for tracking changes over time or recovering from problems.

* Run History:
- When terraform cloud manages a workspace's terraform runs, it retains a record of all run activity, including summaries, logs, reference to the changes that caused the run and user commands.

8. Both terraform cloud and terraform CLI have features called "workspaces" but they function differently

9. Terraform CLI:
- Terraform CLI workspaces are associated with a specific working directory and isolates multiple state files in the same working directory, letting you manage multiple groups of resources with a single configuration.
- The terraform CLI does not required you to create CLI workspaces.

10. Terraform Cloud:
- Terraform cloud workspaces are required. They represent all of the collections of infrastructure in an organization.
- They are also a major component of role-based access in Terraform cloud. You can grant individual users and user groups permissions for one or more workspaces that dictate whether they can manage variables, perform, runs etc.
- You can not manage resources in terraform cloud without creating at least one workspace.

#### Terraform Cloud - VCS Integration
1. Terraform cloud is more powerful when we integrate it with version control system provider.
2. Although we can use many of Terraform Cloud's feature without one, a VCS connection provides additional features and improved workflow.
3. 1 When workspaces are linked to a VCS repo, terraform cloud can automatically initiate terraform runs when changes are commited to the specified branch.
4. 2 Terraform cloud makes code review easier by automatically predicting how pull requests will affect infra.
5. 3 Publishing new versions of a private terraform module is as easy as publishing a tag to the module's repo.

- Terraform recommends configuring VCS access when first setting up an organization and you might need to add additional VCS providers later depending on how your organization groups. 
- Configuring a new VCS provider requires permission to manage VCS settings for the organization.
- Terraform cloud supports the VCS providers like github, gitlab, bitbucket, azure devops etc.

1. Workspaces organize infrastructure into meaningful groups.
2. We can create new workspaces when we need to manage a new collection of infrastructure resources.
3. You can create workspaces using terraform cloud UI, workspaces API, terraform enterprise provider, no-code provisioning
4. To create a workspace, you must be a member of a team with "manage all projects", "manage all workspaces" or "admin permissions".
5. Terraform recommends using consistent and informative names for new workspaces.
6. One common approach is combining the workspace's such as the component, the component's run environment and the region where the workspace is provisioning infrastructure.
- networking-prod-us-east
- networking-dev-east
- monitoring-prod-us-west
- monitoring-dev-us-west
7. You can add additional attributes to your workspace names as needed. For example, you can add infrastructure provider, datacenter or line of business.
8. After you create a new workspace from version control repo, terraform cloud scans its configuration files for terraform variables and displays any that do not have default value and do not have a definition in an existing global variable set.
9. Terraform can not perform successful runs in the workspace until you set values for the variables.
10. If you connected a VCS repo to the workspace, terraform cloud automatically registers a webhook with your VCS provider.
11. After we have manually start a run, terraform cloud automatically queues a plan when new commits appear in the selected branch of linked repo or someone opens a pull request on that branch.
12. To start working with terraform cloud, we need to specific the credentials for the respective cloud platform.
13. Using static credentials in the workspace to authenticate providers presents a security risk, even if we are rotating the creds regularly.
14. Dynamic provider creds helps us to improve the security posture by letting us provision new, temporary credentials for each run.
15. We can configure dynamic credentials for each terraform cloud workspace.
16. This workflow eliminates the need to manually manage and rotate creds across the organization.
17. This also let us use the cloud platform's authentication and authorization tools to scope permissions based on metadata, such as a run's phase, the workspace and the organization.

** How Dynamic Creds Work:
- We configure a trust relationship between the cloud platform and terraform cloud.
- As a part of the process, we can define rules that let terraform cloud workspace and runs access specific resources.
- Then, the following process occurs for each terraform plan and apply.
- Terraform Cloud generates a workload identity token. The token is compliant with OpenID connect Protocol (OIDC) standards and includes information about the organization, workspace and run stage.
- When a plan or apply begins, terraform cloud sends the workload identity token to the cloud platform, along with other info needed to authenticate.
- The cloud platform uses terraform cloud's public key to verify the workload identity token.
- If verification succeeds, the cloud platform returns a set of fresh temporary creds for terraform cloud to use.
- Teraform cloud sets up these creds within the run environment for the terraform provider to use.
- The terraform plan or apply proceeds.
- When the plan or apply completes, the run environment is torn down and temporary credentials are discarded.

* Set up a trust Relationship *
  * You musy configure a relationship between terraform cloud and other cloud platform.
  * The exact details of this process will be different depending on the cloud platform.
* Configure Cloud Platform Access *
  * You must configure roles and policies for the cloud platform to define the workspace's access to infrastructure resources.
* Configure Terraform Cloud Workspace *
  * You musy add specific environment variables to the workspace to tell Terraform cloud how to authenticate to the other cloud platforms during plans and applies.
  * Each cloud platform has it's own set of environment variables to configure dynamic creds. The process for each setp is different for each cloud platforms.

- Before we start running the plan or apply stage on the terraform cloud platform, we will need to setup the authentication so that terraform cloud can access the cloud platform and create the resources on that platform.
- You can use terraform cloud's native OpenIS connect integration with AWS to get dynamic credentials for the AWS provider in the Terraform runs.

#### Terraform Cloud State File
1. Every Terraform Cloud workspace has its own separate state data which is used for runs within that workspace.
2. In remote runs, terraform cloud automatically configures terraform to use the workspace's state.
3. Terraform configuration does not need an explicit backend configuration and even if a backend configuration is present, it will be overridden.
4. In local runs, we can use a workspace's state by configuring the CLI integration and authenticating with a user token that has permission to read and write the state versions for the relevant workspace.
5. When using a terraform configuration that references outputs from another workspace, the authentication token must also have permission to read state outputs for that workspace
6. In addition to the current state, terraform cloud retains historical state version, which can be used to analyze infrastructure changes over time.
7. You can view a workspace's state versions from it's states tab
8. Each state in the list indicates which run and which VCS commit was associated with
9. CLick a state in the list for more details, including a diff against the previous state and a link to the raw state file.
10. 






