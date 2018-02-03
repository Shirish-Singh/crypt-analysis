import { Injectable } from '@angular/core';
import {Http, Headers, RequestOptions} from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import { TweetModel } from '../model/tweetmodel';

@Injectable()
export class DataService {

  result: any;

  constructor(private _http: Http) { }

     getTweets(): Observable<TweetModel[]> {
      return this._http.get('/api/ts')
      .map(result => result.json());
  }

}
