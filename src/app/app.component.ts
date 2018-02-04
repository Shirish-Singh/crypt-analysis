import { Component, OnInit } from '@angular/core';
// Import the DataService
import { DataService } from './services/data.service';
import { StreamData } from './model/streamdata';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
// Define a users property to hold our user data
streamdatas: StreamData[] = [];
// Create an instance of the DataService through dependency injection
constructor(private _dataService: DataService) {}

interval: any;

  ngOnInit(): void {
    this.refreshData();
    this.interval = setInterval(() => {
        this.refreshData();
    }, 500);

  }

  refreshData() {
    this._dataService.getTweets().subscribe(record => this.streamdatas = record);
  }
}


  // Access the Data Service's getUsers() method we defined
  // this._dataService.getTweets()
  //     .subscribe(res => this.tweets = res);
