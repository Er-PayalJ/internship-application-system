import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Router } from '@angular/router';
import {  RouterLink } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, HttpClientModule, RouterLink],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {

  name = '';
  email = '';
  mobile = '';
  password = '';

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  register() {

    const formData = new FormData();

    formData.append('name', this.name);
    formData.append('email', this.email);
    formData.append('mobile', this.mobile);
    formData.append('password', this.password);

    this.http.post<any>(
      'http://127.0.0.1:5000/register',
      formData
    ).subscribe({

      next: (res) => {

        alert(res.message);

        localStorage.setItem('email', this.email);

        this.router.navigate(['/otp']);

      },

      error: (err) => {

        if (err.error?.message) {
          alert(err.error.message);
        } else {
          alert("Registration Failed");
        }

      }
      

    });

  }

}

