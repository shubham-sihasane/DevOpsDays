`terraform version` OR `terraform --version` ⌘ Check the installed version of terraform, including providers version after initialization

`aws --version` ⌘ Check the installed aws CLI version

`tarrform init` ⌘ Prepare your working directory for other commands

`terraform validate` ⌘ Check whether the configuration is valid

`terraform plan` ⌘ Show changes required by the current configuration

`terraform apply --auto-approve` ⌘ Create or update infrastructure, auto approval is optional

`terraform destory --auto-approve` ⌘ Destroy previously-created infrastructure, auto approval is optional

`terraform destory --target <resource-fullname>` ⌘ Destroy specific resource

All other commands:
  console       Try Terraform expressions at an interactive command prompt
`terraform fmt` ⌘ Reformat your configuration in the standard style
  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote Terraform modules
  graph         Generate a Graphviz graph of the steps in an operation
  import        Associate existing infrastructure with a Terraform resource
  login         Obtain and save credentials for a remote host
  logout        Remove locally-stored credentials for a remote host
  metadata      Metadata related commands
  modules       Show all declared modules in a working directory
  output        Show output values from your root module
  providers     Show the providers required for this configuration
  query         Search and list remote infrastructure with Terraform
  refresh       Update the state to match remote systems
  show          Show the current state or a saved plan
  stacks        Manage HCP Terraform stack operations
  state         Advanced state management
  taint         Mark a resource instance as not fully functional
  test          Execute integration tests for Terraform modules
  untaint       Remove the 'tainted' state from a resource instance
  version       Show the current Terraform version
  workspace     Workspace management

Global options (use these before the subcommand, if any):
  -chdir=DIR    Switch to a different working directory before executing the
                given subcommand.
  -help         Show this help output or the help for a specified subcommand.
  -version      An alias for the "version" subcommand.


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

