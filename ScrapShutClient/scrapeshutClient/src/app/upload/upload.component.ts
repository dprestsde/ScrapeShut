import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup} from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.scss']
})
export class UploadComponent implements OnInit {

  DJANGO_SERVER = 'http://localhost:8000';
  form:FormGroup;
  response;
  imageURL;
  name: string ="";
  email:string="";
  phone: string="";
  photoselected:File;
  videoselected:File;
  choiceselected: string="";

  constructor(private http: HttpClient) { }


  ngOnInit() {
   
  }
  OnImageChanged(event){
    this.photoselected = event.target.files[0];
  }
  OnFileChanged(event){
    this.videoselected=event.target.files[0];
  }

  choice(select){
    this.choiceselected = select;
    console.log(select)
  }

  onUpload(){
    console.log("Upload clicked")
    
    const fd = new FormData();
    fd.append("name", this.name);
    fd.append("email", this.email);
    fd.append("phone",this.phone);
    fd.append("photo",this.photoselected);
    fd.append("file",this.videoselected);
    fd.append("choice", this.choiceselected);
    console.log("Upload clicked")
    console.log(fd);
    this.http.post<any>('http://localhost:8000/upload/',
         fd
        //  ,
        //  {
        //       headers: new HttpHeaders().set('Content-Type','application/json')
        //   }
          ).subscribe(response => {
            this.response=response;
          });
  }




}
