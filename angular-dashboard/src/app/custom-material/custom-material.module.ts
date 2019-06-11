import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { 
  MatToolbarModule, MatButtonModule 
} from '@angular/material'

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MatToolbarModule,
    MatButtonModule,
  ],
  exports : [
    MatToolbarModule,
    MatButtonModule
  ]
})
export class CustomMaterialModule { }
