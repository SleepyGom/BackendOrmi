
const $form = document.querySelector("form");
const $input = document.querySelector("input");
const $chatList = document.querySelector("ul");
const $radioData = document.querySelectorAll(".data")



// openAI API
let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;


// 사용자의 질문
let personalData = [];

function addData(){
    for(let i of $radioData){
        if(i.checked || i.name === 'textData'){
            personalData.push(i.value)
        }
    }
    
}

let question;

function addQuestion(){
    question = `${personalData[2]} ${personalData[0]}${personalData[1] === "" ? '':' '}${personalData[1]}${personalData[1] === "" ?'가':'이'} 읽기 좋은 책 제목 5가지 정도를 json형태로 추천해줘`
    
}

// 질문과 답변 저장
let data = [
    {
        role: "system",
        content: "assistant는 유능한 책 마스터이다.",
    },{
        role: "user",
        content : `운동을 좋아합니다. 20대 남성의 맞는 책을 추천해줘 json 형태로 답변을 줘 내가 원하는 형태는 [{
            answer :'운동을 좋아하는 20대 남성에게 추천 할 책은 '즐겁게 운동해야지' 입니다.',
            keyword : '즐겁게 운동해야지',
        }] 이야`,
    },{
        role: "assistant",
        content:`[{
            answer : '운동을 좋아하는 20대 남성에게 추천 할 책은 '즐겁게 운동해야지' 입니다.',
            keyword : '즐겁게 운동해야지',
        }]`,
    }
];


// 화면에 뿌려줄 데이터, 질문들
let questionData = [];

// input에 입력된 질문 받아오는 함수
// $input.addEventListener("input", (e) => {
//     question = e.target.value;
// });

// 사용자의 질문을 객체를 만들어서 push
const sendQuestion = (question) => {
    if (question) {
        data.push({
        role: "user",
        content: question,
        });
        questionData.push({
        role: "user",
        content: question,
        });
    }

};

// 화면에 질문 그려주는 함수
const printQuestion = async () => {
if (question) {
    let li = document.createElement("li");
    li.classList.add("question");
    questionData.map((el) => {
    li.innerText = el.content;
    });
    $form.innerHTML = ''
    $form.appendChild(li);
    questionData = [];
    question = false;
}
};


let answerJson ;
// 화면에 답변 그려주는 함수
const printAnswer = (answer) => {
    answerJson = JSON.parse(answer);
    let div = document.createElement("div");
    $form.innerHTML = ''
    div.classList.add(`answer`);
    if(answerJson.length < 5){
        console.log('한번더')
        sendQuestion(question);
        apiPost();
        }
    else{
        for(let i = 0; i < answerJson.length; i++){        
            $form.appendChild(div);      
            div.innerHTML += `<p class="bookinfo">${answerJson[i].answer}</p>
            <br/>
            <p>${answerJson[i].keyword}</p>`;
        }
        console.log('5가지 나옴')
    }
    console.log(answerJson)
};





