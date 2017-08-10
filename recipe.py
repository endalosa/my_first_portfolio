ingredients = {
'Heavy cream': '3 cups',
'Whole milk': '1 cup',
'Sugar': '3/4 cup',
'Pure vanilla extract': '1 tablespoon',
'Kosher salt': '1 pinch of',
'Egg yolks': '5',
'Oreos': '4 ounces'}


ingredient_instruction = {
'step 1': 'Whisk the cream, milk, sugar, vanilla and 1/2 teaspoon salt in a medium saucepan and bring to a simmer over medium heat',
'step 2': 'Beat the egg yolks in a medium bowl',
'step 3': 'Slowly whisk 1 cup of the hot cream mixture into the beaten yolks, then pour back into the saucepan, whisking, and return to medium heat',
'step 4': 'Cook, stirring constantly with a wooden spoon, until the mixture thickens, coats the spoon and reaches 180 degrees F on a thermometer, 6 to 8 minutes.',
'step 5': 'Remove from the heat and strain the custard through a fine-mesh sieve into a large bowl or measuring cup; discard the solids.',
'step 6': 'Stir often until the mixture cools to room temperature',
'step 7': 'Lightly press plastic wrap directly against the surface of the custard to prevent a skin from forming.',
'step 8': 'Chill until cold, about 3 hours'
}

print('Type recipe to view the recipe or ingredients to view ingredients')
while (1>0):
    user_input = input()
    if user_input == "recipe":
        x=1
        print(ingredient_instruction['step ' + str(x)] + ' Type next for the next instruction')
        user_input = input()
        while (x < len(ingredient_instruction)):
            if user_input == "next":
                x = x+1
                print(ingredient_instruction['step ' + str(x)] + ' Type next for the next instruction')
                user_input = input()
            if x == 8:
                print('DONE!')
        break
    elif user_input == "ingredients":
        for i in ingredients:
            print(ingredients[i] + ' of ' + i)
        break
    else:
        print ("I don't understand. Type 'recipe' to view the recipe or 'ingredients' 'to see the ingredients")
        continue
