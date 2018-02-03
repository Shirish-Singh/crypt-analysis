const express = require('express');
const router = express.Router();
const MongoClient = require('mongodb').MongoClient;
const ObjectID = require('mongodb').ObjectID;

// Connect
// const connection = (closure) => {
//     return MongoClient.connect('mongodb://localhost:27017/twitter', (err, db) => {
//         if (err) return console.log(err);

//         closure(db);
//     });
// };

// Error handling
const sendError = (err, res) => {
    response.status = 501;
    response.message = typeof err == 'object' ? err.message : err;
    res.status(501).json(response);
};

// Response handling
let response = {
    status: 200,
    data: [],
    message: null
};

// Get users
// router.get('/ts', (req, res) => {
//     connection((db) => {
//         db.collection('twittersearch')
//             .find()
//             .toArray()
//             .then((users) => {
//                 response.data = users;
//                 res.json(response);
//             })
//             .catch((err) => {
//                 sendError(err, res);
//             });
//     });
// });

router.get('/ts', (req, res) => {
MongoClient.connect('mongodb://localhost:27017', function (err, client) {
  if (err) throw err;

  var db = client.db('twitterdb');

  db.collection('twittersearch').find().toArray(function (findErr, result) {
    if (findErr) throw findErr;
    console.log(result);
    res.json(result);
    client.close();
  });
}); 
});

module.exports = router;