const file = document.querySelector("#id_image")

const srcFile = document.querySelector(".custom-file-label")
file.addEventListener('change', (res) => {
    let parseName = res.target.value.split("\\")
    srcFile.innerHTML = parseName[parseName.length - 1]
})