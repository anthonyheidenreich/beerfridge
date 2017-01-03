String.prototype.contains = function contains(match) { return this.indexOf(match) !== -1; }

AWS.config.region = 'us-west-2'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-west-2:43d6d9cb-2f64-4f07-bb19-d46554d40723',
});

var AUTH0_CLIENT_ID='1hqQ9GUYAdeni5J7g5FZFZgY0BBx9alp';
var AUTH0_DOMAIN='bieraustin.auth0.com';
var AUTH0_CALLBACK_URL=location.href;

function guid() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
}
