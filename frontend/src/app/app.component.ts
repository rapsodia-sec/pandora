import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {UsersApiService} from './users/users-api.service';
import {User} from './users/user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  usersListSubs: Subscription;
  usersList: User[];

  constructor(private examsApi: UsersApiService) {
    this.usersListSubs = new Subscription()
    this.usersList = []
  }

  ngOnInit() {
    this.usersListSubs = this.examsApi
      .getUsers()
      .subscribe((res: User[]) => {
          this.usersList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.usersListSubs.unsubscribe();
  }
}
