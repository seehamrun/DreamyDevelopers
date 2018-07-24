function charityDetails(ein, resultCallback) {
  var details_url = 'https://api.data.charitynavigator.org/v2/Organizations/'
                  + ein
                  + '?app_id=71c6533f'
                  + '&app_key=' + charity_api_key
  jQuery.get(details_url, resultCallback)
}


charityDetails(einLookup, function(data) {
  console.log(data)
  var name = document.querySelector('#charityName')
  name.innerHTML = data.charityName
  var deductibility = document.querySelector('#deductibility')
  deductibility.innerHTML = data.irsClassification.deductibility
  var website = document.querySelector('#website')
  website.innerHTML = data.websiteURL
  var cause = document.querySelector('#cause')
  cause.innerHTML = data.mission
})
