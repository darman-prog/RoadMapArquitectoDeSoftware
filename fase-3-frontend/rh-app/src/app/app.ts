import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router'; // <- ¡CRUCIAL! Importar las herramientas de ruta

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],  
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = 'rh-app';
}


