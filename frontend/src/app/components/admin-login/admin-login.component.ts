import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './admin-login.component.html',
  styleUrl: './admin-login.component.css'
})
export class AdminLoginComponent {

  username = '';
  password = '';

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  login() {

    const data = {
      username: this.username,
      password: this.password
    };

    this.http.post<any>('http://127.0.0.1:5000/admin/login', data)
      .subscribe({

        next: (res) => {

          alert(res.message);

          this.router.navigate(['/admin-dashboard']);

        },

        error: (err) => {

          alert(err.error.message);

        }

      });

  }

}