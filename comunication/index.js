const express = require("express")
const { initializeApp } = require("firebase/app");
var { getDatabase , ref,set} = require("firebase/database");
var mysql = require("mysql2")

const con = mysql.createConnection({
    host:"bz25onz1elntysn5y0rs-mysql.services.clever-cloud.com",
    user:"ucgxb9levslhdtna",
    password:"K7bzNyIvNVQRaJj8lKkN",
    database:"bz25onz1elntysn5y0rs",
    port:3306

})

var app = express();
const firebaseConfig = {
    apiKey: "AIzaSyCogfVqOkLzUrkglBeCx_CiWKwwkBG7dDg",
    authDomain: "cosmonautica-98b85.firebaseapp.com",
    databaseURL: "https://cosmonautica-98b85-default-rtdb.firebaseio.com",
    projectId: "cosmonautica-98b85",
    storageBucket: "cosmonautica-98b85.firebasestorage.app",
    messagingSenderId: "459098178302",
    appId: "1:459098178302:web:c6f36e6975ea0912fc1baf",
    measurementId: "G-EKP3V8Q3XS"
  };
  const appli =  initializeApp(firebaseConfig);
  const database = getDatabase(appli);
  

app.get("/cosmos",(req,res) => {

    res.json({"message":req.url});
    

})

app.get("/temperature" , (req,res) => {
    var temp = req.query.temp;
    var hum = req.query.hum;
    con.connect(function(err){
        if(err) throw err;
        var sql = "UPDATE sensors set data = '" + temp+"-" + hum + "' WHERE name='temp';";
        con.query(sql,function(err,result){
            if(err) throw err;
            console.log("valor de sensor cambiado")
            res.json({"status":"ok"})
        })
    })

})

app.get("/getDataSensor" , (req,res) =>{
    con.connect(function(err){
        if(err) throw err;
        var sql = "SELECT * FROM sensors;";
        con.query(sql , function(err, result){
            if(err) throw err;
            console.log(result);
            res.send(result);
        })
    })
})

app.get("/putLoc" , (req,res) =>{
    var id = req.query.id;
    var loc = req.query.loc;
    con.connect(function(err){
        if(err) throw err;
        var sql = "UPDATE users set location = " + loc + " WHERE idPer = " + id + ";";
        con.query(sql , function(err,result){
            if(err) throw err;
            console.log("valor insertado");
            res.json({"id":"1"});;

        })
    })


})

app.get("/init" , (req,res) => {
    var ip = req.query.ip;
    set(ref(database , "url") , {
        url: ip
    })
    res.send("completado");

    

})

app.get("/new" , (req,res) => {
    var id = req.query.id
    console.log("han entrado");
    con.connect(function(err){
        if(err) throw err;
        var sql = "INSERT INTO users(location,data,idPer) VALUES('HREY','HET'," + id  + ");";
        con.query(sql , function(err , result){
            if(err) throw err;
            console.log("creado");
            res.json({"id":"1"});

        })
    })
})

app.get("/users" , (req,res) => {
    con.connect(function(err) {
        if(err) throw err;
        con.query("SELECT * FROM users" , function(err,result){
            console.log(result)
            res.send(result)
        })
    })
})

app.listen(8090 , (err) =>{
    if(err) console.log("error")
    console.log("iniciado");
})