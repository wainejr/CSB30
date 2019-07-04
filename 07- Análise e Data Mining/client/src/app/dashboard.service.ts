import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ChartData {
  labels: any[];
  data: any[];
} 

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  url = "http://127.0.0.1:5000/";

  constructor(
    public http: HttpClient
  ) { 
    window["A_dash"] = this;
  }

  possibleChart = ["count_supergenres", "count_genres_in_supergenres", "most_popular_users", "top_cities", "top_movies", "top_bands"]


  /**
   * Available: count_supergenres, count_genres_in_supergenres, most_popular_users, top_cities, top_movies, top_bands
   * @param choice string of desired chart or index of available charts
   */
  getChart(choice: string | number): Observable<Object | ChartData> {
    return this.http.get(
      this.url + "chart/" 
      + (typeof choice === 'number' ? this.possibleChart[choice] : choice)
    );
  }


}
