import { Component, Input } from '@angular/core';
import { Versions } from '../interfaces/versions';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent {
  @Input() version: Versions = Versions.Emerald;

  coordinates: number[] = [414, 181];
}
