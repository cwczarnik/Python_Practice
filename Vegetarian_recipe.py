# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:04:54 2015

@author: X
"""


def get_recipe_data(ingredients, skill, time):
    
    #get data from website of database
   # ingredients = compared to data
    #skill = something in data that we quantize
    #time = cooktime from data
    return "meat!"

##issue, what about amounts of ingredients? like in kg or lbs of stuff. how do I keep this?
##simple appraoch, ask user
def prompt_user_for_ingredients():
    ingredient_list = []
    ingredient_amount = []
    ingredient_unit = []
    ctr = 0
    while(ctr < 2 ):#limiting a number of ingredients, we'll assume they have seasoning unless it's rare.
        ingredient_list.append(raw_input("what do you have?"))
        ingredient_amount.append(raw_input("how much of this do you have? (i.e. 1 egg, 1 lb of meat, .5 gallon milk) "))
        ingredient_unit(raw_input("in which measurement? (i.e., lb, gallon, egg number)"))
        ctr += 1
    return ingredient_list
        
def prompt_user_for_skill():
    skill_level = raw_input("what is your cooking skill level? (1-10)")
    return skill_level
    
def prompt_user_for_time():
    cooking_time = raw_input("how much time do you have? (0-30) min")
    return cooking_time

def recommend_recipe():
    ingredients = prompt_user_for_ingredients()
    skill =  prompt_user_for_skill()
    time = prompt_user_for_time()
    print "For your skill level of %d and your cooking time of %d" % (int(skill), int(time))
    print " and your ingredients of ", ingredients
    print "your recommended recipe is %s" % (get_recipe_data(ingredients, skill,time))
    
    
recommend_recipe()