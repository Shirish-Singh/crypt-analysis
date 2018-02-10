import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { StreamData } from '../model/streamdata';

@Component({
  selector: 'app-realtime-tweeter',
  templateUrl: './realtime-tweeter.component.html',
  styleUrls: ['./realtime-tweeter.component.css']
})
export class RealtimeTweeterComponent implements OnInit {

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
    this._dataService
      .getTweets()
      .subscribe(record => (this.streamdatas = record));
  }
}
