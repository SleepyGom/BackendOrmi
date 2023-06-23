<<<<<<< HEAD


// api 요청보내는 함수
const apiPost = async () => {
    const result = await fetch(url, {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
        redirect: "follow",
    })
    .then((res) => res.json())
    .then((res) => {
    printAnswer(res.choices[0].message.content);
    })
    .catch((err) => {
    console.log(err);
    });
};



// submit
$form.addEventListener("submit", (e) => {
    e.preventDefault();
    addData();
    addQuestion();
    sendQuestion(question);
    printQuestion();
    apiPost();
});
=======
// api 요청보내는 함수
const apiPost = async () => {
    const result = await fetch(url, {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
        redirect: "follow",
    })
    .then((res) => res.json())
    .then((res) => {
    printAnswer(res.choices[0].message.content);
    })
    .catch((err) => {
    console.log(err);
    });
};

// submit
$form.addEventListener("submit", (e) => {
    e.preventDefault();
    addData();
    addQuestion();
    sendQuestion(question);
    apiPost();
    // printQuestion();
});
>>>>>>> 90cbed311723ee62013ba46f8a49fb74a300916f
