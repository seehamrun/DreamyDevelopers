function queryCharity(query, resultCallback) {
  var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f'
                  + '&app_key=' + app_key
                  + '&search=' + query
                  + '&rated=true'
  jQuery.get(charity_url, resultCallback)
}
// var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f&app_key=75f35a7eec548de064e93a2cdbf3d29d&search=' + query
// + '&rated=true'

//console.log(queryCharity())
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
//}
