import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-admin-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin-dashboard.component.html',
  styleUrl: './admin-dashboard.component.css'
})
export class AdminDashboardComponent implements OnInit {

  applications: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {

    this.loadApplications();

  }

  loadApplications() {

    this.http.get<any[]>("http://127.0.0.1:5000/admin/applications")
      .subscribe(data => {

        this.applications = data;

      });

  }

  accept(id:number){

    this.http.put<any>(
      "http://127.0.0.1:5000/admin/accept/"+id,{})
      .subscribe(res=>{

        alert(res.message);

        this.loadApplications();

      });

  }

  reject(id:number){

    this.http.put<any>(
      "http://127.0.0.1:5000/admin/reject/"+id,{})
      .subscribe(res=>{

        alert(res.message);

        this.loadApplications();

      });

  }

}