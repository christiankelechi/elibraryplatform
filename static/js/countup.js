const displayValues = document.querySelectorAll(".counter-timer");
  let storage =  [];
  let startValue = 0;

  function readInterval(){
    for(let i = 0; i< displayValues.length; i++){
      let endvalue = displayValues[i].getAttribute("data-val");
      storage.push(startValue)
      //Check if value in the storage is same as in the display values
      if(storage[i] !== parseInt(endvalue)){
        storage[i]++;
      }
      displayValues[i].textContent = storage[i];
    }
  }


  // Count on Scroll
  let countUpContainer = document.querySelector(".countup-container");
  window.onscroll = function(){
   var timer = setInterval(()=>{
   let topElement =  countUpContainer.offsetTop;
   let bottomElement = countUpContainer.offsetTop + countUpContainer.clientHeight;
   let topScreen = window.pageYOffset;
   let bottomScreen =  window.pageYOffset + window.innerHeight;

   if(bottomScreen > topElement && topScreen < bottomElement ){
    readInterval();
   }
   else{
  //  Do something
   clearInterval(timer);
   for(let i= 0; i< displayValues.length; i++){
      displayValues[i].textContent = startValue;
      storage = []
    }
   }
  },100);

  }
