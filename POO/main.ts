export class Persone {
  constructor(
    private nom: string = "",
    private age: number = 0,
  ) {}

  public se_presenter(): void {
    console.log(`Je m'appelle ${this.nom} et j'ai ${this.age} !`);
  }
  public est_majeur(): boolean {
    if (this.age >= 18) {
      return true;
    } else {
      return false;
    }
  }
}

const persone1 = new Persone("Guindo", 26);
persone1.se_presenter();
persone1.est_majeur();
