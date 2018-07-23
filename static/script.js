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

queryCharity("hunger", function(data) {
  var resultstr = "";

  for (var i = 0; i < data.length; i++){
    missionStatement = data[i].mission
    charityName = data[i].charityName
    irsClassification = data[i].irsClassification
    console.log(missionStatement)
    console.log(charityName)
    console.log(irsClassification)
    resultstr = resultstr + "<p>'" + missionStatement + ' ' + charityName + ' ' + irsClassification + "'</p>"

  }

  var resultDiv = document.querySelector('#result')
  resultDiv.innerHTML = resultstr
});
