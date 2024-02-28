import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainPageComponent } from './main-page/main-page.component';
import { MapComponent } from './map/map.component';
import { MapButtonComponent } from './map-button/map-button.component';
import { EncounterListMenuComponent } from './encounter-list-menu/encounter-list-menu.component';

@NgModule({
  declarations: [
    AppComponent,
    MainPageComponent,
    MapComponent,
    MapButtonComponent,
    EncounterListMenuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
