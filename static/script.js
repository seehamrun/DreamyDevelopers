function queryCharity(query, resultCallback) {
  var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f'
                  + '&app_key=' + charity_api_key
                  + '&search=' + query
                  + '&rated=true'
  jQuery.get(charity_url, resultCallback)
}

<<<<<<< HEAD
var name = ''

function submitClick() {
  var inputBox = document.querySelector('#queryBox')
  var userInput = inputBox.value
  queryCharity(userInput, function(data) {
    //var resultstr = "";
    var div = ""
    for (var i = 0; i < data.length; i++){
      // console.log(data[i].mission)
      // console.log(data[i].charityName)
      // console.log(data[i].irsClassification.deductibility)

      //resultstr = resultstr + "<p>'" + missionStatement + ' ' + charityName + ' ' + irsClassification + "'</p>"
      name = data[i].charityName
      var resultName = "<h1>" + name + "</h1>"
      var resultMission = "<p>" + data[i].mission + "</p>"
      var resultClassification = "<p>" + data[i].irsClassification.deductibility + "</p>"
      div = div + "<div>" + resultName + resultMission + resultClassification + "</div>"
    }
=======
>>>>>>> 21fa4c6ed6e1e5feea857c0a7d926eadf3bbffab

queryCharity("autism", function(data) {
  var resultstr = "";
  var div = ""
  for (var i = 0; i < data.length; i++){
    console.log(data[i].mission)
    console.log(data[i].charityName)
    console.log(data[i].irsClassification.deductibility)
    //resultstr = resultstr + "<p>'" + missionStatement + ' ' + charityName + ' ' + irsClassification + "'</p>"
    var resultName = "<h1>" + data[i].charityName + "</h1>"
    var resultMission = "<p>" + data[i].mission + "</p>"
    var resultClassification = "<p>" + data[i].irsClassification.deductibility + "</p>"
    div = div + "<div>" + resultName + resultMission + resultClassification + "</div>"
  }

<<<<<<< HEAD
function charityNews(charity, resultCallback) {
  var news_url = 'https://newsapi.org/v2/everything?'
          + 'q=' + charity
          + '&sortBy=popularity'
          + 'apiKey=' + news_api_key
}

console.log(charityNews("Rise Against Hunger"))

window.addEventListener('load', () => {
  document.querySelector('#submit').addEventListener("click", submitClick)
=======
  var resultDiv = document.querySelector('#result')
  resultDiv.innerHTML = div
>>>>>>> 21fa4c6ed6e1e5feea857c0a7d926eadf3bbffab
});
