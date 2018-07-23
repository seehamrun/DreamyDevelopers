function queryCharity(query, resultCallback) {
  var charity_url = 'https://api.data.charitynavigator.org/v2/Organizations?app_id=71c6533f'
                  + '&app_key=' + app_key
                  + '&search=' + query
                  + '&rated=true'
  jQuery.get(charity_url, resultCallback)
}
var missionStatement = ""
var charityName = ""
var irsClassification = ""

queryCharity("hunger", function(data) {
  console.log(data);
  console.log('hey hi hello')
});
