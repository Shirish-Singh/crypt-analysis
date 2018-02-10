import { RouterConstants } from './../../../server/routes/routerconstants';
import { Injectable } from '@angular/core';
import {Http, Headers, RequestOptions} from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import { StreamData } from '../model/streamdata';

@Injectable()
export class DataService {

  result: any;
  constructor(private _http: Http) { }

  /**
   * Get Tweets method
   */
  getTweets(): Observable<StreamData[]> {
      return this._http.get(RouterConstants.GET_RECORD_REST)
      .map(result => result.json());
  }
}
