import json

# Opening JSON file
jsonFile = open('data.json')
data = json.load(jsonFile)

def alphExists(alph):
  return alph in data['alpha']

def stateExists(state):
  for currentState in data['states']:
    if (state == currentState['name']):
      return True
  return False            

def findState(state):
  for currentState in data['states']:
    if (state == currentState["name"]):
      return currentState
  return False

def findNextState(currentState, connector):
  for connection in currentState['connections']:
    if (connection['conector'] == connector):
      return findState(connection["to"])
  return False

# Início
if ( False == stateExists(data['startState']) ):
  print("Estado inicial não existe.")

exits = {'outputs': []}
# Para cada cadeia de entrada
for entry in data['entries']:
  # Pegar o estado inicial
  currentState = findState(data["startState"])
  # Para cada letra do alfabeto
  entryCount = 0
  for conector in entry:
    entryCount += 1
    # Verificar se a letra passada é valida
    if (False == alphExists(conector) ):
      print("Cadeia inválida ", conector)
      continue
    # aqui vai pro prox estado
    currentState = findNextState(currentState, conector)
    if (False == currentState):
      print("Negativo")
      exits.append('%s false'%entry)
      
    if ( entryCount >= len(entry)):
      if (currentState['name'] in data['endStates']):
        print("Positivo")
        exits['outputs'].append({ 'conector': entry, 'response': True})
        break
      print("Negativo")
      exits['outputs'].append({ 'conector': entry, 'response': False})

with open('outputs.json', 'w') as f:
  f.write(str(exits))       
jsonFile.close()
