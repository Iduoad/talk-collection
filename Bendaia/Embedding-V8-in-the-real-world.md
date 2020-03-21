---
title: Embedding V8 in the real world
description: challenges the NativeScript team met embedding V8 in a mobile framework 
type: talk
speaker: Stanimira Vlaeva
source: https://www.youtube.com/watch?v=wz7Znu6tqFw
tags : ['V8','NativeScript','JavaScript']
---
- NativeScript is a framework for building native iOS and android apps using web technologies 
- NativeScript supports angular and Vue.Js
- NativeScript has metadata generator:it gets informations from native library so we can use them in Js
- Java native interface is a bridge between V8 and android runtime 
- Marshalling handles the conversion between JavaScript and Java datatypes
- We do not convert object , we create a java object and a Js proxy 
- Challenges : We should synchronize garpage collector in Java and V8 

