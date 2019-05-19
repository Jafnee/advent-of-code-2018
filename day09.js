const assert = require('assert')
// JS mod operator is scuffed, doesn't do neg numbers.
const mod = (n, m) => ((n % m) + m) % m;


class Node {
    // Doubly Linked List Node
    next = null
    prev = null

    constructor(value) {
        this.value = value
    }
}


class Deque {
    // Inspired by Python's collections.deque
    currentNode = null

    constructor(vals=[]) {
        const {length} = vals
        const nodes = vals.map(val => new Node(val))
        nodes.forEach((node, i)=> {
            // First one
            if (!this.currentNode) {
                this.currentNode = node.next = node.prev = node
                return
            }
            node.prev = this.currentNode

            this.currentNode.next = node
            this.currentNode = node
        })
        // Circle it around
        this.currentNode.next = nodes[0]
    }

    append(val) {
        const newNode = new Node(val)
        newNode.prev = this.currentNode
        newNode.next = this.currentNode.next
        this.currentNode.next.prev = newNode
        this.currentNode.next = newNode
        this.currentNode = newNode
    }

    pop() {
        this.currentNode.next.prev = this.currentNode.prev
        this.currentNode.prev.next = this.currentNode.next
        const popped = this.currentNode.value
        this.currentNode = this.currentNode.prev
        return popped
    }

    rotate(n) {
        // Rotate forwards for positive numbers, backwards for negative.
        const prop = n < 0 ? 'next' : 'prev'
        for (let i = 0; i < Math.abs(n); i++) {
            this.currentNode = this.currentNode[prop]
        }
    }

    // Useful for visualizing
    toArray() {
        let next = this.currentNode.next
        const ret = []
        do {
            ret.push(next.value)
            next = next.next
        } while (next !== this.currentNode.next)
        return ret
    }
}

function pt1(players, lastMarble) {
    const marbles =  new Deque([0])
    const scores = new Array(players).fill(0)

    for (let marble=1; marble<=lastMarble; marble++) {
        const currPlayerIdx = (marble) % players
        if (marble % 23 === 0) {
            marbles.rotate(-7)
            scores[currPlayerIdx] += marble + marbles.pop()
        } else {
            marbles.rotate(2)
            marbles.append(marble)
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
