window.onload = () => {
  document.getElementById("ContinueButton").addEventListener("click", (e) => {
    e.preventDefault(); 

    let CardNumber = document.getElementById("CardNumber").value;
    let ExpirationDateYear = document.getElementById("ExpirationDateYear").value;
    let ExpirationDateMonth = document.getElementById("ExpirationDateMonth").value;
    let SecurityCode = document.getElementById("SecurityCode").value;

    



if (
  !CardNumber || 
  !ExpirationDateYear || 
  !ExpirationDateMonth || 
  !SecurityCode
) {
  alert("Please fill in all fields.");
  return;
}

const pattern = /^5[1-5]/;
if (CardNumber.match(pattern)) {
} else {
  alert("Card number must start with 51, 52, 53, 54, or 55.");
}

if (CardNumber.length < 16) {
  alert("Card number must be 16 digits.");
  return;
}

const TodayDate = new Date();
const TodayYear = TodayDate.getFullYear();
const TodayMonth = TodayDate.getMonth() +1;

if (parseInt(ExpirationDateYear) < TodayYear || (parseInt(ExpirationDateYear) === TodayYear && parseInt(ExpirationDateMonth) < TodayMonth)){
    alert("It looks like your credit card is expired ")
    return
}

if (SecurityCode.length < 3 || SecurityCode.length > 4) {
  alert("CVV code must be 3 or 4 digits.");
  return;
}


    const url = "https://mudfoot.doc.stu.mmu.ac.uk/node/api/creditcard";
    const data = {
      "master_card": parseInt(CardNumber),
      "exp_year": parseInt(ExpirationDateYear),
      "exp_month": parseInt(ExpirationDateMonth),
      "cvv_code": SecurityCode,
};


    fetch(url, {
      method: "post",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      } else if (response.status === 400) {
        throw "Bad data was sent to the server";
      } else {
        throw "Something went wrong";
      }
    })
    .then((resJson) => {
      alert(resJson["message"]);
      const last4 = CardNumber.slice(-4);
      window.location.href = `success.html?last4=${last4}`;
    })
    .catch((error) => {
      alert(error);
    });
  });
};
