import { initializeApp } from "firebase/app";
import { getMessaging, getToken } from "firebase/messaging";


const firebaseConfig = {
  apiKey: "AIzaSyDBKPQAdMr1RrRyxGC6p1Zfb4aS8ZrJipo",
  authDomain: "central-backend-socials.firebaseapp.com",
  projectId: "central-backend-socials",
  storageBucket: "central-backend-socials.appspot.com",
  messagingSenderId: "635620493547",
  appId: "1:635620493547:web:809da75576131ed99e96ae"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = getMessaging(app);
messaging.requestPermission().then(function() {
  return messaging.getToken();
}).then(function(token) {
  console.log(token);
}).catch(function(err) {
  console.log("Denied", err);
});

messaging.onMessage(function(payload) {
  console.log('onMessage: ', payload);
});


