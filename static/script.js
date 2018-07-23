function queryCharity(query, resultCallback) {
  var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f'
                  + '&app_key=' + api_key
                  + '&search=' + query
                  + '&rated=true'
  jQuery.get(charity_url, resultCallback)
}


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

  var resultDiv = document.querySelector('#result')
  resultDiv.innerHTML = div
});
