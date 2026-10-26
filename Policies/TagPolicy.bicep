targetScope = 'subscription'

param policyAssignmentName string = 'require-a-tag-on-resource-groups'
param policyDefinitionID string = '/providers/Microsoft.Authorization/policyDefinitions/96670d01-0a4d-4649-9c89-2d3abc0a5025'
param policyDisplayName string = 'Require a tag on resource groups'

resource assignment 'Microsoft.Authorization/policyAssignments@2023-04-01' = {
  name: policyAssignmentName

  properties: {
    policyDefinitionId: policyDefinitionID

    displayName: policyDisplayName

    parameters: {
      tagName: {
        value: 'Owner'
      }

    
    }
  }
}

output assignmentId string = assignment.id
