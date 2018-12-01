const fs = require('fs')

const numbers = fs.readFileSync('dayone-input.txt', 'utf8')
  .split('\n')
  .map(x => Number.parseInt(x, 10))
  // NaN for last blank line in input file.
  .filter(x => !Number.isNaN(x))

// pt 1
const sum = numbers.reduce((sum, x) => sum + x, 0)
console.log(sum)


function* numbers_repeating() {
  while (true) {
    yield* numbers
  }
}

const occurred_frequencies = {'0': 1}
let current = 0
for (let number of numbers_repeating()) {
  current += number
  if (occurred_frequencies[current]) {
    // pt 2
    console.log(current)
    break
  }
  occurred_frequencies[current] = 1
}
