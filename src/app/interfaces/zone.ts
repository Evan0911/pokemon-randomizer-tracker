export interface Zone {
  zone: string;
  walk?: string[];
  surf?: string[];
  dive?: string[];
  rockSmash?: string[];
  fish?: {
    old?: string[];
    good?: string[];
    super?: string[];
  };
}
