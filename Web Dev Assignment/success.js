window.onload = () => {
  const queryParams = new URLSearchParams(window.location.search);
  const last4 = queryParams.get("last4");


  if (last4) {
    document.getElementById("Last4digit").innerHTML = `Your credit card ends in **** **** **** ${last4}`;
  }
  // if last 4 values exist, then output message
};

