import "dart:io";


Map<String, int> countChars(String string) {
  final Map<String, int> count = string
    .split('')
    .fold({}, (acc, letter) {
      acc[letter] = (acc[letter] ?? 0) + 1;
      return acc;
    });
  return count;
}

int pt1(Iterable<String> ids) {
  var double = 0;
  var triple = 0;

  for (var id in ids) {
    final charCount = countChars(id);
    if (charCount.values.contains(2)) {
      double++;
    }
    if (charCount.values.contains(3)) {
      triple++;
    }
  }
  return double * triple;
}

List<int> stringDiffs(String s1, s2) {
  List<int> diffs = [];
  for (var i=0; i < s1.length; i++) {
    var char1 = s1[i];
    var char2 = s2[i];
    if (char1 != char2) {
      diffs.add(i);
    }
  }
  return diffs;
}

String pt2(Iterable<String> ids) {
  for (var i=0; i < ids.length; i++) {
    var id = ids.elementAt(i);
    var idsToCompare = ids.toList().sublist(i + 1);
    for (var otherId in idsToCompare) {
      var diffs = stringDiffs(id, otherId);
      if (diffs.length == 1) {
        var diffIndex = diffs[0];
        return id.substring(0, diffIndex) + id.substring(diffIndex + 1);
      }
    }
  }
  return "Uh oh, something went wrong";
}

main() async {
  final ids = await File('day02-input.txt').readAsLines();
  // pt 1
  print(pt1(ids));
  // pt 2
  print(pt2(ids));
}
