import { Component, OnInit } from '@angular/core';
import { CommService, User } from '../comm.service';

@Component({
  selector: 'app-lista',
  templateUrl: './lista.component.html',
  styleUrls: ['./lista.component.css']
})
export class ListaComponent implements OnInit {

  users: User[];
  tipoMostrando: string = 'pessoas';

  movies: string[];
  bands: string[];

  // ba

  constructor(
    private comm: CommService
  ) { }

  ngOnInit() {
    this.comm.getUsers().subscribe(u => {
      console.log(u);
      this.users = u.users;
    })
  }

  getUsers() {
    this.comm.getUsers().subscribe(u => {
      this.users = u.users;
    })
  }

  getBands() {
    this.comm.getBands().subscribe(b => {
      this.bands = b
    })
  }

  getMovies() {
    this.comm.getMovies().subscribe(m => {
      this.movies = m
    })
  }
  

  mudarLista(event) {
    switch (event.value) {
      case 'filmes':
        this.getMovies()
        break;
      case 'pessoas':
        this.getUsers
        break;
      case 'bandas':
        this.getBands();
        break;
    }
  }

}
