function queryCharity(query, resultCallback) {
  var charity_url = "http://api.charitynavigator.org/api/v1/search/?app_key=APP_KEY&app_id=APP_ID&field=value"
                  + "api_key=" + api_key
                  + "&q=" + query
                  + "&limit=" + 1
  jQuery.get(charity_url, resultCallback)
}

console.log(queryCharity("hunger"))
console.log('hey hi hello')


// Application ID
// This is the application ID, like a login ID for your application. You should send with each API request.
// Value: 71c6533f


// function queryCharity(query, resultCallback) {
//   var charity_url = "http://api.giphy.com/v1/gifs/search?"
//                   + "api_key=" + api_key
//                   + "&q=" + query
//                   + "&limit=" + 1

  // somehow reformat this so it corresponds with the charity navigator api
  // jQuery.get(giphy_url, resultCallback)
}
