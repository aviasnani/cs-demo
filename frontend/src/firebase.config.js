// src/firebase-config.js
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider } from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyDTTJBG7lfFdaHBdYic9wLB1QsEsRzg7e4",
  authDomain: "loginapp-8b299.firebaseapp.com",
  projectId: "loginapp-8b299",
  storageBucket: "loginapp-8b299.firebasestorage.app",
  messagingSenderId: "860107315304",
  appId: "1:860107315304:web:5f9eaf7d14d689fa7dc3dd",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export { auth, provider };


