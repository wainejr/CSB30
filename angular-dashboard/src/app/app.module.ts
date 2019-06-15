import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { ChartsModule } from "ng2-charts";

import { AppComponent } from "./app.component";
import { RouterModule, Routes } from "@angular/router";
import { FlexLayoutModule } from "@angular/flex-layout";

import { CustomMaterialModule } from "./custom-material/custom-material.module";
import { InitialPageComponent } from "./initial-page/initial-page.component";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { TriviaComponent } from "./trivia/trivia.component";
import { AboutComponent } from "./about/about.component";

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
  }
];

@NgModule({
  declarations: [
    AppComponent,
    InitialPageComponent,
    DashboardComponent,
    TriviaComponent,
    AboutComponent
  ],
  imports: [
    BrowserModule,
    CustomMaterialModule,
    RouterModule.forRoot(routes),
    FlexLayoutModule,
    ChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
