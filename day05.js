const fs = require('fs')


function fullyReactPolymer(polymer) {
  const reactedPolymer = polymer.split('')
  let startIndex = 0
  while (true) {
    let done = true
    for (let i = startIndex; i < reactedPolymer.length; i++) {
      const unit1 = reactedPolymer[i]
      const unit2 = reactedPolymer[i + 1]
      if (unit2 === undefined) {
        continue
      }
      if (unit1.toLowerCase() == unit2.toLowerCase() && unit1 !== unit2) {
        reactedPolymer.splice(i, 2)
        startIndex = i === 0 ? 0 : i - 1
        done = false
        break
      }
    }
    if (done) return reactedPolymer
  }
}

function shortestPolymerLength(polymer) {
  const unitsToReplace = new Set(polymer.toLowerCase())
  const shortest = [...unitsToReplace]
    .reduce((acc, unit) => {
      const re = new RegExp(`(${unit.toLowerCase()}|${unit.toUpperCase()})`, 'g')
      const newPolymer = polymer.replace(re, '')
      const length = fullyReactPolymer(newPolymer).length
      return length < acc ? length : acc
  }, Infinity)
  return shortest
}

const polymer = fs.readFileSync('day05-input.txt', 'utf8')
  .trim()
// pt 1
console.log(fullyReactPolymer(polymer).length)
// pt 2
console.log(shortestPolymerLength(polymer))
