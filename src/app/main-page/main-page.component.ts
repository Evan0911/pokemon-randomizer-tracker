import { Component } from '@angular/core';
import { Versions } from '../interfaces/versions';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent {
  version: Versions = Versions.Emerald;

  constructor(private route: ActivatedRoute) {
    this.route.params.subscribe(params => {
      if (Object.values(Versions).includes(params["version"])) {
        this.version = params["version"];
      }
    });
  }
}
