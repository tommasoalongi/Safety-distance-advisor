//inputting velocity of preceding car and our car and wheather conditions, this file outputs necessary safety distance, supposing limit non-ideal tyres and reaction time

var badReactionTime = 1.3; //search some studies to meet 95th percentile of reaction time

var braking = function (velocitykmh, frictionK, reactionTime) {
    
    var velocity = velocitykmh / 3.6;
    var reactionDistance = velocity*reactionTime;
    
    var deceleration = 9.8 * frictionK;
    var velocitySquared = velocity*velocity;
    var deceleratingDistance =  velocitySquared/(2*deceleration) ;
    
    var totalDistance = reactionDistance + deceleratingDistance;
    return totalDistance;
};

//the preceding car stops in front of me (it is already at the end of its reaction time), I start breaking after a bad reaction time with worse breaking system 

var myBrakingSpace = braking(120, 0.75, badReactionTime); //search 95ish percentile of breaking capacity 
var precedingBrakingSpace = braking(120, 0.95, 0); //pretty close to 1, 0.95 is very ideal, almost impossible

var idealDistance = myBrakingSpace - precedingBrakingSpace +5; //5 meters error
console.log(idealDistance);
