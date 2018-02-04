const express = require("express");
const router = express.Router();
const MongoClient = require("mongodb").MongoClient;
const ObjectID = require("mongodb").ObjectID;

const DB_URL = "mongodb://localhost:27017";
const DB_NAME = "twitterdb";
const DB_COLLECTION_NAME = "twittersearch";
const TS_REST_CALL = "/ts";

const sendError = (err, res) => {
  response.status = 501;
  response.message = typeof err == "object" ? err.message : err;
  res.status(501).json(response);
};

// Response handling
let response = {
  status: 200,
  data: [],
  message: null
};

router.get(TS_REST_CALL, (req, res) => {
  MongoClient.connect(DB_URL, function(err, client) {
    if (err) throw err;

    var db = client.db(DB_NAME);

    db
      .collection(DB_COLLECTION_NAME)
      .find({ "data.lang": "en" })
      .sort({ $natural: -1 })
      .limit(5)
      .toArray(function(findErr, result) {
        if (findErr) {
          console.log("Please check your db connection.");
          throw findErr;
        }
        console.log(result);
        res.json(result);
        //    client.close();
      });
  });
});

module.exports = router;

// Connect
// const connection = (closure) => {
//     return MongoClient.connect('mongodb://localhost:27017/twitter', (err, db) => {
//         if (err) return console.log(err);

//         closure(db);
//     });
// };

// Error handling

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
