// This is extremely slow to complete pt2.
// Will need to redo with a doubly linked list implementation for a
// significant speed up.

const assert = require('assert')
// JS mod operator is scuffed, doesn't do neg numbers.
const mod = (n, m) => ((n % m) + m) % m;

function pt1(players=7, lastMarble=25) {
    const marbles = [0]
    const scores = new Array(players).fill(0)
    let currMarbleIdx = 0

    for (let marble=1; marble<=lastMarble; marble++) {
        const currPlayerIdx = (marble) % players
        if (marble % 23 === 0) {
            const popIdx = mod(currMarbleIdx - 7, marbles.length)
            // Remove marble and add up score for turn
            const scoreEarned = marbles.splice(popIdx, 1)[0] + marble
            scores[currPlayerIdx] += scoreEarned

            // Marble to the right of popped is now current marble
            currMarbleIdx = popIdx
        } else {
            let insertIdx = (currMarbleIdx + 2) % marbles.length
            marbles.splice(insertIdx, 0, marble)
            currMarbleIdx = insertIdx
        }
    }
    return Math.max(...scores)
}

assert.strictEqual(pt1(7, 25), 32)
assert.strictEqual(pt1(10, 1618), 8317)
assert.strictEqual(pt1(13, 7999), 146373)
assert.strictEqual(pt1(17, 1104), 2764)
assert.strictEqual(pt1(30, 5807), 37305)

// pt1
console.log(pt1(419, 71052))
// pt2
console.log(pt1(419, 71052 * 100))
