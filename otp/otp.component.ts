import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-otp',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './otp.component.html',
  styleUrl: './otp.component.css'
})
export class OtpComponent {

  email = '';
  otp = '';

  constructor(private http: HttpClient) {}

  verifyOTP() {

    const data = {
      email: this.email,
      otp: this.otp
    };

    this.http.post('http://127.0.0.1:5000/verify', data)
      .subscribe({
        next: (res: any) => {
          alert(res.message);
        },
        error: (err) => {
          alert(err.error.message);
        }
      });

  }

}