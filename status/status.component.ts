import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-status',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './status.component.html',
  styleUrl: './status.component.css'
})
export class StatusComponent implements OnInit {

  applications: any[] = [];
  student_id: any;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {

    this.student_id = localStorage.getItem("student_id");

    this.http.get<any[]>(
      `http://127.0.0.1:5000/status/${this.student_id}`
    ).subscribe({

      next: (data) => {

        this.applications = data;

      },

      error: () => {

        alert("Unable to load status");

      }

    });

  }

}