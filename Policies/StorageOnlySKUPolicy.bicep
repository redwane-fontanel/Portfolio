  targetScope = 'subscription'

  param policyAssignmentName string = 'storage-accounts-allowed-skus'
  param policyDefinitionID string = '/providers/Microsoft.Authorization/policyDefinitions/7433c107-6db4-4ad1-b57a-a76dce0154a1'
  param policyDisplayName string = 'Storage accounts should be limited by allowed SKUs'

  resource assignment 'Microsoft.Authorization/policyAssignments@2023-04-01' = {
    name: policyAssignmentName

    properties: {
      policyDefinitionId: policyDefinitionID

      displayName: policyDisplayName

      parameters: {
        listOfAllowedSKUs: {
          value: [
            'Standard_LRS'
          ]
        }
        effect: {
          value: 'Deny'
        }
      }
    }
  }

  output assignmentId string = assignment.id
