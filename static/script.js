function queryCharity(query, resultCallback) {
  var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f'
                  + '&app_key=' + charity_api_key
                  + '&search=' + query
                  + '&rated=true'
  jQuery.get(charity_url, resultCallback)
}

function submitClick() {
  var loader = document.querySelector('.sk-cube-grid')
  loader.style.display = 'block'
  var inputBox = document.querySelector('#queryBox')
  var resultPane = document.querySelector('#resultPane')
  resultPane.style.display = 'none'
  var userInput = inputBox.value
  if (userInput == '') {
    loader.style.display = 'none'
    resultPane.style.display = 'block'
    return
  }
  else if (userInput != '') {
    queryCharity(userInput, function(data) {
      var div = ""
      for (var i = 0; i < data.length; i++){
        var name = data[i].charityName
        var resultName = "<h1><a href='/details?charity=" + data[i].ein + "'>" + name + "</a></h1>"
        var resultMission = "<p>" + data[i].mission + "</p>"
        var resultClassification = "<p>" + data[i].irsClassification.deductibility + "</p>"
        div = div + "<div>" + resultName + resultMission + resultClassification + "</div>"
      }
      var resultDiv = document.querySelector('#result')
      resultDiv.innerHTML = div
      loader.style.display = 'none'
      resultPane.style.display = 'block'
    })
  }
}

window.addEventListener('load', () => {
  document.querySelector('#submit').addEventListener("click", submitClick)
  document.querySelector('#queryBox').addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode
    if (e.keyCode === 13) {
      submitClick()
    }
  });
});
