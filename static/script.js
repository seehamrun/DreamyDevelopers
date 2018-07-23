function queryCharity(query, resultCallback) {
  var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f'
                  + '&app_key=' + api_key
                  + '&search=' + query
                  + '&rated=true'
  jQuery.get(charity_url, resultCallback)
}
var missionStatement = ""
var charityName = ""
var irsClassification = ""

function submitClick() {
  var inputBox = document.querySelector('#searchBar')
  var userInput = inputBox.value
  queryCharity("hunger", function(data) {
    console.log(data);
    console.log('hey hi hello');
  });
}







  // document.querySelector('#submit').addEventListener("click", submitClick);
