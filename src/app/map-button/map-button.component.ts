import { Component, Input } from '@angular/core';
import { States } from '../interfaces/states';

@Component({
  selector: 'app-map-button',
  templateUrl: './map-button.component.html',
  styleUrls: ['./map-button.component.css']
})
export class MapButtonComponent {
  @Input() coordinates: number[] = [0, 0];
  @Input() state: States = States.Active;
  @Input() onClick: () => void = () => {};
}
