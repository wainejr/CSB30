import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

import { ChartsModule } from "ng2-charts";

import { AppComponent } from "./app.component";
import { RouterModule, Routes } from "@angular/router";
import { FlexLayoutModule } from "@angular/flex-layout";

import { CustomMaterialModule } from "./custom-material/custom-material.module";
import { InitialPageComponent } from "./initial-page/initial-page.component";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { TriviaComponent } from "./trivia/trivia.component";
import { AboutComponent } from "./about/about.component";
import { DashboardService } from './dashboard.service';
import { CommService } from './comm.service';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ListaComponent } from './lista/lista.component';

const routes: Routes = [
  {
    path: "",
    component: InitialPageComponent
  },
  {
    path: "dashboard",
    component: DashboardComponent
  },
  {
    path: "trivia",
    component: TriviaComponent
  },
  {
    path: "about",
    component: AboutComponent
  },
  {
    path: "lista",
    component: ListaComponent
  },
  
];

@NgModule({
  declarations: [
    AppComponent,
    InitialPageComponent,
    DashboardComponent,
    TriviaComponent,
    AboutComponent,
    ListaComponent,
    
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    CustomMaterialModule,
    RouterModule.forRoot(routes),
    FlexLayoutModule,
    HttpClientModule,
    FormsModule,
    ChartsModule
  ],
  providers: [DashboardService, CommService],
  bootstrap: [AppComponent]
})
export class AppModule {}
