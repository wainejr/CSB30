import { Component, OnInit } from "@angular/core";
import { DashboardService } from '../dashboard.service';
import { Label } from 'ng2-charts';
import { ChartDataSets } from 'chart.js';

@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.css"]
})
export class DashboardComponent implements OnInit {
  possibleChart = [
    {url: "count_supergenres", nome: "Super generos", labelName: "Super Gêneros"},
    {url: "count_genres_in_supergenres", nome: "Generos em super generos ", labelName: "Gêneros"},
    {url: "most_popular_users", nome: "Usuários mais populares", labelName: "Usuários"},
    {url: "top_cities", nome: "Cidades mais populares", labelName: "Cidades"},
    {url: "top_movies", nome: "Filmes mais populares", labelName: "Filmes"},
    {url: "top_bands", nome: "Bandas mais populares", labelName: "Banda"}
  ]

  currentChart = "top_bands";
  currentPage = "top_bands";
  currentData: any[];
  currentLabels: any[];
  viewData: any[];
  viewLabels: any[];

  dataNum: number = 20;
  page: number = 0;
  maxPage;
  tipoMostrando: string = 'chart';


  constructor(
    private dash: DashboardService
  ) {}

  public barChartOptions = {
    scaleShowVerticalLines: false,
    responsive: true,
    
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true
          }
        }
      ]
    }
  };
  public barChartLabels: Label[] = [
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012"
  ];
  public barChartType = "bar";
  public barChartLegend = true;
  public barChartData: ChartDataSets[] = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: "Series A" },
    { data: [28, 48, 40, 19, 86, 27, 90], label: "Series B" }
  ];

  ngOnInit() {

    this.dash.getChart(this.currentChart).subscribe(data=> {
      this.currentData = data["data"];
      this.currentLabels = data["labels"];
      this.maxPage = Math.floor(this.currentData.length/this.dataNum);
      this.updateData()
    })
  }
  updateData() {
    this.viewData = this.currentData.slice(this.page*this.dataNum, (this.page+1)*this.dataNum);
    this.viewLabels = this.currentLabels.slice(this.page*this.dataNum, (this.page+1)*this.dataNum);
    this.barChartLabels = this.viewLabels;
    let chartInfo = this.getChart(this.currentChart);
    this.barChartData = [{data: this.viewData, label: chartInfo["labelName"], backgroundColor: "#673ab7",}];

  }

  getChart(url: string) {
    return this.possibleChart.find(v => v.url === url);
  }

  mudaPag(addToPage) {
    console.log(this.page);
    this.page += addToPage;
    if(this.page < 0) this.page = 0;
    if(this.page > this.maxPage) this.page = this.maxPage;
    this.updateData();
  }

  mudarChart(event) {
    this.currentChart = event.value
    this.dash.getChart(event.value).subscribe(data => {
      this.page = 0;
      this.currentData = data["data"];
      this.currentLabels = data["labels"];
      this.maxPage = Math.floor(this.currentData.length/this.dataNum);
      this.updateData()
    })
  }
}
