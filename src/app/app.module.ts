import { NguiTabModule } from '@ngui/tab';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { HttpModule } from '@angular/http';
import {DataService} from './services/data.service';
import { RealtimeTweeterComponent } from './realtime-tweeter/realtime-tweeter.component';
import { SentimentAnalysisComponent } from './sentiment-analysis/sentiment-analysis.component';
import { TelegramComponent } from './telegram/telegram.component';

@NgModule({
  declarations: [
    AppComponent,
    RealtimeTweeterComponent,
    SentimentAnalysisComponent,
    TelegramComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    NguiTabModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {}
 }
