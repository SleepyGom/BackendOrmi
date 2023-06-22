const btn = document.createElement('button')
btn.innerText = '눌럿!'
const body = document.querySelector("body")
body.append(btn)

btn.addEventListener('click', (event) => {
    console.log(event);
});