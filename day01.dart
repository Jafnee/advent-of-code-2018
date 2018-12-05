import 'dart:io';

int sumFrequencies(Iterable<int> frequencies) {
  return frequencies.reduce((acc, f) => acc + f);
}

cycle(Iterable list) sync* {
  while (true) {
    yield* list;
  }
}

int repeatingFrequency(Iterable<int> frequencies) {
  final occured = Set.from([0]);
  var sum = 0;
  for (var freq in cycle(frequencies)) {
    sum += freq;
    if (!occured.add(sum)) {
      return sum;
    }
  }
}

main() async {
  final String contents = await new File('day01-input.txt').readAsString();
  final Iterable<int> frequencies =  contents
    .trim()
    .split("\n")
    .map((f) => int.parse(f));
  // pt 1
  print(sumFrequencies(frequencies));
  // pt 2
  print(repeatingFrequency(frequencies));
}
