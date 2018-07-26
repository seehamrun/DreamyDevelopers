function validateForm(){
  var charity = document.querySelector('[name="charityName"]').value;
  var amountDonated = document.querySelector('[name="amountDonated"]').value;
  var dateDontaed = document.querySelector('[name="dateDonated"]').value;
  if (charity == "" || amountDonated == "" || dateDonated == "") {
    alert("Please enter something into the fields below!")
    return false
  }
  else {
    return true
  }
}
