param policyAssignmentName string = 'allowed-locations'
param policyDefinitionID string = '/providers/Microsoft.Authorization/policyDefinitions/e56962a6-4747-49cd-b67b-bf8b01975c4c'
param policyDisplayName string = 'Allowed locations'
targetScope = 'subscription'

resource assignment 'Microsoft.Authorization/policyAssignments@2023-04-01' = {
  name: policyAssignmentName
 

  properties: {
    policyDefinitionId: policyDefinitionID

    displayName: policyDisplayName

    parameters: {
      listOfAllowedLocations: {
        value: [
          'francenorth', 'francecentral', 'uksouth', 'ukwest', 'northeurope', 'westeurope'
        ]
      }

      effect: {
        value: 'Deny'
      }
    }
  }
}

output assignmentId string = assignment.id
