const express = require('express')
const axios = require('axios')
const app = express()

app.use(express.static('static'))
app.use(express.json())
app.use(express.urlencoded({extended:true}))


app.post('/result',async (req,res)=>{
    // console.log(req.body)
    try{
        console.log(req.body)
        let mood = req.body.mood
        let number = req.body.number
        link = `http://localhost:5000/result?mood=${mood}&number=${number}`
        let data = await axios.get(link)
        data = data.data;
        console.log(data)
        res.send(data)
    }
    catch(e){
        // console.log(e)
        res.send(e)
    }
})


app.listen(8080)