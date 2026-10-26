  targetScope = 'subscription'

  param policyAssignmentName string = 'storage-account-deny-policy-assignment'
  param policyDefinitionID string = '/subscriptions/b8c8747b-edc4-4534-b3ab-6249e9d54dd5/providers/Microsoft.Authorization/policyDefinitions/DenyStorageAccountCreation'
  param policyDisplayName string = 'Do not allow creation of storage accounts'

  resource assignment 'Microsoft.Authorization/policyAssignments@2023-04-01' = {
    name: policyAssignmentName

    properties: {
      policyDefinitionId: policyDefinitionID

      displayName: policyDisplayName
    }
  }

  output assignmentId string = assignment.id
