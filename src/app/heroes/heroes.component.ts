import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {

  constructor(private heroService: HeroService) { }

  ngOnInit() {
    this.getHeroes();
  }

  hero: Hero = {
    id: 1,
    name: 'Windstorm'
  }

  heroes: Hero[];

  getHeroes(): void {
    this.heroService.getHeroes().subscribe(heroes => this.heroes = heroes);
  }

  //heroes = HEROES;

  selectedHero: Hero;
  onSelect(hero: Hero): void {
    this.selectedHero = hero;
    // console.log(this.selectedHero.name);
  }

}
