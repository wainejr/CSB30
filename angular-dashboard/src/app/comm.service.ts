import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface User {
  id: string;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class CommService {

  url = "http://127.0.0.1:5000/";

  constructor(public http: HttpClient) { 
    window["A_comm"] = this;
  }

  getUsers() : Observable<any> {
    return this.http.get(this.url + 'users');
  }

  getDistance(userId: string): Observable<any> {
    return this.http.get(this.url + 'relationship_level/' + userId);
  }

  getBands(): Observable<any> {
    return this.http.get(this.url + 'list/bands');
  }

  getMovies(): Observable<any> {
    return this.http.get(this.url + 'list/movies');
  }

  getCommomFriends(user1Id, user2Id): Observable<any> {
    return this.http.get(this.url + "list/common_friends/" + user1Id + "&&" + user2Id);
  }

  yearRating(): Observable<any> {
    return this.http.get(this.url + "most_popular_decades");
  }
}
