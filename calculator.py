#inputting velocity of preceding car and our car and wheather conditions, this file outputs necessary safety distance, supposing limit non-ideal tyres and reaction time

badReactionTime = 1.3 #search some studies to meet 95th percentile of reaction time

def braking (velocitykmh, frictionK, reactionTime) :
    
    velocity = velocitykmh / 3.6
    reactionDistance = velocity*reactionTime
    
    deceleration = 9.8 * frictionK
    velocitySquared = velocity*velocity
    deceleratingDistance =  velocitySquared/(2*deceleration)
    
    totalDistance = reactionDistance + deceleratingDistance
    return totalDistance

#the preceding car stops in front of me (it is already at the end of its reaction time), I start breaking after a bad reaction time with worse breaking system 

myBrakingSpace = braking(110, 0.75, badReactionTime) #search 95ish percentile of breaking capacity 
precedingBrakingSpace = braking(120, 0.95, 0) #pretty close to 1, 0.95 is very ideal, almost impossible

idealDistance = myBrakingSpace - precedingBrakingSpace +5 #5 meters error
print (idealDistance)
