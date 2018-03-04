import { TelegramStreamData } from './../model/TelegramStreamData';
import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-telegram',
  templateUrl: './telegram.component.html',
  styleUrls: ['./telegram.component.css']
})
export class TelegramComponent implements OnInit {

  // Define a users property to hold our user data
  streamdatas: TelegramStreamData[] = [];

  // Create an instance of the DataService through dependency injection
  constructor(private _dataService: DataService) {
  }

  interval: any;

  ngOnInit(): void {
    this.refreshData();
    this.interval = setInterval(() => {
      this.refreshData();
    }, 10);
  }

  refreshData() {
    this._dataService
      .getTelegram()
      .subscribe(record => (this.streamdatas = record));
      }

}
