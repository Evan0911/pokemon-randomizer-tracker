import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainPageComponent } from './main-page/main-page.component';
import { ListTrackerComponent } from './list-tracker/list-tracker.component';

const routes: Routes = [
  { path: '', component: MainPageComponent },
  { path: 'map', component: MainPageComponent },
  { path: 'map/:version', component: MainPageComponent },
  { path: 'list', component: ListTrackerComponent },
  { path: 'list/:version', component: ListTrackerComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
