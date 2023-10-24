from view import menu, getSelection, executeSelection

while True:
    menu()
    selection = getSelection()
    continueLoop = executeSelection(selection)
    if not continueLoop:
        break