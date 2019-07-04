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
  user1Friend: User; user2Friend: User;
  calculatedDistance: boolean = false;
  distance: number;

  commonFriends: boolean = false;
  friends: string[];


  decadas: any[] = [];
  decLancamento: boolean = false;

  constructor(public comm: CommService) { }

  ngOnInit() {

    this.comm.getUsers().subscribe(u => {
      this.users = u["users"];
    });

    this.comm.yearRating().subscribe(data => {
      console.log(data);
      Object.keys(data).forEach(k=>{
        this.decadas.push({decada: k, likes: data[k]});
      })
      let el = this.decadas.shift();
      this.decadas.push(el);
      el = this.decadas.shift();
      this.decadas.push(el);
      this.decLancamento = true;
    })
    

    

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

  getCommonFriends() {
    this.comm.getCommomFriends(this.user1Friend.id, this.user2Friend.id).subscribe(
      data => {
        console.log(data);
        this.friends = data;
        this.commonFriends = true;
      }
    )
  }

}
