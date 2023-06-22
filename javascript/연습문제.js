// 첫번째 문제
let first_q = [10, 20, 30, 10, 20, 30, 40, 10]
let avr_f = first_q.reduce((a,b) => a + b)/first_q.length
let answer1 = []
for(let i =0; i < first_q.length ; i++){
    answer1.push(first_q[i] - avr_f)**2
}

//avr_f = 21.25
//answer1 =[-11.25, -1.25, 8.75, -11.25, -1.25, 8.75, 18.75, -11.25]
// 두번쨰 문제
let sec_q = '5, 4, 10, 2, 5'
let sec_q_s = sec_q.split(',')
let answer = 0
for(let i = 0; i < sec_q.length; i++){
    answer += parseInt(sec_q_s)
}
answer / sec_q_s.length // 14

// 세번째
let tq = [11, 22, 33, 111, 2];
console.log(tq.join('').reduce((a,b) => a+b))