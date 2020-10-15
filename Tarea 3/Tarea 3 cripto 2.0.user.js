// ==UserScript==
// @name         Tarea 3 cripto 2.0
// @namespace    http://tampermonkey.net/
// @version      2
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/Elizabeth/Desktop/a.html
// @require      http://run.plnkr.co/preview/ckg7awg8p00083a66fh66emzi/blowfish.js
// @grant        none
// ==/UserScript==


(function() {
    'use strict';
   var a = document.getElementsByClassName("Blowfish")[0].getAttribute("id");
   var key = document.getElementsByClassName("key")[0].getAttribute("id")
   var bf = new Blowfish(key, "cbc");
   var xd = bf.base64Decode(a)
   var iv = document.getElementsByClassName("iv")[0].getAttribute("id")
   var decrypted = bf.decrypt(xd , iv);
   document.getElementsByClassName("Blowfish")[0].innerText = decrypted;

})();