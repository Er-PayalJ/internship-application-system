import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-apply',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './apply.component.html',
  styleUrl: './apply.component.css'
})
export class ApplyComponent {

  company_id: any;
  student_id: any;
  resume: any;

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
    private router: Router
  ) {

    this.company_id = this.route.snapshot.queryParamMap.get('company_id');

    this.student_id = localStorage.getItem("student_id");

  }

  selectResume(event: any) {

    this.resume = event.target.files[0];

  }

  apply() {

    const formData = new FormData();

    formData.append("student_id", this.student_id);
    formData.append("company_id", this.company_id);
    formData.append("resume", this.resume);

    this.http.post<any>("http://127.0.0.1:5000/apply", formData)
      .subscribe({

        next: (res) => {

          alert(res.message);

          this.router.navigate(['/status']);

        },

        error: (err) => {

          alert(err.error.message);

        }

      });

  }

}