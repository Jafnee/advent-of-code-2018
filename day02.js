const fs = require('fs')

const ids = fs.readFileSync('day02-input.txt', 'utf8')
  .trim()
  .split('\n')

// Array of obj {char: number of times found}
const occurrencesCounters = ids.map(id => {
  const asArray = id.split('')
  const charCount = asArray.reduce((counter, char) => {
    counter[char] = (counter[char] || 0) + 1
    return counter
  }, {})
  return charCount
})

const occurrencesValues = occurrencesCounters.map(Object.values)

const [doubleCount, tripleCount] = occurrencesValues.reduce(([double, triple], occurrences) => {
    if (occurrences.includes(2)) double += 1
    if (occurrences.includes(3)) triple += 1
    return [double, triple]
  }, [0, 0])
// pt 1
console.log(doubleCount * tripleCount)


const idsAndToCompare = ids.map((id, index) => {
  // Find what ids to compare this one against
  const idsToCompare = ids.slice(index + 1)
  return [id, idsToCompare]
})

for (let [id, idsToCompare] of idsAndToCompare) {
  for (otherId of idsToCompare) {
    // Get char diffs against current id
    const diff = otherId.split('').reduce((acc, char, i) => {
      if (char !== id[i]) acc.push(i)
      return acc
    }, [])

    if (diff.length === 1) {
      const diffIndex = diff[0]
      // pt 2
      // Rebuild string excluding the diff char
      console.log(id.slice(0, diffIndex) + id.slice(diffIndex + 1))
      break
    }
  }
}
