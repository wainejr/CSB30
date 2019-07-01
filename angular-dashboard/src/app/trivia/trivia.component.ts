import { Component, OnInit } from '@angular/core';
import { User, CommService } from '../comm.service';

@Component({
  selector: 'app-trivia',
  templateUrl: './trivia.component.html',
  styleUrls: ['./trivia.component.css']
})
export class TriviaComponent implements OnInit {

  users: User[];

  user1: User; user2: User;
  calculatedDistance: boolean = false;
  distance: number;

  constructor(public comm: CommService) { }

  ngOnInit() {

    this.comm.getUsers().subscribe(u => {
      this.users = u["users"];
      console.log("users:", this.users);
    });

    

    

  }

  calculateDistance() {
    if(!this.user1 || !this.user2) {
      alert("Selecione os usuários para calcular a distancia");
      return;
    }
    this.comm.getDistance(this.user1.id).subscribe(d=> {
      console.log("d", d);
      let us = d["distancias"].find(v => v["nome"] == this.user2.name);
      if(!us) {
        alert("A distancia entre essas pessoas é infinito");
        return;
      }
      this.distance = us["distancia"];
      this.calculatedDistance = true;
    })
  }

}
