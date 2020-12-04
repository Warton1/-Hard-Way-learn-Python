my_name = 'Panyu Zhang'
my_age = 25 # not a lie
my_height = 180 #cm
my_weight = 180 #g
my_eye = 'brown'
my_teeth = 'white'
my_hair = 'Black'

print ("Let's talk about %s." % my_name)
print ("He's %d cm tall." % my_height)
print ("He's %d g heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eye and %s hair." % (my_eye, my_hair))
print ("His teeth are ussually %s depending on the coffe" % my_teeth)


#this line is tricky, try to get it exactly right
print ("If I add %r, %r, and %r I get %r" % (my_age, my_height, my_weight, my_age + my_height + my_weight))