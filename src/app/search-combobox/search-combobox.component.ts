import { Component, Input } from '@angular/core';
import { Pokemon } from '../interfaces/pokemon';

@Component({
  selector: 'app-search-combobox',
  templateUrl: './search-combobox.component.html',
  styleUrls: ['./search-combobox.component.css']
})
export class SearchComboboxComponent {
  @Input() pokemons: Pokemon[] = [];
}
