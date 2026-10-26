targetScope = 'subscription'

  param policyAssignmentName string = 'allowed-resource-types'
  param policyDefinitionID string = '/subscriptions/b8c8747b-edc4-4534-b3ab-6249e9d54dd5/providers/Microsoft.Authorization/policyDefinitions/AllowedResourceTypes'
  param policyDisplayName string = 'Allowed Resource Types'

  resource assignment 'Microsoft.Authorization/policyAssignments@2023-04-01' = {
    name: policyAssignmentName

    properties: {
      policyDefinitionId: policyDefinitionID

      displayName: policyDisplayName
    }
  }

  output assignmentId string = assignment.id
