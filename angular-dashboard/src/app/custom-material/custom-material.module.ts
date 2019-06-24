import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { 
  MatToolbarModule, MatButtonModule, MatFormFieldModule, MatInputModule, MatSelectModule, MatIconModule 
} from '@angular/material'

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MatToolbarModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatIconModule
  ],
  exports : [
    MatToolbarModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatIconModule
  ]
})
export class CustomMaterialModule { }
