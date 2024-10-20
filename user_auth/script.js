<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBpRLIeHMM2OR28LzcnYWM-c39so5-p6mU",
    authDomain: "train-8b14e.firebaseapp.com",
    projectId: "train-8b14e",
    storageBucket: "train-8b14e.appspot.com",
    messagingSenderId: "899832956534",
    appId: "1:899832956534:web:11a7deebc5990c2b0cc157",
    measurementId: "G-RZB0HTN4E4"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>