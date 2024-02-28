import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { Pokemon, PokemonServer } from '../interfaces/pokemon';

@Injectable({
  providedIn: 'root'
})
export class PokeapiService {
  private apiUrl = 'https://pokeapi.co/api/v2/pokemon?limit=386'; // Replace with your API URL

  constructor(private http: HttpClient) { }

  getPokemons(): Observable<Pokemon[]> {
    return this.http.get<PokemonServer>(this.apiUrl).pipe(
      map((res) => {
        return res.results.map((res): Pokemon => {
          return {
            name: res.name,
            isCaught: false
          };
        });
      })
    );
  }
}
