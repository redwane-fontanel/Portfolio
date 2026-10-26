  targetScope = 'subscription'

  param policyAssignmentName string = 'containerapp-zone-redundancy-policy-assignment'
  param policyDefinitionID string = '/subscriptions/b8c8747b-edc4-4534-b3ab-6249e9d54dd5/providers/Microsoft.Authorization/policyDefinitions/ContainerAppZoneRedundancy'
  param policyDisplayName string = 'Container App zone redundancy policy'

  resource assignment 'Microsoft.Authorization/policyAssignments@2023-04-01' = {
    name: policyAssignmentName

    properties: {
      policyDefinitionId: policyDefinitionID

      displayName: policyDisplayName
    }
  }

  output assignmentId string = assignment.id
