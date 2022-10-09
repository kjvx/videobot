
const url = 'https://randomuser.me/api/'

const x = new XMLHttpRequest()

x.onreadystatechange = () => {
    if (x.status === 200) {
        console.log('request ok')
    }
    //let json = JSON.parse(x.responseText)
    //console.log(json.results[0].name)
}


x.open('GET', url, true)

x.send()