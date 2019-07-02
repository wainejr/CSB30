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
    {url: "count_supergenres", nome: "Super generos", labelName: "Super Gêneros", labelInfo: "Gêneros"},
    {url: "count_genres_in_supergenres", nome: "Generos em super generos ", labelInfo: "Gêneros"},
    {url: "most_popular_users", nome: "Usuários mais populares", labelName: "Usuários", labelInfo: "amigos"},
    {url: "top_cities", nome: "Cidades mais populares", labelName: "Cidades", labelInfo: "Pessoas na sala"},
    {url: "top_movies", nome: "Filmes mais populares", labelName: "Filmes", labelInfo: "Curtidas"},
    {url: "top_bands", nome: "Bandas mais populares", labelName: "Bandas", labelInfo: "Curtidas"},
    {url: "followers_by_band", nome: "Bandas mais seguidas", labelName: "Bandas", labelInfo: "Seguidores"},
    {url: "bands_rating", nome: "Notas das Bandas", labelName: "Bandas", labelInfo: "Nota"},
  ]

  currentChart = "top_bands";
  currentPage = "top_bands";
  currentData: any[];
  currentLabels: any[];
  allData: any[];
  allLabels: any[];
  viewData: any[];
  viewLabels: any[];

  filterName: string;
  tipoFiltro: string = 'contem';
  funcoesFiltro: Object = {
    "contem" : function(val: string, base: string): boolean {
      return base.toLowerCase().indexOf(val.toLowerCase()) > -1;
    },
    "comeca" : function(val: string, base: string): boolean {
      return base.toLowerCase().indexOf(val.toLowerCase()) == 0;
    },
    "termina" : function(val: string, base: string): boolean {
      return base.toLowerCase().lastIndexOf(val.toLowerCase()) == base.length - val.length;
    },
  }
  filtro: ((val: string, base: string)=>boolean) = this.funcoesFiltro[this.tipoFiltro];

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
  public barChartLabels: Label[] = [];
  public barChartType = "bar";
  public barChartLegend = true;
  public barChartData: ChartDataSets[] = [];

  ngOnInit() {

    this.dash.getChart(this.currentChart).subscribe(data=> {
      this.allData = data["data"];
      this.allLabels = data["labels"];
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
    this.barChartData = [{
      data: this.viewData, 
      label: chartInfo["label"],
      backgroundColor: "#673ab7",
      hoverBackgroundColor: "#482d77"
    }];

  }

  getChart(url: string) {
    return this.possibleChart.find(v => v.url === url);
  }

  mudaPag(addToPage) {
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

  mudaFiltro(event?) {
    if(event) {
      this.filtro = this.funcoesFiltro[this.tipoFiltro];
    }
    if(this.filterName)
      this.filtra()
    else {
      this.currentData = this.allData.slice();
      this.currentLabels = this.allLabels.slice();
    }
  }

  filtra() {
    this.currentData = []
    this.currentLabels = this.allLabels.filter((base, index) => {
      let result = this.filtro(this.filterName, base);
      if(result) this.currentData.push(this.allData[index]);
      return result;
    });
    this.maxPage = Math.floor(this.currentData.length/this.dataNum);
    this.page = 0;
    this.updateData();

  }
}
