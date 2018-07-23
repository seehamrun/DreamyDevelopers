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

queryCharity("homeless", function(data) {
  var resultstr = "";
  var div = ""
  for (var i = 0; i < data.length; i++){
    missionStatement = data[i].mission
    charityName = data[i].charityName
    irsClassification = data[i].irsClassification
    console.log(missionStatement)
    console.log(charityName)
    console.log(irsClassification)
    //resultstr = resultstr + "<p>'" + missionStatement + ' ' + charityName + ' ' + irsClassification + "'</p>"
    var resultName = "<h1>" + charityName + "</h1>"
    var resultMission = "<p>" + missionStatement + "</p>"
    var resultClassification = "<p>" + irsClassification + "</p>"
    div = div + "<div>" + resultName + resultMission + resultClassification + "</div>"
  }

  var resultDiv = document.querySelector('#result')
  resultDiv.innerHTML = div
});
