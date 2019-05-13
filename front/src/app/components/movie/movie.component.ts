import { Component, OnInit, EventEmitter, Output, Input } from '@angular/core';
import { ProviderService } from 'src/app/shared/services/provider.service';
import { IMovie } from 'src/app/shared/models/models';
import { timeout } from 'q';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.css']
})
export class MovieComponent implements OnInit {

  constructor(private provider: ProviderService) { }

  
  public movie: IMovie;
  
  ngOnInit() {
    this.getMovie();
  }

  getMovie()
  {
      this.movie = JSON.parse(localStorage.getItem('movieFromMovies'));
      console.log("recieve " + this.movie.title);
  }
}