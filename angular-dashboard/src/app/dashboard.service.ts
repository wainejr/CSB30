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


  getChart(str): Observable<Object | ChartData> {
    return this.http.get(this.url + "chart/" + str);
  }


}
