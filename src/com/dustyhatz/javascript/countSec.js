// Create an array of input length
function createArray(length) {
	
	// Initialize empty array
	const arr = []

	// For the length of the array add that number (i) to the array
	for (let i = 1; i <= length; i++) {

		// Add number to the array
		arr.push(i)

	}
	// Return the array
	return arr
}


// Print each second for the duration of input seconds
function countSec(seconds) {

	// Create an array of seconds using the creatArray function
	const arr = createArray(seconds)

	// Initiate the delay amount for setTimout function
	let time = 0

	// For every number in the array, print that number after a one second delay
	for (let i = 0; i < arr.length; i++) {
		setTimeout(console.log, time,	arr[i])

		// Increment the time delay by one second
		time = time + 1000
	}
}


// Call the function using 20 seconds
countSec(20)