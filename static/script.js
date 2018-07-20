var api_key = "75f35a7eec548de064e93a2cdbf3d29d"


function queryCharity(query, resultCallback) {
  var charity_url = "https://api.data.charitynavigator.org/v2"
                  + "api_key=" + api_key
                  + "&q=" + query
                  + "&limit=" + 1
  jQuery.get(charity_url, resultCallback)
}

console.log(queryCharity("hunger"))


// Application ID
// This is the application ID, like a login ID for your application. You should send with each API request.
// Value: 71c6533f


  // somehow reformat this so it corresponds with the charity navigator api
  // jQuery.get(giphy_url, resultCallback)
}
