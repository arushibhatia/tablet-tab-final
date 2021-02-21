
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyDFmMqDWXrnXSNgPKiKAeHcxV_nXQ5840I",
    authDomain: "tablet-tab.firebaseapp.com",
    projectId: "tablet-tab",
    storageBucket: "tablet-tab.appspot.com",
    messagingSenderId: "523003992278",
    appId: "1:523003992278:web:87af6f240ca90b09dc1177"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  const auth = firebase.auth();

  function signUp(){
    var email = document.getElementById('email');
    var password = document.getElementById('password');

    firebase.auth().createUserWithEmailAndPassword(email.value, password.value)
  .then((userCredential) => {
    // Signed in 
    var user = userCredential.user;
    alert("You have been signed up!");
    // ...
  })
  .catch((error) => {
    alert(error.code);
    var errorCode = error.code;
    var errorMessage = error.message;
    
  });


  }

  function signIn(){
    var email = document.getElementById('email');
    var password = document.getElementById('password');

    // const promise = auth.signInWithEmailAndPassword(email.value, password.value);
    // promise.catch(e=>alert(e.message));

    var authFlag = true;


    firebase.auth().signInWithEmailAndPassword(email.value, password.value)
          .then((userCredential) => {
      // Signed in
      // alert("Signed In");
        var user = userCredential.user;
        window.location.replace('index2.html');
  
    })
    .catch((error) => {
      alert(error.code);
      var errorCode = error.code;
      var errorMessage = error.message;
    });



  }; 