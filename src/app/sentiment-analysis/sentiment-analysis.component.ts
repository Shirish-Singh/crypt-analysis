import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { StreamData } from '../model/streamdata';
import { SentimentData } from '../model/SentimentData';

declare var sentiment: any;

@Component({
  selector: 'app-sentiment-analysis',
  templateUrl: './sentiment-analysis.component.html',
  styleUrls: ['./sentiment-analysis.component.css']
})

export class SentimentAnalysisComponent implements OnInit {


  // Define a users property to hold our user data
sentimentdatas: SentimentData[] = [];

  // Create an instance of the DataService through dependency injection
  constructor(private _dataService: DataService) {}
  interval: any;
  value: any;


  ngOnInit(): void {

    this.refreshData();
    this.interval = setInterval(() => {
      this.refreshData();
    }, 500);
  }

  refreshData() {
    this._dataService
      .getSentimentData()
      .subscribe(record => (this.sentimentdatas = record));
  }
}
