const express = require("express");
const router = express.Router();
const MongoClient = require("mongodb").MongoClient;
const ObjectID = require("mongodb").ObjectID;

const DB_URL = "mongodb://localhost:27017";
const DB_NAME = "analyticsDB";
const TWITTER_DB_COLLECTION_NAME = "twittersearch";
const TELEGRAM_DB_COLLECTION_NAME = "telegramData";
const SENTIMENT_DB_COLLECTION_NAME = "sentiments";
const TS_REST_CALL ='/ts';
const SENTIMENT_REST_CALL = '/sentiment';
const TELEGRAM_REST_CALL = '/telegram';

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
  MongoClient.connect(DB_URL,
    function(err, client) {
    if (err)  throw err;
    var db = client.db(DB_NAME);
    db
      .collection(TWITTER_DB_COLLECTION_NAME)
      .find({ "data.lang": "en" })
      .sort({ $natural: -1 })
      .limit(10)
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


router.get(SENTIMENT_REST_CALL, (req, res) => {
  MongoClient.connect(DB_URL,
    function(err, client) {
    if (err)  throw err;
    var db = client.db(DB_NAME);
    db
      .collection(SENTIMENT_DB_COLLECTION_NAME)
      .find()
      .sort({ $natural: -1 })
      .limit(10)
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

router.get(TELEGRAM_REST_CALL, (req, res) => {
  MongoClient.connect(DB_URL,
    function(err, client) {
    if (err)  throw err;
    var db = client.db(DB_NAME);
    db
      .collection(TELEGRAM_DB_COLLECTION_NAME)
      .find()
      .sort({ $natural: -1 })
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

