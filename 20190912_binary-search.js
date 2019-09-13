// from Scratch to js
// const readline = require('readline');

const nameList = [
  'Alex',
  'Anzu',
  'Bianca',
  'Carlos',
  'Dan',
  'Daniel',
  'Diego',
  'Douglas',
  'Elen',
  'Gabriel',
  'Hotsuma',
  'Kam',
  'Mika',
  'Naoki',
  'Richard',
  'Rick',
  'Ryohei',
  'Shohei',
  'Tae',
  'Wenda',
  'Yuka',
  'Yuki',
  'Yusuke'
];

// 標準入力で検索
process.stdin.resume();
process.stdin.setEncoding('utf8');

var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', line => {
  // input_string = line;
  // console.log(line);
  if (nameList.includes(line)) {
    binarySearch(line);
    process.exit();
  } else {
    console.log(`${line} doesn't exist...`);
    process.exit();
  }
});
reader.on('close', () => {});

var binarySearch = function(x) {
  let steps = 0;
  let target = nameList.indexOf(x) + 1;
  let min = 1;
  let max = nameList.length;
  loop: while (min <= max) {
    guess = Math.round((min + max) / 2);
    ++steps;
    if (guess == target) {
      console.log(`Found it at ${nameList[guess - 1]}`);
      console.log(`It took ${steps} steps!`);
      break loop;
    } else {
      if (target < guess) {
        max = guess - 1;
      } else {
        min = guess + 1;
      }
    }
  }
};

// binarySearch(7);

// ループで全検索
// let i;
// for (i = 0; i < 23; i++) {
//   binarySearch(i);
// }

// 標準入力で検索
// binarySearch();
