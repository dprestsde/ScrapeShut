import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewComponent implements OnInit {

  constructor(private http: HttpClient) { }
  ngOnInit() {
  }
   response:any =null;
   Search:string="";

  search(){
    console.log(this.Search);
    console.log("Clicked");
    this.http.get('http://localhost:8000/upload/api/?search='+ this.Search)
    .subscribe((response) => {
    this.response = response;
    console.log(this.response)
  })
}

}