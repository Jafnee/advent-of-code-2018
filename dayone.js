const fs = require('fs')


const numbers = fs.readFileSync('dayone-input.txt', 'utf8')
  .trim()
  .split('\n')
  .map(Number)

// pt 1
const sum = numbers.reduce((sum, x) => sum + x, 0)
console.log(sum)


function* numberRepeating() {
  while (true) {
    yield* numbers
  }
}

const occurredFrequencies = {'0': 1}
let current = 0
for (let number of numberRepeating()) {
  current += number
  if (occurredFrequencies[current]) {
    // pt 2
    console.log(current)
    break
  }
  occurredFrequencies[current] = 1
}
