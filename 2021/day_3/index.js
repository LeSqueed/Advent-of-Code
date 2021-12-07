import { readFileSync } from 'fs';

const filename = new URL('input.txt', import.meta.url); //Load file from folder where script is running.
const input = readFileSync(filename).toString().split('\n') //Read lines into input as array.

//Calculate at every position if there's more 1's or 0's, if the end result has a positive value at array position corresponding to bit position it has more 1's and vice versa. 0 is equal.
function calcPositions(data, offset=0){
    const values = []
    for(let i = 0; i in data; i++){
        for(let c =0; c in Array.from(data[i].replace(/(\r\n|\n|\r)/gm, "")); c++){
            let current = Array.from(data[i])
            if(values[c] === undefined){ //If undefined create an initial value of 0.
                values[c] = 0
            }
            if(current[c] == 0){ //If it's a 0 subtract one
                values[c] -= 1
            }
            if(current[c] == 1){ //If it's a 1 add one
                values[c] += 1
            }
        }
    }
    return values
}

//Uses data from calcPositions with an offset to generate oxygen data based on most common value for that position.
function getOxygen(data, offset, valueData ){
    const values =[]
    const toCheck = (valueData[offset] < 0) ? '0' : '1'
    for(let i = 0; i in data; i++){
        if(Array.from(data[i][offset]) == toCheck){
            values.push(data[i])
        }
    }
    return values
}

//Opossite of Oxygen function
function getCO2(data, offset, valueData ){
    const values =[]
    const toCheck = (valueData[offset] < 0) ? '0' : '1'
    for(let i = 0; i in data; i++){
        if(Array.from(data[i][offset]) != toCheck){
            values.push(data[i])
        }
    }
    return values
}

let offset = 0  //Offset used to place the curser on the right bit.
let positionValue = []
let toProcessOxygen = input
let toProcessCO2 = input

let noLoop = 5 //For debugging to avoid infinite loops. Add if statement where this decreases by 1 and check when it hits 0 for a break.

//Get Oxygen value
while(toProcessOxygen.length != 1){
    for(let i = 0; i in toProcessOxygen; i++){
        positionValue = calcPositions(toProcessOxygen) //This has array of positions, if positive or 0 it has to turn into a 1, if lower than 0 into a 0.
        toProcessOxygen = getOxygen(toProcessOxygen, offset++, positionValue)
    }
}

offset = 0 //Reset offset
while(toProcessCO2.length != 1){
    for(let i = 0; i in toProcessCO2; i++){
        positionValue = calcPositions(toProcessCO2) //This has array of positions, if positive or 0 it has to turn into a 1, if lower than 0 into a 0.
        toProcessCO2 = getCO2(toProcessCO2, offset++, positionValue)
    }
}

//Convert binary to dec.
const Oxygen = parseInt(toProcessOxygen,2)
const CO2 = parseInt(toProcessCO2, 2)
const lifesupportRating = (Oxygen*CO2)

//Output the resulting rating by mutliplying the values.
console.log('Life support rating is: '+String(lifesupportRating))