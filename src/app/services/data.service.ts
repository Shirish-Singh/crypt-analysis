import { TelegramStreamData } from './../model/telegramStreamData';
import { RouterConstants } from "./../../../server/routes/routerconstants";
import { Injectable } from "@angular/core";
import { Http, Headers, RequestOptions } from "@angular/http";
import "rxjs/add/operator/map";
import { Observable } from "rxjs/Observable";
import { StreamData } from "../model/streamdata";
import { SentimentData } from "../model/SentimentData";

@Injectable()
export class DataService {
  result: any;
  constructor(private _http: Http) {}

  /**
   * Get Tweets method
   */
  getTweets(): Observable<StreamData[]> {
    return this._http
      .get(RouterConstants.GET_RECORD_REST)
      .map(result => result.json());
  }

  /**
   * Get Tweets method
   */
  getSentimentData(): Observable<SentimentData[]> {
    return this._http
      .get(RouterConstants.GET_SENTIMENT_REST)
      .map(result => result.json());
  }

    /**
   * Get Tweets method
   */
  getTelegram(): Observable<TelegramStreamData[]> {
    return this._http.get(RouterConstants.GET_TELGERAM_REST)
    .map(result => result.json());
}
}
