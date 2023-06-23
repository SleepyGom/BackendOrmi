const $form = document.querySelector('form')

const bookPost = async () =>{
    const url = `https://dapi.kakao.com/v3/search/book?target=title&query=${answer.keyword}`
    
    //fetch(api주소, {header : Authorization : 'KaKaoAK restapikey'})
    const result = await fetch(url,{
        method : "GET",
        headers : {Authorization: "KakaoAK 6b3776a709af1d7c758d1c501b5399d4"},
    })
    .then((res) => {
        return res.json()
    })
    .then((res)=>{
        console.log(res)
        $form.innerHTML =  `
        <div>${res.documents[0].title}</div>
        <div><img src ="${res.documents[0].thumbnail}"/></div>
        `
    })
    .catch((err) => {
        console.log(err)
    })
};


$form.addEventListener("submit", (e) =>{
    e.preventDefault()
    bookPost();
})
