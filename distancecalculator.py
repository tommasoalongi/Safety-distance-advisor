
#method with assumption focal dist

percentual_of_pixels = 100

focal_distance = 9.5 #cm
image_height = percentual_of_pixels/100*12 #cm
height = 1.4 #m

distance = height*focal_distance/image_height #m
print(distance)


#method with full screen calibration

height_fullscreen = 1.44 #m
distance_fullscreen = 1.25 #m
height = 1.44 #m
screen_percentage = 39/100

distance = distance_fullscreen/screen_percentage * height/height_fullscreen

print(distance)
