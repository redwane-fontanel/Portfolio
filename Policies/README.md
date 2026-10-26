Azure Policies Folder

This folder contains Azure Policy assignments created using Bicep templates. The policies were developed and tested in the student subscription.

LocationPolicy.bicep: 

The Location Policy is assigned at subscription scope using the built-in Allowed locations policy definition. Allowed locations configured: France Central, France North, UK South, UK West, North Europe, West Europe.

Testing revealed that the custom location policy could be applied successfully for resource group deployments.
However, the subscription already contained a higher-level policy assignment restricting resource deployment locations. This existing assignement cannot be deleted or modified.

Policy Details:

Policy Name: Allowed locations
Policy Definition ID: e56962a6-4747-49cd-b67b-bf8b01975c4c
Scope: Subscription
Effect: Deny

Deployment:

$deployParams = @{
    Name         = "PolicyDeployment"
    Location     = "francecentral"
    TemplateFile = ".\LocationPolicy.bicep"
}

TagPolicy.bicep:

This policy ensures that all resource groups contain a required tag. In this implementation, the required tag is Owner.

Policy Details:

Policy Name: Require a tag on resource groups
Policy Definition ID: 96670d01-0a4d-4649-9c89-2d3abc0a5025
Scope: Subscription
Required Tag: Owner

Deployment:

$deployParams = @{
    Name         = "PolicyDeployment"
    Location     = "francecentral"
    TemplateFile = ".\TagPolicy.bicep"
}

New-AzSubscriptionDeployment @deployParams


DenyStorageAccountCreationAssignment.bicep: 

This policy prevents the creation of any Azure Storage Account within the assigned subscription.

A custom policy definition was created in DenyStorageAccount.json. The JSON file contains the policy rule that denies resources of type Microsoft.Storage/storageAccounts.

The custom policy definition was created using:

New-AzPolicyDefinition 
  -Name 'DenyStorageAccountCreation' 
  -DisplayName 'Do not allow creation of storage account.'
  -Policy 'DenyStorageAccountCreation.json'

The policy definition was then deployed using:

$deployParams = @{
    Name         = "PolicyDeployment"
    Location     = "francecentral"
    TemplateFile = "./DenyStorageAccountCreationAssignment.bicep"
}

New-AzSubscriptionDeployment @deployParams


ContainerAppZoneRedundancyPolicyAssignment.bicep:

This policy ensures that Azure Container App Environments are created with zone redundancy disabled.

A custom policy definition was created in ContainerAppZoneRedundancyPolicy.json. The JSON file contains the policy rule that evaluates the Microsoft.App/managedEnvironments/zoneRedundant property and denies deployments where the property is not set to false.

The custom policy definition was created using:

New-AzPolicyDefinition 
  -Name 'ContainerAppZoneDisabled' `
  -DisplayName 'Container App environments must have zone redundancy disabled' 
  -Policy 'ContainerAppZoneRedundancyPolicyAssignment.json'
  
The policy definition was then deployed using:

$deployParams = @{
    Name         = "PolicyDeployment"
    Location     = "francecentral"
    TemplateFile = "./ContainerAppZoneRedundancyPolicyAssignment.bicep"
}


StorageOnlySKUPolicy.bicep:

This policy restricts the creation of Azure Storage Accounts to a single allowed SKU. In this implementation, only Standard_LRS storage accounts can be created.

The policy uses the built-in policy definition Storage accounts should be limited by allowed SKUs.

Policy Details:

Policy Name: Storage accounts should be limited by allowed SKUs
Policy Definition ID: 7433c107-6db4-4ad1-b57a-a76dce0154a1
Scope: Subscription
Allowed SKU: Standard_LRS
Effect: Deny
Deployment
$deployParams = @{
    Name         = "PolicyDeployment"
    Location     = "francecentral"
    TemplateFile = ".\StorageOnlySKUPolicy.bicep"
}

New-AzSubscriptionDeployment @deployParams


AllowedResourceTypesAssignment.bicep:

This policy restricts the Azure resource types that can be deployed within the assigned subscription. Only the resource types specified in the custom policy are permitted. Any attempt to deploy a resource type outside of the allowlist is denied.

A custom policy definition was created in AllowedResourceTypes.json. The JSON file contains the policy rule that allows only the following resource types:

Microsoft.App/managedEnvironments
Microsoft.App/containerApps
Microsoft.Storage/storageAccounts

Policy Details
Policy Name: Allowed Resource Types
Policy Type: Custom
Scope: Subscription
Effect: Deny

Create the Policy Definition:

New-AzPolicyDefinition 
  -Name 'AllowedResourceTypes' 
  -DisplayName 'Allowed Resource Types' 
  -Policy 'AllowedResourceTypes.json'
  
Deploy the Policy Assignment:

$deployParams = @{
    Name         = "PolicyDeployment"
    Location     = "francecentral"
    TemplateFile = ".\AllowedResourceTypesAssignment.bicep"
}

New-AzSubscriptionDeployment @deployParams
