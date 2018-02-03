import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
//import { TweetListComponent } from './tweet-list/tweet-list.component';
import { HttpModule }  from '@angular/http';
import {DataService} from './services/data.service';


@NgModule({
  declarations: [
    AppComponent
  //  TweetListComponent
    
  ],
  imports: [
    BrowserModule,
    HttpModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule {

  tweets: Array<any>;
  constructor(private _dataService: DataService){
    this._dataService.getTweets()
    .subscribe(res => this.tweets = res);
  }

 }
