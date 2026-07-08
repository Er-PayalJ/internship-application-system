import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule,RouterLink],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  email = '';
  password = '';

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  login() {

    const data = {
      email: this.email,
      password: this.password
    };

    this.http.post<any>('http://127.0.0.1:5000/login', data)
      .subscribe({

        next: (res) => {

          alert(res.message);

          localStorage.setItem("student_id", res.student_id);

          localStorage.setItem("student_name", res.name);

          this.router.navigate(['/dashboard']);

        },

        error: (err) => {

          alert(err.error.message);

        }

      });

  }

}