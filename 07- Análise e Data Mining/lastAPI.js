var api_key = "bd5fbf6ee62822e70562d977b0016c1b";

var root_url = "https://ws.audioscrobbler.com"
var get_user_info_url = "/2.0/?method=user.getinfo&format=json";
var user_attr = "&user=";
var get_top_artists_url = "/2.0/?method=user.gettopartists&format=json"; 
var api_attr = "&api_key=" + api_key;
var attr_1 = "&period=7day";
var TWEET_SIZE = 280;
var tweet;

function getTopArtists() {
    if($("#last-nickname")) {
        user_url = user_attr + $("#last-nickname").val();
        var get_top_artists = root_url + get_top_artists_url + user_url + api_attr + attr_1;

        $.get(get_top_artists, function(data, status) {
            prepareTweet(data);
        });

    } else {
        console.log("nao deu");
    }
        
} 

function prepareTweet(data) {

    var nick_name = "";
    var user_url = user_attr + $("#last-nickname").val();
    $.get(root_url + get_user_info_url + user_url + api_attr, function(user_data, status) {
        nick_name = user_data.user.name;
        var i = 0;
        tweet_header_begin = nick_name + "'s top ";
        tweet_header_end = "artists this week: ";
        tweet = tweet_header_begin + tweet_header_end;
        var artist = data.topartists.artist[i].name.toString() + "(" + data.topartists.artist[i].playcount.toString() + ")";

        while(tweet.length + artist.length < TWEET_SIZE ) {
            tweet = tweet + artist;
            i++;
            artist = ", " + data.topartists.artist[i].name.toString() + "(" + data.topartists.artist[i].playcount.toString() + ")";
        }
        $("#fill-response").text(tweet);
        $("#tweet").text(tweet);
        console.log("Tweet: " + tweet + " size: " + tweet.length);
    });

};