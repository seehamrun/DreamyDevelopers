function charityDetails(ein, resultCallback) {
  var details_url = 'https://api.data.charitynavigator.org/v2/Organizations/'
                  + ein
                  + '?app_id=71c6533f'
                  + '&app_key=' + charity_api_key
  jQuery.get(details_url, resultCallback)
}

var currentFavorite = null;

function charityNews(charity, resultCallback) {
  var news_url = 'https://newsapi.org/v2/everything?'
          + 'q=' + charity
          + '&sortBy=relevancy'
          + '&apiKey=' + news_api_key
  jQuery.get(news_url, resultCallback)
}

charityDetails(einLookup, function(data) {
  var name = document.querySelector('#charityName')
  name.innerHTML = data.charityName
  var deductibility = document.querySelector('#deductibility')
  deductibility.innerHTML = data.irsClassification.deductibility
  var website = document.querySelector('#website')
  website.innerHTML = data.websiteURL
  website.href = data.websiteURL
  var cause = document.querySelector('#cause')
  cause.innerHTML = data.mission

  var charName = document.querySelector('#charName')
  charName.value = data.charityName
  var charWebsite = document.querySelector('#charWebsite')
  charWebsite.value = data.websiteURL
  var charDeduct = document.querySelector('#charDeductibility')
  charDeduct.value = data.irsClassification.deductibility

  charityNews(data.charityName, function(data) {
    console.log(data)
    var articles = data.articles
    var div = ""
    for (var i = 0; i < articles.length; i++){
      var resultTitle = "<h3>" + articles[i].title + "</h3>"
      var resultDate = "<h5>" + articles[i].publishedAt.slice(0, 10) + "</h5>"
      var resultDescription = "<p>" + articles[i].description + "</p>"
      div = div + "<article>" + resultTitle + resultDate + resultDescription + "</article>"
    }
    var charityArticle = document.querySelector('#charityArticle')
    charityArticle.innerHTML = div
  })
})

function addCharityToFavorites(currentFavorite, doneCallback) {
  console.log("clicked too")
}

function addFavoriteClick() {
  console.log("clicked")
  addCharityToFavorites(currentFavorite, () => {
    alert("Saved!")
  })
}

window.addEventListener('load', () => {
  document.querySelector('#favorite').addEventListener('click', addFavoriteClick)
});
