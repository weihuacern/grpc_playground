var grpc = require('grpc');

var messages = require('../message/auth-user_pb.js');
var services = require('../message/auth-user_grpc_pb');

var port = 2021

function main() {
  var client = new services.AuthUserClient('localhost:'+port.toString(),
      grpc.credentials.createInsecure());

  console.log('-----CreateAuthUser-----')
  var request = new messages.CreateAuthUserRequest();
  client.createAuthUser(request, function(err, response) {
    console.log(response.getReply().getMsg());
  });

  console.log('-----ReadAuthUser-----')
  var request = new messages.ReadAuthUserRequest();
  client.readAuthUser(request, function(err, response) {
    console.log(response.getReply().getMsg());
  });

  console.log('-----UpdateAuthUser-----')
  var request = new messages.UpdateAuthUserRequest();
  client.updateAuthUser(request, function(err, response) {
    console.log(response.getReply().getMsg());
  });

  console.log('-----DeleteAuthUser-----')
  var request = new messages.DeleteAuthUserRequest();
  client.deleteAuthUser(request, function(err, response) {
    console.log(response.getReply().getMsg());
  });
}

main();
