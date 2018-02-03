import { Component, OnInit } from '@angular/core';
// Import the DataService
import { DataService } from './services/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
// Define a users property to hold our user data
tweets: Array<any>;

// Create an instance of the DataService through dependency injection
constructor(private _dataService: DataService) {
  // Access the Data Service's getUsers() method we defined
  // this._dataService.getTweets()
  //     .subscribe(res => this.tweets = res);
  }

  interval: any;

  ngOnInit(): void {
    this.refreshData();
    this.interval = setInterval(() => {
        this.refreshData();
    }, 500);

  }

  refreshData() {
    this._dataService.getTweets().subscribe(record => this.tweets = record);
  }
}
