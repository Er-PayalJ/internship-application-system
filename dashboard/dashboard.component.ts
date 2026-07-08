import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {

  companies: any[] = [];
  studentName = '';

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit(): void {

    this.studentName = localStorage.getItem('student_name') || '';

    this.http.get<any[]>('http://127.0.0.1:5000/companies')
      .subscribe({
        next: (data) => {
          this.companies = data;
        },
        error: () => {
          alert('Unable to load companies');
        }
      });

  }

  logout() {

    localStorage.clear();
    this.router.navigate(['/login']);

  }

}