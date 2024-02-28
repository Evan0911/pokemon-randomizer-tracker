export interface Pokemon {
  name: string;
  isCaught: boolean;
}

export interface PokemonServer {
  count: number;
  next: string | null;
  previous: string | null;
  results: {
    name: string;
    url: string;
  }[];
}
