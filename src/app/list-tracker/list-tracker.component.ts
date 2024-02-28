import { Component } from '@angular/core';
import { Pokemon } from '../interfaces/pokemon';
import { PokeapiService } from '../services/pokeapi.service';
import encounterEmerald from '../utils/encounter-formatter/encounter-emerald-without-name.json';
import { Zone } from '../interfaces/zone';

@Component({
  selector: 'app-list-tracker',
  templateUrl: './list-tracker.component.html',
  styleUrls: ['./list-tracker.component.css']
})
export class ListTrackerComponent {
  pokemons: Pokemon[] = [];
  encounterList: Zone[] = encounterEmerald;

  constructor(private pokeapiService: PokeapiService){}

  ngOnInit(): void {
    this.pokeapiService.getPokemons().subscribe(pokemons => this.pokemons = pokemons);
  }
}
