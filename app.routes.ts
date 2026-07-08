import { Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HomeComponent } from './components/home/home.component';
import { RegisterComponent } from './components/register/register.component';
import { OtpComponent } from './components/otp/otp.component';
import { LoginComponent } from './components/login/login.component';
import { ApplyComponent } from './components/apply/apply.component';
import { StatusComponent } from './components/status/status.component';
import { AdminLoginComponent } from './components/admin-login/admin-login.component';
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard.component';

export const routes: Routes = [

  {
    path:'',
    component:HomeComponent
  },
  {
    path:'dashboard',
    component:DashboardComponent
},

  {
    path:'register',
    component:RegisterComponent
  },

  {
    path:'otp',
    component:OtpComponent
  },

  {
    path:'login',
    component:LoginComponent
  },
  {
    path:'apply',
    component:ApplyComponent
},
{
    path:'status',
    component:StatusComponent
},
{
  path:'admin-login',
  component:AdminLoginComponent
},
{
  path:'admin-dashboard',
  component:AdminDashboardComponent
}

];





